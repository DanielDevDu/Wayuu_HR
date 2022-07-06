// ======= Styles ====== //
import "./index.css";

// ======= Tools ======= //
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react'

// ======= Pages ======= //
import Login from './pages/Login'
import Profile from './pages/Profile'


// ============================= App Function ===================== //

export default function App() {

  // =============== States =========== //

  const [userId, setUserId] = React.useState(null);
  const [login, setLogin] = React.useState({})

  console.log("----- app ----")
  console.log(login)
  console.log("----- app ----")

  // =============== JSX ============== //

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Login setLogin={setLogin} login={login} />} />
        <Route path='profile' element={<Profile userId={login} />} />
      </Routes>
    </BrowserRouter>
  )
}