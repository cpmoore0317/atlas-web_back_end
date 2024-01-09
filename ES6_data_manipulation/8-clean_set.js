// cpmoore0317

export default function cleanSet(set, startString) {
  const filteredValues = [...set].filter((value) =>
    value.startsWith(startString)
  );
  const resultString = filteredValues.join(" ,");
  return resultString;
}
