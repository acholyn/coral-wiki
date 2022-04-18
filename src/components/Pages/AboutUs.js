import { Col, Container } from "react-bootstrap";
import PageTitle from "../PageTitle";
import "../../App.css";

export default function AboutUs() {
  return (
    <Container className="Page">
      <PageTitle title="About" />
      <Container>
        <Col>info</Col>
        <Col>pic</Col>
      </Container>
    </Container>
  );
}
