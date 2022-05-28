from secrets import choice
from tkinter import E
import random

def menu_count_setup(restaurant,menu):
    for i in range(len(restaurant)):
        menu[restaurant[i][0]] = 0
    return

def choice_menu(choice_restaurant,menu_count):
    menu = random.sample(choice_restaurant,1)[0][0]
    menu_count[menu] += 1
    return menu

# A~F까지 6개의 식당 메뉴를 튜플로 초기화
A_restaurant=(("김치찌개", 5000),("된장찌개",4000),("부대찌개",4500),("제육볶음",5500),("비빔밥", 6000),("갈비탕",8000),("닭볶음탕",7000))
B_restaurant=(("짜장면", 5800),("짬뽕",5900),("탕수육",9000),("볶음밥",5500),("군만두",3000))
C_restaurant=(("돈까스",7300),("치즈돈까스",8300),("새우튀김",2350),("우동",3800))
D_restaurant=(("양념치킨",6000),("후라이드치킨",5900),("간장치킨",6050),("파닭",6200),("닭껍질튀김",3120),("어니언치킨",6700),("마늘치킨",7000),("수원왕갈비치킨",9999),("소주",3000),("맥주",3500))
E_restaurant=(("스팸마요",3600),("스팸김치볶음밥",4600),("치킨마요",3200),("돈치마요",3600),("돈까스카레",4300))
F_restaurant=(("순대국밥",6200),("소머리국밥",7400),("돼지국밥",6500),("콩나물국밥",4500),("설렁탕",5000),("육개장",5600),("뼈해장국",6000),("추어탕",6200))



# 식당 이용 횟수(restaurants dict) 6개 생성, 값은 0으로 초기화.
restaurants_count={"A_restaurant":0, "B_restaurant":0, "C_restaurant":0, "D_restaurant":0, "E_restaurant":0, "F_restaurant":0 }

# 메뉴 선택 횟수(menu_count dict) 6개 생성, 각 메뉴별 선택 횟수는 0으로 초기화.
A_menu_count={}
menu_count_setup(A_restaurant,A_menu_count)
B_menu_count={}
menu_count_setup(B_restaurant,B_menu_count)
C_menu_count={}
menu_count_setup(C_restaurant,C_menu_count)
D_menu_count={}
menu_count_setup(D_restaurant,D_menu_count)
E_menu_count={}
menu_count_setup(E_restaurant,E_menu_count)
F_menu_count={}
menu_count_setup(F_restaurant,F_menu_count)

# 테이블 사용 횟수(tables List) 30개 생성, 값은 0으로 초기화.
tables_count=[0 for i in range(30)]


people_count=random.randrange(50,501)
print("1일차 방문객: %d" % people_count)

for i in range(people_count):
    
    # A~F 식당중 하나를 선택해야하기 때문에 range값을 아래와 같이 부여함.
    range=['A_restaurant','B_restaurant','C_restaurant','D_restaurant','E_restaurant','F_restaurant']
    choice_restaurant=random.sample(range,1)[0]
    restaurants_count[choice_restaurant] +=1

    print("선택한 식당: %s" % choice_restaurant)


    #메뉴 정하기
    if(choice_restaurant=="A_restaurant"):
        choice_menu=choice_menu(A_restaurant,A_menu_count)
    elif(choice_restaurant=="B_restaurant"):
        choice_menu=choice_menu(B_restaurant,B_menu_count)
    elif(choice_restaurant=="C_restaurant"):
        choice_menu=choice_menu(C_restaurant,C_menu_count)
    elif(choice_restaurant=="D_restaurant"):
        choice_menu=choice_menu(D_restaurant,D_menu_count)
    elif(choice_restaurant=="E_restaurant"):
        choice_menu=choice_menu(E_restaurant,E_menu_count)
    elif(choice_restaurant=="F_restaurant"):
        choice_menu=choice_menu(F_restaurant,F_menu_count)

    print("선택한 메뉴: %s" % choice_menu)


    # 테이블 정하기
    choice_table=random.randrange(30)
    tables_count[choice_table]+=1



print(restaurants_count)
print(A_menu_count)
print(B_menu_count)
print(C_menu_count)
print(D_menu_count)
print(E_menu_count)
print(F_menu_count)
print(tables_count)
