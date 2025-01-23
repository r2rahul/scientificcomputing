#include <Rcpp.h>
using namespace Rcpp;

// Function declarations
long reverse(long);
bool isPalindrome(long);
String isLychrel(long);
long count_lychrel(long);

// Maximum number of iterations for Lychrel number check
static const int MAX_ITERATIONS = 49;

//' Rcpp Implementation of Project Euler Problem 55: Lychrel Numbers
//' 
//' This code solves the Lychrel numbers problem from Project Euler.
//' A Lychrel number is a number that never forms a palindrome through
//' the iterative process of reversing and adding.
//' 
//' @references https://projecteuler.net/problem=55

//' Count Lychrel numbers up to n
//'
//' @param n The upper limit to check for Lychrel numbers
//' @return The count of Lychrel numbers up to n
//' @export
// [[Rcpp::export]]
long count_lychrel(long n) {
  long num_lychrel = 0;
  for(int j = 10; j <= n; j++) {
    if(isLychrel(j) == "false") {
      num_lychrel += 1;
    }
  }
  return num_lychrel;
}

//' Check if a number is a Lychrel number
//'
//' @param x The number to check
//' @return "true" if the number is not Lychrel, "false" if it is Lychrel
//' @export
// [[Rcpp::export]]
String isLychrel(long x) {
  for(int i = 0; i <= MAX_ITERATIONS; i++) {
    x = x + reverse(x);
    // Uncomment to debug:
    // Rcout << "The Iteration Number: " << i << "\n";
    if(isPalindrome(x)) {
      return "true";  // Not a Lychrel number
    }
  }
  return "false";  // Lychrel number
}

//' Check if a number is a palindrome
//'
//' @param number The number to check
//' @return true if the number is a palindrome, false otherwise
bool isPalindrome(long number) {
  return number == reverse(number);
}

//' Reverse a number
//'
//' @param number The number to reverse
//' @return The reversed number
long reverse(long number) {
  long reverse = 0;
  while (number > 0) {
    long remainder = number % 10;
    reverse = (reverse * 10) + remainder;
    number = number / 10;
  }
  return reverse;
}

/*** R
# Test calls of functions
isLychrel(47)
count_lychrel(100)
*/
