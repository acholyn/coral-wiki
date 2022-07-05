import { Container, Tabs, Tab, Alert } from "react-bootstrap";
import { NewContributorForm } from "../Utilities/NewContributorForm";
import PageTitle from "../PageTitle";
import { contributorsList } from "../../contents/contributorsList";
import "./PageStyling.css";

export default function Contributors() {
  return (
    <Container className="Page">
      <PageTitle title="Contributors" />
      <Tabs defaultActiveKey="current" className="mb-3 justify-content-center">
        <Tab eventKey="current" title="Current">
          <Container>
            {contributorsList.map((contributor, i) => (
              <p className="contributors" key={i}>
                <b>
                  <a href={contributor.link}>{contributor.fullname}</a>
                </b>{" "}
                - <i>{contributor.role}</i>
              </p>
            ))}{" "}
          </Container>
        </Tab>
        <Tab eventKey="new" title="New (Join Us!)">
          <Alert variant="info">
            If you'd like to submit a new definition, please use the form below
            or send us an email and we'll get back to you as soon as we can.
          </Alert>
          <NewContributorForm />
        </Tab>
      </Tabs>
    </Container>
  );
}
