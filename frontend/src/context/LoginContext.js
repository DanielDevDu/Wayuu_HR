import React from 'react';
import axios from "axios";
const { REACT_APP_ENDPOINT_API } = process.env;

export const LoginContext = React.createContext();


// ============== Context Component =================== //

export const AuthProvider = ({ children }) => {

  // ===================== States ======================= //

  const [userId3, setUserId] = React.useState("");
  const [isAuthorized3, setIsAuthorized2] = React.useState(true);

  return (
    <LoginContext.Provider value={{ isAuthorized3, userId3 }} >
      {children}
    </LoginContext.Provider>
  )
}