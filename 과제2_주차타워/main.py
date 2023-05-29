# Python 프로그래밍 언어를 사용해서 다음 조건에 맞는 코드를 작성하고 제출하세요.
# 제출은 파일로 제출해주세요. 파일명은 "컴과사_과제2_학번" 으로 제출해주세요.
#  - 파일명 예: 컴과사_과제2_207512

from 주차타워2 import choice_funct_num

print("■" * 50)
print("■■ == 주차타워(ver 1.1) ==")
print("■■ CNU 주차타워에 방문해주셔서 감사합니다.")
print("■" * 50)

parking_lot = []

while True:
    print("■" * 50)
    print("■ 메인 기능")
    print("□ 1.차량입고")
    print("□ 2.차량출고")
    print("□ 3.차량입고정보")
    print("□ 4.프로그램 종료")
    print("■" * 50)

    funct_num = choice_funct_num(4)

    if funct_num == 1:
        if len(parking_lot) ==5:
            print("더 이상 차량을 입고할 수 없습니다.")
            print(f"최대: 5대, 현재: {len(parking_lot)}대")
        else:
            car_number = input("입고할 차량 번호를 입력하세요(4자리 정수): ")
            if len(car_number) == 4:
                parking_lot.append(car_number)
                print("차량이 입고되었습니다.")
            else:
                print("잘못된 차량 번호 형식입니다.")

    elif funct_num == 2:
        car_number = input("출고할 차량 번호를 입력하세요(4자리 정수): ")
        if len(car_number) == 4:
            if car_number in parking_lot:
                parking_lot.remove(car_number)
                print("차량이 출고되었습니다.")
            else:
                print("차량이 존재하지 않습니다.")
        else:
            print("잘못된 차량 번호 형식입니다.")

    elif funct_num == 3:
        print("현재 차량 입고 정보:")
        for i, car_number in enumerate(parking_lot):
            print(f"{i + 1}층: {car_number}")

    elif funct_num == 4:
        print("■" * 50)
        print("■■ 프로그램을 종료합니다.")
        print("■" * 50)
        exit()
