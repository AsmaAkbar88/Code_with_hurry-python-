#walrus Operator:--
if (n := len("Asma Akbar") > 5):
    print(f" Length is {n}")
#Output:        Length is True

    # ___________________________________________

if(b := len([2 , 4, 55, 6 , 7]) >3 ):
    print(f"List is too long {b} elements, expected <= 3")  
    
     #Output:  List is too long True elements, expected <= 3

    #  ___________________________________________


from typing import List , Tuple , Dict , Union

number : List[int] = [1 , 44, 6 , 7 , 76]
# print(number)    #Output:    [1, 44, 6, 7, 76]


person : Tuple[str , int]  = ("Asma Akbar" , 60)
# print(person)    #Output:        ('Asma Akbar', 60)

scores: Dict [ str , int] = {"Asma" : 90 , "Akbar" : 80}
# print(scores)    #Output:    {'Asma': 90, 'Akbar': 80}

identifer : Union[ int , str] = "Asma123"
print(identifer)    #output:     Asma123


    #  ___________________________________________
