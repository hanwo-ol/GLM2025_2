---
title: "GLM Log-Linear Model Homework 4-6"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 4

$I \times J$ 분할표에 대한 포아송 로그선형모형(독립성 모형)이 다음과 같다고 하자.
$$ \log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y $$

(1) $\log(\mu_{ij} / \mu_{ik}) = \lambda_j^Y - \lambda_k^Y$ 임을 증명하라.
(2) 만약 모든 $\lambda_j^Y = 0$ 이라면, $\pi_{j|i} = 1/J$ 임을 보여라.
*(참고: 문제 원문의 수식이 깨져 있으나, 문맥상 위와 같은 표준적인 성질을 묻는 것으로 해석됨)*

## 풀이

### (1) 증명
로그선형모형 식에 따라 셀 기대도수 $\mu_{ij}$는 다음과 같다.
$$ \log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y $$
$$ \log \mu_{ik} = \lambda + \lambda_i^X + \lambda_k^Y $$

두 식을 빼면:
$$ \log \mu_{ij} - \log \mu_{ik} = (\lambda + \lambda_i^X + \lambda_j^Y) - (\lambda + \lambda_i^X + \lambda_k^Y) $$
공통된 항($\lambda, \lambda_i^X$)은 소거되므로:
$$ \log \left( \frac{\mu_{ij}}{\mu_{ik}} \right) = \lambda_j^Y - \lambda_k^Y $$

이는 같은 행($i$) 내에서 두 열($j, k$) 간의 기대도수 비율(로그 값)이 열 효과 파라미터($\lambda^Y$)의 차이로만 결정됨을 보여준다.

### (2) 증명
만약 모든 $j$에 대해 $\lambda_j^Y = 0$ 이라면, 모형은 다음과 같이 단순화된다.
$$ \log \mu_{ij} = \lambda + \lambda_i^X $$
즉, $\mu_{ij} = \exp(\lambda + \lambda_i^X)$ 이며, 이는 $j$에 의존하지 않는 상수이다. 편의상 이를 $C_i$라 하자.

행 $i$가 주어졌을 때 열 $j$에 속할 조건부 확률 $\pi_{j|i}$는 다음과 같다.
$$ \pi_{j|i} = \frac{\mu_{ij}}{\sum_{k=1}^J \mu_{ik}} $$

모든 $\mu_{ik}$가 $C_i$로 동일하므로:
$$ \pi_{j|i} = \frac{C_i}{\sum_{k=1}^J C_i} = \frac{C_i}{J \times C_i} = \frac{1}{J} $$

따라서, 열 효과가 없으면($\lambda_j^Y = 0$) 각 행에서의 조건부 분포는 균등분포(Uniform Distribution)를 따른다.

---

# 문제 5

어떤 지역의 사고 통계에 따르면, 평균 부상 사고(Injury accidents) 건수는 1건, 평균 비부상 사고(Non-injury accidents) 건수는 3건이다. 총 10건의 사고가 발생했을 때, 그중 2건이 부상 사고일 확률은 얼마인가?

## 풀이

두 사고 발생 건수를 각각 확률변수 $X_1$ (부상), $X_2$ (비부상)라 하자.
문제의 조건에 따라 $X_1, X_2$는 서로 독립인 포아송 분포를 따른다고 가정한다.
- $X_1 \sim \text{Poisson}(\lambda_1 = 1)$
- $X_2 \sim \text{Poisson}(\lambda_2 = 3)$

구하고자 하는 것은 총 사고 건수($X_1 + X_2$)가 10일 때, 부상 사고($X_1$)가 2건일 조건부 확률 $P(X_1 = 2 | X_1 + X_2 = 10)$이다.

**이론:**
서로 독립인 포아송 확률변수들의 합 $S = X_1 + X_2$가 주어졌을 때, $X_1$의 조건부 분포는 이항분포를 따른다.
$$ X_1 | (X_1 + X_2 = n) \sim \text{Binomial}(n, p) $$
여기서 성공 확률 $p$는 다음과 같다.
$$ p = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{1}{1 + 3} = 0.25 $$

**계산:**
$n = 10, p = 0.25$ 인 이항분포에서 $X_1 = 2$ 일 확률을 구한다.
$$ P(X_1 = 2) = \binom{10}{2} (0.25)^2 (0.75)^8 $$
$$ = 45 \times 0.0625 \times 0.1001129... $$
$$ \approx \mathbf{0.2816} $$

따라서 약 **28.16%**이다.

---

# 문제 6

평균적으로 코드 500줄당 1개의 버그가 발생한다고 한다. 어떤 프로그래머가 각각 300줄짜리 프로그램 5개를 작성했다면, 총 버그 수가 2개 이하일 확률은 얼마인가?

## 풀이

**파라미터 설정:**
- 단위 버그 발생률: $\lambda_{unit} = \frac{1}{500}$ (버그/줄)
- 총 코드 라인 수: $L = 300 \times 5 = 1500$ (줄)

총 버그 수 $Y$는 포아송 분포를 따르며, 그 평균($\lambda_{total}$)은 다음과 같다.
$$ \lambda_{total} = \lambda_{unit} \times L = \frac{1}{500} \times 1500 = 3 $$
즉, $Y \sim \text{Poisson}(3)$.

**확률 계산:**
구하고자 하는 확률은 $P(Y \le 2)$이다.
$$ P(Y \le 2) = P(Y=0) + P(Y=1) + P(Y=2) $$
포아송 확률질량함수 $P(Y=k) = \frac{e^{-\lambda} \lambda^k}{k!}$ 를 이용한다 ($\lambda=3$).

1. $P(Y=0) = \frac{e^{-3} 3^0}{0!} = e^{-3} \approx 0.0498$
2. $P(Y=1) = \frac{e^{-3} 3^1}{1!} = 3 e^{-3} \approx 0.1494$
3. $P(Y=2) = \frac{e^{-3} 3^2}{2!} = \frac{9}{2} e^{-3} = 4.5 e^{-3} \approx 0.2240$

**합계:**
$$ P(Y \le 2) = e^{-3} (1 + 3 + 4.5) = 8.5 e^{-3} $$
$$ \approx 8.5 \times 0.049787 $$
$$ \approx \mathbf{0.4232} $$

따라서 약 **42.32%**이다.

---
**검증 코드 (Python)**

```python
from scipy.stats import binom, poisson

# 문제 5
# Binomial(n=10, p=0.25), k=2
p5 = binom.pmf(2, 10, 0.25)
print(f"Problem 5: {p5:.4f}")

# 문제 6
# Poisson(lambda=3), k<=2
p6 = poisson.cdf(2, 3)
print(f"Problem 6: {p6:.4f}")
```

**출력:**
```
Problem 5: 0.2816
Problem 6: 0.4232
```
