import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { gsap } from 'gsap';

export default function SignUp() {
  useEffect(() => {
    gsap.fromTo(
      ".form-container",
      { opacity: 0, y: -50 },
      { opacity: 1, y: 0, duration: 1, ease: "power2.out" }
    );
    
    gsap.fromTo(
      ".button",
      { scale: 1 },
      { scale: 1.05, duration: 0.3, repeat: -1, yoyo: true, ease: "power2.inOut" }
    );
  }, []);

  return (
    <div className="flex p-10 justify-center ">
      <div className="form-container bg-white shadow-lg rounded-lg p-8 w-full max-w-md">
        <h1 className="text-xl sm:text-3xl font-semibold text-gray-800 mb-6 text-center">Sign Up</h1>
        <form className="flex flex-col gap-5">
          <input
            type="text"
            name="username"
            placeholder="Username"
            id="username"
            className="text-center text-lg p-1 sm:p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            id="email"
            className="text-center text-lg p-1 sm:p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            id="password"
            className="text-center text-lg p-1 sm:p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            type="submit"
            className="button bg-violet-700 text-white p-1 sm:p-3 rounded-md w-full mt-1 sm:mt-4 hover:bg-blue-800 transition-colors"
          >
            Sign Up
          </button>
        </form>
        <div className='flex gap-2 mt-5'>
          <p>Have an Account ?</p>
          <Link to ={"/sign-in"}>
           <span className='text-blue-500'>Sign In</span>
          </Link>
        </div>
      </div>
    </div>
  );
}
