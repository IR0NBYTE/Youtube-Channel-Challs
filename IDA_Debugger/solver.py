# This chall come from the flare-ctf !

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits = 8: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits = 8: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

key = 0x56

enc_data = b"bngcg`debd"

ans = []
for elt in enc_data:
    ans.append(elt ^ 0x56)

printf(f"arg1 : {"".join([chr(c) for c in ans])}")


arg2 = []
for elt in range(0x10):
    arg2.insert(elt, 0)

arg2[0] = rol(0x1b, 0xf2)

arg2[1] = 0x30 ^ 0xb3 ^ 0xf2 ^ 0x40

arg2[2] = 0x1f ^ 0x71

arg2[3] = rol(0xb0, 0xbc) - 0xa3

arg2[4] = 0xe8 + 0x79

arg2[5] = rol(0xf6 + 0x28, 0x82)

# Continue reversing all the blocks to get the full flag. 

for index, item in enumerate(arg2):
    print(chr(item & 0xff), end = "")


