export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }

  map.forEach((el, key) => {
    if (el === 1) {
      map.set(key, 100);
    }
  });

  return map;
}
