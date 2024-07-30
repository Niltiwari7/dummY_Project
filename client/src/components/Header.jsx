import React, { useEffect } from 'react';
import { gsap } from 'gsap';
import { Link } from 'react-router-dom';

export default function Header() {
  useEffect(() => {
    gsap.fromTo(
      ".header",
      { opacity: 0, y: -50 },
      { opacity: 1, y: 0, duration: 1 }
    );
    gsap.fromTo(
      ".title",
      { opacity: 0, x: -150 },
      { opacity: 1, x: 0, duration: 1, delay: 0.5 }
    );
    gsap.fromTo(
      ".nav-item",
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 0.5, stagger: 0.2, delay: 1 }
    );
  }, []);

  return (
    <header className="header bg-sky-500 shadow-md">
      <div className="flex justify-between items-center max-w-6xl mx-auto p-2 sm:p-3">
        <Link to='/'>
          <h1 className="title font-bold text-sm sm:text-xl flex flex-wrap">
            <span className="text-white sm:text-4xl">MahaKal</span>
            <span className="text-gray-500 sm:text-xl">Construction</span>
          </h1>
        </Link>
        <div className="flex flex-1 justify-end items-center sm:ml-4 sm:mx-6">
          <form className="hidden sm:block sm:mr-4">
            <input
              type="text"
              placeholder="Search.."
              className="p-2 rounded border-2 border-white focus:outline-none focus:ring-2 focus:ring-sky-300"
            />
          </form>
          <ul className="hidden sm:flex gap-4">
            <Link to='/' className="nav-item">
              <button className="hover:bg-sky-700 text-white px-3 py-2 rounded sm:text-xl ">
                Home
              </button>
            </Link>
            <Link to='/about' className="nav-item">
              <button className="hover:bg-sky-700 text-white px-3 py-2 sm:text-xl rounded">
                About
              </button>
            </Link>
          </ul>
          <Link to='/sign-in'>
          <button className="nav-item hover:bg-sky-700 text-white px-3 py-2 sm:text-xl rounded ml-4  ">
            Sign In
          </button>
          </Link>
        </div>
      </div>
    </header>
  );
}
