import { Navigate, Outlet } from "react-router-dom";

const ProtectedRoutes = ({signedIn}) => {
    if (!signedIn) {
        return <Navigate to='/register'/>
    }
    return <Outlet />
}

export default ProtectedRoutes;