import random
from func_test import *


## 메인 코드 시작
for day in range(month):

    people_count=random.randrange(people_range_min,people_range_max+1)
    print("%d일차 방문객: %d" % (day+1,people_count))

    for i in range(people_count):
        # print("%d 번째 손님이 입장했습니다." %(i+1))

        # 식당 정하기
        choice_restaurant=choice_restaurant_func(restaurants_range)
        # print("선택한 식당: %s" % choice_restaurant)

        # 메뉴 정하기
        choice_menu=choice_menu_func(choice_restaurant)
        # print("선택한 메뉴: %s" % choice_menu)

        # 테이블 정하기
        choice_table=choice_table_func(tables_range)
        # print("선택한 테이블 %d" % choice_table)

        # print()


restaurants_count['A_restaurant']=2000
restaurants_count['B_restaurant']=2000
test123={**A_menu_count,**B_menu_count,**C_menu_count,**D_menu_count,**E_menu_count,**F_menu_count}

print("식당별 주문 횟수 %s" % restaurants_count)
print("A식당 메뉴별 주문 횟수 %s" % A_menu_count)
print("B식당 메뉴별 주문 횟수 %s" % B_menu_count)
print("C식당 메뉴별 주문 횟수 %s" % C_menu_count)
print("D식당 메뉴별 주문 횟수 %s" % D_menu_count)
print("E식당 메뉴별 주문 횟수 %s" % E_menu_count)
print("F식당 메뉴별 주문 횟수 %s" % F_menu_count)
print("테이블별 사용 횟수 %s" % tables_count)
print(sum(tables_count))


max_sales_restaurant=[k for k,v in restaurants_count.items() if max(restaurants_count.values()) == v]
max_sales_menu=[k for k,v in test123.items() if max(test123.values()) == v]
# max_sit_table=[k for k,v in tables_count.items() if max(tables_count.values()) == v]
print("가장 많은 매출을 실적을 올린 식당: %s"% max_sales_restaurant)
print("가장 많이 팔린 메뉴: %s" % max_sales_menu)
# print("손님들이 가장 많이 이용한 테이블 번호: %d" %max_sit_table)

## 메인 코드 종료