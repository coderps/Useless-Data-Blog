import React from "react";
import Post1 from "./post1";
import Post2 from "./post2";

const getPostClass = (post) => {
  switch (post) {
    case "post1":
      return <Post1 />;
    case "post2":
      return <Post2 />;
    default:
      return <div>Not Found</div>;
  }
};

export default getPostClass;
