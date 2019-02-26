// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// create instance of struct node
node *root;
unsigned int word_count = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    // declare variables
    node *trav = root; // avoid using original node

    // loop through text char by char
    int wordlen = strlen(word);
    for (int i = 0; i < wordlen; i++)
    {
        unsigned char letter = word[i];

        // check if current char is a letter or an apostrophe
        // set char to lowercase for case insensitivity
        if (letter == '\'')
            letter = 26;
        else if (isupper(letter))
            letter += (32 - 'a');
        else
            letter -= 'a';

        // follow path if exists
        if (trav->path[letter] == NULL)
            return false;

        trav = trav->path[letter];
    }
    // return appropriate bool value
    if (trav->is_word)
        return true;

    return false;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{

    // load dictionary
    FILE *dict = fopen(dictionary, "r");

    // check if dictionary loaded successfully, if not, return 1
    if (!dict)
        return false;

    // define variables
    root = calloc(1, sizeof(node));
    // sanity check
    if (!root)
        return false;
    node *trav = root;

    int trav_index; // used to calculate which path to follw

    for (int c = fgetc(dict); c != EOF; c = fgetc(dict))
    {
        // check if end of word is reached
        if (c == '\n')
        {
            trav->is_word = true;
            word_count++;
            // reset path
            trav = root;
        }
        else
        {
            // check if current char is an apostrophe or letter
            if (c == '\'')
                trav_index = 26;
            else if (c >= 'A' && c <= 'Z')
                trav_index = c - ('a' - 32);
            else
                trav_index = c - 'a';

            // check is path is already cleared, if not clear one
            if (!trav->path[trav_index])
            {
                //trav = malloc(sizeof(node));
                trav->path[trav_index] = calloc(1, sizeof(node));

                // check whether malloc was successful
                if (!trav->path[trav_index])
                    return false;
            }
            trav = trav->path[trav_index];
        }
    }
    // close file and reset path, before returning true
    fclose(dict);
    trav = root;
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload()
{
    // reset path
    node *dict = root;
    // close node
    free_node(dict);
    return true;
}

void free_node(node *dict)
{
    // iterate through letters in alphabet
    for (int i = 0; i < 27; i++)
    {
        // check whether path exists. If so, enter path and attempt to free nodes.
        if (dict->path[i])
            // recursion
            free_node(dict->path[i]);
    }
    // free memory
    free(dict);
}
