export default function getStudentIdsSum(arr) {
  return arr.reduce((val, cur) => val + cur.id, 0);
}
