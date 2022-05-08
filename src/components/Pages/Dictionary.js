// use JSON for contents

import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import definitions from "../../contents/definitions.json";

export default function Dictionary() {
  // const defs = definitions.map()

  return (
    <Container className="Page">
      <PageTitle title="Dictionary" />
      <Container className="dictionary">
        {definitions.map((word, i) => (
          <p key={i}>
            <b>{word.TERM}</b> (<i>{word.ROLE}</i>) <br></br>
            {word.DEFINITION}
            {/* make conditionals for referrals (see also) */}
            {word.REFERRALS.length >= 2 && (
              <span>
                {" "}
                See also <a href={word.REFERRALS}>{word.REFERRALS}</a>
              </span>
            )}
          </p>
        ))}
      </Container>
    </Container>
  );
}
