// secant_method.cpp
// Implementation of the Secant Method for root finding

#include <iostream>
#include <cmath>
#include <iomanip>

// Avoid using namespace std in header files
// It's used here for brevity, but in larger projects, explicit qualification is preferred
using namespace std;

/**
 * @brief Function for which we want to find the root
 * @param x The input value
 * @return The function value at x
 */
double f(double x) {
    return pow(x, 2) - 4;
}

/**
 * @brief Implements the Secant Method for root finding
 * @param x0 First initial guess
 * @param x1 Second initial guess
 * @param err Error tolerance for convergence
 * @param max_it Maximum number of iterations
 * @return The approximate root found by the method
 */
double secant_method(double x0, double x1, double err, int max_it) {
    int iter = 0;
    double x2, f0, f1, f2;

    cout << "Iteration,x0,x1,f(x0),f(x1),x2" << endl;
    do {
        f0 = f(x0);
        f1 = f(x1);
        
        // Check if f(x0) - f(x1) is too close to zero
        if (abs(f0 - f1) < err) {
            cout << "Small slope. Method might fail." << endl;
            return x1;
        }
        
        // Calculate the new approximation
        x2 = x1 - f1 * (x0 - x1) / (f0 - f1);
        f2 = f(x2);
        
        cout << fixed << setprecision(6)
             << iter + 1 << "," << x0 << "," << x1 << ","
             << f0 << "," << f1 << "," << x2 << endl;        
        x0 = x1;
        x1 = x2;
        iter++;
    } while (abs(f2) > err && iter < max_it);

    if (iter == max_it) {
        cout << "Method failed to converge within " << max_it << " iterations." << endl;
    } else {
        cout << "Converged after " << iter << " iterations." << endl;
    }

    return x2;
}

/**
 * @brief Main function to demonstrate the Secant Method
 * @return 0 on successful execution
 */
int main() {
    // Constants and initial values
    const double kX0 = 0.0;
    const double kX1 = 6.0;
    const double kRelThresh = 1e-6;
    const int kMaxIterations = 100;

    double root = secant_method(kX0, kX1, kRelThresh, kMaxIterations);
    
    cout << fixed << setprecision(8);
    cout << "Approximate root: " << root << endl;
    cout << "f(root) = " << f(root) << endl;
    
    return 0;
}
