import React from "react";
import Posts from "./posts/posts.json";
import { Link } from "react-router-dom";
import PostLayout from "./postLayout";
import "../../static/css/experiments.scss";

const Experiments = () => {
  const NumOfPosts = Object.keys(Posts.posts).length;

  const getPosts = () => {
    return Object.keys(Posts.posts).map((post, idx) => {
      const title = Posts.posts[post].title;
      return (
        <div key={idx}>
          <Link to={"/experiments/" + title.toLowerCase().replaceAll(" ", "-")}>
            {title}
          </Link>
        </div>
      );
    });
  };

  const getPostLinks = () => {
    return (
      <>
        Posts so far: {NumOfPosts} and counting...
        {getPosts()}
        ...Pokemon Cards Go Here
      </>
    );
  };

  return <PostLayout content={getPostLinks()} />;
};

export default Experiments;
