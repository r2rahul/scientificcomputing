#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

// Function to find root
double f(double x) {
    return x*x - 4;
}

double fp(double x) {
    return 2*x;
}

double newton_raphson(double x0, double err, int max_it) {
    double x = x0;
    int iter = 0;
    while (iter <= max_it) {
        double fx = f(x);
        double fd = fp(x);
        if(abs(fd) < 1e-10) {
            cout << "Derivative close to zero; method will fail" << endl;
            return x;
        }
        double x_new = x - (fx / fd);
        double rel_err = abs(x_new - x) / x;
        if( rel_err < err) {
            cout << "Converged after " << iter + 1 << " iterations" << endl;
            cout << "Solution is " << x_new << endl;
            return x_new; 
        }
        x = x_new;
        cout << "Iteration " << iter << endl;
        cout << "Guess Value " << x_new << endl;
        cout << "Function value " << fx << endl;
        iter++;
    }
    cout << "Failted to converge within" << max_it << "Iterations" << endl;
    return x;
}

int main() {
    double initial_guess = 1.0;
    double epsilon = 1e-6;
    int max_iterations = 1000;

    double root = newton_raphson(initial_guess, epsilon, max_iterations);
    cout << fixed << setprecision(8);
    cout << "Approximate root: " << root << std::endl;
    cout << "f(root) = " << f(root) << std::endl;
    return 0;
}
