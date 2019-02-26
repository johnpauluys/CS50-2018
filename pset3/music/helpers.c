// Helper functions for music

#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "helpers.h"

const string notes[] = {"A", "A#", "B", "C", "C#", "D",
                        "D#", "E", "F", "F#", "G", "G#"
                       };

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    // convert 1st and last char of fraction into ints
    float x = atoi(&fraction[0]);
    float y = atoi(&fraction[2]);
    // calc fraction
    float dur = x/y;
    // divide fraction by 1/8
    int duration = dur / 0.125;
    return duration;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // piano index will be incremented and used to calculate frequency
    int piano_index = 0;
    // set octave to 0
    int o = 0;
    float f = 0.0;
    do
    {
        // strlen(notes) should also work, but I understand too little of
        // newly introduced data types
        for (int n = 0; n < 12; n++)
        {
            // create an array of chars (string) of each note
            char temp_note[4];
            if (n < 3)
                sprintf(temp_note, "%s%i", notes[n], o);
            else
                sprintf(temp_note, "%s%i", notes[n], o+1);
            // after string is created check if note is flat
            if (strlen(note) == 3 && note[1] == 'b')
                {
                    if ((strncmp(&note[0], &temp_note[0], 1) == 0) && (strncmp(&note[2], &temp_note[1], 1) == 0))
                    {
                        f = piano_index - 49;  // adjust for flat note
                        // calc frequency
                        float frequency = pow(2, f/12) * 440;
                        // round frequency off
                        int rounded = round(frequency);
                        return rounded;
                    }
                }
            // otherwise check if note is the current piano key
            else if (strcmp(note, temp_note) == 0)
            {   // no adjustments necessary, as these notes are present in notes
                f = piano_index - 48;
                // calc frequency
                float frequency = pow(2, f/12) * 440;
                // round frequency off
                int rounded = round(frequency);
                return rounded;
            }
            // inceremnt piano
            piano_index++;
        }
        // inceremnt octave
        o++;
    }
    while (o < 8);
    return 0;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (strcmp(s, "") == 0)
        return true;
    else
        return false;
}
