#from Crypto.Util.number import *

def invert_num(x):
    hex_str = hex(x)

    hex_string = hex_str[2:]

    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    hex_bytes = [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

    ascii_bytes = bytes(hex_bytes)
    
    print(ascii_bytes.decode('utf-8'))

# x = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
# invert_num(x)