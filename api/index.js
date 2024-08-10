import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import userRouter from './routes/user.route.js'
dotenv.config()
const app = express();

mongoose.connect(process.env.MONGO_URI).then(()=>{
    console.log("MongoDb is connected");
    
})

app.listen(3000,()=>{
    console.log(`Server is running 3000!`);  
})

app.use('/api/user',userRouter);