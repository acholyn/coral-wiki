import { Container } from "react-bootstrap";
import "../App.css";

export default function PageTitle(props) {
  //   const titlePrefix = 'CCRW | '

  return (
    <Container fluid className="justify-content-center pagetitle">
      {props.title}
      <hr></hr>
    </Container>
  );
}
