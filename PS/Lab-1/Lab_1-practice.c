#include<stdio.h>
#include<math.h>

#define DIVIDER 2

int main()
{
    int num1,num2; // input variable
    int sum; // problem variable
    double result; // output variable

    printf("Enter an integer (num1)> ");
    scanf("%d",&num1);

    printf("Enter an integer (num2)> ");
    scanf("%d",&num2);

    sum = num1+num2;
    result = (double)sum / DIVIDER;

    printf("Result: %f",result);

    return(0);
}