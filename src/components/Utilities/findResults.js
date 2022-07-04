import defs from "../../contents/definitions.json";

const definitions = Array.from(defs);

export function findResults(searchText) {
  // eslint-disable-next-line array-callback-return
  const foundResults = definitions.filter((obj) => {
    const checkBoxes = Array.from(
      document.querySelectorAll("input[type='checkbox']")
    );

    let termsCheckbox = checkBoxes[0];
    let definitionsCheckbox = checkBoxes[1];
    let typeCheckbox = checkBoxes[2];

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
  return foundResults;
}
