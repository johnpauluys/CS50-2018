#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// declare global variables
// set max password length
int pwdlen = 5;
char salt[3];
char *coded;

// declare function(s)
void run_thru(int lvl, int dpth, char pw[pwdlen + 1], char *hash);

int main(int argc, char *argv[])
// check if program is used correctly
{
    char key[pwdlen + 1];
    if (argc != 2)
    // exit if used wrongly
    {
        printf("Usage: %s HASH\n", argv[0]);
        return 1;
    }
    else
    {
        char *hash = argv[1];
        // get me some salt
        for (int s = 0; s < sizeof(salt) - 1; s++)
            salt[s] = hash[s];

        // loop through each char of the password
        for (int pw_chr = 0; pw_chr < pwdlen; pw_chr++)
        {
            for (int pw_len = 0; pw_len < pw_chr; pw_len++)
                run_thru(pw_len, pw_chr, key, hash);
        }
    }
}

void run_thru(int lvl, int dpth, char pw[pwdlen + 1], char *hash)
{
    // loop through alphabet
    for (int i = 0; i < 52; i++)
    {
        // loop through lower and uppercase letters
        char letter = (i < 26) ? i + 65 : i + 97 - 26;
        // change pw's last character to letter value
        pw[lvl] = letter;

        // if the end of a word is reached, check hash (crypt)
        if (lvl == dpth)
        {
            coded = crypt(pw, salt);
            if (strcmp(hash, coded) == 0)
            {
                printf("%s\n", pw);
                exit(0);
            }
        }
        // else recurse
        else if (pw[lvl] != (52 + 97 - 26))
        {
            run_thru(lvl + 1, dpth, pw, hash);
        }
    }
}