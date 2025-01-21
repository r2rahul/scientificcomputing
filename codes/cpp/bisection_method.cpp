#include <iostream>
#include <cmath>
#include <iomanip>

 //using namespace std;
 using std::cout;
 using std::cin;
 using std::endl;
 using std::fixed;
 using std::setprecision;

double f(double x) {
    return pow(x, 2) - x - 1;
}

double bisection_method(double lb, double ub, double e, int max_iter) {
    int iter = 0;
    if(f(lb) * f(ub) >= 0) {
        cout << "Bisection method fails for given bounds" << endl;
        return 0;
    }

    std::cout << "Iteration,Lower Bound,Upper Bound,Median Point,f(Lower),f(Upper),f(Median)" << std::endl;

    while (iter < max_iter) {
        double c = (lb + ub) / 2;
        double f_lb = f(lb);
        double f_ub = f(ub);
        double f_mid = f(c);
        double err = abs(ub - lb);
        cout << fixed << setprecision(6)
            << iter << "," << lb << "," << ub << "," << c << ","
            << f_lb << "," << f_ub << "," << f_mid << endl;
        if(f_mid == 0 && err < e) {
            cout << "Root found after iter " << iter + 1 << endl; 
            return c;
        }
        if(f_lb * f_mid < 0) {
            ub = c;
        } else {
            lb = c;
        } 
        iter++;
    }
    cout << "Failted to converge within" << max_iter << "Iterations" << endl;
    return e;
}


int main() {
    double lb0 = -3;
    double ub0 = 1;
    double err = 1e-6;
    int m_it = 100;
    double root = bisection_method(lb0, ub0, err, m_it);
    cout << fixed << setprecision(9);
    cout << "Approximate Root is " << root << endl; 
    return 0;
}