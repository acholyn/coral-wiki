import Definitions from "./compileDefinitions";

const definitions = [...Definitions()];

export function findResults(searchText) {
  // eslint-disable-next-line array-callback-return
  const foundResults = definitions.filter((obj) => {
    const checkBoxes = Array.from(
      document.querySelectorAll("input[type='radio']")
    );

    let termCheckbox = checkBoxes[0];
    let definitionCheckbox = checkBoxes[1];
    let typeCheckbox = checkBoxes[2];

    const termResults = obj["TERM"]
      .toLowerCase()
      .includes(searchText.toLowerCase());

    const definitionResults = obj["DEFINITION"]
      .toLowerCase()
      .includes(searchText.toLowerCase());

    const typeResults = obj["TYPE"]
      .toLowerCase()
      .includes(searchText.toLowerCase());

    if (termCheckbox.checked) return termResults;
    if (definitionCheckbox.checked) return definitionResults;
    if (typeCheckbox.checked) return typeResults;
    if (
      !termCheckbox.checked &&
      !definitionCheckbox.checked &&
      !typeCheckbox.checked
    )
      return termResults;
  });
  return foundResults;
}
