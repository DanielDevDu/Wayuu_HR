import "./index.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { DataProvider } from "./context/UserContext";
import { AuthProvider } from "./context/LoginContext";

import Login from "./components/Login";
import MidSection from "./components/MidSection";
import LeftSection from "./components/LeftSection";
import RightSection from "./components/RightSection";
import { useEffect, useState } from "react";
import { GetUserInfo } from "./Services/UserService";

function App() {
  const [isAuthorized, setIsAuthorized] = useState(false);

  const [userInfo, setUserInfo] = useState({});
  const [departments, setDepartments] = useState([]);
  const [roles, setRoles] = useState([]);

  const [userId, setUserId] = useState("");

  useEffect(() => {
    GetUserInfo(userId).then((response) => {
      setUserInfo(response.data);
      setDepartments(response.data.employee_department);
      setRoles(response.data.employee_role);
    });
  }, [isAuthorized]);

  console.log("********")
  console.log(userInfo)
  console.log("********")

  if (!isAuthorized) {
    return (
      <BrowserRouter>
        <Routes>
          <Route
            path="/"
            element={
              <>
                {/* <input onChange={(e) => setUserId(e.target.value)}></input>
                <button onClick={() => setIsAuthorized(true)}>Login</button> */}

                <Login
                  setUserId={setUserId}
                  userId={userId}
                  setIsAuthorized={setIsAuthorized}
                />
              </>
            }
          />
        </Routes>
      </BrowserRouter >
    );
  }

  return (
    <main className="App">
      <div className="container">
        <AuthProvider>
          <DataProvider>
            <LeftSection />
            <MidSection
              data={userInfo}
              departments={departments}
              roles={roles}
              setUserId={setUserId}
              userId={userId}
            />
            <RightSection />
          </DataProvider>
        </AuthProvider>
      </div>
    </main>
  );
}

export default App;
