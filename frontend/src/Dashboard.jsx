import { userState } from "react"
const Dashboard =() => {
    const [open, setOpen] = userState(true);
    const Menus = [
        { title: "Dashboard", src: "Chart_fill"},
        { title: "Accounts", src: "User", gap:true},
        { title: "Analytics", src: "Chart"},
        { title: "Settings", src: "Settings"}
    ]
    return (
        <div className="flex">
            <div className={`${open ? 'w-72': "w-20"} 
            duration-300 h-screen p-5 pt-8 bg-dark-purple`}>
                <img
                 src="./src/assests/control.png"
                 className={`absolute cursor-pointer rounded h-full
                 -right-3 top-9 w-7 border-2 border-dark-purple $(!open && 'rotate-180'}`}
                 onClick={() => setOpen(!open)}
                 />
                 <div className ="flex gap-x-4 items-center">
                    <img src = "./src.assests/logo.png" 
                    className={`cursor-pointer duration-500 ${
                        open && "rotate-[360deg]"}`}
                    />
                    <hi className={`text-white origin-left font-medium text-xl 
                    duration-300 ${!open &&  `scale-0`}`}>Designer</hi>
                 </div>
                 <ul className="pt-6">
                    {Menus.map((menu,index) =>  (
                        <li key={index} 
                            className={`text-gray-300 text-sm flex items-center
                            gap-x-4 cursor-pointer p-2 hover:bg-light-white rounded-mds
                            ${menu.gap ? "mt-9" : "mt-2"} ${index === 0 && "bg-light-white"}'}`}>
                            <img src= {`./src/assets/${menu.src}.png`} />
                            <span className={`${!open && 'hidden'} origin-left duration-200`}>{menu.title}</span>
                        </li>
                    ))}
                 </ul>
            </div>
            <div className="p-7 text-2x1 font-semibold flex-1 h-screen">
                <hi>Home Page</hi>
            </div>
         </div>
    )
}

export default Dashboard;