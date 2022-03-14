import React from "react";
import Logo from "../general/logo";
import Intro from "./intro";
import "../../static/css/landing.scss";
import NavBtns from "./navBtns";
import DonateBtn from "./donateBtn";

const LandingPage = () => {
  return (
    <div className="landing-page">
      <Logo />
      <div className="general-padding">
        <Intro />
        <NavBtns />
        <DonateBtn />
      </div>
    </div>
  );
};

export default LandingPage;
