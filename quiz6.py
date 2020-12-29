def std_weight(height, gender):
    if gender == "남성":
        sta_weight = round(height/100 * height/100 * 22, 2) #소수점 2번째 까지 반올림 round(값, 2)
        return print(f"키 {height}cm {gender}의 표준 체중은 {sta_weight}kg 입니다.")
    elif gender == "여성":
        sta_weight = round(height/100 * height/100 * 21, 2)
        return print(f"키 {height}cm {gender}의 표준 체중은 {sta_weight}kg 입니다.")
    

std_weight(175, "남성")
std_weight(164, "여성")