import csv

class Heap:
    def __init__(self):
        self.__A = []

    def insert(self, x):
        self.__A.append(x)
        self.__percolateUp(len(self.__A) - 1)

    def __percolateUp(self, i):
        if i > 0:
            parent = (i - 1) // 2
            if self.__A[i] > self.__A[parent]:
                self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
                self.__percolateUp(parent)

    def deleteMax(self):
        if not self.__A:
            return None

        max_val = self.__A[0]
        last = self.__A.pop()

        if self.__A:
            self.__A[0] = last
            self.__percolateDown(0)

        return max_val

    def __percolateDown(self, i):
        child = 2 * i + 1
        right = 2 * i + 2

        if child < len(self.__A):
            if right < len(self.__A) and self.__A[child] < self.__A[right]:
                child = right

            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)

    def isEmpty(self):
        return len(self.__A) == 0


h = Heap()

with open("birthday.csv", "r", encoding="utf-8-sig") as f:
    reader = csv.reader(f)
    next(reader)  # 헤더 건너뛰기

    for row in reader:
        if len(row) < 4:
            continue

        name = row[0].strip()
        year = row[1].strip()
        month = row[2].strip()
        day = row[3].strip()

        # 빈 값 있는 행은 건너뛰기
        if year == "" or month == "" or day == "":
            continue

        h.insert((int(year), int(month), int(day), name))

print("생일이 늦은 순서 10명")
print("----------------------")

for i in range(10):
    person = h.deleteMax()
    if person is None:
        break

    year, month, day, name = person
    print(f"{i+1}. {name} - {year}년 {month}월 {day}일")