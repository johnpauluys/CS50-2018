#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// get keyword from command line input
int main(int argc, string argv[])
{
    if (argc == 2)
    {
        string key = argv[1];
        // check if all chars in keyword are alphabetical chars
        // exit if not
        for (int c = 0; c < strlen(key); c++)
        {
            if (isalpha(key[c]) == false)
            {
                // exit if char other than alpha chars are present
                printf("Usage: %s KEYWORD\n", argv[0]);
                exit(1);
            }
        }
        // get user input (plaintext)
        string plaintext = get_string("plaintext: ");
        // set a counter for chars in key
        int k_counter = 0;
        printf("ciphertext: ");
        for (int c = 0; c < strlen(plaintext); c++)
        {
            // check if char isalpha
            if (isalpha(plaintext[c]))
            {
                // calc k
                int k = tolower(key[k_counter % strlen(key)]) - 97;
                // handle uppercase and lowercase and print char
                if (isupper(plaintext[c]))
                {
                    printf("%c", ((plaintext[c] - 65) + k) % 26 + 65);

                }
                else if (islower(plaintext[c]))
                {
                    printf("%c", ((plaintext[c] - 97) + k) % 26 + 97);
                }
                k_counter++;
            }
            else
            {
                // if char is not alphabetical char, print plaintext char
                printf("%c", plaintext[c]);
            }
        }
        // print new line
        printf("\n");

    }
    else
    {
        // print error message and exit
        printf("Usage: %s KEYWORD\n", argv[0]);
        exit(1);
    }
}
