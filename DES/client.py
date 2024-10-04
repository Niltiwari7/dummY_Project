import socket
IP = [58, 50, 42, 34, 26, 18, 10, 2,
60, 52, 44, 36, 28, 20, 12, 4,
62, 54, 46, 38, 30, 22, 14, 6,
64, 56, 48, 40, 32, 24, 16, 8,
57, 49, 41, 33, 25, 17, 9, 1,
59, 51, 43, 35, 27, 19, 11, 3,
61, 53, 45, 37, 29, 21, 13, 5,
63, 55, 47, 39, 31, 23, 15, 7]
FP = [40, 8, 48, 16, 56, 24, 64, 32,
39, 7, 47, 15, 55, 23, 63, 31,
38, 6, 46, 14, 54, 22, 62, 30,
37, 5, 45, 13, 53, 21, 61, 29,
36, 4, 44, 12, 52, 20, 60, 28,
35, 3, 43, 11, 51, 19, 59, 27,
34, 2, 42, 10, 50, 18, 58, 26,
33, 1, 41, 9, 49, 17, 57, 25]
E = [32, 1, 2, 3, 4, 5,
4, 5, 6, 7, 8, 9,
8, 9, 10, 11, 12, 13,
12, 13, 14, 15, 16, 17,
16, 17, 18, 19, 20, 21,
20, 21, 22, 23, 24, 25,
24, 25, 26, 27, 28, 29,
28, 29, 30, 31, 32, 1]
S_BOX = [
# S1
[
[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],
# S2
[
[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],
# S3
[
[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],
# S4
[
[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],
# S5
[
[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
],
# S6
[
[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
],
# S7
[
[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
# S8
[
[13, 2, 8, 4, 6, 11, 15, 1, 10, 9, 3, 14, 5, 0, 12, 7],
[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
[7, 11, 4, 1, 9, 12, 5, 8, 6, 10, 15, 3, 14, 0, 13, 2],
[2, 1, 14, 7, 10, 11, 6, 8, 0, 13, 9, 5, 3, 15, 12, 4],
]
]
P = [16, 7, 20, 21, 29, 12, 28, 17,
1, 15, 23, 26, 5, 18, 31, 10,
2, 8, 24, 14, 32, 27, 3, 9,
19, 13, 30, 6, 22, 11, 4, 25]
PC1 = [57, 49, 41, 33, 25, 17, 9,
1, 58, 50, 42, 34, 26, 18,
10, 2, 59, 51, 43, 35, 27,
19, 11, 3, 60, 52, 44, 36,
63, 55, 47, 39, 31, 23, 15,
7, 62, 54, 46, 38, 30, 22,
14, 6, 61, 53, 45, 37, 29,
21, 13, 5, 28, 20, 12, 4]
PC2 = [14, 17, 11, 24, 1, 5, 3, 28,
15, 6, 21, 10, 23, 19, 12, 4,
26, 8, 16, 7, 27, 20, 13, 2,
41, 52, 31, 37, 47, 55, 30, 40,
51, 45, 33, 48, 44, 49, 39, 56,
34, 53, 46, 42, 50, 36, 29, 32]
# Utility Functions
def string_to_binary(string):
return ''.join(f'{ord(c):08b}' for c in string)
def binary_to_string(binary):
return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))
def permute(block, table):
return ''.join(block[x - 1] for x in table)
def xor(a, b):
return ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))
def left_shift(bits, n):
return bits[n:] + bits[:n]
def generate_subkeys(key):
key = permute(key, PC1)
C = key[:28]
D = key[28:]
subkeys = []
shifts = [1, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 1]
for shift in shifts:
C = left_shift(C, shift)
D = left_shift(D, shift)
subkeys.append(permute(C + D, PC2))
return subkeys
def f_function(R, subkey):
R_expanded = permute(R, E)
R_xored = xor(R_expanded, subkey)
R_sbox = ''
for i in range(8):
row = int(R_xored[i * 6] + R_xored[i * 6 + 5], 2)
col = int(R_xored[i * 6 + 1:i * 6 + 5], 2)
R_sbox += f'{S_BOX[i][row][col]:04b}'
return permute(R_sbox, P)
def des_encrypt_block(plaintext, subkeys):
if len(plaintext) != 64:
raise ValueError("The block length must be 64 bits for DES")
block = permute(plaintext, IP)
L, R = block[:32], block[32:]
intermediate_results = []
for i in range(16):
L, R = R, xor(L, f_function(R, subkeys[i]))
intermediate_results.append(L + R)
block = permute(R + L, FP)
return block, intermediate_results
def des_encrypt(message, key):
key = string_to_binary(key).zfill(64)
subkeys = generate_subkeys(key)
padded_message = pad_message(message)
message_blocks = [padded_message[i:i + 64] for i in range(0, len(padded_message), 64)]
encrypted_blocks = []
encrypt_round_states = []
for block in message_blocks:
block, intermediate_results = des_encrypt_block(block, subkeys)
encrypted_blocks.append(block)
encrypt_round_states.extend(intermediate_results)
return ''.join(encrypted_blocks), encrypt_round_states
def des_decrypt_block(ciphertext, subkeys):
if len(ciphertext) != 64:
raise ValueError("The block length must be 64 bits for DES")
block = permute(ciphertext, IP)
L, R = block[:32], block[32:]
intermediate_results = []
for i in range(15, -1, -1):
L, R = R, xor(L, f_function(R, subkeys[i]))
intermediate_results.append(L + R)
block = permute(R + L, FP)
return block, intermediate_results
def des_decrypt(ciphertext, key):
key = string_to_binary(key).zfill(64)
subkeys = generate_subkeys(key)
ciphertext_blocks = [ciphertext[i:i + 64] for i in range(0, len(ciphertext), 64)]
decrypted_blocks = []
decrypt_round_states = []
for block in ciphertext_blocks:
block, intermediate_results = des_decrypt_block(block, subkeys)
decrypted_blocks.append(block)
decrypt_round_states.extend(intermediate_results)
decrypted_binary = ''.join(decrypted_blocks)
decrypted_binary = decrypted_binary.rstrip('0')
return decrypted_binary, decrypt_round_states
def pad_message(message):
binary_message = string_to_binary(message)
padded_length = (64 - (len(binary_message) % 64)) % 64
padded_message = binary_message + '0' * padded_length
return padded_message
def format_round_states(round_states):
return [hex(int(''.join(round_state), 2))[2:].zfill(16) for round_state in round_states]
key = "Security"
import socket
def client_program():
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 65432))
client_socket.send(b"Request for Ciphertext")
data = client_socket.recv(1024)
if data:
print(f"Received Ciphertext: {data.decode()}")
ciphertext = data.decode()
decrypted_binary, decrypt_results = des_decrypt(ciphertext, key)
print("\nIntermediate Results (IP, Round 1, 2, ..., 16) in HEX format:")
formatted_decrypt_results = format_round_states(decrypt_results)
for i, result in enumerate(formatted_decrypt_results):
if i+1==17:
break
print(f"Round {i + 1}: {result}")
decrypted_text = binary_to_string(decrypted_binary)
print(f"\nText after decryption: {decrypted_text}")
if __name__ == "__main__":
client_program()
