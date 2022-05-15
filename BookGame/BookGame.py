# 만약 13 13 10이 나오면 무승부
# 10 10 13이 나오면 13이 승

# A B C
# 10 10 13
# 가장 높은 값이 두개 이상이라면 무승부 그러면 리스트에서 크기순으로 정렬해서 맨앞에껄로 비교하면 될듯?
import random
from unittest import result

from numpy import append

def number_to_list(number,list):
    for i in str(number):
        list.append(i)

def calculation_result(people_list):
    result = int(people_list[0])+int(people_list[1])+int(people_list[2])
    total_list.append(result)
    return result

def test(number):
    result=0
    number_list = list(map(int, str(number)))
    for i in range(len(number_list)):
        result += int(number_list[i])
    print(result)
    

    


pages_number={"a" : random.randrange(100,1000), "b":random.randrange(100,1000), "c":random.randrange(100,1000)}
print("A의 숫자: %d" % pages_number["a"])
print("B의 숫자: %d" % pages_number["b"])
print("C의 숫자: %d" % pages_number["c"])

test(pages_number["a"])




A_people_number=random.randrange(100,1000)
B_people_number=random.randrange(100,1000)
C_people_number=random.randrange(100,1000)
#people_number: 사용자가 뽑은 페이지 (100~999)
A_people_list = []
B_people_list = []
C_people_list = []
#people_list: 사용자가 뽑은 페이지 값을 잘라서 list에 넣음
total_list=[]
#total_list: 세명의 사용자가 뽑은 페이지 합이 들어감

print()
print("A의 숫자: %d" % A_people_number)
print("B의 숫자: %d" % B_people_number)
print("C의 숫자: %d" % C_people_number)

number_to_list(A_people_number,A_people_list)
number_to_list(B_people_number,B_people_list)
number_to_list(C_people_number,C_people_list)

A_people_result=calculation_result(A_people_list)
B_people_result=calculation_result(B_people_list)
C_people_result=calculation_result(C_people_list)

print("A의 합계: %d" % A_people_result)
print("B의 합계: %d" % B_people_result)
print("C의 합계: %d" % C_people_result)
print(total_list)

