# 코드를 실행하기에 앞서 로직에 필요한 함수들을 정의했습니다.

# 내장된 range 함수에서는 3번째 인자값인 step에 소수점이 입력되지 않기 때문에 
# 소수점을 반영할 수 있는 새로운 range함수를 생성했습니다.
def myrange(start, end, step):
    r = start
    while(r<end):
        yield r
        r += step
# yield 함수는 return 함수와 비슷하지만, 큰 특징이 있습니다.
# yield 함수가 호출되면 값을 반환하고 그 시점에서 함수를 잠시 정지시킵니다.
# 그리고 다음에 yield 함수가 호출되면 이전에 정지된 시점부터 다시 로직을 실행합니다. 

# int 타입의 입력값을 검증하기 위한 함수입니다.
def int_input(msg):
    while True:
        try:
            n = int(input(msg))
            break
        except ValueError:
            print("int 형태의 값을 입력하세요.")
    return n
# try, execpt 는 예외처리 함수라고 불립니다. 
# try의 코드를 실행한 뒤, 에러가 발생하면 except ValueError 코드를 실행합니다.

# float 타입의 입력값을 검증하기 위한 함수입니다.
def float_input(msg):
    while True:
        try:
            n = float(input(msg))
            break
        except ValueError:
            print("float 형태의 값을 입력하세요.")
    return n

# 토끼의 속도가 두 사람의 속도보다 느리다면 토끼가 항상 두 사람보다 뒤에 있기 때문에
# 해당 값이 들어온다면 다시 입력하게 하는 함수입니다.
def rabbit_speed_check(A_person_speed,B_person_speed):
    while True:
        Rabbit_speed = float_input("토끼의 속도를 입력하세요 (단위: m/s): ")
        if Rabbit_speed > A_person_speed and Rabbit_speed > B_person_speed:
            break
        else:
            print("토끼의 속도가 사람의 속도보다 빨라야합니다.")
    return Rabbit_speed
  
# 소수점에 자리에 '0 ~ 4' 이외의 값이 입력된다면 다시 입력하게 하는 함수입니다.
def decimal_point_check():
    while True:
        decimal_point_num = int(input("소수점 몇자리까지 계산하시겠습니까? (입력값: 0 ~ 4): "))
        if decimal_point_num == 0 or decimal_point_num == 1 or decimal_point_num == 2 or decimal_point_num == 3 or decimal_point_num == 4:
            break
        else:
            print("0부터 4 사이의 정수값만 입력 가능합니다.")
    return decimal_point_num

# 토끼의 기진맥진 질문에 'Y/N' 이외의 값이 들어온다면 다시 입력하게 하는 함수입니다.
def rabbit_tired_check():
    while True:
        Rabbit_tired = input("토끼가 터널 길이보다 많이 뛰었을 경우 기진맥진 처리 하시겠습니까? (Y/N): ")
        if Rabbit_tired == 'Y' or Rabbit_tired == 'N':
            break
        else:
            print("'Y' 혹은 'N'값만 입력 가능합니다.")
    return Rabbit_tired   

# 현재 시간을 분과 초로 바꿔주는 함수입니다.
def time_change(time):
    minute = time / 60
    seconds = time % 60
    return minute, seconds
    
