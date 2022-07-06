import React from 'react';
import axios from "axios";
import { LoginContext } from "./LoginContext";
const { REACT_APP_ENDPOINT_API } = process.env;

export const UserContext = React.createContext();



const defaultDepartment = {
  name: "",
  status: false,
};

const defaultRole = {
  name: "",
  status: false,
};


// ==================== API Requests ========================== //

const headers = {
  Authorization: "Basic " + btoa("admin.test11@gmail.com:Dcba654321"),
};

export const GetUserInfo2 = async (id) => {
  const URL = `${REACT_APP_ENDPOINT_API}employee/${id}/`;
  return await axios.get(URL, { headers });
};


// ============== Context Component =================== //

export const DataProvider = ({ children }) => {

  // ===================== Context imports =============== //

  // const { userId3 } = React.useContext(LoginContext);

  // ===================== States ======================= //

  // const [userInfo2, setUserInfo2] = React.useState({ userIn: "test" });
  // const [departments2, setDepartments2] = React.useState(["dept", "test"]);
  // const [roles2, setRoles2] = React.useState(["roles", "test"]);
  // const [isAuthorized2, setIsAuthorized2] = React.useState(false);
  // const [userId2, setUserId2] = React.useState(userId3);
  const [password, setPassword] = React.useState("aaa");



  // ==================== State Modifiers ============= //

  // React.useEffect(() => {
  //   GetUserInfo2(userId2).then((response) => {
  //     setUserInfo2(response.data);
  //     setDepartments2(response.data.departments);
  //     setRoles2(response.data.roles);
  //     console.log("++++")
  //     console.log(response)
  //   });
  // }, [isAuthorized2]);



  // ===================== JSX ====================== //
  return (
    <UserContext.Provider value={{
      // userInfo2,
      // departments2,
      // roles2,
      // isAuthorized2,
      // userId2,
      password,
      setPassword,
    }} >
      {children}
    </UserContext.Provider>
  )
}