class DataCollector:
    def __init__(self):
        self.data = []

    def add_data(self, value):
        self.data.append(value)

    def get_average(self):
        if len(self.data) == 0:
            return 0
        return sum(self.data) / len(self.data)

    def get_max(self):
        if len(self.data) == 0:
            return 0
        return max(self.data)

    def get_min(self):
        if len(self.data) == 0:
            return 0
        return min(self.data)


class Analyzer:
    def calculate_difference(self, value, average):
        return abs(value - average)


class AnomalyDetector:
    def __init__(self, limit):
        self.limit = limit

    def check(self, difference):
        if difference > self.limit:
            return "이상 데이터 발견"
        return "정상 데이터"

    def get_risk_level(self, difference):
        if difference >= 50:
            return "심각"
        elif difference >= 30:
            return "경고"
        elif difference >= 20:
            return "주의"
        else:
            return "정상"


class Report:
    def show_result(self, value, average, difference, result, risk):
        print("\n----------------------")
        print("현재 CPU 사용률 :", value)
        print("현재 평균 :", round(average, 2))
        print("평균과 차이 :", round(difference, 2))
        print("분석 결과 :", result)
        print("위험도 :", risk)

        if result == "이상 데이터 발견":
            print("관리자 확인 필요")

        print("----------------------")

    def show_summary(
        self,
        total,
        normal_count,
        anomaly_count,
        average,
        maximum,
        minimum
    ):
        print("\n===== 최종 분석 결과 =====")
        print("총 데이터 수 :", total)
        print("정상 데이터 :", normal_count)
        print("이상 데이터 :", anomaly_count)

        if total > 0:
            rate = anomaly_count / total * 100
            print("이상 발생률 :", round(rate, 2), "%")

        print("평균 CPU 사용률 :", round(average, 2))
        print("최고 CPU 사용률 :", maximum)
        print("최저 CPU 사용률 :", minimum)
        print("========================")


collector = DataCollector()
analyzer = Analyzer()
detector = AnomalyDetector(20)
report = Report()

normal_count = 0
anomaly_count = 0

while True:

    current_cpu = int(input("현재 CPU 사용률 입력 (-1 입력 시 종료) : "))

    if current_cpu == -1:
        break

    collector.add_data(current_cpu)

    average = collector.get_average()

    difference = analyzer.calculate_difference(
        current_cpu,
        average
    )

    result = detector.check(difference)

    risk = detector.get_risk_level(
        difference
    )

    if result == "정상 데이터":
        normal_count += 1
    else:
        anomaly_count += 1

    report.show_result(
        current_cpu,
        average,
        difference,
        result,
        risk
    )

print("\n프로그램 종료")

report.show_summary(
    len(collector.data),
    normal_count,
    anomaly_count,
    collector.get_average(),
    collector.get_max(),
    collector.get_min()
)