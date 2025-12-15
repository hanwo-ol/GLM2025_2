# 확장이론 1 (Extension Theory 1)

## 1. $\sigma$-finite (시그마 유한)

**정의**: 공간 $(\Omega, \mathcal{A})$를 고려하자. 여기서 $\mathcal{A}$는 $\Omega$에 대한 세미링(Semi-ring)이다. 만약 어떠한 집합함수 $\tilde{m}: \mathcal{A} \to [0, \infty]$ (단, $\tilde{m}(\emptyset) = 0$)가 아래 조건을 만족한다면, $\tilde{m}$을 $\mathcal{A}$에서 **$\sigma$-finite(시그마 유한)**하다고 한다.

$$
\exists~ \Omega_1, \Omega_2, \dots \in \mathcal{A} \quad \text{such that}
$$

1.  $\bigcup_{i=1}^{\infty} \Omega_i = \Omega$
2.  $\forall n \in \mathbb{N}: \tilde{m}(\Omega_n) < \infty$

---

### 예제 1

집합함수 $\tilde{m}$이 $\mathcal{A}$ 위에서 $\sigma$-finite 한지 판별하라.

*   $\Omega = \mathbb{R}$
*   $\mathcal{A} = \{\emptyset, \mathbb{R}\} \cup \{[-n, n] : n \in \mathbb{N}\}$
*   $\tilde{m}(A) = \begin{cases} \infty & A = \mathbb{R} \\ 0 & \text{otherwise} \end{cases}$

**(풀이)**

$\tilde{m}$은 $\sigma$-finite 하다. 이를 보이기 위해 정의의 조건을 만족하는 수열 $\{\Omega_n\}$을 찾으면 된다.

$\Omega_n = [-n, n]$ 이라고 정의하자.
이때 $\Omega_n \in \mathcal{A}$ 이다.

1.  $\bigcup_{n=1}^{\infty} \Omega_n = \bigcup_{n=1}^{\infty} [-n, n] = \mathbb{R} = \Omega$
2.  모든 $n \in \mathbb{N}$에 대하여, $[-n, n] \neq \mathbb{R}$ 이므로 $\tilde{m}(\Omega_n) = \tilde{m}([-n, n]) = 0 < \infty$ 이다.

따라서 두 조건을 모두 만족하므로 $\tilde{m}$은 $\sigma$-finite 하다.

---

## 2. 카라테오도리의 확장 정리 (Carathéodory's Extension Theorem)

### 이론 (확률 버전)

$\mathcal{A} \subset 2^{\Omega}$를 $\Omega$에 대한 세미링이라고 하자. $\mathcal{A}$ 에서 정의된 '확률 비슷한' 집합함수 $\tilde{P}: \mathcal{A} \to [0, 1]$ 가 아래 조건들을 만족한다고 하자.

1.  $\tilde{P}(\emptyset) = 0$
2.  $\tilde{P}(\Omega) = 1$
3.  $\tilde{P}$ is additive on $\mathcal{A}$ (유한 가법성)
4.  $\tilde{P}$ is $\sigma$-subadditive on $\mathcal{A}$ (시그마 준가법성)

그러면 이 집합함수 $\tilde{P}$는 $\sigma(\mathcal{A})$ 위에서의 확률측도(Probability Measure) $\mathbb{P}$로 **확장(extension)** 할 수 있다. 그리고 이 확장은 **유일(unique)**하다.

### 이론 ($\sigma$-유한 측도 버전)

$\mathcal{A} \subset 2^{\Omega}$를 $\Omega$에 대한 세미링이라고 하자. $\mathcal{A}$ 에서 정의된 '$\sigma$-유한 측도 비슷한' 집합함수 $\tilde{m}: \mathcal{A} \to [0, \infty]$ 가 아래 조건들을 만족한다고 가정하자.

