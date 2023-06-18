import { userState } from "react"
const Dashboard =() => {
    const [open, setOpen] = userState(true);
    return (
        <div className="flex">
            <div className={`${open ? 'w-72': "w-20"} duration-300 h-screen bg-dark-purple`}>
                <img
                 src="./src/assests/control.png"
                 className={`absolute cursor-pointer rounded h-full
                 -right-3 top-9 w-7 border-2 border-dark-purple $(!open && 'rotate-180'}`}
                 onClick={() => setOpen(!open)}
                 />
            </div>
            <div className="p-7 text-2x1 font-semibold">
                <hi>Home Page</hi>
            </div>
         </div>
    )
}

export default Dashboard;