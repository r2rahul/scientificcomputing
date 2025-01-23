// bisection_method.cpp
// Implementation of the Bisection Method for root finding

#include <iostream>
#include <cmath>
#include <iomanip>

// Avoid using namespace std; instead, use specific using declarations
using std::cout;
using std::cin;
using std::endl;
using std::fixed;
using std::setprecision;

/**
 * @brief Function for which we want to find the root
 * @param x The input value
 * @return The function value at x
 */
double f(double x) {
    return pow(x, 2) - x - 1;  // The function f(x) = x^2 - x - 1
}

/**
 * @brief Implements the Bisection Method for root finding
 * @param lb Lower bound of the interval
 * @param ub Upper bound of the interval
 * @param e Error tolerance for convergence
 * @param max_iter Maximum number of iterations
 * @return The approximate root found by the method
 */
double bisection_method(double lb, double ub, double e, int max_iter) {
    int iter = 0;
    
    // Check if the function changes sign over the interval
    if (f(lb) * f(ub) >= 0) {
        cout << "Bisection method fails for given bounds" << endl;
        return 0;
    }

    // Print header for the iteration table
    cout << "Iteration,Lower Bound,Upper Bound,Median Point,f(Lower),f(Upper),f(Median)" << endl;

    while (iter < max_iter) {
        // Calculate the midpoint
        double c = (lb + ub) / 2;
        
        // Evaluate the function at lower bound, upper bound, and midpoint
        double f_lb = f(lb);
        double f_ub = f(ub);
        double f_mid = f(c);
        
        // Calculate the current error (interval width)
        double err = std::abs(ub - lb);
        
        // Print the current iteration data
        cout << fixed << setprecision(6)
             << iter << "," << lb << "," << ub << "," << c << ","
             << f_lb << "," << f_ub << "," << f_mid << endl;
        
        // Check if we've found the root within the error tolerance
        if (f_mid == 0 && err < e) {
            cout << "Root found after iter " << iter + 1 << endl; 
            return c;
        }
        
        // Update the interval based on where the sign change occurs
        if (f_lb * f_mid < 0) {
            ub = c;  // Root is in the left half
        } else {
            lb = c;  // Root is in the right half
        } 
        
        iter++;
    }
    
    // If we've reached this point, the method didn't converge
    cout << "Failed to converge within " << max_iter << " iterations" << endl;
    return e;  // Return the error tolerance as a fallback
}

/**
 * @brief Main function to demonstrate the Bisection Method
 * @return 0 on successful execution
 */
int main() {
    // Define constants for the method parameters
    const double kLowerBound = -3.0;
    const double kUpperBound = 1.0;
    const double kErrorTolerance = 1e-6;
    const int kMaxIterations = 100;

    // Call the bisection method
    double root = bisection_method(kLowerBound, kUpperBound, kErrorTolerance, kMaxIterations);
    
    // Print the result with high precision
    cout << fixed << setprecision(9);
    cout << "Approximate Root is " << root << endl; 
    return 0;
}
