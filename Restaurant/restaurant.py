from secrets import choice
from threading import local
from tkinter import E
import random

def menu_count_setup(restaurant,menu):
    for i in range(len(restaurant)):
        menu[restaurant[i][0]] = 0
    return

def menu_count_setup2(restaurant_range):
    for i in range(restaurant_range):
        print(i)
    return

def choice_restaurant_func(restaurant_range):
    choice_restaurant=random.sample(restaurant_range,1)[0]
    choice_restaurant+="_restaurant"
    restaurants_count[choice_restaurant] +=1
    return choice_restaurant

def choice_menu_func(choice_restaurant):
    menu_count=choice_restaurant[0:1]+"_menu_count"
    choice_menu = random.sample(eval(choice_restaurant),1)[0][0] # 식당에서 메뉴를 랜덤으로 선택
    eval(menu_count)[choice_menu] += 1 # A~F_menu_count 변수에서 선택된 메뉴의 값 증가
    return choice_menu

def choice_table_func(table_range):
    choice_table=random.randrange(table_range)
    tables_count[choice_table]+=1
    return choice_table

#전역변수 초기화
# A~F까지 6개의 식당 메뉴를 튜플로 초기화
A_restaurant=(("김치찌개", 5000),("된장찌개",4000),("부대찌개",4500),("제육볶음",5500),("비빔밥", 6000),("갈비탕",8000),("닭볶음탕",7000),("테스트",1111))
B_restaurant=(("짜장면", 5800),("짬뽕",5900),("탕수육",9000),("볶음밥",5500),("군만두",3000))
C_restaurant=(("돈까스",7300),("치즈돈까스",8300),("새우튀김",2350),("우동",3800))
D_restaurant=(("양념치킨",6000),("후라이드치킨",5900),("간장치킨",6050),("파닭",6200),("닭껍질튀김",3120),("어니언치킨",6700),("마늘치킨",7000),("수원왕갈비치킨",9999),("소주",3000),("맥주",3500))
E_restaurant=(("스팸마요",3600),("스팸김치볶음밥",4600),("치킨마요",3200),("돈치마요",3600),("돈까스카레",4300))
F_restaurant=(("순대국밥",6200),("소머리국밥",7400),("돼지국밥",6500),("콩나물국밥",4500),("설렁탕",5000),("육개장",5600),("뼈해장국",6000),("추어탕",6200))

# 식당 이용 횟수(restaurants dict) 6개 생성, 값은 0으로 초기화.
restaurants_count={"A_restaurant":0, "B_restaurant":0, "C_restaurant":0, "D_restaurant":0, "E_restaurant":0, "F_restaurant":0 }

# A~F까지의 식당을 랜덤으로 선택하기 위한 범위 지정.
restaurant_range=['A','B','C','D','E','F']

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

menu_count_setup2(restaurant_range)

# 테이블 사용 횟수(tables List) 30개 생성, 값은 0으로 초기화.
tables_count=[0 for i in range(30)]


people_count=random.randrange(50,501)
print("1일차 방문객: %d" % people_count)

for i in range(people_count):
    print("%d 번째 손님이 입장했습니다." %(i+1))

    # 식당 정하기
    choice_restaurant=choice_restaurant_func(restaurant_range)
    print("선택한 식당: %s" % choice_restaurant)

    # 메뉴 정하기
    choice_menu=choice_menu_func(choice_restaurant)
    print("선택한 메뉴: %s" % choice_menu)

    # 테이블 정하기
    choice_table=choice_table_func(30)
    print("선택한 테이블 %d" % choice_table)

    print()


print("식당별 주문 횟수 %s" % restaurants_count)
print("A식당 메뉴별 주문 횟수 %s" % A_menu_count)
print("B식당 메뉴별 주문 횟수 %s" % B_menu_count)
print("C식당 메뉴별 주문 횟수 %s" % C_menu_count)
print("D식당 메뉴별 주문 횟수 %s" % D_menu_count)
print("E식당 메뉴별 주문 횟수 %s" % E_menu_count)
print("F식당 메뉴별 주문 횟수 %s" % F_menu_count)
print("테이블별 사용 횟수 %s" % tables_count)
print(sum(tables_count))