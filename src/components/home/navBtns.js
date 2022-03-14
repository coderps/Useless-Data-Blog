import React from "react";
import { Link } from "react-router-dom";
import HoverButton from "../general/hoverButton";

const NavBtns = () => {
  return (
    <div className="navBtns">
      <Link to="/experiments">
        <HoverButton text="Experiments" />
      </Link>
      <Link to="/bets">
        <HoverButton text="Bets" />
      </Link>
      <Link to="/contact-us">
        <HoverButton text="Contact Us" />
      </Link>
    </div>
  );
};

export default NavBtns;
