import React from 'react';

export default function PersonalCard() {
  const [employee, setEmployee] = React.useState({})


  React.useEffect(function () {
    console.log("success")
    fetch("http://localhost:8000/api/employee/7b2dbe4f-e51b-4e76-8f7b-3ccc86ce8306/", {
      headers: {
        'Authorization': 'Basic ' + btoa("admin.test13@gmail.com:123456")
      }
    })
      .then(res => res.json())
      .then(data => setEmployee(data))
  }, [])

  return (
    <pre>{JSON.stringify(employee, null, 2)}</pre>
  )

}