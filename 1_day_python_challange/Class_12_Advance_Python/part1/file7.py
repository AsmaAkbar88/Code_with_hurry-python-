#enumerate (index pta krna)

lsitt = [3 , 66 , 8 , 35 , 1 , 778 , 7 , 4 , 555]
index = 0
for i in lsitt:
    print(f"The item number at index {index} ,  is {i}")
    index += 1

    # _________________________________________

lsitt = [3 , 66 , 8 , 35 , 1 , 778 , 7 , 4 , 555]
for index , items  in enumerate(lsitt):
    print(f"The item number at index {index} is {items}")


# ____________________________________________________