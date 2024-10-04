import math

# Rotation and constants setup
rotate_by = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

constants = [int(abs(math.sin(i + 1)) * 4294967296) & 0xFFFFFFFF for i in range(64)]

# Padding the message according to MD5 specification
def pad(msg):
    msg_len_in_bits = (8 * len(msg)) & 0xffffffffffffffff
    msg.append(0x80)  # Append the bit '1' to the message
    while len(msg) % 64 != 56:
        msg.append(0)  # Padding with zeros

    # Append the original message length in bits (64 bits at the end)
    msg += msg_len_in_bits.to_bytes(8, byteorder='little')
    return msg

# Initial values of MD5 buffer
init_MDBuffer = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

# Left rotate function
def leftRotate(x, amount):
    x &= 0xFFFFFFFF
    return (x << amount | x >> (32 - amount)) & 0xFFFFFFFF

# Processing message in 512-bit blocks (64 bytes)
def processMessage(msg):
    init_temp = init_MDBuffer[:]  # Copy initial buffer values
    total_blocks = len(msg) // 64

    for block_num, offset in enumerate(range(0, len(msg), 64)):
        print(f"Block {block_num + 1}:\n{'=' * 50}")
        A, B, C, D = init_temp
        block = msg[offset:offset + 64]

        for i in range(64):
            if i < 16:
                func = lambda b, c, d: (b & c) | (~b & d)
                index_func = lambda i: i
            elif 16 <= i < 32:
                func = lambda b, c, d: (d & b) | (~d & c)
                index_func = lambda i: (5 * i + 1) % 16
            elif 32 <= i < 48:
                func = lambda b, c, d: b ^ c ^ d
                index_func = lambda i: (3 * i + 5) % 16
            else:
                func = lambda b, c, d: c ^ (b | ~d)
                index_func = lambda i: (7 * i) % 16

            F = func(B, C, D)
            G = index_func(i)
            to_rotate = A + F + constants[i] + int.from_bytes(block[4 * G: 4 * G + 4], byteorder='little')
            newB = (B + leftRotate(to_rotate, rotate_by[i])) & 0xFFFFFFFF
            A, B, C, D = D, newB, B, C

            # Printing each round information
            round_label = (i // 16) + 1
            if i % 16 == 0:
                print(f"====================================================Round {round_label}:============================================")
            print(f"Step {i + 1}: A={hex(A)}, B={hex(B)}, C={hex(C)}, D={hex(D)}")

        for i, val in enumerate([A, B, C, D]):
            init_temp[i] += val
            init_temp[i] &= 0xFFFFFFFF  # Ensure it's within 32 bits

        print(f"After Block {block_num + 1} Processing: A={hex(init_temp[0])}, B={hex(init_temp[1])}, C={hex(init_temp[2])}, D={hex(init_temp[3])}")
        print(f"{'=' * 50}\n")

    return sum(buffer_content << (32 * i) for i, buffer_content in enumerate(init_temp))

# Converting processed message digest to hex format
def MD_to_hex(digest):
    raw = digest.to_bytes(16, byteorder='little')
    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

# MD5 function
def md5(msg):
    msg = bytearray(msg, 'ascii')  # Convert message to a byte array
    msg = pad(msg)  # Pad the message
    processed_msg = processMessage(msg)  # Process the message
    message_hash = MD_to_hex(processed_msg)  # Convert the processed message to hex format
    print("Hash Value:", message_hash)

# Main entry point
if __name__ == '__main__':
    message = input("Enter the message: ")
    md5(message)
