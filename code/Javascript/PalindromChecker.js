function checkPalindrom (str) {
  return str == str.split('').reverse().join('');
}

console.log(checkPalindrom("halah"));
