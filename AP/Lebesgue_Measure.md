# 르벡 측도 (Lebesgue Measure)

## 예제 8: 르벡 측도의 구성 ($\star\star\star$)

**상황**: $\Omega = \mathbb{R}$ 이라고 하고, 다음과 같은 세미링 $\mathcal{A}$를 고려하자.
$$
\mathcal{A} = \big\{(a, b] : -\infty < a < b < \infty \big\} \cup \{\emptyset\}
$$
이 $\mathcal{A}$ 위에서 '시그마 유한 측도 비슷한' 함수 $\tilde{\lambda}: \mathcal{A} \to [0, \infty)$를 다음과 같이 정의하자.
*   $\tilde{\lambda}(\emptyset) = 0$
*   $\tilde{\lambda}((a, b]) = b - a$

**목표**: $\tilde{\lambda}$가 $\mathcal{A}$ 위에서 (3) Additivity와 (4) $\sigma$-Subadditivity를 만족함을 보여라. 이것이 성립하면 카라테오도리 확장 정리에 의해 $\tilde{\lambda}$는 $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ 위에서의 **르벡 측도(Lebesgue Measure)** $\lambda$로 유일하게 확장된다.

### 1. Additivity (유한 가법성)

구간 $I = (a, b]$가 서로소인 유한 개의 구간 $I_1, \dots, I_n$의 합집합으로 표현된다고 하자. 즉, $I = \bigcup_{k=1}^n I_k$. 여기서 $I_k = (a_k, b_k]$ 라고 하자.
일반성을 잃지 않고 $a = a_1 < b_1 = a_2 < b_2 = \dots < b_n = b$ 순서로 정렬할 수 있다.

$$
\sum_{k=1}^n \tilde{\lambda}(I_k) = \sum_{k=1}^n (b_k - a_k) = (b_1 - a_1) + (b_2 - a_2) + \dots + (b_n - a_n)
$$
이것은 텔레스코핑 합(telescoping sum)이 되어 중간항들이 소거된다.
$$
= b_n - a_1 = b - a = \tilde{\lambda}(I)
$$
따라서 Additivity가 성립한다.

### 2. $\sigma$-Subadditivity (시그마 준가법성)

**Claim**: 임의의 $(a, b] \in \mathcal{A}$와 $(a_n, b_n] \in \mathcal{A}$ ($n \in \mathbb{N}$) 에 대하여,
$$
(a, b] \subset \bigcup_{n=1}^{\infty} (a_n, b_n] \implies b - a \leq \sum_{n=1}^{\infty} (b_n - a_n)
$$

**(증명)**
원래 강의록에서 생략된 증명이다. 하이네-보렐(Heine-Borel) 정리(컴팩트성)를 이용하여 증명한다.

임의의 $\epsilon > 0$을 고정하자.

1.  **닫힌 구간으로 축소 (Compact set)**:
    우리가 측정하고자 하는 구간 $(a, b]$ 내부에, 길이 차이가 $\epsilon$보다 작게 나는 닫힌 구간(Compact interval)을 잡을 수 있다.
    $[a + \epsilon, b] \subset (a, b]$. (단, $a+\epsilon < b$라 가정. 그렇지 않으면 구간 길이가 매우 작으므로 자명함)

2.  **열린 구간으로 확대 (Open cover)**:
    각 덮개 구간 $(a_n, b_n]$을 살짝 부풀려 열린 구간으로 만든다.
    $(a_n, b_n + \epsilon/2^n) \supset (a_n, b_n]$.

3.  **커버 관계 확인**:
    $$
    [a + \epsilon, b] \subset (a, b] \subset \bigcup_{n=1}^{\infty} (a_n, b_n] \subset \bigcup_{n=1}^{\infty} (a_n, b_n + \epsilon/2^n)
    $$
    즉, 컴팩트 집합 $[a + \epsilon, b]$가 열린 구간들의 모임 $\bigcup_{n=1}^{\infty} (a_n, b_n + \epsilon/2^n)$에 의해 덮여 있다.

4.  **하이네-보렐 정리 (Heine-Borel Theorem)**:
    컴팩트 집합의 열린 덮개(Open cover)는 유한 부분 덮개(Finite subcover)를 가진다.
    따라서 적당한 자연수 $N$이 존재하여 다음이 성립한다.
    $$
    [a + \epsilon, b] \subset \bigcup_{k=1}^{N} (a_{n_k}, b_{n_k} + \epsilon/2^{n_k})
    $$
    편의상 인덱스를 재정렬하여 $1, \dots, N$이라고 하자.
    $$
    [a + \epsilon, b] \subset \bigcup_{n=1}^{N} (a_n, b_n + \epsilon/2^n)
    $$

