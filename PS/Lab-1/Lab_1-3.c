#include<stdio.h>
#include<math.h>

#define ANNUAL_INTEREST 1.5

int main()
{
    int purchase_price,down_payment,time_peroid;
    
    printf("Please enter the purchase price> ");
    scanf("%d",&purchase_price);
    printf("Please enter the down payment> ");
    scanf("%d",&down_payment);
    printf("Please enter the total number of payment> ");
    scanf("%d",&time_peroid);

    double monthly_interest = ANNUAL_INTEREST/12;
    double borrow_amount = purchase_price-down_payment;
    double result = (monthly_interest*borrow_amount) / (1-pow(1+monthly_interest,-time_peroid)); // สูตร

    printf("******************************\n");
    printf("The amount borrowed: $%.2f\n",borrow_amount);
    printf("The monthly payment: $%.2f",result);

    return(0);
}