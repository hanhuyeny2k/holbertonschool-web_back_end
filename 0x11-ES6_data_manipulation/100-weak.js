export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  weakMap.set(endpoint, (weakMap.get(endpoint) || 0) + 1);
}
