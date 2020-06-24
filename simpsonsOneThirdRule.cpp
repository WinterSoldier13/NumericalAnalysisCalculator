// https://www.geeksforgeeks.org/program-simpsons-13-rule/
// 1.Select a value for n, which is the number of parts the interval is divided into.
// 2.Calculate the width, h = (b-a)/n
// 3.Calculate the values of x0 to xn as x0 = a, x1 = x0 + h, …..xn-1 = xn-2 + h, xn = b.
// Consider y = f(x). Now find the values of y(y0 to yn) for the corresponding x(x0 to xn) values.
// 4.Substitute all the above found values in the Simpson’s Rule Formula to calculate the integral value.

// CPP program for simpson's 1/3 rule
#include <iostream>
#include <math.h>
using namespace std;

// Function to calculate f(x)
float func(float x)
{
	return 1/(1+x);
}

// Function for approximate integral
float simpsons_(float ll, float ul, int n)
{
	// Calculating the value of h
	float h = (ul - ll) / n;

	// Array for storing value of x and f(x)
	float x[10], fx[10];

	// Calculating values of x and f(x)
	for (int i = 0; i <= n; i++) {
		x[i] = ll + i * h;
		fx[i] = func(x[i]);
	}

	// Calculating result
	float res = 0;
	for (int i = 0; i <= n; i++) {
		if (i == 0 || i == n)
			res += fx[i];
		else if (i % 2 != 0)
			res += 4 * fx[i];
		else
			res += 2 * fx[i];
	}
	res = res * (h / 3);
	return res;
}

// Driver program
int main()
{
	float lower_limit = 2; // Lower limit
	float upper_limit = 4; // Upper limit
	int n = 6; // Number of interval
	cout << simpsons_(lower_limit, upper_limit, n)<<endl;
	return 0;
}
