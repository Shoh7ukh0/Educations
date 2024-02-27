import { Routes, Route } from "react-router-dom";
import AuthRoutes from "./routes/authRoutes";
import { authRoutes, protectedRoutes } from "./config/routes";
import AppRoute from "./assets/components/AppRoute";
import ProtectedRputes from './routes/protectedRoutes';
import { Suspense } from "react";
import { useSelector } from "react-redux";

const App = () => {
  const { signedIn } = useSelector(s => s.session);

  return (
    <Suspense fallback={<h1>Loading...</h1>}>
        <Routes>
          <Route path="/" element={<ProtectedRputes signedIn={signedIn} />}>
              {protectedRoutes.map(route => 
                <Route path={route.path} element={<AppRoute element={route.element}/>} key={route.key} />
              )}
          </Route>
          <Route path="/" element={<AuthRoutes signedIn={signedIn} />}>
            {authRoutes.map(route => 
              <Route path={route.path} element={<AppRoute element={route.element}/>} key={route.key} />
            )}
          </Route>
          <Route path="*" element={<h1>Page Not Found</h1>}></Route>
        </Routes>
    </Suspense>
  );
};

export default App;