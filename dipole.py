print("PiFM Dipole Calculator"'\n')
print("")
def dipole():
    frequency = float(eval(input("Enter broadcast frequency in MHz to calculate a half-wave dipole."'\n''\n')))
    print(("You entered %s MHZ."'\n' % frequency))
    length = 142.5 / frequency
    element = length / 2
    print(round(length,2), "metres, is the total length of the antenna."'\n')
    print(round(element,2), "metres, is the length of each element.")
dipole()