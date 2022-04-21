import { Form, Button, Container, Row, Col, Card } from "react-bootstrap";
import "../../App.css";

export function NewContributorForm() {
  return (
    // todo: change placeholder text size to flexible
    <Container>
      <Card>
        <Container className="justify-content-center" style={{ width: "80vw" }}>
          <Form as={Card.Body}>
            <Row>
              <Form.Group className="mb-3" as={Col}>
                <Form.Control type="name" placeholder="Enter name" />
                <Form.Text>Include titles if applicable </Form.Text>
              </Form.Group>

              <Form.Group className="mb-3" as={Col}>
                <Form.Control type="email" placeholder="name@example.com" />
              </Form.Group>
            </Row>
            <Form.Group className="mb-3" as={Row}>
              <Form.Control placeholder="Affiliation/University" />
            </Form.Group>

            <Form.Group className="mb-3" as={Row}>
              <Form.Control placeholder="Website or profile link" />
            </Form.Group>
            <Row>
              <Form.Text>Tell us about your word</Form.Text>
              <Form.Group className="mb-3" as={Col}>
                <Form.Control placeholder="Term" />
              </Form.Group>
              <Form.Group className="mb-3" as={Col}>
                <Form.Control placeholder="Type" />
                <Form.Text>eg. noun, adjective, verb </Form.Text>
              </Form.Group>
            </Row>
            <Form.Group className="mb-3" as={Row}>
              <Col lg>
                <Form.Control as="textarea" rows={3} />{" "}
              </Col>
              <Form.Text className="text-muted">
                If you want to submit in bulk, send us an{" "}
                <a href="mailto:lab.amanda.ch@gmail.com?subject=Coral Wiktionary">
                  email
                </a>{" "}
                and we'll get back to you as soon as we can.
              </Form.Text>
            </Form.Group>

            <Button
              variant="primary"
              type="submit"
              style={{
                background: "var(--seablue)",
                border: "none",
                color: "var(--blueshadow",
              }}>
              Submit
            </Button>
          </Form>
        </Container>
      </Card>
    </Container>
  );
}
