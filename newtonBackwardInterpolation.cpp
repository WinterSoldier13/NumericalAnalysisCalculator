// // https://www.geeksforgeeks.org/newton-forward-backward-interpolation/

// // CPP Program to interpolate using
// // newton backward interpolation
// #include <bits/stdc++.h>
// using namespace std;

// // Calculation of u mentioned in formula
// float u_cal(float u, int n)
// {
// 	float temp = u;
// 	for (int i = 1; i < n; i++)
// 		temp = temp * (u + i);
// 	return temp;
// }

// // Calculating factorial of given n
// int fact(int n)
// {
// 	int f = 1;
// 	for (int i = 2; i <= n; i++)
// 		f *= i;
// 	return f;
// }

// int main()
// {
// 	// number of values given
// 	int n = 5;
// 	float x[] = { 1891, 1901, 1911,
// 				1921, 1931 };

// 	// y[][] is used for difference
// 	// table and y[][0] used for input
// 	float y[n][n];
// 	y[0][0] = 46;
// 	y[1][0] = 66;
// 	y[2][0] = 81;
// 	y[3][0] = 93;
// 	y[4][0] = 101;

// 	// Calculating the backward difference table
// 	for (int i = 1; i < n; i++) {
// 		for (int j = n - 1; j >= i; j--)
// 			y[j][i] = y[j][i - 1] - y[j - 1][i - 1];
// 	}

// 	// Displaying the backward difference table
// 	for (int i = 0; i < n; i++) {
// 		for (int j = 0; j <= i; j++)
// 			cout << setw(4) << y[i][j]
// 				<< "\t";
// 		cout << endl;
// 	}

// 	// Value to interpolate at
// 	float value = 1925;

// 	// Initializing u and sum
// 	float sum = y[n - 1][0];
// 	float u = (value - x[n - 1]) / (x[1] - x[0]);
// 	for (int i = 1; i < n; i++) {
// 		sum = sum + (u_cal(u, i) * y[n - 1][i]) /
// 									fact(i);
// 	}

// 	cout << "\n Value at " << value << " is "
// 		<< sum << endl;
// 	return 0;
// }

#include <stdio.h>

#include <math.h>

#include <string.h>
int main()
{
	int n, i, j, k;
	float mx[10], my[10], x, x0 = 0, y0, sum, h, fun, p, diff[20][20], y1, y2, y3, y4;
	printf("\n enter the no. of terms -");
	scanf("%d", &n);
	printf("\n enter the value in the form of x - ");
	for (i = 0; i < n; i++)
	{
		printf("\n enter the value of x%d- ", i + 1);
		scanf("%f", &mx[i]);
	}
	printf("\n enter the value in the form of y - ");
	for (i = 0; i < n; i++)
	{
		printf("\n\n enter the value of y%d- ", i + 1);
		scanf("%f", &my[i]);
	}
	printf("\n enter the value of x for");
	printf("\nwhich you want the value of of y -");
	scanf("%f", &x);
	h = mx[1] - mx[0];
	for (i = 0; i < n - 1; i++)
	{
		diff[i][1] = my[i + 1] - my[i];
	}
	for (j = 2; j <= 4; j++)
	{
		for (i = 0; i < n - j; i++)
		{
			diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1];
		}
	}
	i = 0;
	while (!mx[i] > x)
	{
		i++;
	}
	x0 = mx[i];
	sum = 0;
	y0 = my[i];
	fun = 1;
	p = (x - x0) / h;
	sum = y0;
	for (k = 1; k <= 4; k++)
	{
		fun = (fun * (p - (k - 1)) / k);
		sum = sum + fun * diff[i][k];
	}
	printf("\n when x=%6.4f,y=%6.8f", x, sum);
	printf("\n press enter to exit");
}
