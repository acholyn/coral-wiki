import { Form, Button, Container, Row, Col, Card } from "react-bootstrap";
import "../../App.css";

export function ContactForm() {
  return (
    <Container className="mb-2">
      <Card>
        <Container className="justify-content-center" style={{ width: "60vw" }}>
          <Form as={Card.Body}>
            <Form.Group className="mb-3" as={Row}>
              <Form.Label column sm={3} className="text-right">
                Name
              </Form.Label>
              <Col md>
                <Form.Control type="name" placeholder="Enter name" />
              </Col>
            </Form.Group>

            <Form.Group className="mb-3" as={Row}>
              <Form.Label column sm={3} className="text-right">
                Email address
              </Form.Label>
              <Col md>
                <Form.Control type="email" placeholder="name@example.com" />
              </Col>
            </Form.Group>

            <Form.Group className="mb-3" as={Row}>
              <Form.Label column sm={3} className="text-right">
                Message
              </Form.Label>
              <Col lg>
                <Form.Control as="textarea" rows={3} />{" "}
              </Col>
              <Form.Text className="text-muted" style={{ marginLeft: "5vw" }}>
                If you want to submit a definition, check out the{" "}
                <a href="/contributors">contributor page</a>.
              </Form.Text>
            </Form.Group>

            <Button
              variant="primary"
              type="submit"
              style={{
                background: "var(--seablue)",
                border: "none",
                color: "var(--blueshadow)",
                marginLeft: "20vw",
              }}>
              Submit
            </Button>
          </Form>
        </Container>
      </Card>
    </Container>
  );
}
