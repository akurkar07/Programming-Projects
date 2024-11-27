# base 2 to base 4 and vice versa
# ACGT are 0,1,2,3

# def DNA2BIN(dna):
#     binary = ""
#     for base in dna:
#         binary += lookup[base]
#     return binary

lookup = {
    "A":"00",
    "C":"01",
    "G":"10",
    "T":"11"
}

l2 = [["A","00"],["C","01"],["G","10"],["T","11"]]
l3 = ["A","C","G","T"]

with open("input.txt","r") as file:
    inp = file.read()

def BIN2DNA(binary):
    dna = []
    for count in range(0,len(binary),2):
        dna.append(binary[count:count+2])
    accdna = []
    for i in dna:
        accdna.append(l3[list(lookup.values()).index(i)])
    return "".join(accdna)
#inp = str(input("Enter chars > "))
x = ''.join(format(ord(i), '08b') for i in inp)
print(BIN2DNA(x))