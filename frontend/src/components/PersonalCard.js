import React from 'react';

export default function PersonalCard() {
  const [employeeCard, setEmployeeCard] = React.useState({
    full_name: "",
    roles: "",
    email: "",
  })
  const [employeeInfo, setEmployeeInfo] = React.useState({})

  React.useEffect(function () {
    console.log("success")
    fetch("http://localhost:8000/api/employee/2141d567-272a-4a10-a35c-bc89679d4448/", {
      headers: {
        'Authorization': 'Basic ' + btoa("admin.test13@gmail.com:123456")
      }
    })
      .then(res => res.json())
      .then(data => setEmployeeInfo(data))
  }, [])

  function placeholder() {
    setEmployeeCard(() => {
      return (
        {
          full_name: employeeInfo.full_name,
          roles: employeeInfo.roles,
          email: employeeInfo.email,
        }
      )
    })
  }


  return (
    <fieldset>
      <p>picture goes here</p>
      <div>
        <p>Employee name: {employeeInfo.full_name}</p>
        <p>Role: {employeeInfo.role}</p>
        <p>e-mail: {employeeInfo.email}</p>
      </div>
    </fieldset>
  )

}