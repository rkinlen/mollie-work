def dec2bin(number):
    bin = ""
    while  number >=  0:
        remainder  = number % 2
        number = int(number /2)
        bin = str(remainder)+bin
        if number == 0  :
            break
        
    
    #print ("bin", bin)
    return bin

assert dec2bin(0) == "0"
assert dec2bin(1) == "1"
assert dec2bin(2) == "10"
assert dec2bin(3) == "11"
assert dec2bin(128) == "10000000"

if __name__ == "__main__":
    decInput = False

    while decInput == False:
        try:
            decInput = int(input("number:  "))
        except:
            print("invalid number")

    print("Binary", dec2bin(decInput))