# 사람과 토끼가 시간대별로 움직이는 메인 함수입니다.
def main(decimal_point,time):

    # 토끼의 현재 좌표를 초기화합니다.
    Rabbit_coord = 0
    
    print()

    # 계산 전 A, B, 토끼의 시작 위치를 절대값으로 출력합니다.
    print("A의 시작 위치: 0")

    # B는 터널의 오른쪽 끝에서 시작하기 때문에 B의 위치는 Tunnel_distance 값과 동일합니다.
    print("B의 시작 위치: %.4f"% Tunnel_distance)
    print("토끼의 시작 위치: 0")

    # 토끼의 유턴 횟수값을 초기화합니다.
    count = 0

    # 시간 증가 값을 통해 for문을 실행합니다.
    for time in myrange(time,3600,decimal_point):

        # 사람 A와 B가 현재 시간 기준 총 이동한 거리입니다.
        Total_move = (A_person_speed * time) + (B_person_speed * time)

        # 사람 A의 현재 좌표입니다.
        A_person_coord=(A_person_speed * time)

        # 사람 B의 현재 좌표입니다. 
        # 절대값이기 때문에 (터널의 길이 - B가 이동한 거리)를 좌표라고 지정했습니다.
        B_person_coord=(Tunnel_distance-(B_person_speed * time))

        # 토끼의 이동거리 입니다.
        Rabbit_move = (Rabbit_speed * time)

        # 토끼가 이동한 총 거리를 계산한 결과값입니다.
        Rabbit_total_move = (Rabbit_speed * time)

        # 디버깅을 위해 미리 만들어놓은 코드입니다.
        # 주석을 해제하면 시간 단위별로 A, B, 토끼의 위치가 출력됩니다.
        """
        print("------%.4f초 경과------"% time)
        print("A의 위치: %.4f"% A_person_coord)
        print("B의 위치: %.4f"% B_person_coord)
        print("토끼의 위치: %.4f"% Rabbit_coord)
        print("토끼가 이동한 거리: %.4f"% Rabbit_total_move)
        print("A와 B가 이동한 거리: %.4f"% Total_move)
        """

        # 토끼의 기진맥진 값이 Y이면서
        if Rabbit_tired == 'Y':
            
            # 토끼가 이동한 총 거리가 터널의 길이보다 길때
            if Rabbit_total_move > Tunnel_distance:

                # 미리 정의해둔 time_change 함수를 실행시키고
                # 결과값을 minute, seconds 변수에 저장합니다.
                minute, seconds = time_change(time)

                # minute 변수가 1보다 크다면
                if minute >= 1:
                    # 분, 초 형식으로 시간을 출력합니다.
                    print("----- %d분 %.4f초 경과 -----"% (minute, seconds))
                # minute 변수가 1보다 작다면
                else:
                    # 초 형식으로 시간을 출력합니다.
                    print("-------%.4f초 경과-------"% seconds)
                
                # 토끼가 기진맥진 했으므로 결과값을 출력합니다.
                print("토끼가 터널의 길이보다 많이 뛰어서 기진맥진하며 기절했습니다.")
                print("A의 위치: %.4f"% A_person_coord)
                print("B의 위치: %.4f"% B_person_coord)
                print("터널의 길이: %.4f"% Tunnel_distance)
                print("토끼가 뛴 거리: %.4f"% Rabbit_total_move)
                print("토끼가 유턴한 횟수: %d"% count)

                # 프로그램을 종료시킵니다.
                exit()
        
        # 메인 함수의 time값이 0일때 계산을 시작하겠다고 알립니다.
        if time == 0:
            print()
            print("------시작하겠습니다.------")
            print()

        # count값을 2로 나눴을때, 나머지가 0이면 토끼는 오른쪽을 향해 뜁니다.
        elif count % 2 == 0:

            # 토끼의 현재 위치 = 토끼의 원래 위치 + ((토끼의 속도 * (현재시간 + 시간 증가 값)) - 토끼가 이동한 거리)
            Rabbit_coord = Rabbit_coord + ((Rabbit_speed * (time + decimal_point)) - Rabbit_move)

            # 토끼의 위치가 B의 위치보다 크다면 토끼가 유턴하는 if문입니다.
            if Rabbit_coord > B_person_coord:

                # 위의 시간 출력 과정과 동일합니다.
                minute, seconds = time_change(time)
                if minute >= 1:
                    print("----- %d분 %.4f초 경과 -----"% (minute, seconds))
                else:
                    print("-------%.4f초 경과-------"% seconds)

                print("%.4f 위치에서 토끼가 B를 만나 유턴했습니다."% Rabbit_coord)
                print("A의 위치: %.4f"% A_person_coord)
                print("B의 위치: %.4f"% B_person_coord)
                print("A와 B가 이동한 거리: %.4f"% Total_move)
                print("토끼가 이동한 총 거리: %.4f"% Rabbit_total_move)
                print()
                # 토끼가 A를 향해 유턴했기 때문에, count를 1 증가시킵니다.
                count += 1

        # count값을 2로 나눴을때, 나머지가 1이면 토끼는 왼쪽 향해 뜁니다.
        elif count % 2 == 1:

            # 토끼의 현재 위치 = 토끼의 기존 위치 - (( 토끼의 속도 * (현재 시간 + 시간 증가 값)) - 토끼의 이동거리)
            Rabbit_coord = Rabbit_coord - ((Rabbit_speed * (time + decimal_point)) - Rabbit_move)

            # 토끼의 위치가 A의 위치보다 작다면 토끼가 유턴하는 if문입니다.
            if Rabbit_coord < A_person_coord:

                # 토끼의 이동거리 변수를 토끼의 위치값으로 초기화시킵니다.
                Rabbit_move = Rabbit_coord

                # 위의 시간 출력 과정과 동일합니다.
                minute, seconds = time_change(time)
                if minute >= 1:
                    print("----- %d분 %.4f초 경과 -----"% (minute, seconds))
                else:
                    print("-------%.4f초 경과-------"% seconds)

                print("%.4f 위치에서 토끼가 A를 만나 유턴했습니다."% Rabbit_coord)
                print("A의 위치: %.4f"% A_person_coord)
                print("B의 위치: %.4f"% B_person_coord)
                print("A와 B가 이동한 거리: %.4f"% Total_move)
                print("토끼가 이동한 총 거리: %.4f"% Rabbit_total_move)
                print()

                # 토끼가 B를 향해 유턴했기 때문에, count를 1 증가시킵니다.
                count += 1

        # 터널의 총 거리보다 A,B의 총 이동 거리 값이 크다면
        # A와 B가 만났다는 것을 의미합니다. 즉 토끼는 잡혔습니다.
        if Tunnel_distance < Total_move:

            # 위의 시간 출력 과정과 동일합니다.
            minute, seconds = time_change(time)
            if minute >= 1:
                print("A와 B가 %d분 %.4f초 만에 만났습니다."% (minute, seconds))
                print("즉, 토끼는 %d분 %.4f초 만에 잡혔습니다."% (minute, seconds))
            else:
                print("A와 B가 %.4f초 만에 만났습니다."% (seconds))
                print("즉, 토끼는 %.4f초 만에 잡혔습니다."% (seconds))

            print("토끼는 유턴을 %d번 했습니다"% count)
            print("토끼가 이동한 총 거리: %.4f"% Rabbit_total_move)
            print("터널의 총 거리: %.4f"% Tunnel_distance)

            # for문에서 탈출합니다.
            break
