import PersonalCard from "./PersonalCard";
import ProfilePicture from "./ProfilePicture";
import React from "react";


export default function MidSection({ data, departments, roles, userId, setUserId }) {

  setUserId("Cristian")

  return (
    <div className="mid-side">
      <div className="mid-content fade-in">
        <ProfilePicture />
        <PersonalCard data={data} departments={departments} roles={roles} />
      </div>
    </div>
  );
}
