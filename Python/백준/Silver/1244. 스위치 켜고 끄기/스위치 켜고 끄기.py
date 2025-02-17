# N : 스위치 개수
num_of_switches = int(input())

# switches : 스위치 초기 상태
switches = list(map(int, input().split()))

# num_of_students : 학생수
num_of_students = int(input())

for _ in range(num_of_students):
    gender, given_num = map(int, input().split())

    if gender == 1:
        for i in range(given_num-1, num_of_switches, given_num):
            switches[i] = (switches[i] + 1) % 2
    if gender == 2:
        center = given_num - 1
        switches[center] = (switches[center] + 1) % 2
        k = 1
        while center - k >= 0 and center + k < num_of_switches and switches[center - k] == switches[center + k]:
            switches[center - k] = (switches[center - k] + 1) % 2
            switches[center + k] = (switches[center + k] + 1) % 2
            k += 1
            
for i in range(num_of_switches):
    print(switches[i], end=" ")
    if (i + 1) % 20 == 0:
        print()
