#include <stdio.h>

int main(int argc, char *argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        fprintf(stderr, "Usage: ./recover image\n");
        return 1;
    }

    // open input file
    FILE *inptr = fopen(argv[1], "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", argv[1]);
        return 2;
    }

    // set counter and 1st temp filename
    int counter = 0;
    char filename[8];
    sprintf(filename, "%03i.jpg", counter);

    FILE *img = fopen(filename, "w");
    if (img == NULL)
    {
        fprintf(stderr, "Could not write to file.\n");
        return 3;
    }

    // create variable to hold a set amount bytes
    unsigned char buffer[512];

    // iterate through inptr until it returns 1 (feof | ferror)
    while (fread(buffer, sizeof(buffer), 1, inptr) == 1)
    {
        // check structure
        if (buffer[0] == 0xff &&
            buffer[1] == 0xd8 &&
            buffer[2] == 0xff &&
            (buffer[3] & 0xe0) == 0xe0)
        {
            // check if first jpeg has been found
            if (counter == 0)
            {
                // incrementing counter to initiate fwrite
                counter++;
            }
            else
            {
                // close previous img FILE
                fclose(img);
                // create new filename
                sprintf(filename, "%03i.jpg", counter);

                // create new file before incrementing counter
                img = fopen(filename, "w");
                if (img == NULL)
                {
                    fprintf(stderr, "Could not write to file %s.\n", filename);
                    return 3;
                }
                counter++;
            }
        }
        // end iteration by writing to outptr
        if (counter > 0)
        {
            fwrite(&buffer, sizeof(buffer), 1, img);
        }
    }
    fclose(inptr);
    fclose(img);
}