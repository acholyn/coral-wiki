import AC from "../../contents/definitionsAC.json";
import DG from "../../contents/definitionsDG.json";
import IO from "../../contents/definitionsIO.json";
import PS from "../../contents/definitionsPS.json";
import TZ from "../../contents/definitionsTZ.json";

export default function Definitions() {
  var defLetterSections = [...AC, ...DG, ...IO, ...PS, ...TZ];
  const definitions = defLetterSections.sort();

  return definitions;
}
// this could be further expanded such that categories are included
// meaning the Dictionary page could have category tabs as well as "all"
