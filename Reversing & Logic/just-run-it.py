const _ = [100,116,119,119,124,109,114,116,115,88,117,114,105,88,115,111,98,88,100,104,99,98,122];

const flag = _.reduce(
  (s, c) => s + String.fromCharCode(c ^ 0b111),
  ''
);

console.log(flag);