---
title: "GLM Log-Linear Model Homework 1-3"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 1

다음 각 명제가 참인지 거짓인지 판별하라.

(1) $X, Y, Z$: 상호 독립 (Mutual Independence) $\implies$ 결합 독립 (Joint Independence)
(2) $Y \perp (X, Z)$ (결합 독립) $\implies$ $X \perp Y|Z$ 그리고 $Y \perp Z|X$
(3) $X \perp Y|Z$ 그리고 $Y \perp Z|X$ $\implies$ $X \perp Y$ 그리고 $Y \perp Z$

## 풀이

### (1) 참 (True)
상호 독립(Mutual Independence)이란 결합 확률질량함수가 각 주변 확률질량함수의 곱으로 표현되는 것을 의미한다.
$$ P(X, Y, Z) = P(X)P(Y)P(Z) $$
결합 독립(Joint Independence), 예를 들어 $Y \perp (X, Z)$는 다음을 의미한다.
$$ P(X, Y, Z) = P(Y)P(X, Z) $$
만약 상호 독립이라면 $P(X, Z) = P(X)P(Z)$이므로,
$$ P(X, Y, Z) = P(Y)[P(X)P(Z)] = P(Y)P(X, Z) $$
가 성립한다. 따라서 상호 독립이면 임의의 변수 조합에 대한 결합 독립이 성립한다.

### (2) 참 (True)
전제 조건 $Y \perp (X, Z)$는 $P(Y|X, Z) = P(Y)$를 의미한다.
조건부 독립 $X \perp Y|Z$의 정의는 $P(Y|X, Z) = P(Y|Z)$이다.
$Y$가 $(X, Z)$와 독립이면 $Y$는 $Z$와도 주변 독립($Y \perp Z$)이므로 $P(Y|Z) = P(Y)$이다.
따라서 $P(Y|X, Z) = P(Y) = P(Y|Z)$가 되어 $X \perp Y|Z$가 성립한다.
마찬가지로 $Y \perp Z|X$도 성립한다.

### (3) 거짓 (False)
조건부 독립이 성립한다고 해서 주변 독립(Marginal Independence)이 보장되지는 않는다.
예를 들어, $X$와 $Z$가 독립적인 동전 던지기이고, $Y = X \text{ XOR } Z$ (또는 $Y = X + Z \pmod 2$)라고 하자.
$Z$가 주어졌을 때 $X$와 $Y$는 결정적인 관계(함수 관계)를 가지므로 독립이 아닐 수 있지만, 구조에 따라 조건부 독립을 만족하는 반례를 구성할 수 있다.
더 일반적인 반례로 **Simpson's Paradox**와 관련된 구조를 들 수 있다. $X \perp Y|Z$ (층별 오즈비=1)이라도 $Z$가 교란변수로 작용하면 $X \not\perp Y$ (주변 오즈비 $\neq 1$)일 수 있다.
즉, 3원 상호작용이 없거나 조건부 독립이라도, 주변 연관성은 층화 변수($Z$)의 분포에 따라 달라진다.

---

# 문제 2

만약 $\theta_{XY(1)} = \cdots = \theta_{XY(K)}$ (동질성 연관, Homogeneous Association)라면, $\log \theta_{XY(k)} = \lambda_{11}^{XY} + \lambda_{22}^{XY} - \lambda_{12}^{XY} - \lambda_{21}^{XY}$ 임을 증명하라. (단, $2 \times 2 \times K$ 테이블 가정)

*참고: 문제 원문의 수식이 깨져 보이나, 문맥상 동질성 연관 하에서 로그 오즈비와 로그선형모형 파라미터 간의 관계를 묻는 문제로 해석됨.*

## 풀이

로그선형모형(Log-Linear Model)에서 셀 기대도수 $\mu_{ijk}$에 대한 모형($XY, XZ, YZ$ 상호작용 포함, 3원 상호작용 없음)은 다음과 같다.

$$ \log \mu_{ijk} = \lambda + \lambda_i^X + \lambda_j^Y + \lambda_k^Z + \lambda_{ij}^{XY} + \lambda_{ik}^{XZ} + \lambda_{jk}^{YZ} $$

$k$층(Level $k$ of $Z$)에서의 $X, Y$ 간의 조건부 오즈비 $\theta_{XY(k)}$는 다음과 같이 정의된다.

$$ \theta_{XY(k)} = \frac{\mu_{11k} \mu_{22k}}{\mu_{12k} \mu_{21k}} $$

양변에 로그를 취하면 로그 오즈비는 다음과 같다.

$$ \log \theta_{XY(k)} = \log \mu_{11k} + \log \mu_{22k} - \log \mu_{12k} - \log \mu_{21k} $$

로그선형모형 식을 대입하면, $i, j$에 의존하지 않는 항($\lambda, \lambda_k^Z$)과 $k$에만 의존하는 항($\lambda_{ik}^{XZ}, \lambda_{jk}^{YZ}$)들은 상쇄되어 사라진다.