5.  **유한 가법성 및 부등식 적용**:
    유한 개의 열린 구간들이 닫힌 구간을 덮을 때, 길이의 합에 대한 부등식이 성립함은 초등적인 논리로 보일 수 있다. (덮는 구간들의 길이 합 $\geq$ 덮이는 구간 길이)
    $$
    (b) - (a + \epsilon) \leq \sum_{n=1}^{N} \text{Length}\big( (a_n, b_n + \epsilon/2^n) \big)
    $$
    $$
    b - a - \epsilon \leq \sum_{n=1}^{N} (b_n + \epsilon/2^n - a_n) = \sum_{n=1}^{N} (b_n - a_n) + \sum_{n=1}^{N} \frac{\epsilon}{2^n}
    $$
    우변의 두 번째 항은 무한 등비급수의 합 $\epsilon$보다 작다.
    $$
    b - a - \epsilon \leq \sum_{n=1}^{N} (b_n - a_n) + \epsilon \leq \sum_{n=1}^{\infty} (b_n - a_n) + \epsilon
    $$

6.  **$\epsilon$ 극한**:
    위 부등식은 임의의 $\epsilon > 0$에 대해 성립한다.
    $$
    b - a - 2\epsilon \leq \sum_{n=1}^{\infty} (b_n - a_n)
    $$
    여기서 $\epsilon \to 0$ 극한을 취하면,
    $$
    b - a \leq \sum_{n=1}^{\infty} (b_n - a_n)
    $$
    증명 완료. $\blacksquare$

---

## 예제 11: 다양한 구간 정의와 르벡 측도의 유일성

측도 공간 $(\mathbb{R}, \mathcal{R}, \lambda)$를 선언하자. 여기서 $\mathcal{R} = \mathcal{B}(\mathbb{R})$ (보렐 시그마 필드)이고 $\lambda$는 르벡 측도이다.
기존의 세미링 $\mathcal{A}_1 = \{(a, b]\}$ 외에 다른 형태의 구간들로도 르벡 측도를 유일하게 정의할 수 있음을 보인다.

### 고려하는 집합족들
1.  $\mathcal{A}_1 = \{(a, b] : -\infty < a < b < \infty\} \cup \{\emptyset\}$ (기존)
2.  $\mathcal{A}_2 = \{[a, b) : -\infty < a < b < \infty\} \cup \{\emptyset\}$
3.  $\mathcal{A}_3 = \{[a, b] : -\infty < a < b < \infty\} \cup \{\emptyset\}$
4.  $\mathcal{A}_4 = \{(a, b) : -\infty < a < b < \infty\} \cup \{\emptyset\}$

각 집합족 위에서 길이 함수 $\tilde{\lambda}_i$ (구간 길이는 $b-a$)를 정의했을 때, 이들 모두 동일한 르벡 측도 $\lambda$로 확장됨을 보인다.

**(증명)**

다음 세 단계를 보이면 충분하다.
1.  $\sigma(\mathcal{A}_1) = \sigma(\mathcal{A}_2) = \sigma(\mathcal{A}_3) = \sigma(\mathcal{A}_4) = \mathcal{B}(\mathbb{R})$
2.  $\lambda$는 $\mathcal{A}_2, \mathcal{A}_3, \mathcal{A}_4$ 위에서도 길이 함수와 일치한다. (즉, $\lambda([a,b)) = b-a$ 등)
3.  $\mathcal{A}_2, \mathcal{A}_3, \mathcal{A}_4$는 모두 $\pi$-system이다. (유일성 보장)

---

### Step 1: 시그마 필드의 일치

모든 시그마 필드가 단원소 집합 $\{c\}$를 포함함을 먼저 보인다.

*   $\{c\} = \bigcap_{n=1}^{\infty} (c - 1/n, c+1/n) \in \sigma(\mathcal{A}_4)$
*   $\{c\} = \bigcap_{n=1}^{\infty} (c - 1/n, c] \in \sigma(\mathcal{A}_1)$
*   비슷한 방식으로 $\sigma(\mathcal{A}_2), \sigma(\mathcal{A}_3)$에도 포함됨.

