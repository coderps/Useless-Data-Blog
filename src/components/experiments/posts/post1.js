import React from "react";
import Posts from "./posts.json";

class Post1 extends React.Component {
  constructor(props) {
    super(props);
    this.title = Posts.posts.post1.title;
  }

  render() {
    return <div>My content</div>;
  }
}

export default Post1;
