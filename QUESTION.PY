# Write the codes either in Python OR C/C++

# ################ Assignment 3 ###############
# Write a Gauss Jordan code with partial pivoting and solve the follow problems –

# Q1. Solve :
# 	x + 3y + 2z = 2
# 	2x + 7y + 7z = -1
# 	2x + 5y + 2z = 7

# Q2. Solve :
# 2y + 5z = 1
# 3x – y + 2z = - 2
#  x – y + 3z = 3
# Q3.Find the inverse of the matrix (FYI inverse exists) and check A A-1 = I :
#  1   -3    7
#     A =  -1    4   -7
#            -1    3   -6
# You should write separate functions for --
# (a) partial pivoting, (b) Gauss-Jordan method, (c) matrix multiplication
# then call them from the main function.Read the matrices from files. Avoid using “break” but may
# use “next” or “continue”


# PROGRAM STARTS


# A function for partialn pivot
def partialpivot(a, b):
    n = len(a)
    for r in range(0, n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1, n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    for x in range(0, n):
                        d1 = a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                        d1 = b[r]
                        b[r] = b[r1]
                        b[r1] = d1

# Function for gauss jordan


def gaussjordan(a, b):
    n = len(a)
    bn = len(b[0])
    for r in range(0, n):
        # Calling the function partial pivot
        partialpivot(a, b)
        pivot = a[r][r]
        for c in range(r, n):
            a[r][c] = a[r][c]/pivot
        for c in range(0, bn):
            b[r][c] = b[r][c]/pivot
        for r1 in range(0, n):
            if r1 == r or a[r1][r] == 0:
                continue
            else:
                factor = a[r1][r]
                for c in range(r, n):
                    a[r1][c] = a[r1][c] - factor*a[r][c]
                for c in range(0, bn):
                    b[r1][c] = b[r1][c] - factor*b[r][c]

# Function for matrix multiplication


def matmulti(a, b):
    p2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    n = len(a)
    for x in range(n):
        for i in range(n):
            for y in range(n):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    print("Matrix product: ")
    for r in p2:
        print(r)


# Now solving question one
with open('Q.1.1.TXT', 'r') as f:
    A1 = [[int(num) for num in line.split()] for line in f]

with open('Q.1.2.TXT', 'r') as f:
    B1 = [[int(num) for num in line.split()] for line in f]
# Calling the function gaussjordan
gaussjordan(A1, B1)
print(" Question one solution: ")
for x in range(0, 3):
    print(B1[x][0])


# Question two solving
with open('Q.2.1.TXT', 'r') as f:
    A2 = [[int(num) for num in line.split()] for line in f]

with open('Q.2.2.TXT', 'r') as f:
    B2 = [[int(num) for num in line.split()] for line in f]
# Calling the function gaussjordan
gaussjordan(A2, B2)
print("Question two solution: ")
for x in range(0, 3):
    print(B2[x][0])


# Question three solving
with open('A.TXT', 'r') as f:
    A3 = [[int(num) for num in line.split()] for line in f]

with open('IDENTITY.TXT', 'r') as f:
    B3 = [[int(num) for num in line.split()] for line in f]

# Calling the function gaussjordan
gaussjordan(A3, B3)
print("Inverse matrix given")
for r in B3:
    print(r)

with open('A.TXT', 'r') as f:
    A4 = [[int(num) for num in line.split()] for line in f]

matmulti(A4, B3)


# OUTPUT
#  Question one solution:
# 3.0
# 1.0
# -2.0
# Question two solution:
# -2.0
# -2.0
# 1.0
# Inverse matrix given
# [-3.0, 3.0, -7.0]
# [1.0, 1.0, 0.0]
# [1.0, 0.0, 1.0]
# Matrix product:
# [1.0, 0.0, 0.0]
# [0.0, 1.0, 0.0]
# [0.0, 0.0, 1.0]
# PS C:\Users\Ravi\Desktop\python12\ASSIGNMENT3>
