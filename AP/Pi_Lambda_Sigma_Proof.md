# 파이시스템($\pi$-system)이면서 람다시스템($\lambda$-system)이면 시그마 필드($\sigma$-field)이다

이 문서는 측도론의 중요한 정리 중 하나인 **"어떤 집합족이 $\pi$-시스템이면서 동시에 $\lambda$-시스템(Dynkin System)이라면, 그 집합족은 시그마 필드이다"**라는 명제에 대한 증명입니다. 이 정리는 딘킨의 $\pi$-$\lambda$ 정리(Dynkin's $\pi$-$\lambda$ Theorem)를 증명하는 핵심 단계로 사용됩니다.

---

## 1. 정의 (Definitions)

증명에 앞서 필요한 개념들을 정의합니다. 전체 집합을 $\Omega$, 그 부분집합들의 모임을 $\mathcal{P}$라고 합시다.

### 1.1. 파이시스템 ($\pi$-system)
집합족 $\mathcal{P}$가 **유한 교집합(Finite Intersection)**에 대해 닫혀 있으면 $\pi$-시스템이라고 합니다.
$$ A, B \in \mathcal{P} \implies A \cap B \in \mathcal{P} $$

### 1.2. 람다시스템 ($\lambda$-system)
집합족 $\mathcal{L}$이 다음 세 가지 조건을 만족하면 $\lambda$-시스템(또는 딘킨 시스템)이라고 합니다.
1.  **전체 집합 포함:** $\Omega \in \mathcal{L}$
2.  **여집합에 대해 닫힘 (또는 차집합 성질):** $A, B \in \mathcal{L}$이고 $A \subset B$이면, $B \setminus A \in \mathcal{L}$.
    *   (참고: $\Omega \in \mathcal{L}$ 조건과 결합하면, $A \in \mathcal{L} \implies A^c = \Omega \setminus A \in \mathcal{L}$ 임을 알 수 있습니다.)
3.  **서로소인 가산 합집합에 대해 닫힘 (Disjoint Countable Union):**
    $A_1, A_2, \dots \in \mathcal{L}$이고 서로소($A_i \cap A_j = \emptyset, i \neq j$)이면, $\bigcup_{n=1}^{\infty} A_n \in \mathcal{L}$.

### 1.3. 시그마 필드 ($\sigma$-field)
집합족 $\mathcal{F}$가 다음 세 가지 조건을 만족하면 시그마 필드입니다.
1.  $\Omega \in \mathcal{F}$
2.  $A \in \mathcal{F} \implies A^c \in \mathcal{F}$
3.  **가산 합집합에 대해 닫힘 (Countable Union):** (서로소가 아니어도 됨)
    $A_1, A_2, \dots \in \mathcal{F} \implies \bigcup_{n=1}^{\infty} A_n \in \mathcal{F}$

---

## 2. 정리 (Theorem)

> 집합족 $\mathcal{P}$가 $\pi$-시스템이면서 동시에 $\lambda$-시스템이라면, $\mathcal{P}$는 시그마 필드이다.

---

## 3. 증명 (Proof)

$\mathcal{P}$가 시그마 필드의 3가지 조건을 만족함을 순서대로 보이면 됩니다.

### Step 1: 전체 집합과 여집합 조건 확인
$\mathcal{P}$는 $\lambda$-시스템이므로 정의에 의해 다음을 만족합니다.
1.  $\Omega \in \mathcal{P}$ (만족)
2.  $A \in \mathcal{P} \implies A^c = \Omega \setminus A \in \mathcal{P}$ (만족)

이제 남은 것은 **Step 3: 일반적인 가산 합집합(General Countable Union)**에 대해 닫혀 있음을 보이는 것입니다.

### Step 2: 유한 합집합(Finite Union)에 대해 닫혀 있음을 증명
$\lambda$-시스템은 *서로소*인 경우에만 합집합을 허용하므로, 서로소가 아닌 경우($A \cup B$)를 처리해야 합니다. 드모르간 법칙을 사용합니다.

두 집합 $A, B \in \mathcal{P}$를 생각합시다.
1.  $\mathcal{P}$는 여집합에 대해 닫혀 있으므로 ($A^c \in \mathcal{P}$, $B^c \in \mathcal{P}$).
2.  $\mathcal{P}$는 $\pi$-시스템이므로 교집합에 대해 닫혀 있습니다.
    $$ A^c \cap B^c \in \mathcal{P} $$
3.  다시 여집합을 취하면, 드모르간의 법칙에 의해 합집합이 됩니다.
    $$ (A^c \cap B^c)^c = A \cup B $$
    $\mathcal{P}$는 여집합에 대해 닫혀 있으므로, $A \cup B \in \mathcal{P}$입니다.

즉, **$\mathcal{P}$는 유한 합집합에 대해 닫혀 있습니다.**

### Step 3: 가산 합집합(Countable Union)에 대해 닫혀 있음을 증명
임의의 수열 $A_1, A_2, \dots \in \mathcal{P}$에 대해 $ \bigcup_{n=1}^{\infty} A_n \in \mathcal{P} $임을 보여야 합니다.
이 집합들은 서로소가 아닐 수 있으므로, **서로소인 집합들로 변환(Disjointification)**하는 과정을 거칩니다.

새로운 집합열 $E_n$을 다음과 같이 정의합니다.
*   $E_1 = A_1$
*   $E_2 = A_2 \setminus A_1 = A_2 \cap A_1^c$
*   $E_3 = A_3 \setminus (A_1 \cup A_2) = A_3 \cap (A_1 \cup A_2)^c$
*   ...
*   $E_n = A_n \setminus \left( \bigcup_{k=1}^{n-1} A_k \right) = A_n \cap \left( \bigcup_{k=1}^{n-1} A_k \right)^c$

여기서 $E_n \in \mathcal{P}$인지 확인해 봅시다.
1.  앞선 Step 2에 의해, 유한 합집합 $F_{n-1} = \bigcup_{k=1}^{n-1} A_k$는 $\mathcal{P}$에 속합니다.
2.  $\mathcal{P}$는 여집합에 닫혀 있으므로 $F_{n-1}^c \in \mathcal{P}$입니다.
3.  $\mathcal{P}$는 $\pi$-시스템(교집합)에 닫혀 있으므로, $E_n = A_n \cap F_{n-1}^c \in \mathcal{P}$입니다.

이제 $E_n$들은 구조적으로 서로소(disjoint)이며, 그 합집합은 원래의 합집합과 같습니다.
$$ \bigcup_{n=1}^{\infty} E_n = \bigcup_{n=1}^{\infty} A_n $$

$E_n \in \mathcal{P}$이고 서로소이므로, **$\lambda$-시스템의 성질(서로소인 가산 합집합)**에 의해:
$$ \bigcup_{n=1}^{\infty} E_n \in \mathcal{P} $$
따라서,
$$ \bigcup_{n=1}^{\infty} A_n \in \mathcal{P} $$

### 결론 (Conclusion)
$\mathcal{P}$는 전체 집합을 포함하고, 여집합에 닫혀 있으며, 일반적인 가산 합집합에도 닫혀 있으므로 **시그마 필드($\sigma$-field)**입니다.

---

## 4. 참고문헌

1.  **Dynkin system** - Wikipedia
    *   [https://en.wikipedia.org/wiki/Dynkin_system](https://en.wikipedia.org/wiki/Dynkin_system)
    *   Dynkin system과 $\pi$-system의 관계에 대한 정리를 참고하였습니다.
2.  **Billingsley, P. (1995). Probability and Measure.**
    *   확률론 교재의 표준적인 증명 방식을 참고하였습니다.
