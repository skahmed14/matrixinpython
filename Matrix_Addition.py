m=int(input("Enter no of rows : "))
n=int(input("Enter no of columns : "))

col = m
row = n

matrix_1=[[0 for x in range(col)] for y in range(row)]

matrix_2=[[0 for x in range(col)] for y in range(row)]

result_matrix=[[0 for x in range(col)] for y in range(row)]

for i in range(row):
    for j in range(col):
        user_input1=int(input("Enter the value for first Matrix[" + str(i)+"]"+"["+str(j) + "] : " ))
        matrix_1[i][j]=user_input1




for i in range(row):
    for j in range(col):
        user_input2=int(input("Enter the value for second Matrix[" + str(i)+"]"+"["+str(j) + "] : "))
        matrix_2[i][j]=user_input2



for i in range(row):
    for j in range(col):
        result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]

print("The sum of the two matrices is",result_matrix)





