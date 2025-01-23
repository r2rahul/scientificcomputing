// newton_raphson.cpp
// Implementation of the Newton-Raphson Method for root finding

#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

/**
 * @brief Function for which we want to find the root
 * @param x The input value
 * @return The function value at x
 */
double f(double x) {
    return x*x - 4;  // f(x) = x^2 - 4
}

/**
 * @brief Derivative of the function f(x)
 * @param x The input value
 * @return The derivative value at x
 */
double fp(double x) {
    return 2*x;  // f'(x) = 2x
}

/**
 * @brief Implements the Newton-Raphson Method for root finding
 * @param x0 Initial guess
 * @param err Error tolerance for convergence
 * @param max_it Maximum number of iterations
 * @return The approximate root found by the method
 */
double newton_raphson(double x0, double err, int max_it) {
    double x = x0;
    int iter = 0;
    while (iter <= max_it) {
        double fx = f(x);
        double fd = fp(x);
        
        // Check if derivative is close to zero
        if(abs(fd) < 1e-10) {
            cout << "Derivative close to zero; method will fail" << endl;
            return x;
        }
        
        // Calculate new approximation
        double x_new = x - (fx / fd);
        
        // Calculate relative error
        double rel_err = abs(x_new - x) / x;
        
        // Check for convergence
        if(rel_err < err) {
            cout << "Converged after " << iter + 1 << " iterations" << endl;
            cout << "Solution is " << x_new << endl;
            return x_new; 
        }
        
        x = x_new;
        
        // Print iteration information
        cout << "Iteration " << iter << endl;
        cout << "Guess Value " << x_new << endl;
        cout << "Function value " << fx << endl;
        
        iter++;
    }
    
    cout << "Failed to converge within " << max_it << " iterations" << endl;
    return x;
}

/**
 * @brief Main function to demonstrate the Newton-Raphson Method
 * @return 0 on successful execution
 */
int main() {
    const double kInitialGuess = 1.0;
    const double kEpsilon = 1e-6;
    const int kMaxIterations = 1000;

    double root = newton_raphson(kInitialGuess, kEpsilon, kMaxIterations);
    
    cout << fixed << setprecision(8);
    cout << "Approximate root: " << root << endl;
    cout << "f(root) = " << f(root) << endl;
    
    return 0;
}
