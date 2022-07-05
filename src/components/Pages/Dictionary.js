// use JSON for contents

import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import definitions from "../../contents/definitions.json";

export default function Dictionary() {
  const handleAnchorClick = (event) => {
    let hash = event.target.hash;
    let anchorElem = document.querySelector(hash);
    if (anchorElem == null) {
      let linkParentElem = event.target;
      linkParentElem.style.color = "red";
    }
    event.preventDefault();
    anchorElem.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
    // animate the word so users know which one it is?
    // anchorElem.animate([
    //   { transform: "scale(1.1)" },
    //   { duration: "1s" },
    //   { iterations: "1" },
    //   { delay: "0.6s" },
    // ]);
  };

  return (
    <Container className="Page">
      <PageTitle title="Dictionary" />
      <Container className="dictionary">
        {definitions.map((word, i) => (
          <p key={i} id={word.TERM.trim()}>
            <b className="term">{word.TERM}</b> (
            <i className="type">{word.TYPE}</i>) <br></br>
            {word.DEFINITION}
            {/* conditionally show referrals */}
            {word.REFERRALS.length >= 2 && (
              <span>
                {" "}
                See also{" "}
                <a
                  className="ref-link"
                  href={`#${word.REFERRALS}`}
                  onClick={handleAnchorClick}>
                  {word.REFERRALS}
                </a>
              </span>
              // need to sort out 'coined by' and
            )}
          </p>
        ))}
      </Container>
    </Container>
  );
}
