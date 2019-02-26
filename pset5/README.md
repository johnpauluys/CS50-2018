# Questions

## What is pneumonoultramicroscopicsilicovolcanoconiosis?

Pneumonoultramicroscopicsilicovolcanoconiosis is the longest word published in a dictionary.
It refers to a lung disease caused by inhaling very fine (volcanic) ash and/or sand dust.

## According to its man page, what does `getrusage` do?

`getrusage` returns resource usage statistics in a structure (rusage) pointed to by usage.

int getrusage(int who, struct rusage *usage);

## Per that same man page, how many members are in a variable of type `struct rusage`?

16

## Why do you think we pass `before` and `after` by reference (instead of by value) to `calculate`, even though we're not changing their contents?

To be able to claculate the time, by calculating the difference between `before` and `after` values.

## Explain as precisely as possible, in a paragraph or more, how `main` goes about reading words from a file. In other words, convince us that you indeed understand how that function's `for` loop works.

After the file, containing text to be spell checked, is opened for reading, `main` iterates over each character, checking whether each of them is either an alphabetical character or an apostrophe located anywhere but the beginning of a word. Each qualifying character gets appended to a string called `word`. We keep track of the word length as well as the current character of the word by using the `index` variable. The `index` variable gets incremented for each qualified character found. During each iteration another check is done to ensure that the current word is not longer than the maximum word length (`LENGTH`). If that would be the case, the remaining characters get ignored and `index` gets reset to 0. The same would happen if a character happens to be a digit.

If any other character, except for the ones mentioned above gets encountered, `main` assumes that it has reached the end of a word and a nul terminator (`\0`) is added to end `word`. After incrementing the word counter variable called `words`, the newly found word's spelling gets checked, while calculating the amount of time it needs to be checked. If found, misspelled words get printed, before `index` gets reset to 0 to prepare for the next word.

## Why do you think we used `fgetc` to read each word's characters one at a time rather than use `fscanf` with a format string like `"%s"` to read whole words at a time? Put another way, what problems might arise by relying on `fscanf` alone?

Because `fscanf` looks for whitespace to determine the end of a word, it could include other characters, such as commas and periods. Although one could then write code to strip these characters from the string, but it should in most cases be beneficial to have more control (and simpler design) to use `fgetc` to evaluate each character individually and decide how each should be handled.

## Why do you think we declared the parameters for `check` and `load` as `const` (which means "constant")?

Once one of the functions `check` or `load` is called, there would be no reason for the values of `dictionary` (in `load`) and `word` (in `check`) to be changed.