def choice_funct_num(max_num):
    while True:
        funct_num = int(input(">> 번호: "))
        if funct_num >= 1 and funct_num <= max_num:
            break
        else:
            print(f"경고: 1~{max_num} 사이의 값만 입력해주세요.")
    return funct_num
