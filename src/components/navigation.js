import React from "react";
import { Routes, Route } from "react-router-dom";
import Bets from "./bets/bets";
import Contact from "./contact/contact";
import Donation from "./donation/donation";
import Experiments from "./experiments/experiments";
import LandingPage from "./home/landing";
import Posts from "./experiments/posts/posts.json";
import PostLayout from "./experiments/postLayout";
import getPostClass from "./experiments/posts/getter";

const Navigation = () => {
  const postRoutes = () => {
    return Object.keys(Posts.posts).map((post, idx) => {
      const title = Posts.posts[post].title;
      return (
        <Route
          key={idx}
          path={"/experiments/" + title.toLowerCase().replaceAll(" ", "-")}
          element={<PostLayout content={getPostClass(post)} />}
        />
      );
    });
  };

  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/experiments" element={<Experiments />} />
      {postRoutes()}
      <Route path="/bets" element={<Bets />} />
      <Route path="/contact-us" element={<Contact />} />
      <Route path="/donation" element={<Donation />} />
    </Routes>
  );
};

export default Navigation;