# 함수 선언 부분이 끝났습니다.
# 아래부터 코드가 실행됩니다.


# 사람과 토끼의 위치 변수, 시간 변수를 초기화시킵니다.
A_person_coord = 0
B_person_coord = 0
Rabbit_move = 0
Rabbit_total_move = 0
time = 0

# 계산에 필요한 입력값을 받고, 해당 값을 검증합니다.
Tunnel_distance = float_input("터널 길이를 입력하세요. (단위: m): ")
A_person_speed  = float_input("사람 A의 속도를 입력하세요 (단위: m/s:): ")
B_person_speed = float_input("사람 B의 속도를 입력하세요 (단위: m/s:): ")
Rabbit_speed = rabbit_speed_check(A_person_speed,B_person_speed)
decimal_point_num = decimal_point_check()
Rabbit_tired = rabbit_tired_check()

# 입력값에서 검증받은 값을 통해 시간 변수의 증감값을 초기화시킵니다.
# 소수점 0자리를 원하면 시간 증감값은 1입니다. (1초씩 증가)
if (decimal_point_num == 0):
    decimal_point = 1

# 소수점 1자리를 원하면 시간 증감값은 0.1입니다. (0.1초씩 증가)
elif(decimal_point_num == 1 ):
    decimal_point = 0.1

elif(decimal_point_num == 2 ):
    decimal_point = 0.01

elif(decimal_point_num == 3):
    decimal_point = 0.001

elif(decimal_point_num == 4):
    decimal_point = 0.0001

# 계산 로직을 실행하는 메인 함수를 실행합니다.
main(decimal_point,time)