#1주차 부터 50주차 까지의 보고서 파일을 만드는 프로그램

for week in range(1,51):
    with open(str(week) + "주차.txt", "w", encoding="utf8") as report:
        report.write("- {0} 주차 주간보고 -".format(week))
        report.write("\n부서 :")
        report.write("\n이름 :")
        report.write("\n업무요약 :")
        