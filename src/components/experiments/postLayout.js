import React from "react";
import "../../static/css/experiments.scss";
import Logo from "../general/logo";

const PostLayout = (props) => {
  return (
    <div>
      <Logo font="medium" />
      <div className="post-layout">{props.content}</div>
    </div>
  );
};

export default PostLayout;
