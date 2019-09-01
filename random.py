def findWinners():
    fac = int(input("Enter factor digit: "))
    must = int(input("Enter must-have digit: "))
    n = int(input("Enter the number of participants: "))

    count = 0

    for i in range(1,n+1):
        if ((i % fac == 0) and contains(must, i)):
            count += 1
            print(i)
    print("Total number of winners: ", count)

# this boolean function checks if the number 'num'
# contains the digit 'digit'
def contains(digit, num):
    while num > 0:
        if (num % 10 == digit):
            return True
        else:
            num = num // 10
    return False

findWinners()
