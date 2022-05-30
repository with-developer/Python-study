import random
import openpyxl

wb = openpyxl.Workbook()

## 함수 선언
# A~F 식당의 메뉴별 count dict를 생성하는 함수
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
## 함수 선언 종료

## 전역변수 초기화
# A~F까지의 식당을 랜덤으로 선택하기 위한 범위 지정
restaurants_range=['A','B','C','D','E','F']

# A~F까지 6개의 식당 메뉴를 튜플로 초기화
open_file = open("/Users/junja/Desktop/python/Restaurant/menu.txt")	
A_restaurant = eval(open_file.readline())
B_restaurant = eval(open_file.readline())
C_restaurant = eval(open_file.readline())
D_restaurant = eval(open_file.readline())
E_restaurant = eval(open_file.readline())
F_restaurant = eval(open_file.readline())
open_file.close()


# 테이블 갯수를 지정
tables_range=30

# 방문객 최솟값, 최댓값 지정
people_range_min=50; people_range_max=500;

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
## 전역변수 초기화 종료

## 메인 코드 시작
people_count=random.randrange(people_range_min,people_range_max+1)
print("1일차 방문객: %d" % people_count)

for i in range(people_count):
    print("%d 번째 손님이 입장했습니다." %(i+1))

    # 식당 정하기
    choice_restaurant=choice_restaurant_func(restaurants_range)
    print("선택한 식당: %s" % choice_restaurant)

    # 메뉴 정하기
    choice_menu=choice_menu_func(choice_restaurant)
    print("선택한 메뉴: %s" % choice_menu)

    # 테이블 정하기
    choice_table=choice_table_func(tables_range)
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
## 메인 코드 종료