# fees : [기본 시간, 기본 요금, 단위 시간, 단위 요금]
# records: 시각(HH:MM), 차량번호(길이4인 문자열), 내역(INT or OUT)
# 차량 번호가 작은 자동차부터 청구할 주차요금 차례대로 정수 배열에 담아서 출력
import math

def solution(fees, records):
    answer = []
    default_time, default_fee, each_time, each_fee = fees
    parking={} # 차량의 출입정보 저장
    using_time={} # 차량의 주차장 이용시간 정보를 저장

    for record in records:
        time,number,io = record.split()
        hour,minute = map(int,time.split(':'))
        time = hour*60 + minute
        
        if io == 'IN':
            parking[number]=time
        elif io =="OUT":
            if number in using_time:
                using_time[number] += (time-parking[number])
            else: 
                using_time[number] = time-parking[number]
            del parking[number]
    # 아직 parking에 남아있는 거 = 출차하지 않은 차
    for number, time in parking.items():
        if number in using_time:
            using_time[number]+= 1439-time # 23:59에서 빼주기
        else:
            using_time[number]=1439-time
    for number, time in sorted(using_time.items(), key=lambda x:x[0]):
        answer.append(default_fee + max(0, math.ceil((time-default_time)/each_time))*each_fee)
                          
    return answer