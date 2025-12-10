# 예제 7 풀이: 포함관계에 있는 집합의 확률 (비합리적 확률 함수)

본 문서는 [AP2025 06wk 강의노트](https://guebin.github.io/AP2025/posts/06wk.html)의 **예제 7 (포함관계에 있는 집합의 확률)**에 대한 상세한 풀이입니다.

## 1. 문제 기술

**가정:**
*   전체 집합(Sample Space): $\Omega = \{1, 2, 3\}$
*   시그마 대수(Sigma-algebra): $\mathcal{F} = \{\emptyset, \{1\}, \{2\}, \{3\}, \{1,2\}, \{1,3\}, \{2,3\}, \Omega\}$ (멱집합과 동일)
*   확률 함수(Probability Function) $P$의 정의:
    *   $P(\emptyset) = 0$
    *   $P(\{1\}) = 1/4$
    *   $P(\{2\}) = 1/4$
    *   $P(\{3\}) = 2/4$
    *   $P(\{1,2\}) = 2/4$
    *   $P(\{1,3\}) = 3/4$
    *   $P(\{2,3\}) = 1/4$
    *   $P(\Omega) = 1$

**질문:**
위와 같이 정의된 확률 함수 $P$는 합리적인가? (즉, 확률의 공리를 만족하는가?)

---

## 2. 학부생을 위한 직관적 설명 (Undergraduate Perspective)

**답: 합리적이지 않습니다 (Not Rational).**

확률의 가장 기본적인 규칙 중 하나는 "따로따로 일어날 확률을 더하면 전체 확률이 되어야 한다"는 것입니다.
예를 들어, 주사위에서 2가 나올 확률과 3이 나올 확률을 더하면, (2 또는 3)이 나올 확률과 같아야 합니다.

이 문제에서 주어진 숫자를 보면:
*   2가 뽑힐 확률 $P(\{2\}) = 1/4$
*   3이 뽑힐 확률 $P(\{3\}) = 2/4$

그렇다면 "2 또는 3"이 뽑힐 확률 $P(\{2, 3\})$은 당연히 두 값을 더한 $1/4 + 2/4 = 3/4$이어야 합니다.
하지만 문제에서 주어진 정의를 보면 $P(\{2, 3\}) = 1/4$라고 되어 있습니다.

따라서 **$3/4 \neq 1/4$**이므로, 이 확률 정의는 앞뒤가 맞지 않는 모순입니다.

---

## 3. 엄밀한 증명 (PhD Level Derivation)

확률 측도(Probability Measure)가 되기 위해서는 **가산 가법성(Countable Additivity)**을 만족해야 합니다. 유한 집합의 경우 **유한 가법성(Finite Additivity)**으로 충분합니다.

### 3.1. 유한 가법성 검증
서로소(Disjoint)인 두 사건 $A, B \in \mathcal{F}$ ($A \cap B = \emptyset$)에 대하여, 다음이 성립해야 합니다.
$$ P(A \cup B) = P(A) + P(B) $$

### 3.2. 모순 유도
집합 $A = \{2\}$와 $B = \{3\}$을 선택합니다.
1.  **서로소 확인:** $\{2\} \cap \{3\} = \emptyset$ 이므로 서로소 조건 만족.
2.  **좌변 계산 ($A \cup B$의 확률):**
    주어진 정의에 의해,
    $$ P(\{2\} \cup \{3\}) = P(\{2, 3\}) = 1/4 $$
3.  **우변 계산 (각각의 확률의 합):**
    주어진 정의에 의해,
    $$ P(\{2\}) + P(\{3\}) = 1/4 + 2/4 = 3/4 $$

### 3.3. 결론
$$ P(\{2, 3\}) \neq P(\{2\}) + P(\{3\}) $$
$$ 1/4 \neq 3/4 $$
위 등식이 성립하지 않으므로, 함수 $P$는 확률의 공리(가법성)를 위배합니다. 따라서 이 함수는 확률 측도가 될 수 없습니다.

---

## 4. 파이썬 검증 (Python Verification)

파이썬 코드를 통해 모든 서로소인 부분집합 쌍에 대해 가법성이 성립하는지 전수 조사(Brute-force)하여 검증합니다.

```python
def verify_probability_axioms():
    # 1. 집합과 확률 값 정의
    # 파이썬 set은 unhashable하므로 frozenset 사용
    prob_map = {
        frozenset(): 0.0,
        frozenset({1}): 0.25,
        frozenset({2}): 0.25,
        frozenset({3}): 0.50,
        frozenset({1, 2}): 0.50,
        frozenset({1, 3}): 0.75,
        frozenset({2, 3}): 0.25,  # 문제의 지점
        frozenset({1, 2, 3}): 1.0
    }

    events = list(prob_map.keys())
    is_valid = True

    print("Checking Finite Additivity for Disjoint Sets...")

    # 2. 모든 쌍에 대해 검사
    for i in range(len(events)):
        for j in range(i + 1, len(events)):
            A = events[i]
            B = events[j]

            # 서로소인 경우만 체크
            if A.isdisjoint(B):
                union_AB = A | B

                # 합집합이 정의된 이벤트인지 확인 (여기선 멱집합이라 항상 참)
                if union_AB in prob_map:
                    p_union = prob_map[union_AB]
                    p_sum = prob_map[A] + prob_map[B]

                    # 부동소수점 오차 고려하여 비교
                    if abs(p_union - p_sum) > 1e-9:
                        print(f"[FAIL] Disjoint Pair Found:")
                        print(f"  A = {set(A)}, P(A) = {prob_map[A]}")
                        print(f"  B = {set(B)}, P(B) = {prob_map[B]}")
                        print(f"  P(A U B) = {p_union} != P(A) + P(B) = {p_sum}")
                        is_valid = False

    if is_valid:
        print("\nResult: The probability function is VALID.")
    else:
        print("\nResult: The probability function is INVALID.")

if __name__ == "__main__":
    verify_probability_axioms()
```

### 실행 결과 예상
```text
Checking Finite Additivity for Disjoint Sets...
[FAIL] Disjoint Pair Found:
  A = {2}, P(A) = 0.25
  B = {3}, P(B) = 0.5
  P(A U B) = 0.25 != P(A) + P(B) = 0.75

Result: The probability function is INVALID.
```

---

## 5. 참고 (Note)
해당 강의 노트에는 "Example 7"이라는 번호가 붙은 예제가 두 개 존재합니다.
1.  **본 문서에서 다룬 내용:** $\Omega=\{1,2,3\}$인 이산 공간에서의 확률 공리 위배 예제.
2.  **다른 예제:** $\Omega=\mathbb{R}$인 연속 공간에서 르벡 측도의 확장에 관한 예제 ("혹시..."로 시작하는 부분).

일반적으로 "Example 7"은 첫 번째로 등장하는 이산 확률 문제를 지칭하며, 이는 확률론의 기초인 공리적 정의를 이해하는 데 중요한 반례(Counter-example)입니다.

## 참고문헌 (References)

1.  **AP2025 06wk 강의노트**
    *   [https://guebin.github.io/AP2025/posts/06wk.html](https://guebin.github.io/AP2025/posts/06wk.html)
    *   해당 페이지의 "예제7 – 포함관계에 있는 집합의 확률" 섹션을 인용하였습니다.
