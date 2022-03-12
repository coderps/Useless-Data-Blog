import React from "react";
import Logo from "../logo";
import Intro from "./intro";
import "../../static/css/landing.css";

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Logo />
      <div className="general-padding">
        <Intro />
      </div>
    </div>
  );
};

export default LandingPage;
