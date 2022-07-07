// ======= Styles ======= //
import "../Login.css";

// ======= Tools ======= //
import { useNavigate } from 'react-router-dom';
import React from 'react'


// =================== Component ======================= //
export default function Login({ setLogin, login }) {

  // =========== States ====================== //
  const [email, setEmail] = React.useState("")
  const [password, setPassword] = React.useState("")
  const [resp, setResp] = React.useState({})

  // ============= Routing =================== //
  const navigate = useNavigate()

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);
    fetch("http://localhost:8000/api/login/", {
      method: "POST",
      body: formData
    })
      .then(response => response.json())
      .then(result => setLogin(result))
  }

  function navigateProfile() {
    if (login.status === 200) {
      navigate('/profile')
    }
  }
  React.useEffect(() => {
    setLogin(login)
  }, [])

  React.useEffect(() => {
    navigateProfile()
  }, [login])


  // =================== JSX ======================= //
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
                  onChange={(e) => setEmail(e.target.value)}
                  value={email}
                />
              </div>
            </div>
            <div className="__Login__input-div pass">
              <div className="__Login__i">
                <i className="__Login__fas __Login__fa-lock"></i>
              </div>
              <div className="__Login__div">
                <input
                  type="password"
                  className="__Login__input"
                  placeholder="Password"
                  onChange={(e) => setPassword(e.target.value)}
                  value={password}
                />
              </div>
            </div>
            <a href="#">Forgot Password?</a>
            <button
              className="__Login__btn"
              onClick={handleSubmit}
            >
              Login</button>
          </form>
        </div>
      </div>
    </main>
  )
}