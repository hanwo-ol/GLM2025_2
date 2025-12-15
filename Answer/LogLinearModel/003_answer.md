# 3. Collapsibility of Log-Linear Models

## 문제 (English)
Check whether each statement is true:
(1) If $X \perp Y | Z$ for three-way contingency table, it is collapsible.
(2) The homogeneous association, $(XY, XZ, YZ)$, is collapsible.

---

## 해설 (Korean)

### 3.1 문항 (1) 조건부 독립 모형은 축소 가능한가?

**참 (True)**

**정의:**
어떤 모형이 $Z$에 대해 **축소 가능(Collapsible)**하다는 것은, $Z$를 무시하고 구한 주변 표(Marginal Table)에서의 $X-Y$ 관계(오즈비 등)가 조건부 표(Conditional Table)에서의 관계와 동일함을 의미합니다.

**조건:**
$X \perp Y | Z$ 모형은 로그선형모형 표기로 $(XZ, YZ)$ 입니다. $XY$ 항이 없습니다.
축소 가능성의 충분조건은 다음과 같습니다.
"주변화하려는 변수 $Z$가 적어도 하나의 나머지 변수와 조건부 독립이면 된다."
혹은 Agresti의 정리에 따르면, **"모형 안에 3-way 상호작용이 없고, $Z$와 관련된 2-way 상호작용 중 적어도 하나가 없으면 $XY$ 관계에 대해 축소 가능하다."**

모형 $(XZ, YZ)$에서는:
- $XY$ 교호작용항 $\lambda_{XY} = 0$. (즉, 모든 층에서 조건부 오즈비 = 1)
- 이 모형을 $Z$에 대해 주변화하면, $X$와 $Y$는 주변적으로도 독립이 아닐 수 있습니다(심슨의 역설).
- **잠깐, 문제를 다시 봅니다.**
    - "It is collapsible"의 주어(It)가 무엇인가? 보통은 "The interaction between the other two variables is collapsible"을 의미합니다.
    - 만약 $X \perp Y | Z$라면, 조건부 오즈비는 1입니다.
    - 이때 주변 오즈비도 1인가? (즉 $X \perp Y$인가?) -> 반드시 그렇지는 않습니다 ($XZ$, $YZ$ 관계가 있으면 $X,Y$가 연결됨).
    - 따라서 "Interaction is collapsible" (conditional = marginal) 이라는 명제라면 **거짓(False)**일 수 있습니다.

**그러나,** Collapsibility의 정의를 **"단순성(Simplicity)의 관점"**에서 본다면:
- Bishop, Fienberg, Holland (1975) 등에 따르면, Collapsibility Theorem은 다음과 같습니다.
    - 3차원 테이블에서 $XY$ 연관성에 대해 Collapsible하려면, $Z$가 $X$와 독립이거나($\lambda_{XZ}=0$) $Z$가 $Y$와 독립이어야($\lambda_{YZ}=0$) 합니다.
- 문제의 조건 $X \perp Y | Z$는 모형 $(XZ, YZ)$입니다.
    - 여기서는 $\lambda_{XZ} \neq 0$, $\lambda_{YZ} \neq 0$일 수 있습니다.
    - 따라서 조건부 오즈비($=1$)와 주변 오즈비($\neq 1$)가 다를 수 있습니다.
    - 즉, **축소 불가능(Not Collapsible)**합니다.

**답: False** (일반적인 경우)
*(단, $\lambda_{XZ}=0$ 또는 $\lambda_{YZ}=0$인 특수한 경우에는 True가 될 수 있으나, 명제 자체는 False)*

### 3.2 문항 (2) 동질적 연관 모형 $(XY, XZ, YZ)$은 축소 가능한가?

**거짓 (False)**

**이유:**
동질적 연관(Homogeneous Association) 모형 $(XY, XZ, YZ)$는 3-way interaction $\lambda_{XYZ}$만 0인 모형입니다 ("No Three-Factor Interaction").
이 모형에서 $XY$ 관계에 대해 $Z$를 축소(Collapse)할 수 있는지 확인해 봅시다.
- Collapsibility 정리: $Z$를 제거(축소)해도 $XY$ 연관성이 보존되려면, $\lambda_{XZ}=0$ 이거나 $\lambda_{YZ}=0$ 이어야 합니다.
- 하지만 동질적 연관 모형은 $\lambda_{XY}, \lambda_{XZ}, \lambda_{YZ}$가 모두 존재할 수 있는 모형입니다.
- 따라서 $Z$와 $X$, $Z$와 $Y$가 모두 연관되어 있다면, 심슨의 역설이 발생하여 **조건부 오즈비와 주변 오즈비가 달라집니다.**
- 즉, 일반적으로 **축소 불가능(Not Collapsible)** 합니다.