이를 이용해 서로를 표현할 수 있다. 예를 들어 $\sigma(\mathcal{A}_2) = \sigma(\mathcal{A}_1)$ 만 보자.
*   $(a, b] = [a, b] \setminus \{a\} = ([a, b) \cup \{b\}) \setminus \{a\}$
    *   여기서 $[a, b) \in \mathcal{A}_2$.
    *   $\{a\}, \{b\} \in \sigma(\mathcal{A}_2)$ (단원소 집합 생성 가능).
    *   따라서 $(a, b] \in \sigma(\mathcal{A}_2)$ 이므로 $\sigma(\mathcal{A}_1) \subset \sigma(\mathcal{A}_2)$.
*   반대 방향도 유사하게 성립.

결국 모두 보렐 시그마 필드 $\mathcal{B}(\mathbb{R})$과 같다.

---

### Step 2: $\lambda$와 길이 함수의 일치

핵심은 **한 점의 측도가 0**임을 보이는 것이다. 즉 $\forall x \in \mathbb{R}: \lambda(\{x\}) = 0$.
이것이 증명되면, 구간 끝점의 포함 여부가 길이에 영향을 주지 않으므로 $\lambda([a, b]) = \lambda((a, b)) = b-a$가 성립한다.

**(증명: $\lambda(\{x\}) = 0$)**

가정: 어떤 $x$에 대해 $\lambda(\{x\}) > 0$ 이라고 하자.

1.  $\mathbb{R}$에서 임의의 구간 $(c-1, c+1]$을 잡는다. 이 구간의 길이는 2이다.
    $$
    \lambda((c-1, c+1]) = 2
    $$
2.  이 구간 내의 모든 유리수들의 집합 $\mathbb{Q}^* = (c-1, c+1] \cap \mathbb{Q}$를 생각하자.
    유리수는 가산 집합(countable set)이므로 $\mathbb{Q}^* = \{q_1, q_2, \dots\}$ 로 나열할 수 있다.
3.  측도의 단조성(Monotonicity)에 의해:
    $$
    \lambda(\mathbb{Q}^*) \leq \lambda((c-1, c+1]) = 2 \quad \cdots (\star)
    $$
4.  측도의 가산 가법성($\sigma$-additivity)에 의해:
    $$
    \lambda(\mathbb{Q}^*) = \lambda\left(\bigcup_{i=1}^{\infty} \{q_i\}\right) = \sum_{i=1}^{\infty} \lambda(\{q_i\})
    $$
    우리는 '평행이동 불변성(Translation Invariance)'을 가정하거나, 혹은 모든 점이 대등한 성질을 갖는다고 볼 때, 만약 어떤 점의 측도가 양수라면 모든 점의 측도가 동일하거나 적어도 양수일 것이다. (더 엄밀하게는 르벡 측도의 평행이동 불변성을 쓴다. $\lambda(\{x\}) = \lambda(\{x+h\})$).
    따라서 모든 $q_i$에 대해 $\lambda(\{q_i\}) = \alpha > 0$ 라고 하면,
    $$
    \sum_{i=1}^{\infty} \lambda(\{q_i\}) = \sum_{i=1}^{\infty} \alpha = \infty \quad \cdots (\star\star)
    $$
    (혹은, $\lambda(\{x\}) > 0$인 점이 하나라도 있으면 유리수 조밀성에 의해 그런 점을 무한히 많이 포함시킬 수 있는 논리를 펴기도 함)
5.  $(\star)$ 식은 2 이하인데, $(\star\star)$ 식은 무한대이다. 이는 모순이다.
    따라서 $\lambda(\{x\}) = 0$ 이어야 한다.

$\therefore$ 끝점이 포함되든 안 되든 구간의 측도는 길이($b-a$)와 같다.

---

### Step 3: $\pi$-system 확인

모든 구간들의 모임 $\mathcal{A}_2, \mathcal{A}_3, \mathcal{A}_4$는 교집합을 취했을 때 다시 구간(또는 공집합)이 되므로 $\pi$-system이다.
(예: $(a, b) \cap (c, d) = (\max(a, c), \min(b, d))$ 혹은 $\emptyset$)

**결론**:
1.  모든 $\mathcal{A}_i$는 동일한 시그마 필드($\mathcal{B}(\mathbb{R})$)를 생성한다.
2.  모든 $\mathcal{A}_i$ 위에서 길이 함수는 르벡 측도 $\lambda$와 일치한다.
3.  모든 $\mathcal{A}_i$는 $\pi$-system이다.
4.  따라서 확장이론 2에 의해, 어떤 구간 정의를 사용하든 확장된 르벡 측도 $\lambda$는 **유일하다.**
