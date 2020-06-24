// // https://www.geeksforgeeks.org/program-for-newton-raphson-method/
// // Compute values of func(x) and derivFunc(x) for given initial x
// // Compute h: h = func(x) / derivFunc(x)
// // While h is greater than allowed error ε
//     // h = func(x) / derivFunc(x)
//     // x = x – h

// // C++ program for implementation of Newton Raphson Method for
// // solving equations
// #include<bits/stdc++.h>
// #define EPSILON 0.001
// using namespace std;

// // An example function whose solution is determined using
// // Bisection Method. The function is x^3 - x^2 + 2
// double func(double x)
// {
// 	return x*x*x - x*x + 2;
// }

// // Derivative of the above function which is 3*x^x - 2*x
// double derivFunc(double x)
// {
// 	return 3*x*x - 2*x;
// }

// // Function to find the root
// void newtonRaphson(double x)
// {
// 	double h = func(x) / derivFunc(x);
// 	while (abs(h) >= EPSILON)
// 	{
// 		h = func(x)/derivFunc(x);

// 		// x(i+1) = x(i) - f(x) / f'(x)
// 		x = x - h;
// 	}

// 	cout << "The value of the root is : " << x;
// }

// // Driver program to test above
// int main()
// {
// 	double x0 = -20; // Initial values assumed
// 	newtonRaphson(x0);
// 	return 0;
// }

#include <stdio.h>
#include <math.h>
#include <string.h>

#define f(x) cos(x) - x *exp(x)
#define df(x) -sin(x) - x*exp(x) - exp(x)

void NEW_RAP();

int main()
{
	printf("\n Solution by NEWTON RAPHSON method\n");
	printf("\n Equation is: ");

	printf("\n\t\t\t 3*X - COS X - 1=0 \n\n");
	NEW_RAP();
}

void NEW_RAP()
{
	double x1, x0;
	double f0, f1;
	double df0;
	int i = 1;
	int itr;
	double EPS;
	double error;
	for (x1 = 0;; x1 += 0.01)
	{
		f1 = f(x1);
		if (f1 > 0)
		{
			break;
		}
	}
	x0 = x1 - 0.01;
	f0 = f(x0);
	printf(" Enter the number of iterations:");
	scanf(" %d", &itr);
	printf(" Enter the maximum possible error:");
	scanf("%f", &EPS);
	if (fabs(f0) > f1)
	{
		printf("\n\t\t The root is near to %.4f\n", x1);
	}
	if (f1 > fabs(f(x0)))
	{
		printf("\n\t\t The root is near to %.4f\n", x0);
	}
	x0 = (x0 + x1) / 2;
	for (; i <= itr; i++)
	{
		f0 = f(x0);
		df0 = df(x0);
		x1 = x0 - (f0 / df0);
		printf("\n\t\t The %d approximation to the root is:%f", i, x1);
		error = fabs(x1 - x0);
		if (error < EPS)
		{
			break;
		}
		x0 = x1;
	}
	if (error > EPS)
	{
		printf("\n\n\t NOTE:- ");
		printf("The number of iterations are not sufficient.");
	}
	printf("\n\n\n\t\t\t ------------------------------");
	printf("\n\t\t\t The root is %.4f ", x1);
	printf("\n\t\t\t ------------------------------");
}