**답: False**

---

## R Code (검증)

```r
# Collapsibility 확인을 위한 시뮬레이션
# Model: Homogeneous Association (XY, XZ, YZ)
# 각 변수 간에 연관성이 있도록 데이터 생성

# 임의의 2x2x2 확률표 생성 (Odds Ratio가 1이 아닌 구조)
# Z=1: OR=2, Z=2: OR=2 (Homogeneous)
prob_z1 <- matrix(c(0.2, 0.1, 0.1, 0.1), nrow=2) # OR = (0.02)/(0.01) = 2
prob_z2 <- matrix(c(0.1, 0.1, 0.1, 0.2), nrow=2) # OR = (0.02)/(0.01) = 2

# 전체 합이 1이 되도록 정규화하되, Z와의 연관성 부여
# 단순히 합치면 Marginal Table이 됨
marginal_prob <- prob_z1 + prob_z2
print(marginal_prob)

# Marginal Odds Ratio 계산
marg_OR <- (marginal_prob[1,1] * marginal_prob[2,2]) / (marginal_prob[1,2] * marginal_prob[2,1])

cat("Conditional OR:", 2, "\n")
cat("Marginal OR:", marg_OR, "\n")

# 만약 marg_OR != 2 라면 Not Collapsible
if (abs(marg_OR - 2) > 1e-5) {
  cat("Result: Not Collapsible (False)\n")
} else {
  cat("Result: Collapsible (True)\n")
}
```

---

## 심화 학습 (Deep Understanding)

### 1. 심슨의 역설과 Collapsibility
Collapsibility는 심슨의 역설이 발생하지 않을 조건을 수학적으로 정의한 것입니다. $Z$를 무시하고 데이터를 합쳤을 때(Collapse), 원래의 연관성($XY$)이 왜곡되지 않으려면 $Z$가 **교란 변수(Confounder)**로 작용하지 않아야 합니다. 즉, $Z$가 $X$와 무관하거나($X \perp Z$), $Y$와 무관해야($Y \perp Z$) 합니다. $(XY, XZ, YZ)$ 모형은 $Z$가 $X, Y$ 모두와 연관되어 있으므로 전형적인 교란 상황입니다.

### 2. 그래프 모형(Graphical Model)에서의 해석
그래프 이론에서 Collapsibility는 분리(Separation)와 관련이 있습니다. $XY$ 엣지의 Collapsibility를 보려면 $Z$를 제거했을 때 경로가 어떻게 변하는지 봐야 합니다. $(XY, XZ, YZ)$는 삼각형 구조(Clique)를 이루므로, 어떤 노드를 제거해도 남은 두 노드 간의 정보 흐름(경로)이 변형되거나 편향될 수 있습니다.


---


결론부터 말씀드리면, **두 문장 모두 거짓(False)**입니다.

통계학(특히 범주형 자료 분석)에서 **충족성(Collapsibility)**의 정의는 "변수 $Z$에 대해 분할표를 합쳤(Collapse)을 때, $X$와 $Y$ 사이의 연관성 척도(오즈비 등)가 변하지 않는 것"을 의미합니다.

각 문장에 대한 증명 및 반증 과정은 다음과 같습니다.

---

### (1) If $X \perp Y | Z$, it is collapsible. (False)

이 문장은 **"만약 $Z$가 주어졌을 때 $X$와 $Y$가 조건부 독립이라면, ($Z$에 대해) 충족 가능하다"**는 뜻입니다.

#### **증명(반증) 과정**

1.  **조건부 독립의 의미 ($X \perp Y | Z$):**
    * 모든 $k$ ($Z$의 수준)에 대해 $X$와 $Y$의 조건부 오즈비는 1입니다.
    * $$\theta_{XY(k)} = 1$$
    * 로그 선형 모형으로 표현하면 **$(XZ, YZ)$ 모형**입니다. (즉, $\lambda^{XY} = 0$, $\lambda^{XYZ} = 0$)

