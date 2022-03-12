import React from "react";
import "../../static/css/general.css";

const Intro = () => {
  const IreneProfileLink = "https://www.instagram.com/miausola/";
  const PraxProfileLink = "https://www.instagram.com/praxtheslayer/";

  return (
    <div className="theme-borders monospace-font intro">
      Hey! Welcome to our page! We are a psycho-biologist [
      <a href={IreneProfileLink} target="_blank">
        Irene
      </a>
      ] and a geeky computer scientist [
      <a href={PraxProfileLink} target="_blank">
        Prax
      </a>
      ] who enjoy conducting useless experiments and post them on this website.
      The experiments presented here may content unreliable and bizarre
      information; if you value science too much, we do not encourage you to
      read these posts.
    </div>
  );
};

export default Intro;
