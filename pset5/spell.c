// Implements a spell-checker

#include <ctype.h>
#include <stdio.h>
#include <sys/resource.h>
#include <sys/time.h>

#include "dictionary.h"

// Undefine any definitions
#undef calculate
#undef getrusage

// Default dictionary
#define DICTIONARY "dictionaries/large"

// Prototype
double calculate(const struct rusage *b, const struct rusage *a);

// my code
typedef struct _trie
{
    bool is_word;
    struct _trie *path[27];
}
node;

// declare functions
void load(node *dict, FILE dictionary);
void check(node *dict);
void unload(node *dict);


int main(int argc, char *argv[])
{
    // Check for correct number of args
    if (argc != 2 && argc != 3)
    {
        printf("Usage: speller [dictionary] text\n");
        return 1;
    }

    // Structures for timing data
    struct rusage before, after;

    // Benchmarks
    double time_load = 0.0, time_check = 0.0, time_size = 0.0, time_unload = 0.0;

    // Determine dictionary to use
    char *dictionary = (argc == 3) ? argv[1] : DICTIONARY;

    node *root = malloc(sizeof(node));

    // Load dictionary
    getrusage(RUSAGE_SELF, &before);
    bool loaded = load(root, dictionary);
    getrusage(RUSAGE_SELF, &after);

    // Exit if dictionary not loaded
    if (!loaded)
    {
        printf("Could not load %s.\n", dictionary);
        return 1;
    }

    // Calculate time to load dictionary
    time_load = calculate(&before, &after);

    // Try to open text
    char *text = (argc == 3) ? argv[2] : argv[1];
    FILE *file = fopen(text, "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", text);
        unload();
        return 1;
    }

    // Prepare to report misspellings
    printf("\nMISSPELLED WORDS\n\n");

    // Prepare to spell-check
    int index = 0, misspellings = 0, words = 0;
    char word[LENGTH + 1];

    // Spell-check each word in text
    for (int c = fgetc(file); c != EOF; c = fgetc(file))
    {
        // Allow only alphabetical characters and apostrophes
        if (isalpha(c) || (c == '\'' && index > 0))
        {
            // Append character to word
            word[index] = c;
            index++;

            // Ignore alphabetical strings too long to be words
            if (index > LENGTH)
            {
                // Consume remainder of alphabetical string
                while ((c = fgetc(file)) != EOF && isalpha(c));

                // Prepare for new word
                index = 0;
            }
        }

        // Ignore words with numbers (like MS Word can)
        else if (isdigit(c))
        {
            // Consume remainder of alphanumeric string
            while ((c = fgetc(file)) != EOF && isalnum(c));

            // Prepare for new word
            index = 0;
        }

        // We must have found a whole word
        else if (index > 0)
        {
            // Terminate current word
            word[index] = '\0';

            // Update counter
            words++;

            // Check word's spelling
            getrusage(RUSAGE_SELF, &before);
            bool misspelled = !check(word);
            getrusage(RUSAGE_SELF, &after);

            // Update benchmark
            time_check += calculate(&before, &after);

            // Print word if misspelled
            if (misspelled)
            {
                printf("%s\n", word);
                misspellings++;
            }

            // Prepare for next word
            index = 0;
        }
    }

    // Check whether there was an error
    if (ferror(file))
    {
        fclose(file);
        printf("Error reading %s.\n", text);
        unload();
        return 1;
    }

    // Close text
    fclose(file);

    // Determine dictionary's size
    getrusage(RUSAGE_SELF, &before);
    unsigned int n = size();
    getrusage(RUSAGE_SELF, &after);

    // Calculate time to determine dictionary's size
    time_size = calculate(&before, &after);

    // Unload dictionary
    getrusage(RUSAGE_SELF, &before);
    bool unloaded = unload();
    getrusage(RUSAGE_SELF, &after);

    // Abort if dictionary not unloaded
    if (!unloaded)
    {
        printf("Could not unload %s.\n", dictionary);
        return 1;
    }

    // Calculate time to unload dictionary
    time_unload = calculate(&before, &after);

    // Report benchmarks
    printf("\nWORDS MISSPELLED:     %d\n", misspellings);
    printf("WORDS IN DICTIONARY:  %d\n", n);
    printf("WORDS IN TEXT:        %d\n", words);
    printf("TIME IN load:         %.2f\n", time_load);
    printf("TIME IN check:        %.2f\n", time_check);
    printf("TIME IN size:         %.2f\n", time_size);
    printf("TIME IN unload:       %.2f\n", time_unload);
    printf("TIME IN TOTAL:        %.2f\n\n",
           time_load + time_check + time_size + time_unload);

    // Success
    return 0;
}

