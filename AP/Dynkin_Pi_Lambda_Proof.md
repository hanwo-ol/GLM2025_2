# 딘킨의 $\pi$-$\lambda$ 정리 (Dynkin's $\pi$-$\lambda$ Theorem) 증명

본 문서는 [AP2025 10wk 강의노트](https://guebin.github.io/AP2025/posts/10wk.html)의 핵심 내용인 **딘킨의 $\pi$-$\lambda$ 정리**에 대한 상세 증명입니다.

---

## 1. 정리 (Theorem)

집합족 $\mathcal{P} \subset 2^{\Omega}$가 **$\pi$-시스템(Pi-system)**이면, 다음이 성립한다.
$$ l(\mathcal{P}) = \sigma(\mathcal{P}) $$
여기서 $l(\mathcal{P})$는 $\mathcal{P}$를 포함하는 최소한의 $\lambda$-시스템이고, $\sigma(\mathcal{P})$는 $\mathcal{P}$를 포함하는 최소한의 $\sigma$-필드이다.

> **의미:** $\mathcal{P}$를 포함하는 최소한의 시그마 필드를 찾기 위해서, $\mathcal{P}$를 포함하는 최소한의 람다 시스템만 찾아도 충분하다. 이는 측도의 유일성 증명(Uniqueness of Measure) 등에 강력하게 사용된다.

---

## 2. 증명 전략 (Strategy)

$$ l(\mathcal{P}) \subset \sigma(\mathcal{P}) \quad \text{and} \quad l(\mathcal{P}) \supset \sigma(\mathcal{P}) $$

1.  **방향 1: $l(\mathcal{P}) \subset \sigma(\mathcal{P})$**
    *   모든 $\sigma$-필드는 $\lambda$-시스템이다. (자명함)
    *   $\sigma(\mathcal{P})$는 $\mathcal{P}$를 포함하는 $\sigma$-필드이므로, 당연히 $\lambda$-시스템이기도 하다.
    *   $l(\mathcal{P})$는 $\mathcal{P}$를 포함하는 *가장 작은* $\lambda$-시스템이므로, $\sigma(\mathcal{P})$에 포함된다.

2.  **방향 2: $l(\mathcal{P}) \supset \sigma(\mathcal{P})$**
    *   이것을 보이기 위해 **"$l(\mathcal{P})$가 $\sigma$-필드임"**을 증명하면 된다.
    *   $l(\mathcal{P})$가 $\sigma$-필드라면, $\mathcal{P}$를 포함하는 $\sigma$-필드 중 하나가 되므로, 가장 작은 $\sigma$-필드인 $\sigma(\mathcal{P})$를 포함하게 된다.
    *   $l(\mathcal{P})$는 이미 $\lambda$-시스템이므로, **"$l(\mathcal{P})$가 $\pi$-시스템(교집합에 닫힘)임"**만 추가로 보이면 된다. (참고: $\pi$-시스템 + $\lambda$-시스템 = $\sigma$-필드)

---

## 3. 상세 증명 (Proof)

목표: **$l(\mathcal{P})$가 $\pi$-시스템임을 보이자.**
즉, 임의의 $A, B \in l(\mathcal{P})$에 대하여 $A \cap B \in l(\mathcal{P})$임을 보여야 한다.

이를 위해 다음과 같은 집합족 $\mathcal{D}_E$를 정의한다. 임의의 집합 $E \in l(\mathcal{P})$에 대하여,
$$ \mathcal{D}_E = \{ F \in l(\mathcal{P}) : E \cap F \in l(\mathcal{P}) \} $$

증명은 다음 3단계로 진행된다.

### Step 1: 임의의 $E \in l(\mathcal{P})$에 대하여, $\mathcal{D}_E$는 $\lambda$-시스템이다.
1.  **전체집합 포함:** $\Omega \in l(\mathcal{P})$이고 $E \cap \Omega = E \in l(\mathcal{P})$이므로 $\Omega \in \mathcal{D}_E$.
2.  **차집합에 닫힘:** $A, B \in \mathcal{D}_E$이고 $A \subset B$라 하자.
    $$ (B \setminus A) \cap E = (B \cap E) \setminus (A \cap E) $$
    $B \in \mathcal{D}_E \implies B \cap E \in l(\mathcal{P})$
    $A \in \mathcal{D}_E \implies A \cap E \in l(\mathcal{P})$
    $l(\mathcal{P})$는 $\lambda$-시스템이므로 차집합에 닫혀 있어, $(B \cap E) \setminus (A \cap E) \in l(\mathcal{P})$.
    따라서 $B \setminus A \in \mathcal{D}_E$.
3.  **서로소 합집합에 닫힘:** 서로소인 $B_1, B_2, \dots \in \mathcal{D}_E$에 대하여,
    $$ (\bigcup_{n} B_n) \cap E = \bigcup_{n} (B_n \cap E) $$
    각 $B_n \cap E \in l(\mathcal{P})$이고 서로소이므로, $l(\mathcal{P})$의 성질에 의해 그 합집합도 $l(\mathcal{P})$에 속함.
    따라서 $\bigcup B_n \in \mathcal{D}_E$.

**결론:** 모든 $E \in l(\mathcal{P})$에 대해 $\mathcal{D}_E$는 $\lambda$-시스템이다.

---

### Step 2: $\mathcal{P} \subset \mathcal{D}_X$ for all $X \in \mathcal{P}$
먼저 "기본 재료"인 $\mathcal{P}$의 원소들끼리의 교집합을 생각해보자.
임의의 $X \in \mathcal{P}$를 고정하자.
모든 $Y \in \mathcal{P}$에 대하여, $\mathcal{P}$는 $\pi$-시스템이므로 $X \cap Y \in \mathcal{P} \subset l(\mathcal{P})$이다.
즉, $Y \in \mathcal{D}_X$이다.
따라서 **$\mathcal{P} \subset \mathcal{D}_X$**이다.

여기서 중요한 확장을 한다.
$\mathcal{D}_X$는 $\mathcal{P}$를 포함하는 $\lambda$-시스템이다 (Step 1에 의해).
$l(\mathcal{P})$는 $\mathcal{P}$를 포함하는 *최소한의* $\lambda$-시스템이다.
따라서 **$l(\mathcal{P}) \subset \mathcal{D}_X$**이다.

이 결과의 의미:
$$ \forall X \in \mathcal{P}, \forall F \in l(\mathcal{P}) \implies X \cap F \in l(\mathcal{P}) $$
즉, **순서를 바꾸면 $X \in \mathcal{D}_F$이다.**

---

### Step 3: $l(\mathcal{P}) \subset \mathcal{D}_E$ for all $E \in l(\mathcal{P})$
이제 임의의 $E \in l(\mathcal{P})$를 고정하자.
Step 2의 결과에 의해, 모든 $X \in \mathcal{P}$에 대해 $X \in \mathcal{D}_E$가 성립한다. (왜냐하면 $X \cap E \in l(\mathcal{P})$니까).
따라서 **$\mathcal{P} \subset \mathcal{D}_E$**이다.

다시 논리를 적용한다.
$\mathcal{D}_E$는 $\mathcal{P}$를 포함하는 $\lambda$-시스템이다.
따라서 최소성에 의해 **$l(\mathcal{P}) \subset \mathcal{D}_E$**이다.

**최종 결론:**
임의의 $E \in l(\mathcal{P})$와 임의의 $F \in l(\mathcal{P})$에 대하여, $F \in \mathcal{D}_E$가 성립한다.
정의상 이는 $E \cap F \in l(\mathcal{P})$를 의미한다.
즉, **$l(\mathcal{P})$는 교집합에 대해 닫혀 있는 $\pi$-시스템이다.**

---

## 4. 참고: 용어 정의

### $\sigma$-유한 측도 ($\sigma$-finite measure)
측도 공간 $(\Omega, \mathcal{F}, m)$에서, 다음 조건을 만족하는 집합열 $\Omega_1, \Omega_2, \dots \in \mathcal{F}$이 존재하면 $m$을 $\sigma$-유한 측도라고 한다.
1.  $\bigcup_{n=1}^{\infty} \Omega_n = \Omega$ (전체를 덮음)
2.  $\forall n, m(\Omega_n) < \infty$ (각 조각은 유한함)

> **예시:** 르벡 측도 $\lambda$는 $\mathbb{R}$ 전체에서 무한대($\infty$)이지만, $\Omega_n = [-n, n]$으로 쪼개면 각 길이는 $2n$으로 유한하므로 $\sigma$-유한 측도이다.

---

## 5. 참고문헌

1.  **AP2025 10wk 강의노트**
    *   [https://guebin.github.io/AP2025/posts/10wk.html](https://guebin.github.io/AP2025/posts/10wk.html)
    *   딘킨의 $\pi$-$\lambda$ 정리 증명 과정을 인용 및 재구성하였습니다.
2.  **Probability and Measure (Billingsley)**
    *   $\pi$-$\lambda$ 정리의 표준 증명 방식을 참고하였습니다.
