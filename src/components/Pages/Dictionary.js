// use JSON for contents

import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import { dictionaryContents } from "../../contents/dictionaryContents";

export default function Dictionary() {
  return (
    <Container className="Page">
      <PageTitle title="Dictionary" />
      <Container>
        {dictionaryContents.map((word) => (
          <p>
            <b>{word.term}</b> (<i>{word.type}</i>) <br></br>
            {word.definition}
            {/* make conditionals for referrals (see also) */}
            {/* {&& word.referral.length > 2 ()} */}
          </p>
        ))}
      </Container>
    </Container>
  );
}
