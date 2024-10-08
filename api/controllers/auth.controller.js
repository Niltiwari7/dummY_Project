import User from "../models/User.models.js";
import bcryptjs from 'bcryptjs';

export const signup = async (req, res,next) => {
    try {
        const { username, email, password } = req.body;

        const hashedPassword = await bcryptjs.hash(password, 10);
        const newUser = new User({ username, email, password: hashedPassword });
        await newUser.save();
        res.status(201).json({ message: "User Created Successfully" });
    } catch (error) {
       next(error);
    }
};
