# [Bronze II] 거스름돈 - 5585 

[문제 링크](https://www.acmicpc.net/problem/5585) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

그리디 알고리즘

### 제출 일자

2025년 2월 8일 13:54:22

### 문제 설명

<p>타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>입력은 한줄로 이루어져있고, 타로가 지불할 돈(1 이상 1000미만의 정수) 1개가 쓰여져있다.</p>

### 출력 

 <p>제출할 출력 파일은 1행으로만 되어 있다. 잔돈에 포함된 매수를 출력하시오.</p>

### 회고

 <p>문제를 해결할 때 비교 연산자의 선택이 적절한지 재검토하는 습관을 가져야겠다.
초기에 거스름돈 금액과 잔돈 리스트의 원소를 비교할 때, 나는 “현재 거스름돈 금액이 잔돈 리스트의 원소보다 크다면” 몫을 구하고, 나머지를 현재 거스름돈 금액으로 갱신하는 방식으로 구현했다.</p>

 <p>그러나 단순히 “크다면(>)“으로 비교할 경우, 입력 값이 999일 때 거스름돈 금액이 1이 되고, 이후 잔돈 리스트의 마지막 원소인 1과 비교할 때 **“크거나 같다(≥)”**가 아니라면 몫을 구하지 않게 된다. 이처럼 연산자를 사용하기 전에 내가 구현하려는 로직을 충분히 검토하고, 적절한 비교 연산자를 선택하는 것이 엣지 케이스에서 발생할 수 있는 오류를 줄이는 데 도움이 될 것이다.</p>

### Retrospective

 <p>I should make it a habit to re-evaluate whether I have chosen the appropriate comparison operator when solving problems.</p>

 <p>Initially, when comparing the amount of change with the elements in the coin list, I implemented it in a way where if the current amount of change is greater than a coin value, I calculate the quotient and update the remaining amount.</p>

 <p>However, if I use only the “greater than (>)” operator, an issue arises. For example, if the input value is 999, the remaining change eventually becomes 1. At this point, when comparing it with the last element of the coin list (which is 1), the condition fails because it checks for “greater than (>)” instead of “greater than or equal to (≥),” preventing the quotient from being calculated.</p>

 <p>This experience has taught me that before using a comparison operator, I should carefully consider the logic I want to implement. Choosing the right operator can help prevent mistakes, especially in edge cases.</p>
