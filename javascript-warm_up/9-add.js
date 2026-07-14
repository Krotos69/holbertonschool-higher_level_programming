#!/usr/bin/node
function add(a, b) {
	return a + b;
}

const a = parseInt(Process.argv[2]);
const b = parseInt(Process.argv[3]);

console.log(add(a, b));
