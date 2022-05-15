from curses import keyname
import random

def calculation_result(number):
    result=0
    number_list = list(map(int, str(number)))
    for i in range(len(number_list)):
        result += int(number_list[i])
    return result
    
pages_number={"a" : random.randrange(100,1000), "b":random.randrange(100,1000), "c":random.randrange(100,1000)}
print("A의 페이지: %d" % pages_number["a"])
print("B의 페이지: %d" % pages_number["b"])
print("C의 페이지: %d" % pages_number["c"])

page_result={"a":calculation_result(pages_number["a"]), "b":calculation_result(pages_number["b"]),"c":calculation_result(pages_number["c"])}
print(page_result)

game_result={"a":0,"b":0,"c":0}

max_key=[k for k,v in page_result.items() if max(page_result.values()) == v]

if ( len(max_key) > 1 ):
    print("무승부")
else:
    print(max_key)

