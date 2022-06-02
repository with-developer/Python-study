import random


## 상수값 지정
# 한 달은 30일로 지정
month=30

# 식당의 메뉴 갯수 최솟값, 최댓값 지정
menu_count_range_min=4; menu_count_range_max=10

# 메뉴 가격의 최솟값, 최댓값 지정
menu_price_range_min=1000; menu_price_range_max=9999

# 테이블 갯수를 지정
tables_range=30

# 방문객 최솟값, 최댓값 지정
people_range_min=50; people_range_max=500;

#menu.txt 파일 절대 경로값 지정
path="/Users/junja/Desktop/python/Restaurant/menu.txt"
## 상수값 지정 종료


## 함수 선언
# A~F식당의 메뉴 갯수와 가격을 랜덤하게 생성하는 함수
def make_menu(restaurant_name):	
    for i in range(random.randrange(menu_count_range_min,menu_count_range_max+1)):
        menu = tuple((restaurant_name+"_menu_"+str(i+1),random.randrange(menu_price_range_min,menu_price_range_max+1)) for i in range(i+1))
    open_file.write(restaurant_name+"_restaurant: "+str(menu)+"\n") # 생성된 식당의 메뉴와 가격을 menu.txt에 저장
    return menu

# A~F 식당의 메뉴별 Count dict를 생성하는 함수
def menu_count_setup(restaurant,menu):
    for i in range(len(restaurant)):
        menu[restaurant[i][0]] = 0
    return

# A~F 식당 중 하나를 랜덤으로 선택하는 함수
def choice_restaurant_func(restaurants_range):
    choice_restaurant=random.sample(restaurants_range,1)[0]
    choice_restaurant+="_restaurant"
    restaurants_count[choice_restaurant] +=1
    return choice_restaurant

# 식당에서 메뉴를 랜덤으로 선택하는 함수
def choice_menu_func(choice_restaurant):
    menu_count=choice_restaurant[0:1]+"_menu_count"
    choice_menu = random.sample(eval(choice_restaurant),1)[0][0]
    eval(menu_count)[choice_menu] += 1
    return choice_menu

# 테이블을 랜덤으로 선택하는 함수
def choice_table_func(table_range):
    choice_table=random.randrange(table_range)
    tables_count[choice_table]+=1
    return choice_table

# 식당별 수익을 도출하는 함수
def restaurants_revenue_func(restaurants_range):
    for name in restaurants_range:
        restaurant=name[0:1]+"_restaurant"
        menu_count=name[0:1]+"_menu_count"
        for i in range(len(eval(menu_count))):
            menu=name+"_menu_"+str(i+1)
            restaurants_revenue[restaurant] += eval(menu_count)[menu]*eval(restaurant)[i][1]
    return
## 함수 선언 종료


## 전역변수 초기화
# A~F까지의 식당을 랜덤으로 선택하기 위한 범위 지정
restaurants_range=['A','B','C','D','E','F']

# A~F까지 6개의 식당 메뉴를 튜플로 초기화
open_file = open(path, "w")	
A_restaurant=make_menu("A")
B_restaurant=make_menu("B")
C_restaurant=make_menu("C")
D_restaurant=make_menu("D")
E_restaurant=make_menu("E")
F_restaurant=make_menu("F")
open_file.close()

# 식당 이용 횟수(restaurants dict) 6개 생성, 값은 0으로 초기화.
restaurants_count={"A_restaurant":0, "B_restaurant":0, "C_restaurant":0, "D_restaurant":0, "E_restaurant":0, "F_restaurant":0 }

# 메뉴 선택 횟수(menu_count dict) 6개 생성, 각 메뉴별 선택 횟수는 0으로 초기화.
A_menu_count={}; B_menu_count={}; C_menu_count={}; D_menu_count={}; E_menu_count={}; F_menu_count={}
for i in (restaurants_range):
    restaurant=i+"_restaurant"
    menu_count=i+"_menu_count"
    menu_count_setup(eval(restaurant),eval(menu_count))

# 테이블 사용 횟수(tables List) 30개 생성, 값은 0으로 초기화.
tables_count=[0 for i in range(tables_range)]

# 매출액 계산
restaurants_revenue={"A_restaurant":0, "B_restaurant":0, "C_restaurant":0, "D_restaurant":0, "E_restaurant":0, "F_restaurant":0 }

## 전역변수 초기화 종료