1.  $\tilde{m}(\emptyset) = 0$
2.  $\tilde{m}$ is $\sigma$-finite on $\mathcal{A}$
3.  $\tilde{m}$ is additive on $\mathcal{A}$
4.  $\tilde{m}$ is $\sigma$-subadditive on $\mathcal{A}$

그러면 이 집합함수 $\tilde{m}$은 $\sigma(\mathcal{A})$ 위에서의 $\sigma$-유한 측도(Measure)로 **확장**될 수 있다. 그리고 이 확장은 **유일**하다.

> **Warning**: 이 이론은 '확률 비슷한 함수', '유한측도 비슷한 함수', '$\sigma$-유한측도 비슷한 함수'에는 성립하지만, 일반적인 '측도 비슷한 함수'(infinite measure 등)에 대해서는 유일성이 성립하지 않을 수 있다.

---

## 3. 관련 예제

### 예제 2

$\Omega = \{1, 2, 3, 4\}$ 라고 하자. 관심 있는 집합들의 모임(세미링)은 다음과 같다.
$$
\mathcal{A} = \{\emptyset, \{1\}, \{2\}, \{3, 4\}, \Omega\}
$$
이 집합 위에서 다음과 같은 함수 $\tilde{P}$를 정의하자.

*   $\tilde{P}(\emptyset) = 0$
*   $\tilde{P}(\{1\}) = 1/4$
*   $\tilde{P}(\{2\}) = 1/2$
*   $\tilde{P}(\{3, 4\}) = 1/4$
*   $\tilde{P}(\Omega) = 1$

$\mathcal{A}$는 시그마 필드가 아니므로 $\tilde{P}$를 확률측도라고 부를 수 없다. 이를 확장할 수 있는가?

**(풀이)**

1.  **세미링 확인**: $\mathcal{A}$는 세미링의 조건을 만족한다. (교집합 닫힘, 차집합이 유한개의 서로소인 원소의 합으로 표현됨)
2.  **조건 확인**:
    *   $\tilde{P}(\emptyset)=0$, $\tilde{P}(\Omega)=1$.
    *   **Additivity**: 서로소인 원소들의 합에 대해 값이 보존되는지 확인한다.
        *   $\{1\} \cup \{2\} \notin \mathcal{A}$ 이므로 체크할 필요 없음.
        *   $\{1\} \cup \{2\} \cup \{3,4\} = \Omega$.
        *   $\tilde{P}(\{1\}) + \tilde{P}(\{2\}) + \tilde{P}(\{3,4\}) = 1/4 + 1/2 + 1/4 = 1 = \tilde{P}(\Omega)$. 성립.
    *   **$\sigma$-subadditivity**: 유한 집합이므로 additivity가 성립하면 자동으로 성립한다.

3.  **결론**: 확장이론 1(확률 버전)에 의해, $\tilde{P}$는 $\sigma(\mathcal{A})$ 위에서의 확률측도 $\mathbb{P}$로 **유일하게** 확장된다.

---

### 예제 3

$\Omega = \{1, 2, 3, 4\}$, $\mathcal{A} = \{\emptyset, \{1\}, \{2\}, \{3, 4\}, \Omega\}$ (예제 2와 동일).
생성된 시그마 필드 $\sigma(\mathcal{A})$는 다음과 같다.
$$
\sigma(\mathcal{A}) = \big\{\emptyset, \{1\}, \{2\}, \{1, 2\}, \{3, 4\}, \{1, 3, 4\}, \{2, 3, 4\}, \Omega \big\}
$$

위의 시그마 필드에서 예제 2와 다른 방식으로 확률을 정의할 수도 있다.

**Case 1: $\mathbb{P}_1$**

| Set | $\emptyset$ | $\{1\}$ | $\{2\}$ | $\{3, 4\}$ | $\Omega$ | $\{1, 2\}$ | $\{1, 3, 4\}$ | $\{2, 3, 4\}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\tilde{P}_1$ | 0 | $1/3$ | $1/3$ | $1/3$ | 1 | - | - | - |
| $\mathbb{P}_1$ | 0 | $1/3$ | $1/3$ | $1/3$ | 1 | $2/3$ | $2/3$ | $2/3$ |

