// use JSON for contents

import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import Definitions from "../Utilities/compileDefinitions";

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
    // use target of event?
    // anchorElem.animate([
    //   { transform: "scale(1.1)" },
    //   { duration: "1s" },
    //   { iterations: "1" },
    //   { delay: "0.6s" },
    // ]);
  };
  const definitions = [...Definitions()];
  console.log(definitions);

  return (
    <Container className="Page">
      <PageTitle title="Dictionary" />
      <Container className="dictionary">
        {definitions.map(({ TERM, TYPE, DEFINITION, REFERRALS }, i) => (
          <p key={i} id={TERM.trim()}>
            <b className="term">{TERM}</b> (<i className="type">{TYPE}</i>){" "}
            <br></br>
            {DEFINITION}
            {/* conditionally show referrals */}
            {/* needs to be updated to take list of referrals? */}
            {REFERRALS.length >= 1 && (
              <span>
                {" "}
                See also{" "}
                <a
                  className="ref-link"
                  href={`#${REFERRALS[0]}`}
                  onClick={handleAnchorClick}>
                  {REFERRALS[0]}
                </a>
              </span>
            )}
            {/* {REFERRALS.map((ref) => (
              <span>
                {" "}
                See also{" "}
                <a
                  className="ref-link"
                  href={`#${ref}`}
                  onClick={handleAnchorClick}>
                  {ref}
                </a>
              </span>
            ))} */}
          </p>
        ))}
      </Container>
    </Container>
  );
}
