# binary-to-7segments
This code generates a file containing the conversion of decimal values to 7 segments display. Each line of the file represents a decimal value and the data is the bits-length output to activate 7segment display. LCD is based on the following pattern

<img src="https://user-images.githubusercontent.com/38757175/180287439-6d4d9622-af1c-44c4-bd2d-1fe2e1e2fae1.png" width="250">

Besides, high voltage deactivate the LCD while low voltages activates it.

# Default
- 4x7segments display which correpond to 28 bits output
- 10.000 decimals representation (0 to 9999)

# Comment
For higher numbers, more LCD's are required which can be easily changed in the code