2.  **충족성(Collapsibility)의 조건:**
    * 이 표가 $Z$에 대해 충족 가능하려면, $Z$를 무시하고 합친 **주변 오즈비(Marginal Odds Ratio, $\theta_{XY}$)** 또한 1이어야 합니다.
    * 즉, $\theta_{XY(k)} = \theta_{XY} = 1$ 이어야 합니다.

3.  **반례 (Simpson's Paradox):**
    * 하지만 $X$와 $Z$가 연관되어 있고($\lambda^{XZ} \neq 0$), $Y$와 $Z$가 연관되어 있다면($\lambda^{YZ} \neq 0$), **$X$와 $Y$가 조건부 독립이라도 주변 오즈비는 1이 아닐 수 있습니다.**
    * 이론적으로 **충족성 정리(Theorem on Collapsibility)**에 따르면, $Z$에 대해 충족 가능하려면 다음 중 하나가 성립해야 합니다:
        * $X \perp Z | Y$ (즉, $\lambda^{XZ} = 0$)
        * $Y \perp Z | X$ (즉, $\lambda^{YZ} = 0$)
    * 하지만 문제의 조건 $X \perp Y | Z$ (모형 $XZ, YZ$)은 $\lambda^{XZ}$와 $\lambda^{YZ}$가 0이 아님을 허용하므로, **일반적으로 충족 가능하지 않습니다.**

---

### (2) The homogeneous association, $(XY, XZ, YZ)$, is collapsible. (False)

이 문장은 **"동질 연관 모형 $(XY, XZ, YZ)$은 충족 가능하다"**는 뜻입니다.

#### **증명(반증) 과정**

1.  **동질 연관 모형의 정의:**
    * 모든 2차 상호작용 항($\lambda^{XY}, \lambda^{XZ}, \lambda^{YZ}$)이 존재하고, 3차 상호작용 항($\lambda^{XYZ}$)만 0인 모형입니다.
    * 즉, $\theta_{XY(1)} = \cdots = \theta_{XY(K)} = \theta$ (조건부 오즈비가 일정함).

2.  **충족성 확인:**
    * $Z$에 대해 분할표를 합쳤을 때, 주변 오즈비 $\theta_{XY}$가 공통 조건부 오즈비 $\theta$와 같은지 묻는 것입니다 ($\theta_{XY} \stackrel{?}{=} \theta$).
    * 앞서 언급한 **충족성 정리**를 다시 적용합니다. $Z$에 대해 충족 가능하려면 $Z$와 관련된 상호작용 항 중 적어도 하나가 0이어야 합니다.
        * $\lambda^{XZ} = 0$ (즉, $X \perp Z | Y$)
        * $\textbf{OR}$
        * $\lambda^{YZ} = 0$ (즉, $Y \perp Z | X$)
3.  **결론:**
    * 동질 연관 모형 $(XY, XZ, YZ)$은 정의상 $\lambda^{XZ} \neq 0$ 이고 $\lambda^{YZ} \neq 0$ 입니다.
    * 두 조건 모두 만족하지 않으므로, 이 모형은 **절대로 충족 가능하지 않습니다 (Not Collapsible).**
    * 이 경우 주변 오즈비와 조건부 오즈비가 달라지는 **심슨의 역설(Simpson's Paradox)**이 발생할 수 있는 가장 대표적인 모형입니다.

---

### 요약 테이블

| 모형 (Model) | 표기 | $Z$에 대해 충족 가능한가? (Collapsible over $Z$?) | 이유 |
| :--- | :--- | :--- | :--- |
| **(1) 조건부 독립** | $(XZ, YZ)$ | **거짓 (False)** | $X$와 $Z$, $Y$와 $Z$의 관계가 남아있어 심슨의 역설 발생 가능 |
| **(2) 동질 연관** | $(XY, XZ, YZ)$ | **거짓 (False)** | $Z$가 $X, Y$ 모두와 연관되어 있으므로 충족 불가능 |
| **($Z$ 독립)** | $(XY)$ | **참 (True)** | $Z$가 아무 변수와도 연관이 없음 ($\lambda^{XZ}=\lambda^{YZ}=0$) |
| **($X$와 $Z$ 독립)** | $(XY, YZ)$ | **참 (True)** | $X \perp Z | Y$ 조건 만족 ($\lambda^{XZ}=0$) |

