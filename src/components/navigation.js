import React from "react";
import { Routes, Route } from "react-router-dom";
import LandingPage from "./home/landing";

const Navigation = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
    </Routes>
  );
};

export default Navigation;
