#include <iostream>
#include<math.h>
using namespace std;
#define EP 0.00005

// Define the function here
double solution(double x) {
   return cos(x) -x*exp(x);
}


void bisection(double a, double b) {
   if (solution(a) * solution(b) >= 0) {
      cout << "You have not assumed right a and b\n";
      return;
   }
   double c = a;
   int allowedIteration = 20;
   int count=0;
   while ((b-a) >= EP) {
      // Find middle point
      c = (a+b)/2;
      // Check if middle point is root
      if (solution(c) == 0.0)
         break;
       // Decide the side to repeat the steps
      else if (solution(c)*solution(a) < 0)
         b = c;
      else
         a = c;

	cout<<"A: "<<a<<" | B: "<<b<<" | C: "<<c<<endl;
	if(count++==allowedIteration)
	break;
   }
   cout << "The value of root is : " << c;
}
 // main function
int main() {
   cout<<"Remember to tweak the No. of iterations and other stuffs"<<endl;
   double a =0, b = 1;
   bisection(a, b);
   return 0;
}
