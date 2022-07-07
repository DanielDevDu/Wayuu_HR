// ======= Tools ======= //
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import React from 'react'

// ============ Component ========= //
export default function Profile({ login }) {

  // =========== States ============ //
  const [userInfo, setUserinfo] = React.useState({});


  React.useEffect(() => {
    setUserinfo(login)
  }, [])

  console.log(userInfo)
  return (
    <h1>You're in profile mf</h1>
  )
}