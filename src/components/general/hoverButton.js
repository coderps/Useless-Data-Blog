import React from "react";
import "../../static/css/landing.scss";

const HoverButton = (props) => {
  return (
    <div className="hover-btn">
      <span>{props.text}</span>
    </div>
  );
};

export default HoverButton;
