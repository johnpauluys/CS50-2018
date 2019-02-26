#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float change_input;
    int total_coins = 0;
    do
    {
        // get user input
        change_input = get_float("Change owed: ");
    }
    while (change_input < 0);
    // convert input to usable data type
    int change = round(change_input * 100);

    // check and count amount of quarters
    if (change / 25 > 0)
    {
        total_coins += change / 25;

        change = change % 25;
    }
    // chack and count amount of dimes
    if (change / 10 > 0)
    {
        total_coins += change / 10;
        change = change % 10;
    }
    // check and count amount of nickels
    if (change / 5 > 0)
    {
        total_coins += change / 5;
        change = change % 5;
    }
    // check and count amount of pennies
    if (change / 1 > 0)
    {
        total_coins = total_coins + change / 1;
        change = change % 1;
    }
    printf("%i\n", total_coins);
}