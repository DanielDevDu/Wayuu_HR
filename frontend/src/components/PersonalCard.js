import React from "react";
import { useState, useEffect } from "react";
import { UserContext } from "../context/UserContext";

const defaultDepartment = {
  name: "",
  status: false,
};

const defaultRole = {
  name: "",
  status: false,
};

export default function PersonalCard({ data, departments, roles }) {
  const { full_name, email } = data;

  const { userInfo2, departments2, roles2, isAuthorized2, userId2 } = React.useContext(UserContext);

  console.log("----------")
  console.log(userInfo2)
  console.log(departments2)
  console.log(roles2)
  console.log(isAuthorized2)
  console.log(userId2);
  console.log("----------")

  const [activeDepartment, setDepartment] = useState(defaultDepartment);
  const [activeRole, setRole] = useState(defaultRole);

  useEffect(() => {
    departments.map((dep) => {
      dep.status === true && setDepartment(dep);
    });
    roles.map((role) => {
      role.status === true && setRole(role.role);
    });
    console.log("In Effect")
    console.log(activeRole)
    console.log("In Effect")
  }, [departments]);

  // setRole(roles.find((role) => role.status === true));

  // console.log(departments.find((dep) => dep.status === true));

  return (
    <div className="home-data fade-in">
      <div className="home-data-text1">
        <ul>
          <li>
            <span className="icon"> <i className="uil uil-user-circle"></i></span>
            <span className="text-tittle"> Name </span>
          </li>
          <li>
            <span className="icon"> <i className="uil uil-fast-mail"></i></span>
            <span className="text-tittle"> Email </span>
          </li>
          <li>
            <span className="icon"> <i className="uil uil-award-alt"></i></span>
            <span className="text-tittle"> Dep. </span>
          </li>
          <li>
            <span className="icon"> <i className="uil uil-swatchbook"></i></span>
            <span className="text-tittle"> Role </span>
          </li>
        </ul>
      </div>
      <div className="home-data-text2">
        <ul>
          <li>
            <span> {full_name} </span>
          </li>
          <li>
            <span> {email} </span>
          </li>
          <li>
            <span> {activeDepartment.name} </span>
          </li>
          <li>
            <span> {activeRole.name} </span>
          </li>
        </ul>
      </div>
    </div >
  );
}
