from module import *

## 메인 코드 시작
for day in range(month):

    people_count=random.randrange(people_range_min,people_range_max+1)
    ## 일일별 방문객 정보 출력용 디버깅 코드
    # print("%d일차 방문객: %d" % (day+1,people_count))
    ## 일일별 방문객 정보 출력용 디버깅 코드 종료

    for i in range(people_count):
        
        choice_restaurant=choice_restaurant_func(restaurants_range) # 식당 선택
        
        choice_menu=choice_menu_func(choice_restaurant) # 메뉴 선택
        
        choice_table=choice_table_func(tables_range) # 테이블 선택

        ## 일일별 주문 정보 출력용 디버깅 코드
        # print("%d 번째 손님이 입장했습니다." %(i+1))
        # print("선택한 식당: %s" % choice_restaurant)
        # print("선택한 메뉴: %s" % choice_menu)
        # print("선택한 테이블 %d" % choice_table)
        # print()
        ## 일일별 주문 정보 출력용 디버깅 코드 종료

# 식당별 매출 계산
restaurants_revenue_func(restaurants_range)

## 결과 정보 출력용 디버깅 코드
# print("식당별 주문 횟수 %s" % restaurants_count)
# print("식당별 매출: %s"% restaurants_revenue)
# print("A식당 메뉴별 주문 횟수 %s" % A_menu_count)
# print("B식당 메뉴별 주문 횟수 %s" % B_menu_count)
# print("C식당 메뉴별 주문 횟수 %s" % C_menu_count)
# print("D식당 메뉴별 주문 횟수 %s" % D_menu_count)
# print("E식당 메뉴별 주문 횟수 %s" % E_menu_count)
# print("F식당 메뉴별 주문 횟수 %s" % F_menu_count)
# print("테이블별 사용 횟수 %s" % tables_count)
## 결과 정보 출력용 디버깅 코드 종료


# 메뉴별 판매 개수를 하나의 Dict에 입력
menu_count_total={**A_menu_count,**B_menu_count,**C_menu_count,**D_menu_count,**E_menu_count,**F_menu_count}
# 가장 많은 매출을 올린 식당 (최댓값이 여러개라도 모두 출력)
high_revenue_restaurant=[k for k,v in restaurants_revenue.items() if max(restaurants_revenue.values()) == v]
# 가장 많이 팔린 식당 (최댓값이 여러개라도 모두 출력)
max_sales_restaurant=[k for k,v in restaurants_count.items() if max(restaurants_count.values()) == v]
# 가장 많이 팔린 메뉴 (최댓값이 여러개라도 모두 출력)
max_sales_menu=[k for k,v in menu_count_total.items() if max(menu_count_total.values()) == v]
# 가장 많이 이용한 테이블 (최댓값이 여러개라도 모두 출력)
max_seating_table=[str(i) for i,v in enumerate(tables_count) if v == max(tables_count)]

print("한달 내 가장 많은 매출을 실적을 올린 식당: %s (%s 원)"% (", ".join(high_revenue_restaurant),format(restaurants_revenue[high_revenue_restaurant[0]], ',')))
print("한달 내 가장 많이 팔린 식당: %s (%d개)" % (", ".join(max_sales_restaurant),restaurants_count[max_sales_restaurant[0]]))
print("한달 내 가장 많이 팔린 메뉴: %s (%d개)" % (", ".join(max_sales_menu),menu_count_total[max_sales_menu[0]]))
print("손님들이 가장 많이 이용한 테이블 번호: %s번 (%d회)" %(", ".join(max_seating_table),(max(tables_count))))
## 메인 코드 종료