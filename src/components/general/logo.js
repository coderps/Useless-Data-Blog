import React from "react";
import "../../static/css/general.scss";

const Logo = (props) => {
  const font = props.font === undefined ? "" : "-" + props.font;
  return <div className={"logo" + font}>USELESS DATA</div>;
};

export default Logo;
