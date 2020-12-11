export default function createIteratorObject(report) {
  const allEmployees = Object.values(report).flatMap((x) => x);

  return {
    * [Symbol.iterator]() {
      for (const employee of allEmployees) {
        yield employee;
      }
    },
  };
}
