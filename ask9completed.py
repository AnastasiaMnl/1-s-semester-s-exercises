input_file = input("Please enter ASCII file")
f = open(input_file, "r")
lines= f.read()
f.close() 

characters = ''.join(format(ord(i),'07b')for i in lines)
characters = list(characters)

zeros = 0
ones= 0
max1 = 0
max0 = 0
i=0
#LONGEST SEQUENCE OF 0's AND 1's
for i in characters:
    if i == '0' :
        zeros=zeros +1
        ones = 0
        if zeros > max0 :
            max0 = zeros
    else:
        ones= ones + 1
        zeros = 0
        if ones > max1 :
            max1 = ones

print("The longest sequencce of 0s is:", max0)
print("The longest sequencce of 1s is:", max1)
