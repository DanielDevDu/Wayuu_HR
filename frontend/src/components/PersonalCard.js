import React from 'react';

export default function PersonalCard() {
  const [employeeInfo, setEmployeeInfo] = React.useState({})

  const [employeeCard, setEmployeeCard] = React.useState({
    full_name: "",
    roles: "",
    email: "",
    department: "",
  })

  React.useEffect(function () {
    console.log("success")
    fetch("http://localhost:8000/api/employee/5db3017e-18ac-4c3a-a4a9-54d48046b656/", {
      headers: {
        'Authorization': 'Basic ' + btoa("tester.staff23@gmail.com:Dcba654321")
      }
    })
      .then(res => res.json())
      .then(data => setEmployeeInfo(data))
  }, [])

  function placeholder() {
    setEmployeeCard(prevState => ({
      ...prevState,
      full_name: employeeInfo.full_name,
      roles: employeeInfo.employee_role.map(role => role.status ? role.role : ''),
      email: employeeInfo.email,
      department: employeeInfo.employee_department.map(dept => dept.status ? dept.department : ''),
    }))
  }

  console.log(employeeCard)

  return (
    <div className="home-data fade-in">
      <button onClick={placeholder}>Render</button>
      <ul>
        <li>
          <span className="icon"> <i className="uil uil-user-circle"></i></span>
          <span className="text-tittle"> Name </span>
          <span className="text1"> {employeeCard.full_name} </span>
        </li>
        <li>
          <span className="icon"> <i className="uil uil-user-circle"></i></span>
          <span className="text-tittle"> Email </span>
          <span className="text2"> {employeeCard.email} </span>
        </li>
        <li>
          <span className="icon"> <i className="uil uil-award-alt"></i></span>
          <span className="text-tittle"> Department </span>
          <span className="text3"> {employeeCard.department} </span>
        </li>
        <li>
          <span class="icon"> <i class="uil uil-swatchbook"></i></span>
          <span className="text-tittle"> Role </span>
          <span className="text4"> {employeeCard.roles} </span>
        </li>
      </ul>
    </div>
  )
}