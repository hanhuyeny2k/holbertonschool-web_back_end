export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw Error('Position outside range');
  }
  const a = new ArrayBuffer(length);
  const b = new Int8Array(a);
  b[position] = value;
  return b;
}
