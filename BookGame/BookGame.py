import random

def page_calculation_result(number):
    result=0
    number_list = list(map(int, str(number)))
    for i in range(len(number_list)):
        result += int(number_list[i])
    return result
    
def game_calculation_result(user):
    game_result[user] += 1

def game(i,user):
    pages_number={}
    page_result={}

    for j in range(len(user)):
        pages_number[user[j]] = random.randrange(100,1000)
        page_result[user[j]] = page_calculation_result(pages_number[user[j]])
        max_key_page=[k for k,v in page_result.items() if max(page_result.values()) == v]

    if ( len(max_key_page) > 1 ):
        winner="무승부"
    else:
        winner=max_key_page[0]
        game_calculation_result(winner)
    if ( len(user)==3):
        print("%d번째 승자는 %s (A: %d -> %d, B: %d -> %d, C: %d -> %d){현재스코어 : %d : %d : %d}" % (i,winner, pages_number["A"],page_result["A"],pages_number["B"],page_result["B"],pages_number["C"],page_result["C"],game_result["A"],game_result["B"],game_result["C"]))
    else:
        print("%d번째 승자는 %s (%s: %d -> %d, %s: %d -> %d){현재스코어 : %d : %d}" % (i,winner,user[0],pages_number[user[0]],page_result[user[0]],user[1],pages_number[user[1]],page_result[user[1]],game_result[user[0]],game_result[user[1]]))

game_result={"A":0,"B":0,"C":0}

for i in range(1,11):
    game(i,['A','B','C'])

max_key_score=[k for k,v in game_result.items() if max(game_result.values()) == v]

while (len(max_key_score) > 1):
    
    for j in range(len(max_key_score)):
        if(j+1==len(max_key_score)):
            print(max_key_score[j], end='')
        else:
            print(max_key_score[j], end='와')
    print("가 각각 %d회로 동률로 게임을 계속합니다!" %(game_result[max_key_score[j]]))
    i+=1
    game(i,max_key_score)
    max_key_score=[k for k,v in game_result.items() if max(game_result.values()) == v]

print("최종 승자는 %s가 %d회 승리하여 우승!" %(max_key_score[0],game_result[max_key_score[0]]))