import base64

def from_base64(x):
    decoded_bytes = bytes.fromhex(x)
    flag = base64.b64decode(decoded_bytes).decode()
    print(flag)
    return 1

x = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
from_base64(x)