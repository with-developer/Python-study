import random

open_file = open("/Users/junja/Desktop/python/Restaurant/menu.txt", "r+")	
restaurants_range=['A','B','C','D','E','F']

A_restaurant=()
for rest in restaurants_range:
    rest_name=rest+"_restaurant"
    print(rest_name)
    for i in range(random.randrange(4,11)):
        a = tuple((rest+"_menu_"+str(i+1),random.randrange(1000,10000)) for i in range(i))
    print(a)
    open_file.write(str(a)+"\n")

# A_restaurant = ()



# for num in range(random.randrange(4,11)):
#     A_restaurant[0] = 0
#     print(A_restaurant)
#     menu = (("메뉴1", 1000), ("메뉴2", 2000))
