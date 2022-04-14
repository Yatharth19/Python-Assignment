# Python-Assignment

This is the code I wrote to generate random numbers as part of a python assignment.
According to (https://engineering.mit.edu/engage/ask-an-engineer/can-a-computer-generate-a-truly-random-number/) real random numbers do not exist because if they existed we cannot write any code for them put pseudo randomness is a reality today.
Even the modules included in various programming languages work on the principle of pseudo randomness.

The algorithm I have implemented here maximizes randomness while predicting the numbers.
The idea to create a n digit random number is that we take a long string and have its first 3(arbitrarily chosen) digits as our initial number(seed). Let this number be x.
Then starting from the last digit of the chosen number, we calculate the sum of the next x numbers. 
We then calculate the average by a modified formula and append the last digit of the obtained modified average like combination of digits to the answer.
We repeat the above process till we get the desired number of digits.

To avoid getting the same number, the seed values are being altered each time by modifying the contents of the file after each iteration.



The obtained values of x and y coordinate are plotted and the value of pi is estimated.
