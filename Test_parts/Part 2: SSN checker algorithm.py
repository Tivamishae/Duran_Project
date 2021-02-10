# Asks the user for their social security number and splits it into 4 variables yyyy, mm, dd, xxxx.
yyyy_mm_dd_xxxx = input("Skriv ditt personnummer (yyyy-mm-dd-xxxx):")
chunks = yyyy_mm_dd_xxxx.split('-')

# - Predetermines the boolean of "validity" as False, later in the code we will see the different ways valid can be turned into True.
validity = False


# Puts the previous splits together and splits it again letter by letter.
yyyymmddxxxx = chunks[0] + chunks[1] + chunks[2] + chunks[3]
def splitword(word):
    return [char for char in word]



# Calculates the first part of the social security number algorithm.
amountlist = list((int(yyyymmddxxxx[2]) * 2, int(yyyymmddxxxx[3]), int(yyyymmddxxxx[4]) * 2, int(yyyymmddxxxx[5]), int(yyyymmddxxxx[6]) * 2, int(yyyymmddxxxx[7]), int(yyyymmddxxxx[8]) * 2, int(yyyymmddxxxx[9]), int(yyyymmddxxxx[10]) * 2))

# Calculates the second part of the social security number algorithm.
# - Predetermines the value of "x" to = 0.
x = 0
# - Iterates all elements in amountlist and separates any numbers with two digits, otherwise they are left as they are. It then adds them together into variable "x".
for i in amountlist:
    if len(str(i)) == 2:
        split_dual_number = splitword(str(i))
        for i in split_dual_number:
            x = x + int(i)
    else:
        x = x + i

# - X is now the added number of all individual digits inside amountlist and by doing the below we split the number we get into two.
split_final_number = (splitword(str(x)))

# - Definition which finalizes whether or not your social security number is valid or not and then changes the boolean of "validity" as a consequence.
def validity_checker():
    if (int(split_final_number[1])) == int(yyyymmddxxxx[11]) and (int(split_final_number[1])) == 0:
        global validity
        validity = True
    else:
        friend_of_10 = 10 - (int(split_final_number[1]))
        if  friend_of_10 == int(yyyymmddxxxx[11]):
            validity = True
        else:
            pass

validity_checker()

print(validity)