// Returns number of seconds between b and a
double calculate(const struct rusage *b, const struct rusage *a)
{
    if (b == NULL || a == NULL)
    {
        return 0.0;
    }
    else
    {
        return ((((a->ru_utime.tv_sec * 1000000 + a->ru_utime.tv_usec) -
                  (b->ru_utime.tv_sec * 1000000 + b->ru_utime.tv_usec)) +
                 ((a->ru_stime.tv_sec * 1000000 + a->ru_stime.tv_usec) -
                  (b->ru_stime.tv_sec * 1000000 + b->ru_stime.tv_usec)))
                / 1000000.0);
    }
}

// FUNCTIONS

void load(node *dict, FILE dictionary)
{
    // define variables
    node *trav = dict;
    int trav_index; // used to calculate which path to follw
    int wrd_index = 0; // used to determine start of new word

    for (int c = fgetc(dictionary); c != EOF; c = fgetc(dictionary))
    {
        // check if end of word is reached
        if (c != '\n')
        {

            if (wrd_index == 0)
            {
                // if current char is a beginning of a new word
                // start at first node
                trav = dict;
            }
            // check if current char is an apostrophe
            if (c == '\'')
                trav_index = 26;
            else
                trav_index = c - 'a';

            // check is path is already cleared, if not clear one
            if (!trav->path[trav_index])
            {
                trav->path[trav_index] = malloc(sizeof(node));
                // check whether malloc was successful
                if (!trav->path[trav_index])
                {
                    fprintf(stderr, "Could not allocate memory.\n");
                    exit(1);
                }

            }
            // create path

            trav = trav->path[trav_index];
            wrd_index++;
        }
        else
        {
            wrd_index = 0;
            trav->is_word = true;
            //printf("\n");
        }
    }
    fclose(dictionary);
}

void check(node *dict)
{
    // open text file
    FILE *text = fopen("texts/cat.txt", "r");
    if (!text)
    {
        fprintf(stderr, "Could not load file.\n");
        exit(1);
    }

    // declare variables
    node *trav = dict; // avoid using original node
    char word[45] = "";
    int letter_index = 0; // counts letters in word

    // loop through text char by char
    for (int letter = fgetc(text); letter != EOF; letter = fgetc(text))
    {
        // check if current char is a letter or an apostrophe
        if (isalpha(letter) || (letter == '\'' && letter_index != 0))
        {
            // copy char to word string
            sprintf(&word[letter_index], "%c", letter);

            // set char to lowercase for case insensitivity
            if (isupper(letter))
            {
                letter += (32 - 'a') ;
            }
            // set apostrophe to last char in path array
            else if (letter == '\'')
                letter = 26;
            else
                letter -= 'a';

            // check if path exists, otherwise create/open one
            if (trav->path[letter])
            {
                trav = trav->path[letter];
            }
            letter_index++;
        }
        // if a char comes up that isn't a letter or an apostrophe
        // theend of a word is probably found and should be checked
        else
        {
            if (!trav->is_word && (strcmp(word, "") != 0))
            {
                printf("%s\n", word);
            }
            // set everything back to zero to start with a new word
            letter_index = 0;
            trav = dict;
            strcpy(word, "");
        }

    }
    fclose(text);
}

void unload(node *dict)
{
    //node trav = *dict;

    for (int i = 0; i < 27; i++)
    {
        if (dict->path[i])
            unload(dict->path[i]);

    }
    free(dict);

}