function FizzBuzz(number){

   for (var index=1; index <= number; index++)
      {
         if (index % 15 === 0)
            console.log("FizzBuzz");
         else if (index % 3 === 0)
            console.log("Fizz");
         else if (index % 5 === 0)
            console.log("Buzz");
         else
            console.log(index);
      }
}

FizzBuzz(16)
