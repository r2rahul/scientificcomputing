#include <Rcpp.h>
using namespace Rcpp;
long reverse(long);
bool isPalindrome(long);
String isLychrel(long);
long count_lychrel(long);
static int MAX_ITERATIONS = 49;

// Rcpp Implementation of Project Euler Problem 55 Lychrel Numbers 
// The problem link is https://projecteuler.net/problem=55

// [[Rcpp::export]]
long count_lychrel(long n)
{ long num_lychrel = 0;
  for(int j = 10; j <= n; j++){
    if(isLychrel(j) == "false"){
      num_lychrel += 1;
    }
  }
  return num_lychrel;
}

// [[Rcpp::export]]
String isLychrel(long x) {
  for(int i = 0; i <= MAX_ITERATIONS; i++)
    {
      x = x + reverse(x);
      // Rcout << "The Iteration Number: " << i << "\n";
      if(isPalindrome(x))
      {
        return "true";
      }
        
    }
  return "false";
}

bool isPalindrome(long number)
{
  return number == reverse(number);
}

long reverse(long number)
{
  long reverse = 0;
  while (number > 0)
  {
    long remainder = number % 10;
    reverse = (reverse * 10) + remainder;
    number = number / 10;
  }
  return reverse;
}

// Test call of functions
/*** R
isLychrel(47)
count_lychrel(100)
*/
