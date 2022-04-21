import { Container } from "react-bootstrap";
import PageTitle from "../PageTitle";

export default function SearchPage() {
  return (
    <Container className="Page">
      <PageTitle title="Search" />
      <Container>
        {/* todo: find searchbox on bootstrap */}
        {/* todo: figure out backend of searching */}
      </Container>
    </Container>
  );
}
