// Declares a dictionary's functionality

#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stdbool.h>

// Maximum length for a word
// (e.g., pneumonoultramicroscopicsilicovolcanoconiosis)
#define LENGTH 45

// Dictionary structure
typedef struct node
{
    bool is_word;
    struct node *path[27];
}
node;

// Prototypes
bool check(const char *word);
bool load(const char *dictionary);
unsigned int size(void);
void free_node(node *dict);
bool unload(void);

#endif // DICTIONARY_H
