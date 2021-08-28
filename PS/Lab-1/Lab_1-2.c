#include<stdio.h>
#include<math.h>

#define PI 3.14159

int main()
{
    double diameter,radius,result;

    printf("Please enter a diameter> ");
    scanf("%lf",&diameter);

    radius = diameter/2;
    result = (4*PI*pow(radius,3))/3;

    printf("The volume of sphere is %.4f",result);

    return(0);

}