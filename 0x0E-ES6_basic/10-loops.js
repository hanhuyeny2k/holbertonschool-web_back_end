export default function appendToEachArrayValue(array, appendString) {
  const out = [];
  for (const el of array) {
    out.push(appendString + el);
  }

  return out;
}
