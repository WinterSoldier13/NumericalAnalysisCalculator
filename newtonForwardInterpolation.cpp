// // https://www.geeksforgeeks.org/newton-forward-backward-interpolation/

// // CPP Program to interpolate using
// // newton forward interpolation
// #include <bits/stdc++.h>
// using namespace std;

// // calculating u mentioned in the formula
// float u_cal(float u, int n)
// {
// 	float temp = u;
// 	for (int i = 1; i < n; i++)
// 		temp = temp * (u - i);
// 	return temp;
// }

// // calculating factorial of given number n
// int fact(int n)
// {
// 	int f = 1;
// 	for (int i = 2; i <= n; i++)
// 		f *= i;
// 	return f;
// }

// int main()
// {
// 	// Number of values given
// 	int n = 4;
// 	float x[] = { 45, 50, 55, 60 };

// 	// y[][] is used for difference table
// 	// with y[][0] used for input
// 	float y[n][n];
// 	y[0][0] = 0.7071;
// 	y[1][0] = 0.7660;
// 	y[2][0] = 0.8192;
// 	y[3][0] = 0.8660;

// 	// Calculating the forward difference
// 	// table
// 	for (int i = 1; i < n; i++) {
// 		for (int j = 0; j < n - i; j++)
// 			y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
// 	}

// 	// Displaying the forward difference table
// 	for (int i = 0; i < n; i++) {
// 		cout << setw(4) << x[i]
// 			<< "\t";
// 		for (int j = 0; j < n - i; j++)
// 			cout << setw(4) << y[i][j]
// 				<< "\t";
// 		cout << endl;
// 	}

// 	// Value to interpolate at
// 	float value = 52;

// 	// initializing u and sum
// 	float sum = y[0][0];
// 	float u = (value - x[0]) / (x[1] - x[0]);
// 	for (int i = 1; i < n; i++) {
// 		sum = sum + (u_cal(u, i) * y[0][i]) /
// 								fact(i);
// 	}

// 	cout << "\n Value at " << value << " is "
// 		<< sum << endl;
// 	return 0;
// }

#include <stdio.h>
// # include <conio.h>
#include <math.h>
// # include <process.h>
#include <string.h>
int main()
{
	int n;
	int i, j;
	float ax[10];
	float ay[10];
	float x;
	float y = 0;
	float h;
	float p;
	float diff[20][20];
	float y1, y2, y3, y4;

	printf("\n Enter the number of terms -");
	scanf("%d", &n);
	printf("Enter the value in the form of x - ");
	for (i = 0; i < n; i++)
	{
		printf("Enter the value of x%d -", i + 1);
		scanf("%f", &ax[i]);
	}
	printf("\n Enter the value in the form of y -");
	for (i = 0; i < n; i++)
	{
		printf("Enter the value of y%d - ",
			   i + 1);
		scanf("%f", &ay[i]);
	}
	printf("\nEnter the value of x for");
	printf("\nwhich you want the value of y -");
	scanf("%f", &x);
	h = ax[1] - ax[0];
	for (i = 0; i < n - 1; i++)
	{
		diff[i][1] = ay[i + 1] - ay[i];
	}
	for (j = 2; j <= 4; j++)
	{
		for (i = 0; i < n - j; i++)
		{
			diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1];
		}
	}
	i = 0;
	do
	{
		i++;
	} while (ax[i] < x);
	i--;
	p = (x - ax[i]) / h;
	y1 = p * diff[i - 1][1];
	y2 = p * (p + 1) * diff[i - 1][2] / 2;
	y3 = (p + 1) * p * (p - 1) * diff[i - 2][3] / 6;
	y4 = (p + 2) * (p + 1) * p * (p - 1) * diff[i - 3][4] / 24;
	y = ay[i] + y1 + y2 + y3 + y4;
	printf("\nwhen x=%6.4f, y=%6.8f ", x, y);
}