import React from 'react';
import "../Login.css";
import { DataProvider } from '../context/UserContext';

export default function Login({ setUserId, userId, setIsAuthorized }) {

  //const { password, setPassword } = React.useContext(DataProvider)



  // ================= JSX ================== //

  return (
    <main>
      <img className="__Login__wave"
        src="https://github.com/Daniel13713/Wayuu_HR/blob/frontend/frontend/img/wave.png?raw=true"
      />
      <div className="__Login__container">
        <div className="__Login__img">
          <img src="https://raw.githubusercontent.com/Daniel13713/Wayuu_HR/5022cb44ddb48084b3bc11a35163215606d86960/frontend/img/bg.svg" />
        </div>
        <div className="__Login__login-content">
          <form>
            <img src="https://raw.githubusercontent.com/Daniel13713/Wayuu_HR/5022cb44ddb48084b3bc11a35163215606d86960/frontend/img/avatar.svg" />
            <h2 className="__Login__title">Welcome</h2>
            <div className="__Login__input-div one">
              <div className="__Login__i">
                <i className="__Login__fas __Login__fa-user"></i>
              </div>
              <div className="__Login__div">
                <input
                  type="text"
                  className="__Login__input"
                  placeholder="E-mail"
                  onChange={(e) => setUserId(e.target.value)}
                />
              </div>
            </div>
            <div className="__Login__input-div pass">
              <div className="__Login__i">
                <i className="__Login__fas __Login__fa-lock"></i>
              </div>
              <div className="__Login__div">
                <input type="password" className="__Login__input" placeholder="Password" />
              </div>
            </div>
            <a href="#">Forgot Password?</a>
            <button className="__Login__btn" onClick={() => setIsAuthorized(true)}>Login</button>
          </form>
        </div>
      </div>
    </main>
  )
}