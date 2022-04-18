import { Container } from "react-bootstrap";
import { ContactForm } from "../Utilities/ContactForm";
import PageTitle from "../PageTitle";
import "../../App.css";

export default function ContactUs() {
  return (
    <Container className="Page">
      <PageTitle title="Contact Us" />
      <Container>
        <ContactForm />{" "}
      </Container>
    </Container>
  );
}
