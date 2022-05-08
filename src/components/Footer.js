import { Container, Nav, Row } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import "./Footer.css";
import { navcontents } from "./NavBar";

export default function Footer() {
  return (
    <Container fluid className="footer">
      <Row className="fhead justify-content-center">
        {" "}
        The Coral Culture & Restoration Wiktionary &copy; 2022
      </Row>
      <hr></hr>
      <Row>
        <Nav className="justify-content-center fnav">
          {navcontents.map((page, i) => (
            <LinkContainer to={page.extension} key={i}>
              <Nav.Link>{page.label}</Nav.Link>
            </LinkContainer>
          ))}
        </Nav>
      </Row>
    </Container>
  );
}
