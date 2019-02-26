#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Get cipher code from command line, print user input (plaintext) in cipher form (ciphertext)
int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // convert argv[1] to integer
        int k = atoi(argv[1]);

        // get string from user input
        string plaintext = get_string("plaintext: ");

        printf("ciphertext: ");
        // encipher string by printing
        for (int c = 0; c < strlen(plaintext); c++)
        {
            // handle uppercase chars
            if (isalpha(plaintext[c]) && isupper(plaintext[c]))
            {
                printf("%c", ((plaintext[c] - 65 + k) % 26) + 65);
            }
            // handle lowercase chars
            else if (isalpha(plaintext[c]) && islower(plaintext[c]))
            {
                printf("%c", ((plaintext[c] - 97 + k) % 26) + 97);
            }
            // handle all other chars
            else
            {
                printf("%c", plaintext[c]);
            }
        }
        printf("\n");
        exit(0);
    }
    else
    {
        printf("Usage: %s [number]\n", argv[0]);
        exit(1);
    }
}