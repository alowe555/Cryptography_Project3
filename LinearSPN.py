#!/usr/bin/env python3
import sys

sbox_input = [0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7]
sbox_output = [0x6, 0x5, 0x1, 0x0, 0x3, 0x2, 0x7, 0x4]
SIZE = len(sbox_input)  # 8

'''
Takes an input and an output and finds N(l) - 2^(number of bits - 1) (number of 'yeses' - 4)
@param input - the input sum for an S-box
@param output - the output sum for an S-box
@return The normalized linear approximation of N(l) of this input/output pair
'''


def approximation(input, output):
    total = 0
    # For each input and output in arrays
    for index in range(SIZE):
        # and gate the sbox input and the approx input
        input_masked = sbox_input[index] & input
        # and gate the sbox output and the approx output
        output_masked = sbox_output[index] & output
        # get single bit xnor of masked input and output, total increases by 1
        # if xnor returns 1
        total += xnor(input_masked, output_masked)
        
    #  NL(a,b) - 4.
    return total - SIZE/2

'''
Calculates the trail bias given the inputs to all s-boxes in the trail
@param sboxes - The input/output sum pairs for all sboxes in the trail
            Ex) [[0x6, 0x7], [0x6, 0x7], [0x7, 0x4], [0x7, 0x4], [0x4, 0x7]]
@return totalBias - The bias of the trail taken by this input in a simple SPN
            This is calculated using the Piling-up Lemma
'''
# trail - [[0x6, 0x7], [0x6, 0x7], [0x7, 0x4], [0x7, 0x4], [0x4, 0x7]]
def trailBias(sboxes):
    # To find the total bias of a trail, you multiply all the biases of each level together
    # You then multiply that number by 2^(number of s-boxes - 1)
    totalBias = 1
    # The simple SPN has 3 s-boxes
    for sbox in sboxes:
        # Take each input and find its linear approximation
        approx = approximation(sbox[0], sbox[1]) /SIZE
        totalBias *= approx
            
    totalBias *= 2 ** (SIZE - 1)
    return totalBias


def xnor(a , b):
    ''' xnor gate with a single bit output -> if
    '''
    if (bin(a).count("1") - bin(b).count("1")) % 2 == 0:
          return 1
    return 0


def main():

    print("      | ", end='')
    for i in sbox_output:
        sys.stdout.write(hex(i)[2:].rjust(5) + " ")
    
    sys.stdout.write("\n")  
    sys.stdout.write("      --------------------------------------------------") 
    sys.stdout.write("\n")  
        
    for row in sbox_input:
        sys.stdout.write(hex(row)[2:].rjust(5) + " | ")
        
        for col in sbox_output:
            sys.stdout.write((str (approximation(row, col))).rjust(5) + " ")

        sys.stdout.write("\n")

    sys.stdout.write("\n--------------------------------------------------\n")

    trail = [[0x6, 0x4], [0x6, 0x4], [0x6, 0x4], [0x4, 0x2]]
    sys.stdout.write('\nThe bias of the trail connecting P1, P2, P4, P5 and H1 is: ' + str(trailBias(trail)))
    sys.stdout.write("\n")
    
if __name__ == "__main__":
    main()
