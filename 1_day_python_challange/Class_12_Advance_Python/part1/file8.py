my_list = [ 0 ,5, 34, 56, 22, 47 ]
squ = []

for i in my_list:
    squ.append(i * i)

print(squ)    #Output:   [0, 25, 1156, 3136, 484, 2209]

# _______________________________________________

my_list = [ 0 ,5, 34, 56, 22, 47 ]
result = [i*i for i  in my_list]
print(result)   #Ooutput:       [0, 25, 1156, 3136, 484, 2209]