**Case 2: $\mathbb{P}_2$**

| Set | $\emptyset$ | $\{1\}$ | $\{2\}$ | $\{3, 4\}$ | $\Omega$ | $\{1, 2\}$ | $\{1, 3, 4\}$ | $\{2, 3, 4\}$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $\tilde{P}_2$ | 0 | 0 | 0 | 1 | 1 | - | - | - |
| $\mathbb{P}_2$ | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 |

**결론**: $\mathcal{A}$ 위에서 $\tilde{P}$를 어떻게 정의하느냐(additivity 등 만족 시)에 따라 $\sigma(\mathcal{A})$로의 확장이 가능하며, 주어진 $\tilde{P}$에 대한 확장은 **유일**하다. (즉, $\tilde{P}_1$은 $\mathbb{P}_1$으로만, $\tilde{P}_2$는 $\mathbb{P}_2$로만 확장된다.)

---

### 예제 4

$\Omega = \{a, b, c, d\}$.
$$
\mathcal{A} = \big\{\{a, b, c\}, \{b, c, d\}\big\}
$$
함수 $\tilde{P}: \mathcal{A} \to [0, 1]$ 정의:
*   $\tilde{P}(\{a, b, c\}) = 3/4$
*   $\tilde{P}(\{b, c, d\}) = 3/4$

$\tilde{P}$를 확장하여 확률측도 $\mathbb{P}: \sigma(\mathcal{A}) \to [0, 1]$를 유일하게 만들 수 있는가?

**(풀이)**

1.  $\mathcal{A}$는 $\emptyset$과 $\Omega$를 포함하지 않으며 교집합에 대해서도 닫혀있지 않으므로 세미링이 아니다. 따라서 확장 정리를 바로 적용할 수 없다.
2.  $\mathcal{A}$를 확장하여 세미링 $\bar{\mathcal{A}}$를 만들어보자.
    $$
    \bar{\mathcal{A}} = \big\{\emptyset, \{a\}, \{d\}, \{b, c\}, \{a, b, c\}, \{b, c, d\}, \Omega\big\}
    $$
    (엄밀히 말하면 $\{a, b, c\} \cap \{b, c, d\} = \{b, c\}$ 등을 추가하고, 차집합 등을 고려하여 구성함)

3.  $\bar{\mathcal{A}}$ 위에서의 함수 $\bar{P}$를 구성한다.
    확률측도의 성질을 만족하려면 다음이 성립해야 한다.
    *   $\mathbb{P}(\Omega) = 1$
    *   $\mathbb{P}(\{a, b, c\}) = 3/4 \implies \mathbb{P}(\{d\}) = 1 - 3/4 = 1/4$
    *   $\mathbb{P}(\{b, c, d\}) = 3/4 \implies \mathbb{P}(\{a\}) = 1 - 3/4 = 1/4$
    *   $\mathbb{P}(\{b, c\}) = \mathbb{P}(\Omega) - \mathbb{P}(\{a\}) - \mathbb{P}(\{d\}) = 1 - 1/4 - 1/4 = 1/2$

    따라서 $\bar{P}$를 다음과 같이 정의할 수 있다.
    *   $\bar{P}(\emptyset) = 0, \quad \bar{P}(\Omega) = 1$
    *   $\bar{P}(\{a\}) = 1/4, \quad \bar{P}(\{d\}) = 1/4$
    *   $\bar{P}(\{b, c\}) = 1/2$
    *   $\bar{P}(\{a, b, c\}) = 3/4, \quad \bar{P}(\{b, c, d\}) = 3/4$

