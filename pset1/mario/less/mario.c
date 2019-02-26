#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // get positive integer from user; repeat until input passes check
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 0 || height > 23);
    // display half pyramid
    for (int i = 0; i < height; i++)
    {
        // display spaces
        for (int j = height - (i + 1); j > 0; j--)
        {
            printf(" ");
        }
        // display bricks
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("#\n");
    }
}