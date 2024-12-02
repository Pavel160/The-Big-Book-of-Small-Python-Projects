# Prime Numbers
**Author**: Al Sweigart (al@inventwithpython.com)

Prime Numbers is a Python project that helps to identify prime numbers, check if a given number is prime, and generate a list of prime numbers up to a given limit.

Tags: prime, numbers, math

## Features
- Check Prime: Check if a number is prime.
- Generate Primes: Generate a list of prime numbers up to a specified limit.
- Efficient Algorithms: The project includes an optimized algorithm for checking prime numbers (e.g., checking only up to the square root of a number).

## Requirements
- Python 3.x

## How It Works
1. Prime Definition: A prime number is a number greater than 1 that cannot be divided evenly by any number other than 1 and itself.
2. Check Prime: To check if a number is prime, the program tests if it is divisible by any number from 2 up to the square root of the number.
3. Generate Primes: The program uses a loop to check all numbers from 2 up to a given limit, identifying and returning the primes.

## Example
### Prime Numbers:
- 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, ...

### Check if a number is prime:
- Is 7 prime? Yes
- Is 10 prime? No

## Usage
1. Run the script to check if a number is prime.
2. Generate prime numbers up to a certain limit.
3. The program will print the result of whether a number is prime and will list primes up to the limit.

### Example of Running the Program:
```python
Enter a number to check if it's prime: 7
Yes, 7 is a prime number!

Enter a limit to generate prime numbers up to: 30
Prime numbers up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
## License
See the [LICENSE](LICENSE) file for details.
