print("->   Sometimes a programmer wants to execute a group of statements for a certain amount of times. this can be done using loops")
print("->   Based on this, loops are further classified into following types\n1) for loop\n2) while loop\n3) nested loop")

# for loop
place = 'hyderabad'
for x in place:
    print(x)

# for k in range(1, 20001):
#     print(k, end= ',')
    
for k in range(0, 20000, 1000):
    print(k, end = ',')

for i in range(3, 40, 7):
    print(i)