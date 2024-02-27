import { Navigate, Outlet } from "react-router-dom";

export default function AuthRoutes({signedIn}) {
    if (signedIn) {
        return <Navigate to='/' />
    }
    return <Outlet />
}