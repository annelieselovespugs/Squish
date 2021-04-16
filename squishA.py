import numpy as np
# Command + Shift + P   =>  type 'run'  and select 'Run script'
# Command + I => runs script

############################

#Takes in a single number as an input between -100 and 100
#Outputs a number between 0 and 1 relative to the input number size
#Given two inputs, iA and iB where iA > iB the outputs oA and oB need to have oA > oB for all inputs.
#A specific input should always calculate the same output
#Every unique input should have a unique output
def squishA (value):
    #value is -100 to 100 (including endpoints)
    #num2 = np.log(value+103) #103 make sure every number is greater than 0 to avoid division issues
    #num3 = 1. / num2
    #num4 = 1 - num3
    #print num4
    output = 1 - (1. / (np.log(value+103))) #103 make sure every number is greater than 0 to avoid division issues
    print output

#test loop gives squishA every number from -100 to 100 (inclusive)
#for x in range (0,201):
    #squishA(x-100)



############################


#Takes in a single number as an input between 0 and 1
#Outputs a number between 0.25 and 0 | 0 and 0.25
#Outputs a number which is greatest when inputting 0.5 and smallest when inputting 0 or 1
#Any inputs < 0.5 produce decreasing outputs as the inputs decrease from 0.5 to 0
#Any inputs > 0.5 also produce decreasing outputs as the inputs increase from 0.5 to 1
#A specific input should always calculate the same output
#Every output has two unique inputs
def CloseToBoundaryA (value):
    if value > 0.5:
        value = value - 0.5
        output = 0.25 - (value / 2.)

    else:
        output = (value / 2.)

    print output


for x in range (0,101):
    CloseToBoundaryA(x/100.)
