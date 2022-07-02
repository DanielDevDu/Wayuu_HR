import React from 'react';

export default function LeftSection() {
  return (
    <div className="left-side">
      <div className="left-content">
        <div className="imgBx fade-in">
          <img src="https://github.com/Daniel13713/Wayuu_HR/blob/frontend/frontend/img/Screenshot_2-removebg-preview.png?raw=true" />
        </div>
        <div className="wayuutitle fade-in">
          <h3 className="home__title"> Wayuu HR </h3>
        </div>
        <div className="left-button fade-in">
          <button className="custom-btn btn-1">Resume</button>
          <button className="custom-btn btn-1">Legal</button>
          <button className="custom-btn btn-1">Man</button>
          <button className="custom-btn btn-1">Team</button>
          <button className="custom-btn btn-1">C. Emp</button>
          <button className="custom-btn btn-1">C. Dept</button>
          <button className="custom-btn btn-1">C. Role</button>
        </div>
      </div>
    </div>
  )
}