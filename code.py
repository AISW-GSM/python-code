class DataCollector:
    def __init__(self):
        self.average = 50 

    def get_average(self):
        return self.average

class Analyzer:
    def calculate_difference(self, value, average):
        return abs(value - average)

class AnomalyDetector:
    def __init__(self, limit):
        self.limit = limit

    def check(self, difference):
        if difference > self.limit:
            return "이상 데이터 발견"
        else:
            return "정상 데이터"

class Report:
    def show_result(self, value, difference, result):
        print("----------------------")
        print("현재 CPU 사용률 :", value)
        print("평균과 차이 :", difference)
        print("분석 결과 :", result)

        # 이상 데이터 발생 시 대응
        if result == "이상 데이터 발견":
            print("서버 과부하 경고")
            print("관리자 확인 필요")

            if value >= 100:
                print("위험 단계 : 매우 높음")
            else:
                print("위험 단계 : 주의")

        print("----------------------")


collector = DataCollector()
analyzer = Analyzer()

detector = AnomalyDetector(20)

report = Report()

average = collector.get_average()

print("정상 데이터 평균 :", average)
print("----------------------")

while True:

    current_cpu = int(input("현재 CPU 사용률 입력 (-1 입력 시 종료) : "))

    if current_cpu == -1:
        print("프로그램 종료")
        break


    difference = analyzer.calculate_difference(
        current_cpu,
        average
    )


    result = detector.check(difference)


    report.show_result(
        current_cpu,
        difference,
        result
    )