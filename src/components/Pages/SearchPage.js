import { Container, Form, FormControl } from "react-bootstrap";
import PageTitle from "../PageTitle";
import { useState } from "react";
import definitions from "../../contents/definitions.json";

export default function SearchPage() {
  const [results, setResults] = useState();
  const defsArray = Array.from(definitions);

  const handleSearchInput = (event) => {
    let searchText = event.target.value;

    if (searchText.includes("@checkbox"))
      searchText = document.getElementById("searchBar").value;

    const checkBoxes = Array.from(
      document.querySelectorAll("input[type='checkbox']")
    );

    let termsCheckbox = checkBoxes[0];
    let definitionsCheckbox = checkBoxes[1];
    let typeCheckbox = checkBoxes[2];

    // ideally this would be in a separate file but
    // it isn't computed properly when separated
    // eslint-disable-next-line array-callback-return
    const findResults = defsArray.filter((obj) => {
      const termResults = obj["TERM"]
        .toLowerCase()
        .includes(searchText.toLowerCase());

      const defResults = obj["DEFINITION"]
        .toLowerCase()
        .includes(searchText.toLowerCase());

      const roleResults = obj["ROLE"]
        .toLowerCase()
        .includes(searchText.toLowerCase());

      if (termsCheckbox.checked) return termResults;
      if (definitionsCheckbox.checked) return defResults;
      if (typeCheckbox.checked) return roleResults;
      if (
        !termsCheckbox.checked &&
        !definitionsCheckbox.checked &&
        !typeCheckbox.checked
      )
        return termResults;
    });
    if (searchText === "" || findResults.length < 1) return setResults(null);

    setResults(findResults);
  };

  const options = [
    { name: "Search terms (default)", value: "@checkbox1" },
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
            {options.map((option, i) => (
              <label className="search-options" key={i}>
                {option.name}
                <input
                  type="checkbox"
                  value={option.value}
                  onClick={handleSearchInput}
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
