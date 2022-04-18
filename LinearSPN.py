#!/usr/bin/env python3
import sys

sbox_input = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
sbox_output = [0x6, 0x5, 0x1, 0x0, 0x3, 0x2, 0x7, 0x4]
SIZE = len(sbox_input)  #8


def approximation(input, output):
    total = 0
    #For each input and output in arrays
    for index in range(SIZE):
        # and gate the sbox input and the approx input
        input_masked = sbox_input[index] & input
        # and gate the sbox output and the approx output
        output_masked = sbox_output[index] & output
        #get single bit xnor of masked input and output, total increases by 1
        #if xnor returns 1
        total += xnor(input_masked, output_masked)
        
 
    #  NL(a,b) −4.
    return total - (SIZE/2)



def xnor(a , b):
    ''' xnor gate with a single bit output -> if
    '''
    if (bin(a).count("1") - bin(b).count("1")) % 2 == 0:
          return 1
    return 0

def main():

 print( "      | ", end='')
 for i in range(SIZE):
        sys.stdout.write(hex(i)[2:].rjust(5) + " ")
 sys.stdout.write("\n")  
    
 for row in sbox_output:
        sys.stdout.write(hex(row)[2:].rjust(5) +  " | ")
        
        for col in sbox_input:
            sys.stdout.write((str (approximation(col, row))).rjust(5) + " ")

        sys.stdout.write("\n")





if __name__ == "__main__":
    main()