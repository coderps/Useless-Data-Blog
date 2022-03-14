import React from "react";
import { Routes, Route } from "react-router-dom";
import Bets from "./bets/bets";
import Contact from "./contact/contact";
import Donation from "./donation/donation";
import Experiments from "./experiments/experiments";
import LandingPage from "./home/landing";

const Navigation = () => {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/experiments" element={<Experiments />} />
      <Route path="/bets" element={<Bets />} />
      <Route path="/contact-us" element={<Contact />} />
      <Route path="/donation" element={<Donation />} />
    </Routes>
  );
};

export default Navigation;
