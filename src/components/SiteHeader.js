import { Col } from "react-bootstrap";
import Container from "react-bootstrap/container";
import Row from "react-bootstrap/Row";
import "./SiteHeader.css";
// import sclogo from "../images/SC_vectorLogo_crop.png";

export default function SiteHeader() {
  return (
    <Container fluid className="siteHeader">
      <Row>
        <Col className="title" md>
          <h1>The Coral Culture & Restoration Wiktionary</h1>
        </Col>
        <Col className="logos" md>
          <img
            src={`${process.env.PUBLIC_URL}/images/SC_vectorLogo_crop.png`}
            width="100"
            alt={"Seascape Caribbean"}
          />
        </Col>
      </Row>
    </Container>
  );
}
