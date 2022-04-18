import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";

export default function SearchPage() {
  return (
    <Container className="Page">
      <PageTitle title="Search" />
      <Container>search stuff</Container>
    </Container>
  );
}
