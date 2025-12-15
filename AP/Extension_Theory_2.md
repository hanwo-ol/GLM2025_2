# 확장이론 2 (Extension Theory 2)

## 1. 확장이론 2 (유일성 정리)

확장이론 1은 존재성(existence)에 초점을 맞추었다면, 확장이론 2는 유일성(uniqueness)을 다루는 강력한 도구이다.

### 이론 (확률측도 버전)

$(\Omega, \sigma(\mathcal{A}), \mathbb{P})$ 가 확률공간이라고 하자. 그리고 $\mathcal{A}$는 **$\pi$-system**이라고 하자.
(참고: $\pi$-system은 교집합에 대해 닫혀있는 집합족을 의미한다.)

확률측도 $\mathbb{P}: \sigma(\mathcal{A}) \to [0, 1]$ 의 값은 **$\mathcal{A}$ 에서의 값으로 유일하게 결정된다.**
즉, 두 확률측도 $\mathbb{P}_1, \mathbb{P}_2$가 모든 $A \in \mathcal{A}$에 대해 $\mathbb{P}_1(A) = \mathbb{P}_2(A)$를 만족한다면, 모든 $B \in \sigma(\mathcal{A})$에 대해 $\mathbb{P}_1(B) = \mathbb{P}_2(B)$이다.

### 이론 ($\sigma$-유한 측도 버전)

$(\Omega, \sigma(\mathcal{A}), m)$ 가 $\sigma$-유한 측도 공간(measure space)이라고 하자. 그리고 $\mathcal{A}$는 $\pi$-system이라고 하자.

$\sigma$-유한 측도 $m: \sigma(\mathcal{A}) \to [0, \infty]$ 의 값은 **$\mathcal{A}$ 에서의 값으로 유일하게 결정된다.**

---

## 2. 관련 예제

### 예제 9 (예제 2 다시 풀기)

**상황**: $\Omega = \{1, 2, 3, 4\}$, $\mathcal{A} = \{\emptyset, \{1\}, \{2\}, \{3, 4\}, \Omega\}$.
$\tilde{P}$는 $\mathcal{A}$ 위에서 정의된 확률 비슷한 함수이다.

*   $\tilde{P}(\{1\}) = 1/4$
*   $\tilde{P}(\{2\}) = 1/2$
*   $\tilde{P}(\{3, 4\}) = 1/4$

**(풀이 1: 확장이론 1 적용)**
$\mathcal{A}$가 세미링임을 보이고, $\tilde{P}$가 가법성 등을 만족함을 보여 확장의 존재성과 유일성을 증명한다. (앞서 다룬 방식)

**(풀이 2: 확장이론 2 적용)**
우선 확장된 확률측도 $\mathbb{P}$가 존재한다고 가정하고(확장이론 1 혹은 간단한 구성으로 확인 가능), 그 유일성을 보이자.

$\mathcal{A}$가 $\pi$-system인지 확인한다.
*   $\emptyset \cap A = \emptyset \in \mathcal{A}$
*   $\{1\} \cap \{2\} = \emptyset \in \mathcal{A}$
*   $\{1\} \cap \{3, 4\} = \emptyset \in \mathcal{A}$
*   모든 원소끼리의 교집합이 다시 $\mathcal{A}$에 속한다.

따라서 $\mathcal{A}$는 $\pi$-system이다. 확장이론 2에 의하여, $\mathcal{A}$ 위에서 값이 결정되면 $\sigma(\mathcal{A})$ 전체에서의 값도 유일하게 결정된다.
즉, 우리는 $\sigma(\mathcal{A})$의 복잡한 원소들($\{1, 2\}$ 등)에 대한 확률을 일일이 정의하지 않아도, $\mathcal{A}$에서의 값만으로 확률측도가 유일함을 보장받는다.

---

### 예제 10 (예제 6 다시 보기)

**상황**: $\Omega = \{1, 2, 3, 4\}$, $\mathcal{A} = \{\emptyset, \{1, 2\}, \{2, 3\}, \Omega\}$.
*   $\tilde{P}(\{1, 2\}) = 1/2$
*   $\tilde{P}(\{2, 3\}) = 1/2$

이 경우 확장이 유일한가?

**(분석)**
앞서 예제 6에서 보았듯이 유일하지 않다 ($\mathbb{P}_1 \neq \mathbb{P}_2$).
확장이론 2의 관점에서 왜 유일성이 깨졌는지 살펴보자.

