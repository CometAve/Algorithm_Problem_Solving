# [Silver II] 마인크래프트 - 18111 

[문제 링크](https://www.acmicpc.net/problem/18111) 

### 성능 요약

메모리: 32412 KB, 시간: 132 ms

### 분류

브루트포스 알고리즘, 구현

### 제출 일자

2025년 2월 21일 17:11:26

### 문제 설명

<p>팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 ‘마인크래프트’를 켰다. 마인크래프트는 1 × 1 × 1(세로, 가로, 높이) 크기의 블록들로 이루어진 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.</p>

<p>목재를 충분히 모은 lvalue는 집을 짓기로 하였다. 하지만 고르지 않은 땅에는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는 ‘땅 고르기’ 작업을 해야 한다.</p>

<p>lvalue는 세로 <em>N</em>, 가로 <em>M</em> 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.</p>

<ol>
	<li>좌표 (<em>i</em>, <em>j</em>)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.</li>
	<li>인벤토리에서 블록 하나를 꺼내어 좌표 (<em>i</em>, <em>j</em>)의 가장 위에 있는 블록 위에 놓는다.</li>
</ol>

<p>1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.</p>

<p>단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 <em>B</em>개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.</p>

### 입력 

 <p>첫째 줄에 <i>N, M</i>, <em>B</em>가 주어진다. (1 ≤ <em>M</em>, <em>N</em> ≤ 500, 0 ≤ <em>B</em> ≤ 6.4 × 10<sup>7</sup>)</p>

<p>둘째 줄부터 <i>N</i>개의 줄에 각각 <i>M</i>개의 정수로 땅의 높이가 주어진다. (<em>i </em>+ 2)번째 줄의 (<em>j </em>+ 1)번째 수는 좌표 (<em>i</em>,<em> j</em>)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.</p>

### 회고
[첫 풀이](https://github.com/HyeseongRo/Algorithm_Problem_Solving/blob/main/PyPy3/%EB%B0%B1%EC%A4%80/Silver/18111.%E2%80%85%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8/%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8.py)

#### 문제 접근 및 초기 풀이  
문제는 주어진 땅의 높이를 일정하게 만드는 데 필요한 최소 시간과 해당 높이를 찾는 문제입니다.  
초기 풀이에서는 0부터 256까지 모든 높이를 대상으로, 매 높이마다 이중 반복문을 돌며 각 위치의 블록을 확인했습니다.

- **시간 복잡도 문제:**  
  매 후보 높이마다 전체 \(N \* M\) 격자를 탐색하므로, 최악의 경우 \(257 \* (N \* M)\)번의 연산이 발생합니다.  
  이 방식은 입력 크기가 커질 경우 Python3에서 시간초과(TLE)를 발생시킬 수 있었습니다.

#### PyPy3에서 통과한 이유  
PyPy3는 JIT 컴파일러를 사용하여 반복문 등의 연산을 최적화하기 때문에, 동일한 알고리즘이라도 실행 속도가 개선되어 제출이 통과되었습니다.

#### 최종 풀이로의 전환 (카운팅 정렬 적용)  
최종 풀이에서는 **카운팅 정렬** 기법을 사용했습니다.

1. **데이터 전처리:**  
   - 전체 격자를 한 번 순회하면서 각 높이(0~256)별 등장 횟수를 기록하는 배열 `heights`를 생성합니다.  
   - 이 과정은 \(O(N \* M)\) 시간에 이루어지며, 이후 반복문에서 동일한 높이 값을 여러 번 계산할 필요가 없어집니다.

2. **목표 높이 반복:**  
   - 후보 높이(0~256)에 대해, 각 고유 높이와 그 개수를 활용하여 필요한 블록 추가 및 제거 작업을 계산합니다.  
   - 내부 반복문의 횟수가 상수(257)로 제한되어 있어, 전체 시간 복잡도는 \(O(257 \* 257)\)로 매우 효율적입니다.
   
이러한 최적화 덕분에 Python3에서도 시간 초과 없이 문제를 해결할 수 있었습니다.

---

### Retrospective

#### Problem Approach and Initial Solution  
The problem involves leveling a ground by adjusting block heights, aiming to achieve a uniform height with minimal time cost.  
In the initial solution, every possible height from 0 to 256 was considered. For each candidate height, the solution iterated through the entire \(N \* M\) grid using nested loops to compute the time required for adjustments.

- **Time Complexity Issue:**  
  For each target height, the entire grid is scanned, resulting in \(257 \* (N \* M)\) operations in the worst-case scenario.  
  With large inputs, this approach led to a time limit exceeded (TLE) error when implemented in Python3.

#### Why It Passed with PyPy3  
PyPy3 employs a JIT compiler that can significantly optimize loop-heavy computations. Even though the underlying algorithm was the same, the execution speed in PyPy3 was improved enough to pass the problem's constraints.

#### Transition to the Final Solution (Using Counting Sort)  
The final solution introduced a counting sort strategy to overcome the inefficiency:

1. **Preprocessing with Counting:**  
   - The grid is traversed once to build an array `heights` that counts how many times each height (0 to 256) occurs.  
   - This preprocessing step takes \(O(N \* M)\) time but avoids re-scanning every cell for each candidate target height.

2. **Iterating Over Target Heights:**  
   - For each candidate target height (0 to 256), the algorithm uses the frequency counts to calculate the total time required for adjustments by multiplying the difference in heights by their occurrence counts.  
   - The inner loop is now fixed to 257 iterations regardless of the grid size, resulting in an overall time complexity of \(O(257 \* 257)\), which is efficient.
   
This optimization allowed the final solution to run within time limits using Python3.


