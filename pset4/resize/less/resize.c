// Enlarges a BMP file to n times the orignal size
// Usage: ./resize n infile outfile

#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 4 || atoi(argv[1]) < 1 || atoi(argv[1]) > 100)
    {
        fprintf(stderr, "Usage: ./resize n infile outfile\n");
        return 1;
    }

    // remember size and filenames
    int n = atoi(argv[1]);
    char *infile = argv[2];
    char *outfile = argv[3];

    // open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 1;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 2;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 1;
    }

    // determine padding for scanlines
    // in-file
    int sm_padding = (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    // out-file
    int lg_padding = (4 - (bi.biWidth * n * sizeof(RGBTRIPLE)) % 4) % 4;


    // update headers for outfile
    bi.biWidth *= n;
    bi.biHeight *= n;
    bi.biSizeImage = ((sizeof(RGBTRIPLE) * bi.biWidth) + lg_padding) * abs(bi.biHeight);
    bf.bfSize = bi.biSizeImage + sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // iterate over infile's scanlines
    for (int i = 0, biHeight = abs(bi.biHeight / n); i < biHeight; i++)
    {
        // iterate over n to add more scanlines to outfile
        for (int v = 0; v < n; v++)
        {
            // iterate over pixels in scanline
            for (int j = 0; j < bi.biWidth / n; j++)
            {
                // temporary storage
                RGBTRIPLE triple;

                // read RGB triple from infile
                fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

                // iterate over width to add extra pixels to outfile
                for (int h = 0; h < n; h++)
                {
                    // write RGB triple to outfile
                    fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
                }
            }

            // add padding to outfile
            for (int k = 0; k < lg_padding; k++)
            {
                fputc(0x00, outptr);
            }
            // move cursor to beginning of line
            fseek(inptr, (sizeof(BITMAPFILEHEADER) + sizeof(BITMAPINFOHEADER) + (sizeof(RGBTRIPLE) * (bi.biWidth / n) + sm_padding) * i), SEEK_SET);
        }
        // skip over padding of in-file, if any
        fseek(inptr, sm_padding + (sizeof(RGBTRIPLE) * (bi.biWidth / n)), SEEK_CUR);
    }

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // success
    return 0;
}