# Python program to generate odd sized magic squares
# A function to generate odd sized magic squares
 
def generateSquare(n):
 
    # 2-D array with all slots set to 0
    magicSquare = []
    for i in range(n):
        temp = []
        for j in range (n):
            temp.append(0)
        magicSquare.append(temp)
    # initialize position of 1
    i = int(n/2)
    j = n-1
     
    # Fill the magic square by placing values
    num = 1
    while num <= (int(n*n)):
        if i == -1 and j == n: # third condition
            j = n-2
            i = 0
        else:
            # next number goes out of right side of square 
            if j == n:
                j = 0
            # next number goes out of upper side
            if i < 0:
                i = n-1
                 
        if magicSquare[i][j]: # 2nd condition
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = num
            num = num+1
                 
        j = j+1
        i = i-1 #1st condition

    return magicSquare
 
 
# Driver program
 
# Works only when n is odd 
 
#Contributed by Harshit Agrawal