$\mathcal{A}$가 $\pi$-system인가?
$$
\{1, 2\} \cap \{2, 3\} = \{2\}
$$
그런데 $\{2\} \notin \mathcal{A}$ 이다.
따라서 $\mathcal{A}$는 교집합에 대해 닫혀있지 않으므로 **$\pi$-system이 아니다.**

이 때문에 확장이론 2의 전제 조건이 만족되지 않아, $\mathcal{A}$에서의 값이 일치하더라도 $\sigma(\mathcal{A})$ 전체에서 일치한다는 보장이 없는 것이다. 실제로 $\mathbb{P}_1(\{2\}) = 1/2$ 이고 $\mathbb{P}_2(\{2\}) = 0$ 으로 서로 달랐지만, 두 측도 모두 $\mathcal{A}$ 상에서는 값을 공유했다. 이는 $\{2\}$에 대한 정보가 $\mathcal{A}$에 없어서 자유도가 생겼기 때문이다.

---

### 예제 10-2 (예제 4 다시 보기 - 원문상 예제 3으로 표기됨)

**상황**: $\Omega = \{a, b, c, d\}$, $\mathcal{A} = \{\{a, b, c\}, \{b, c, d\}\}$.
*   $\tilde{P}(\{a, b, c\}) = 3/4$
*   $\tilde{P}(\{b, c, d\}) = 3/4$

**(풀이)**

**1. 존재성 (Existence)**
$\mathcal{A}$는 세미링이 아니므로 직접 확장이론 1을 쓸 수 없다.
대신 더 큰 세미링 $\mathcal{S} = \{\emptyset, \{a\}, \{b, c\}, \{d\}, \Omega\}$를 고려하자.
이 세미링 위에서 $\tilde{P}_2$를 다음과 같이 정의하자.
*   $\tilde{P}_2(\{a\}) = 1/4$
*   $\tilde{P}_2(\{d\}) = 1/4$
*   $\tilde{P}_2(\{b, c\}) = 1/2$

이 $\tilde{P}_2$는 확장이론 1에 의해 확률측도 $\mathbb{P}_2$로 유일하게 확장된다.
이 $\mathbb{P}_2$가 원래 조건들을 만족하는지 확인하자.
*   $\mathbb{P}_2(\{a, b, c\}) = \mathbb{P}_2(\{a\}) + \mathbb{P}_2(\{b, c\}) = 1/4 + 1/2 = 3/4$. (만족)
*   $\mathbb{P}_2(\{b, c, d\}) = \mathbb{P}_2(\{b, c\}) + \mathbb{P}_2(\{d\}) = 1/2 + 1/4 = 3/4$. (만족)

따라서 조건을 만족하는 확률측도 $\mathbb{P}_2$가 **존재한다.**

**2. 유일성 (Uniqueness)**
다른 확장 $\mathbb{P}_1$이 있다고 가정하자. 즉, $\mathbb{P}_1$도 $\mathcal{A}$ 위에서 $\tilde{P}$와 일치한다.
확률측도의 성질에 의해 다음이 성립해야 한다.
*   $\mathbb{P}_1(\{a\}) = 1 - \mathbb{P}_1(\{b, c, d\}) = 1 - 3/4 = 1/4$
*   $\mathbb{P}_1(\{d\}) = 1 - \mathbb{P}_1(\{a, b, c\}) = 1 - 3/4 = 1/4$
*   $\mathbb{P}_1(\{b, c\}) = \mathbb{P}_1(\{a, b, c\}) - \mathbb{P}_1(\{a\}) = 3/4 - 1/4 = 1/2$

즉, $\mathbb{P}_1$은 $\mathcal{P} = \mathcal{A} \cup \{\{b, c\}, \{a\}, \{d\}\}$ 라는 집합족 위에서 $\mathbb{P}_2$와 값이 같아야 한다.
여기서 $\mathcal{P}$ (또는 더 간단히 $\mathcal{S}$)는 $\pi$-system (실제로는 세미링이자 파이시스템)이 된다.
따라서 확장이론 2에 의해, 이 $\pi$-system 위에서의 값이 같으면 전체 $\sigma(\mathcal{P})$ (즉 $\sigma(\mathcal{A})$) 위에서의 측도도 유일하게 결정된다.

그러므로 $\mathbb{P}_1 = \mathbb{P}_2$ 이어야 한다. 즉, 확장은 **유일하다.**