4.  $\bar{P}$는 세미링 $\bar{\mathcal{A}}$ 위에서 확장 정리의 조건(1-4)을 만족한다. 따라서 $\sigma(\bar{\mathcal{A}}) = \sigma(\mathcal{A})$ 위에서의 확률 $\mathbb{P}$로 유일하게 확장된다.
5.  $\tilde{P}$로부터 $\bar{P}$를 유일하게 결정할 수 있었으므로, 결과적으로 $\tilde{P}$의 확장 $\mathbb{P}$도 유일하다.

---

### 예제 5

$\Omega = \{1, 2, 3\}$, $\mathcal{A} = \{\emptyset, \{1, 2\}, \{2, 3\}, \Omega\}$.
함수 $\tilde{P}: \mathcal{A} \to [0, 1]$ 정의:
*   $\tilde{P}(\emptyset) = 0$
*   $\tilde{P}(\{1, 2\}) = 0$
*   $\tilde{P}(\{2, 3\}) = 0$
*   $\tilde{P}(\Omega) = 1$

확장 가능한가?

**(풀이)**

직관적으로 불가능해 보인다. $\{1, 2\}$와 $\{2, 3\}$의 합집합이 $\Omega$ 전체를 커버하는데 각각의 확률이 0이라는 것은 모순처럼 보인다. 이를 엄밀히 보이자.

귀류법: 확장 가능하다고 가정하자. 즉, $\mathbb{P}: \sigma(\mathcal{A}) \to [0, 1]$가 존재하여 $\mathcal{A}$에서 $\tilde{P}$와 일치한다.

1.  $\mathbb{P}(\{1, 2\}) = 0$
2.  $\mathbb{P}(\{2, 3\}) = 0$
3.  $\mathbb{P}(\Omega) = 1$

확률측도의 성질(Subadditivity)에 의해:
$$
\mathbb{P}(\{1, 2\} \cup \{2, 3\}) \leq \mathbb{P}(\{1, 2\}) + \mathbb{P}(\{2, 3\})
$$
좌변은 $\mathbb{P}(\{1, 2, 3\}) = \mathbb{P}(\Omega) = 1$ 이다.
우변은 $0 + 0 = 0$ 이다.

따라서 $1 \leq 0$ 이라는 모순이 발생한다. 그러므로 확장은 불가능하다.

---

### 예제 6

$\Omega = \{1, 2, 3, 4\}$, $\mathcal{A} = \{\emptyset, \{1, 2\}, \{2, 3\}, \Omega\}$.
함수 $\tilde{P}: \mathcal{A} \to [0, 1]$ 정의:
*   $\tilde{P}(\emptyset) = 0$
*   $\tilde{P}(\{1, 2\}) = 1/2$
*   $\tilde{P}(\{2, 3\}) = 1/2$
*   $\tilde{P}(\Omega) = 1$

확장 가능한가? 유일한가?

**(풀이)**

1.  **세미링 확장**: $\mathcal{A}$는 세미링이 아니다. 이를 포함하는 세미링 $\bar{\mathcal{A}}$를 만들자. 가장 작은 단위인 단원소 집합들로 쪼개는 것이 편하다.
    $$
    \bar{\mathcal{A}} = \{\emptyset, \{1\}, \{2\}, \{3\}, \{4\}, \{1, 2\}, \{2, 3\}, \Omega, \dots \text{ (조합들) }\}
    $$
    핵심적으로, $\{1\}, \{2\}, \{3\}, \{4\}$에 값을 할당해 보자.