구체적으로:
- $\lambda, \lambda_k^Z$: 4개 항 모두에 공통으로 들어있어 (+2, -2) 상쇄됨.
- $\lambda_i^X$: $(i=1)$인 항($\mu_{11k}, \mu_{12k}$)과 $(i=2)$인 항($\mu_{21k}, \mu_{22k}$)에서 각각 상쇄.
- $\lambda_k^{XZ}, \lambda_k^{YZ}$: 각 $i, j$ 조합에 대해 뺄셈으로 상쇄.

남는 항은 $\lambda_{ij}^{XY}$ 항들뿐이다.

$$ \log \theta_{XY(k)} = (\lambda_{11}^{XY} + \lambda_{22}^{XY}) - (\lambda_{12}^{XY} + \lambda_{21}^{XY}) $$
$$ \log \theta_{XY(k)} = \lambda_{11}^{XY} + \lambda_{22}^{XY} - \lambda_{12}^{XY} - \lambda_{21}^{XY} $$

이 식은 $k$에 의존하지 않으므로, 모든 층 $k$에 대해 오즈비가 동일하다($\theta_{XY(1)} = \cdots = \theta_{XY(K)}$)는 동질성 연관 가정을 만족함을 보여준다.

만약 Sum-to-zero 제약조건($\sum_i \lambda_{ij} = \sum_j \lambda_{ij} = 0$)을 사용한다면, $\lambda_{11} = \lambda_{22} = -\lambda_{12} = -\lambda_{21} = \lambda^*$ 이므로 $\log \theta = 4\lambda^*$가 된다.

---

# 문제 3

다음 각 명제가 참인지 거짓인지 확인하라.

(1) 3원 분할표에서 $X \perp Y|Z$ 이면, $XY$ 관계에 대해 분할성(Collapsibility)이 성립한다.
(2) 동질성 연관 모형 $(XY, XZ, YZ)$은 분할적(Collapsible)이다.

## 풀이

### (1) 참 (True)
분할성(Collapsibility)이란 $Z$를 무시하고 구한 주변(Marginal) 오즈비가 조건부(Conditional) 오즈비와 동일한 성질을 말한다.
$X \perp Y|Z$ 라는 것은 모든 층 $k$에서 조건부 오즈비 $\theta_{XY(k)} = 1$ (독립)임을 의미한다.
만약 $Z$에 대해 합(Summing over)하여 구한 주변 테이블에서도 $X$와 $Y$가 독립($\theta_{XY} = 1$)이라면 분할성이 성립한다.
일반적으로 **$XY$ 관계에 대해 분할성이 성립하기 위한 충분조건**은 다음 중 하나가 성립하는 것이다.
1. $X \perp Z | Y$ (즉, $XZ$ 연관성 없음)
2. $Y \perp Z | X$ (즉, $YZ$ 연관성 없음)

그러나 문제의 조건인 $X \perp Y|Z$는 $\lambda_{XY}=0$을 의미한다. 즉 조건부 오즈비가 1이다.
이 경우, $Z$가 교란변수로 작용하여 주변 오즈비가 1이 아닐 수 있다(Simpson's Paradox). 따라서 $X \perp Y|Z$ 만으로는 주변 독립($X \perp Y$)을 보장하지 않는다.
따라서 엄밀히 말하면 **거짓(False)**이다. 조건부 독립이라고 해서 반드시 주변 독립이 성립하는 것은 아니므로(즉, 주변 오즈비 $\neq$ 조건부 오즈비), "분할성이 성립한다(주변=조건부)"는 명제는 항상 참은 아니다.

*보충 설명:* 분할성의 정의를 "조건부 연관성이 주변 연관성과 동일하다"로 본다면, 조건부는 '독립(OR=1)'인데 주변은 '연관(OR!=1)'일 수 있으므로 분할적이지 않다.

### (2) 거짓 (False)
동질성 연관 모형(Homogeneous Association, No 3-factor interaction)은 모든 층에서 오즈비가 동일함($\theta_{XY(1)} = \cdots = \theta_{XY(K)}$)을 의미한다.
하지만 이것이 주변 오즈비(Marginal Odds Ratio)가 조건부 오즈비와 같다는 것(Collapsibility)을 의미하지는 않는다.
분할성이 성립하려면, 위에서 언급했듯이 3원 상호작용이 없을 뿐만 아니라, 적어도 하나의 2원 상호작용($XZ$ 또는 $YZ$)이 없어야 한다.
단순히 모든 2원 상호작용($XY, XZ, YZ$)이 존재하는 동질성 연관 모형에서는 일반적으로 분할성이 성립하지 않는다. (즉, $\theta_{XY, \text{marginal}} \neq \theta_{XY, \text{conditional}}$).
