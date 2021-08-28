#include<stdio.h>
#include<math.h>

int main()
{
    double num;
    double result;

    printf("Enter a number> ");
    scanf("%lf",&num);

    result = sqrt(num);

    printf("Result: %.f",result);

    return(0);
}