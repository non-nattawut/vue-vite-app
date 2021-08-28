#include<stdio.h>

int main()
{
    double n1,n3;
    int n2;

    printf("Please enter a real number (n1)> ");
    scanf("%lf",&n1);
    printf("Please enter an integer number (n2)> ");
    scanf("%d",&n2);

    printf("n1 = %f and n2 = %d\n",n1,n2);
    n3 = (int)n1 + n2;

    printf("So, n3 = %f",n3);

    return(0);
}