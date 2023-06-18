import {useState} from 'react'
import styles from '../style';
import { close, logo, menu } from '../assets';
import { dashLinks } from '../constants';

const Navbar = () => {
  const [toggle, setToggle] = useState(false);
  return (
    <nav className="w-full flex py-6 justify-between items-center navbar">
      <img src={logo} alt="Auth Insurance" className="w-[150px] h-[100px]"/>

      <ul className="list-none sm:flex hidden justify-end items-center flex-1">
        {dashLinks.map((nav, index) => (
          <li
            key={nav.id}
            className={`font-poppins font-normal cursor-pointer text-[16px] pe-5 ${index === dashLinks.length - 1 ? 'mr-0' : 'mr-10'} text-white`}
          >
            <a href={`#${nav.id}`}>
              {nav.title}
            </a>
          </li>
        ))}
          <li>
            <button className={`py-3 px-6 ml-5 rounded bg-blue-gradient font-poppins font-medium text-[16px] text-white outline-none  ${styles}`}> Log Out </button>
          </li>
      </ul>

      <div className="sm:hidden flex flex-1 justify-end items-center">
          <img 
          src={toggle ? close : menu}
          alt="menu"
          className="w-[28px] h-[28px] object-contain"
          onClick={() => setToggle((prev) => !prev)}
          />

          <div className={`${toggle ? 'flex' : 'hidden'} p-6 bg-black-gradient absolute top-20 right-0 mx-4 my-2 min-w-[140px] rounded-xl sidebar`}>
            <ul className="list-none flex flex-col justify-end items-center flex-1">
              {dashLinks.map((nav, index) => (
                <li
                 key={nav.id}
                 className={`font-poppins font-normal cursor-pointer text-[16px] ${index === dashLinks.length - 1 ? 'mr-0' : 'mb-4'} text-white`}
                >
                  <a href={`#${nav.id}`}>
                    {nav.title}
                  </a>
                </li>
              ))}
              <li>
                <button className={`py-4 px-6 rounded bg-blue-gradient font-poppins font-medium text-[18px] text-white outline-none mt-5 ${styles}`}> Log Out </button>
              </li>
            </ul>
          </div>
      </div>   

    </nav>
  )
}

export default Navbar
