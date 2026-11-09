x = int(input("Enter a number: "))

result = ""

if 0 <= x < 2**7:
    bits = bin(x)[2:]
    while len(bits) < 8:
        bits = "0" + bits
    result = bits


elif 2**7 <= x < 2**11:
    bits = bin(x)[2:]
    while len(bits) < 11:
        bits = "0" + bits

    result = "110" + bits[:-6] + " " + "10" + bits[-6:]

elif 2**11 <= x < 2**16:
    bits = bin(x)[2:]
    while len(bits) < 16:
        bits = "0" + bits

    result = "1110"+bits[:4] + " " + "10" + bits[4:10] + " " + "10" +  bits[-6:]

elif 2**16 <= x < 2**21:
    bits = bin(x)[2:]
    while len(bits) < 21:
        bits = "0" + bits

    result = "11110" + bits[:3] + " " + "10" + bits[3:9] + " " + "10" + bits[9:15] + " " + "10" + bits[-6:]


print(result)