#include <stdio.h>
#include <cs50.h>

int main(void)
{
    long long cc_number;
    int sum = 0;
    int number_length = 0;
    int first_digit = 0;
    int second_digit = 0;
    do
    {
        cc_number = get_long_long("Number: ");
    }
    while (cc_number == 0 || cc_number < 0);
    for (long long x = 100; x < cc_number * 10; x *= 100)
    {
        number_length++;
        int digit = (cc_number % x) / (x/10);
        second_digit = digit;
        if (digit * 2 > 9)
        {
            sum += ((digit * 2) % 10) + (((digit * 2) % 100) / 10);
        }
        else
        {
            sum += digit * 2;
        }

    }
    for (long long x = 10; x < cc_number * 10; x *= 100)
    {
       number_length++;
       sum += (cc_number % x) / (x/10);
       first_digit = (cc_number % x) / (x/10);
    }
    if (sum % 10 == 0)
    {
        if (number_length % 2 == 0)
        {
            if (second_digit == 5 && first_digit >= 1 && first_digit <= 5)
            {
                printf("MASTERCARD\n");
            }
            else if (second_digit == 4 && number_length == 16)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
        else
        {
            if (first_digit == 3 && (second_digit == 4 || second_digit == 7) && number_length == 15)
            {
                printf("AMEX\n");
            }
            else if (first_digit == 4 && number_length == 13)
            {
                printf("VISA\n");
            }
            else
            {
                printf("INVALID\n");
            }
        }
    }
    else
    {
        printf("INVALID\n");
    }
}