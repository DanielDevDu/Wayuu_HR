import PersonalCard from './PersonalCard';
import ProfilePicture from './ProfilePicture';
import React from 'react';

const EMPLOYEE = "http://localhost:8000/api/employees/";



export default function MidSection() {
  return (
    <div className="mid-side">
      <div className="mid-content fade-in">
        <ProfilePicture />
        <PersonalCard />
      </div>
    </div>
  );
}

