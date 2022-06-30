import { Container, Form, FormControl } from "react-bootstrap";
import PageTitle from "../PageTitle";
import definitions from "../../contents/definitions.json";
import { useState } from "react";

export default function SearchPage() {
  const defsArray = Array.from(definitions);
  const [results, setResults] = useState();

  const handleSearchInput = (event) => {
    let searchText = event.target.value;

    const findResults = defsArray.filter((obj) => {
      const searchResults = obj["TERM"]
        .toLowerCase()
        .includes(searchText.toLowerCase());
      return searchResults;
    });

    setResults(findResults);
  };

  return (
    <Container className="Page">
      <PageTitle title="Search" />
      <Container>
        <Form className="d-flex">
          <FormControl
            type="text"
            onChange={handleSearchInput}
            placeholder="Begin typing to search terms"
            className="me-2"
            aria-label="Search"
          />
          {/* <Button size="sm" variant="outline-success">
            Search
          </Button> */}
        </Form>

        <div className="results mt-3">
          {results &&
            results.map((result, i) => (
              <p key={i} className="result-item">
                <span className="term">{result.TERM}</span> (
                <i>{result.ROLE}</i>){" "}
                <small className="summary">{result.DEFINITION}</small>{" "}
              </p>
            ))}
        </div>
      </Container>
    </Container>
  );
}
