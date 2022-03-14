import React from "react";
import { Link } from "react-router-dom";
import "../../static/css/landing.scss";

const DonateBtn = () => {
  return (
    <Link to="/donation">
      <div className="donateBtn">
        <span className="gradient-green">
          <b>Donate Us</b>
        </span>
        <span className="smaller">(we are poor)</span>
      </div>
    </Link>
  );
};

export default DonateBtn;
