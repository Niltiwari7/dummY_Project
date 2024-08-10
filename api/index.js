import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';

dotenv.config()
const app = express();

mongoose.connect(process.env.MONGO_URI).then(()=>{
    console.log("MongoDb is connected");
    
})
app.listen(3000,()=>{
    console.log(`Server is running 3000!`);  
})