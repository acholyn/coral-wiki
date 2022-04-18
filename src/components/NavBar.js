import { Nav, Navbar, Row, Col } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

export let navcontents = [
  { label: "Home", extension: "/" },
  { label: "Contributors", extension: "contributors" },
  { label: "About Us", extension: "about" },
  { label: "Contact Us", extension: "contact" },
  { label: "Search", extension: "search" },
];
export default function NavBar() {
  return (
    <Row
      fluid="true"
      className="me-auto justify-content-center border-bottom border-secondary">
      <Navbar bg="light" variant="light">
        {" "}
        <Col xs={2} />
        <Col className="ms-auto">
          <Nav className="justify-content-center">
            {navcontents.map((page) => (
              <LinkContainer to={page.extension}>
                <Nav.Link>{page.label}</Nav.Link>
              </LinkContainer>
            ))}
          </Nav>
        </Col>
        <Col xs={2} />
      </Navbar>
    </Row>
  );
}
