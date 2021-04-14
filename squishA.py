import numpy as np

# Command + Shift + P   =>  type 'run'  and select 'Run script'
# Command + I => runs script


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
for x in range (0,201):
    squishA(x-100)
