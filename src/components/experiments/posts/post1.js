import React from "react";
import Posts from "./posts.json";
import theory from "../../../static/img/post1-theory.jpg";
import "../../../static/css/posts.scss";

class Post1 extends React.Component {
  constructor(props) {
    super(props);
    this.title = Posts.posts.post1.title;
    this.author = "Irene";
    this.date = (
      <>
        19<sup>th</sup> April 2020
      </>
    );
  }

  render() {
    return (
      <div className="post">
        <div className="title">{this.title}</div>
        <div className="author">
          - By {this.author}, {this.date}
        </div>
        <div className="content">
          <p>
            When I first heard this idea from Prax I got very excited: measuring
            the changes in height during the day due to gravity… such a
            non-sense experiment! What I didn't know is that he really meant it:
            he was convinced that the gravity can swing our heights a few
            centimetres up and down every day. A few centimetres!
          </p>
          <p>
            <b>So the idea is simple:</b> when you are standing, the gravity
            will exert more pressure in your longitudinal axis and you will
            shorten; on the contrary, when you are lying the gravity force will
            be perpendicular to you so you will elongate. Here is a simple
            depiction:
          </p>
          <figure>
            <p>
              <img src={theory} alt="theory" className="img-theory" />
            </p>
            <figcaption>Theory</figcaption>
          </figure>
          <p>
            And I repeat: we are not talking about small changes in the
            microscale, <b>we are talking about various cm difference.</b>
          </p>
          <p>I had to prove him wrong, so I accepted the challenge.</p>

          <div className="header">Hypothesis</div>
          <p>
            <b>The height will decrease throughout the day more than 1 cm</b>{" "}
            (due to the effect of gravity).
          </p>
          <p>
            Note that I wrote <i>“due to the effect of gravity”</i> into
            parenthesis because we can't determine the actual cause of the
            height reduction. We still don't have zero-gravity rooms.
          </p>
          <p>
            <b>- Prax's prediction:</b> yes, of course, height decreases with
            gravity a few cm every day and increases during the night while you
            sleep. Didn't you know it?
          </p>
          <p>
            <b>- Irene's prediction:</b> bullshit.
          </p>

          <div className="header">Methods</div>
          <p>
            Two height measurements we taken for each day: 1 before sleeping and
            1 after waking up. Each measurement was repeated two to three times
            to have an estimation of the error. The experiment was conducted for
            4 days.
          </p>
          <p>
            The height measurement system consisted of the following items:
            <ul>
              <li>- A wall</li>
              <li>- Measuring tape</li>
              <li>- Tape (to tape the tape)</li>
              <li>- The lid of a box</li>
              <li>- A clipboard with a painted owl</li>
              <li>- Pen and paper</li>
              <li>
                - Determination to wake up together at the same time every day
              </li>
            </ul>
          </p>
          <p>The measuring method can be seen in the following images:</p>
        </div>
      </div>
    );
  }
}

export default Post1;
