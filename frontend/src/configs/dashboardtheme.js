//customize the theme of the dashboard to enhance user experience with alerts

//skeleton

const dashboardtheme = {
    app :{
        appName: 'AI Authentication',
        appLogoImage: require('@src\assets\logo.png').default
    },
    layout: {
        isRTL: false,
        skin: 'light',
        routerTransition: 'fadeIn',
        type: 'vertical',
        contentwidth: 'full',
        menu: {
            isHidden: false,
            isCollapsed: false
        },
        navbar:{
            type: 'floating',
            backgroundColor: 'primary',
        },
        footer:{
            type: 'static'
        },
        customizer: false,
        scrolling: true
    }
}