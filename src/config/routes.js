import React from "react";

export const authRoutes = [
    {
        path: '/register',
        element: React.lazy(() => import('./../pages/auth/register')),
        key: 'register'
    },
    {
        path: '/login',
        element: React.lazy(() => import('./../pages/auth/login')),
        key: 'login'
    }
];

export const protectedRoutes = [
    {
        path: '/',
        element: React.lazy(() => import('./../pages/private/home/home')),
        key: 'home'
    }
];