2.  **가능한 확장 시도**:
    $\tilde{P}$와 모순되지 않게 $\bar{P}$를 정의해 보자.
    *   조건: $\bar{P}(\{1\}) + \bar{P}(\{2\}) = 1/2$
    *   조건: $\bar{P}(\{2\}) + \bar{P}(\{3\}) = 1/2$
    *   조건: 전체 합은 1. 즉 $\bar{P}(\{4\}) = 1 - (\bar{P}(\{1\}) + \bar{P}(\{2\}) + \bar{P}(\{3\}))$

    **Case 1 ($\bar{P}_1$)**:
    *   $\bar{P}_1(\{1\}) = 0$
    *   $\bar{P}_1(\{2\}) = 1/2$
    *   $\bar{P}_1(\{3\}) = 0$
    *   $\bar{P}_1(\{4\}) = 1/2$
    *   검산: $\bar{P}_1(\{1, 2\}) = 1/2$, $\bar{P}_1(\{2, 3\}) = 1/2$. (만족)

    **Case 2 ($\bar{P}_2$)**:
    *   $\bar{P}_2(\{1\}) = 1/2$
    *   $\bar{P}_2(\{2\}) = 0$
    *   $\bar{P}_2(\{3\}) = 1/2$
    *   $\bar{P}_2(\{4\}) = 0$
    *   검산: $\bar{P}_2(\{1, 2\}) = 1/2$, $\bar{P}_2(\{2, 3\}) = 1/2$. (만족)

3.  **결론**: $\bar{P}_1$과 $\bar{P}_2$는 모두 세미링 위에서 additivity를 만족하므로 각각 확률측도 $\mathbb{P}_1, \mathbb{P}_2$로 확장된다. 하지만 $\mathbb{P}_1(\{1\}) = 0 \neq 1/2 = \mathbb{P}_2(\{1\})$ 이므로 두 측도는 다르다.
    따라서 $\tilde{P}$는 확장 가능하지만, 그 **결과는 유일하지 않다.**

---

### 예제 7 (통계학과라서 행복해)

$\Omega = \{a, b\}$. $\mathcal{A} = \{\emptyset, \{a\}\}$.
$\mathcal{A}$는 세미링이다.
함수 $\tilde{m}: \mathcal{A} \to [0, \infty]$ 정의:
*   $\tilde{m}(\emptyset) = 0$
*   $\tilde{m}(\{a\}) = 1/2$

이 함수는 $(\Omega, \sigma(\mathcal{A}))$에서의 **측도(Measure)**로 확장 가능한가? 유일한가?

**(풀이)**

$\tilde{m}$은 $\mathcal{A}$에서 additivity를 만족한다. (더할 건덕지가 별로 없음)
이를 측도 $m$으로 확장해보자. $m$은 $\sigma(\mathcal{A}) = \{\emptyset, \{a\}, \{b\}, \Omega\}$ 에서 정의되어야 한다.

가능한 확장들:
1.  $m_1$: $m_1(\{a\}) = 1/2$, $m_1(\{b\}) = 1/2 \implies m_1(\Omega) = 1$
2.  $m_2$: $m_2(\{a\}) = 1/2$, $m_2(\{b\}) = 1 \implies m_2(\Omega) = 3/2$
3.  $m_3$: $m_3(\{a\}) = 1/2$, $m_3(\{b\}) = \infty \implies m_3(\Omega) = \infty$

위 모든 경우에 대해 $m$은 측도의 공리(가법성 등)를 만족하며 $\mathcal{A}$ 위에서 $\tilde{m}$과 일치한다.
따라서 **확장 가능하지만 유일하지 않다.**

**이유**: $\sigma$-finite 조건이 없기 때문이다.
만약 $\tilde{m}(\Omega) = 1$과 같은 조건이 추가로 있었다면(즉, 전체 공간의 측도가 유한하거나, $\sigma$-finite 조건이 만족되었다면), 확장은 유일했을 것이다. 이 예제에서는 $\mathcal{A}$ 만으로는 $\Omega$ 전체를 커버하는 유한 측도 집합들의 열을 만들 수 없다( $\{a\}$ 하나로는 $\Omega=\{a,b\}$를 덮을 수 없음). $\tilde{m}$ 자체가 $\sigma$-finite 하지 않으므로(정의역 $\mathcal{A}$ 상에서), 확장 정리의 유일성 조건이 성립하지 않는다.
