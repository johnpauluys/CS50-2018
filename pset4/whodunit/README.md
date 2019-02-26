# Questions

## What's `stdint.h`?

'stdint.h' is a header that declares sets of integer types with fixed widths, where the "width"
of an integer type is the number of bits used to store its value in a binary system.

## What's the point of using `uint8_t`, `uint32_t`, `int32_t`, and `uint16_t` in a program?

Code portability. The standard int variable in C has different bit sizes on different machines.
It might have 32 bits on one computer, but 16 bits on another. This could cause the program to
crash or behave unexpectedly. stdint.h provides us with integer types with fixed numbers of bits.

## How many bytes is a `BYTE`, a `DWORD`, a `LONG`, and a `WORD`, respectively?

8-bit (unsigned), 32-bit (unsinged), 32-bit (signed), 16-bit (unsigned)

## What (in ASCII, decimal, or hexadecimal) must the first two bytes of any BMP file be? Leading bytes used to identify file formats (with high probability) are generally called "magic numbers."

Hexadecimal (0x42 and 0x4D)

## What's the difference between `bfSize` and `biSize`?

bfSize is the file's size in bytes.
biSize is the amount of bytes required by the structure.

## What does it mean if `biHeight` is negative?

A negative biHeight indicates a top-down bitmap that originates from the top and also cannot be compressed.

## What field in `BITMAPINFOHEADER` specifies the BMP's color depth (i.e., bits per pixel)?

biBitCount

## Why might `fopen` return `NULL` in lines 24 and 32 of `copy.c`?

On line 24 it would return NULL if the file doesn't exist or something else avoiding the file to be opened.
On line 32 it might return NULL if the filename exists and is a read-only file or
the disk might not be writable.

## Why is the third argument to `fread` always `1` in our code?

We are working with only one element each time, where the size of the each element is
specified in the second argument.

## What value does line 63 of `copy.c` assign to `padding` if `bi.biWidth` is `3`?

0x00

## What does `fseek` do?

fseek() sets the position indicator to a position in the file being read. The offset argument moves
the indicator to the offset value relative to the start of file, current position or end of file,
depending on what the third argument (SEEK_SET, SEEK_CUR, or SEEK_END, respectively) is.

## What is `SEEK_CUR`?

The current indicator position in the file being read.
