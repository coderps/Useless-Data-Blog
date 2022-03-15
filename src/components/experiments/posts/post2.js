import React from "react";
import Posts from "./posts.json";

class Post2 extends React.Component {
  constructor(props) {
    super(props);
    this.title = Posts.posts.post2.title;
  }

  render() {
    return <div>My content 2</div>;
  }
}

export default Post2;
