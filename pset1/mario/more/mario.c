#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = 0;
    // get integer from user
    do
    {
        height = get_int("Height: ");
    }
    while (height < 0 || height > 23);
    // display pyramid
    for (int i = 0; i < height ; i++)
    {
        // display spaces
        for (int j = (height - i) - 1; j > 0; j--)
        {
            printf(" ");
        }
        // display bricks
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("  ");
        // display more bricks after two spaces
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }

}