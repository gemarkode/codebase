function baseInRange(number, start, end) {
    return number >= Math.min(start, end) && number < Math.max(start, end);
  }
  
  function inRange(number, start, end) {
    if (end === undefined) {
      end = start;
      start = 0;
    }
    return baseInRange(+number, +start, +end);
  }
  
  let in_range = inRange(1, 0, 10);
  console.log(in_range); // true

  let in_range_without_end = inRange(4, 8);
  console.log(in_range_without_end); // true
  
  let not_in_range = inRange(2, 5, 10);
  console.log(not_in_range); // false
  