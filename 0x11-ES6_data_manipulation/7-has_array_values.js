export default function setFromArray(set, array) {
  return array.every((el) => set.has(el));
}
