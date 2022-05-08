import { Row, Col, Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import "../../App.css";

export default function AboutUs() {
  return (
    <Container className="Page">
      <PageTitle title="About" />
      <Row>
        <Col>
          Hello! This site was created by Amanda Ho-Lyn in an effort to create a
          more centralised base for the coral lexicon. She grew up in Jamaica -
          born to a former diver who ran SunDivers no less! This project is
          currently looking for contributors and funding. If you're interested,
          reach out.
          <br></br>
          <sub>
            In future this section will have a more fleshed out description of
            what the project is and aims to do, with less of a personal touch.
          </sub>
        </Col>
        <Col xs={2}>pic</Col>
      </Row>
    </Container>
  );
}
