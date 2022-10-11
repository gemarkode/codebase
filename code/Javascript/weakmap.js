// Create WeakMap
const { inspect } = require('util');

let CountMap = new WeakMap(); // Saving User

function countUser(user) {
    let count = CountMap.get(user) || 0;
    CountMap.set(user, count + 1);
}

let riswanda= { name: "Riswanda Hinata" };
countUser(riswanda);                // Adding user "Riswanda Hinata"

riswanda = null;                    // Data object "Riswanda" deleted

// Set delay for waiting gerbage collector working
setTimeout(function() {
  console.log(inspect(CountMap, { showHidden: true }));
}, 5000);
