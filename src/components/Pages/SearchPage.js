import { Container, Form, FormControl } from "react-bootstrap";
import PageTitle from "../PageTitle";
import { useState } from "react";
// import definitions from "../../contents/definitions.json";
import { findResults } from "../Utilities/findResults";

export default function SearchPage() {
  const [results, setResults] = useState();
  // const defsArray = Array.from(definitions);

  const handleSearchInput = (event) => {
    let searchText = event.target.value;

    if (searchText.includes("@checkbox"))
      searchText = document.getElementById("searchBar").value;

    let foundResults = findResults(searchText);

    if (searchText === "" || foundResults.length < 1) return setResults(null);

    setResults(foundResults);
  };

  const searchOptions = [
    {
      name: "Search terms (default)",
      value: "@checkbox1",
      defaultChecked: true,
    },
    { name: "Search definitions", value: "@checkbox2" },
    { name: "Search by type", value: "@checkbox3" },
  ];

  return (
    <Container className="Page">
      <PageTitle title="Search" />
      <Container>
        <Form className="d-flex">
          <FormControl
            id="searchBar"
            type="text"
            onChange={handleSearchInput}
            placeholder="Begin typing to search terms"
            className="me-2"
            aria-label="Search"
          />
        </Form>

        <Form>
          <div className="search-options-container">
            {searchOptions.map((option, i) => (
              <label className="search-options" key={i}>
                {option.name}
                <input
                  name="searchFilter"
                  type="radio"
                  value={option.value}
                  onClick={handleSearchInput}
                  defaultChecked={option.defaultChecked}
                />
              </label>
            ))}
          </div>
        </Form>
      </Container>{" "}
      <div className="results mt-3">
        {results &&
          results.map((result, i) => (
            <p key={i} className="result-item">
              <span className="term">{result.TERM}</span> (<i>{result.ROLE}</i>){" "}
              <small className="summary">{result.DEFINITION}</small>{" "}
            </p>
          ))}
        {!results && <p className="pagetitle">No results available</p>}
      </div>
    </Container>
  );
}
