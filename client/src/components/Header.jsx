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
      { opacity: 0, x: -50 },
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
      <div className="flex justify-between items-center max-w-6xl mx-auto p-3">
        <Link to='/'>
          <h1 className="title font-bold text-sm sm:text-xl flex flex-wrap">
            <span className="text-white sm:text-4xl">MahaKal</span>
            <span className="text-black-500 sm:text-xl">Construction</span>
          </h1>
        </Link>
        <ul className="flex gap-4">
          <li className="nav-item hidden sm:inline">
            <button className="hover:bg-sky-700 text-white px-3 py-2 rounded sm:text-xl">
              Home
            </button>
          </li>
          <li className="nav-item hidden sm:inline">
            <button className="hover:bg-sky-700 text-white px-3 py-2 sm:text-xl rounded">
              About
            </button>
          </li>
          <li className="nav-item sm:inline">
            <button className="hover:bg-sky-700 text-white px-3 py-2 sm:text-xl rounded">
              Sign In
            </button>
          </li>
        </ul>
        <form>
          <input
            type="text"
            placeholder="Search.."
            className="p-2 rounded border-2 border-white focus:outline-none focus:ring-2 focus:ring-sky-300"
          />
          
        </form>
      </div>
    </header>
  );
}
