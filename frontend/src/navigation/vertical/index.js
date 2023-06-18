import {Mail, Home, Settings, Target, Users, CreditCard, Folder, Anchor, MapPin, Package, ShoppingCart, TrendingUp} from 'react-feather'

export default[

    {
        id: 'home',
        title: 'Home',
        icon: <Home size={20}/>,
        navLink: '/home'
    },
    {
        id: 'payment',
        title: 'Payment',
        icon: <Home size={20}/>,
        navLink: '/payment'
    },
    {
        id: 'settings',
        title: 'Settings',
        icon: <Home size={20}/>,
        navLink: '/settings'
    },
    {
        id: 'history',
        title: 'History',
        icon: <Home size={20}/>,
        navLink: '/history'
    },

    {
        id: 'report',
        title: 'Report',
        icon: <Home size={20}/>,
        navLink: '/report',
    },
    {
        header: 'User Details',
        children:[
            {
                id: 'List',
                title: 'List',
                icon: <List size ={20} />,
                navLink: '/'
            },
            {
                id: 'List',
                title: 'List',
                icon: <List size ={20} />,
                navLink: '/'
            }
        ]
    },

]