import React from "react";
import Posts from "./posts/posts.json";
import { Link } from "react-router-dom";
import PostLayout from "./postLayout";
import "../../static/css/experiments.scss";
import image from "../../static/img/Image.jpg";

const Experiments = () => {
  const NumOfPosts = Object.keys(Posts.posts).length;

  const getPosts = () => {
    return Object.keys(Posts.posts).map((post, idx) => {
      const title = Posts.posts[post].title;
      const link = title.toLowerCase().replaceAll(" ", "-");
      return (
        <div className="card" key={idx}>
          <div className="title">
            <Link to={"/experiments/" + link}>{title}</Link>
          </div>
          <div className="imager">
            <img src={image} alt="useless" />
          </div>
        </div>
      );
    });
  };

  const getPostLinks = () => {
    return (
      <>
        Posts so far: {NumOfPosts} and counting...
        <div className="cards">{getPosts()}</div>
      </>
    );
  };

  return <PostLayout content={getPostLinks()} />;
};

export default Experiments;
