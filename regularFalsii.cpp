#include <stdio.h>
#include <string.h>
#include <math.h>
#define EPS 0.00005



// define the function here
#define f(x) cos(x)-x*exp(x)


void FAL_POS();
int main()
{
    printf("\n Solution by FALSE POSITION method\n"); 
    printf("\n Equation is ");
    printf("\n\t\t\t 3*x + sin(x)-exp(x)=0\n\n");
    FAL_POS();
}
void FAL_POS()
{
    double f0, f1, f2;
    double x0, x1, x2;
    int itr;
    int i;
    printf("Enter the number of iteration:"); 
    scanf("%d",&itr);

    for(x1=0.0;;)
    {
        f1 = f(x1);
        if (f1 > 0)
        {
            break;
        }
        else
        {
            x1 = x1 + 0.1;
        }
    }
    x0=x1-0.1;
    f0=f(x0);
    printf("\n\t\t-----------------------------------------");
    printf("\n\t\t ITERATION\t x2\t\t F(x)\n");
    printf("\t\t--------------------------------------------");
    for(i=0;i<itr;i++)
    {
        x2 = x0 - ((x1 - x0) / (f1 - f0)) * f0;
        f2 = f(x2);
        if (f0 * f2 > 0)
        {
            x1 = x2;
            f1 = f2;
        }
        else
        {
            x0 = x2;
            f0 = f2;
        }
        if (fabs(f(2)) > EPS)
        {
            printf("\n\t\t%d\t%f\t%f\n", i + 1, x2, f2);
        }
    }
    printf("\t\t--------------------------------------------");
    printf("\n\t\t\t\tRoot=%f\n",x2);
    printf("\t\t-------------------------------------------");
}
    