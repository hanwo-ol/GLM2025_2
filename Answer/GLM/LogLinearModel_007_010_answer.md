---
title: "GLM Log-Linear Model Homework 7-10"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 7

$X_1 \sim \text{Poisson}(\lambda_1), \dots, X_k \sim \text{Poisson}(\lambda_k)$ 가 서로 독립인 확률변수라고 하자. 이때 조건부 분포 $P(X_1=x_1, \dots, X_k=x_k | X_1+\dots+X_k=n)$ 이 다항분포(Multinomial Distribution)를 따름을 보여라.
(참고: 문제 원문에는 조건부 변수가 $Y$로 표기되었으나 문맥상 $X$와 동일한 변수로 간주함)

## 풀이

독립인 포아송 확률변수들의 합 $S = \sum_{i=1}^k X_i$는 평균이 $\Lambda = \sum_{i=1}^k \lambda_i$ 인 포아송 분포를 따른다.
$$ S \sim \text{Poisson}(\Lambda) $$

조건부 확률 $P(X_1=x_1, \dots, X_k=x_k | S=n)$ 을 구하기 위해 결합 확률을 주변 확률로 나눈다.
여기서 $\sum x_i = n$ 이어야 확률이 0이 아니다.

$$ P(X_1=x_1, \dots, X_k=x_k | S=n) = \frac{P(X_1=x_1, \dots, X_k=x_k, S=n)}{P(S=n)} $$

분자 부분은 독립성에 의해 각 확률의 곱으로 표현된다 (단, $\sum x_i = n$).
$$ \text{분자} = P(X_1=x_1) \cdots P(X_k=x_k) = \left( \frac{e^{-\lambda_1} \lambda_1^{x_1}}{x_1!} \right) \cdots \left( \frac{e^{-\lambda_k} \lambda_k^{x_k}}{x_k!} \right) $$
$$ = \frac{e^{-\sum \lambda_i} \prod \lambda_i^{x_i}}{\prod x_i!} = \frac{e^{-\Lambda} \prod \lambda_i^{x_i}}{\prod x_i!} $$

분모 부분은 합의 분포이다.
$$ \text{분모} = \frac{e^{-\Lambda} \Lambda^n}{n!} $$

따라서 조건부 확률은:
$$ \frac{\frac{e^{-\Lambda} \prod \lambda_i^{x_i}}{\prod x_i!}}{\frac{e^{-\Lambda} \Lambda^n}{n!}} = \frac{n!}{\prod x_i!} \frac{\prod \lambda_i^{x_i}}{\Lambda^n} $$
$$ = \frac{n!}{x_1! \cdots x_k!} \prod_{i=1}^k \left( \frac{\lambda_i}{\Lambda} \right)^{x_i} $$

여기서 $p_i = \frac{\lambda_i}{\Lambda} = \frac{\lambda_i}{\sum \lambda_j}$ 라고 정의하면, $\sum p_i = 1$ 이다.
$$ = \frac{n!}{x_1! \cdots x_k!} p_1^{x_1} \cdots p_k^{x_k} $$

이는 시행 횟수 $n$, 각 범주의 성공 확률 $p_1, \dots, p_k$ 인 다항분포(Multinomial Distribution)의 확률질량함수와 일치한다.

---

# 문제 8

$X \sim U(0, \theta)$ 일 때, $X$의 관측값이 $x$라면 $\theta$의 우도함수(likelihood function)를 그리고 설명하라.

## 풀이

균일분포 $U(0, \theta)$의 확률밀도함수(PDF)는 다음과 같다.
$$ f(x; \theta) = \begin{cases} \frac{1}{\theta} & 0 \le x \le \theta \\ 0 & \text{otherwise} \end{cases} $$

단일 관측값 $x$가 주어졌을 때, $\theta$에 대한 우도함수 $L(\theta)$는 다음과 같다.
$$ L(\theta) = f(x; \theta) = \frac{1}{\theta} \cdot I(\theta \ge x) $$
(단, $\theta > 0$ 이며, 관측값 $x$는 0보다 크다고 가정)

**우도함수의 형태:**
1. $\theta < x$ 인 구간: $x$가 $\theta$ 범위 밖이므로 불가능한 사건이다. 따라서 $L(\theta) = 0$.
2. $\theta \ge x$ 인 구간: $L(\theta) = \frac{1}{\theta}$. 이는 $\theta$가 증가함에 따라 감소하는 함수이다.

**그래프 설명:**
- 가로축을 $\theta$, 세로축을 $L(\theta)$라 하자.
- $\theta$가 $x$보다 작은 구간에서는 $y=0$ 이다.
- $\theta = x$ 에서 $y = 1/x$ 로 점프(불연속)하며 최댓값을 가진다.
- $\theta > x$ 구간에서는 $y = 1/\theta$ 곡선을 따라 0으로 점근하며 감소한다.

따라서 $\theta$의 최대우도추정량(MLE)은 $\hat{\theta} = x$ 이다.

---

# 문제 9

$Y \sim B(n, \pi)$이고, 파라미터 공간이 이산적으로 $n \in \{2, 3\}$, $\pi \in \{1/2, 1/3\}$ 로 주어진다고 하자. (문제 원문의 깨진 문자를 통상적인 값인 1/2, 1/3로 해석함). 관측된 값 $y$에 따라 $(n, \pi)$의 최대우도추정량(MLE)을 결정하라.

## 풀이

가능한 파라미터 조합 $(\hat{n}, \hat{\pi})$은 총 4가지이다.
1. $(n=2, \pi=1/2)$
2. $(n=2, \pi=1/3)$
3. $(n=3, \pi=1/2)$
4. $(n=3, \pi=1/3)$

각 조합에 대해 관측값 $y$ (가능한 값: 0, 1, 2, 3)가 나올 우도(확률)를 계산하여 비교한다.
이항분포 확률: $P(Y=y) = \binom{n}{y} \pi^y (1-\pi)^{n-y}$

**1. y = 0 인 경우:**
- $n=2, \pi=1/2: (1/2)^2 = 1/4 = 0.25$
- $n=2, \pi=1/3: (2/3)^2 = 4/9 \approx \mathbf{0.444}$ (최대)
- $n=3, \pi=1/2: (1/2)^3 = 1/8 = 0.125$
- $n=3, \pi=1/3: (2/3)^3 = 8/27 \approx 0.296$
- **MLE:** $(\hat{n}, \hat{\pi}) = (2, 1/3)$

**2. y = 1 인 경우:**
- $n=2, \pi=1/2: 2(1/2)(1/2) = 1/2 = 0.5$
- $n=2, \pi=1/3: 2(1/3)(2/3) = 4/9 \approx 0.444$
- $n=3, \pi=1/2: 3(1/2)(1/2)^2 = 3/8 = 0.375$
- $n=3, \pi=1/3: 3(1/3)(2/3)^2 = 12/27 \approx 0.444$
- **MLE:** $(\hat{n}, \hat{\pi}) = (2, 1/2)$

**3. y = 2 인 경우:**
- $n=2, \pi=1/2: (1/2)^2 = 0.25$
- $n=2, \pi=1/3: (1/3)^2 = 1/9 \approx 0.111$
- $n=3, \pi=1/2: 3(1/2)^2(1/2) = 3/8 = \mathbf{0.375}$ (최대)
- $n=3, \pi=1/3: 3(1/3)^2(2/3) = 6/27 \approx 0.222$
- **MLE:** $(\hat{n}, \hat{\pi}) = (3, 1/2)$

**4. y = 3 인 경우:**
- $n=2$: 불가능 ($P=0$)
- $n=3, \pi=1/2: (1/2)^3 = 1/8 = 0.125$
- $n=3, \pi=1/3: (1/3)^3 = 1/27 \approx 0.037$
- **MLE:** $(\hat{n}, \hat{\pi}) = (3, 1/2)$

**결론 (요약):**
- $y=0 \implies (2, 1/3)$
- $y=1 \implies (2, 1/2)$
- $y=2 \implies (3, 1/2)$
- $y=3 \implies (3, 1/2)$

---

# 문제 10

$Y \sim B(n, \pi)$이고 $n$은 알려져 있을 때, 관측값 $Y=y$에 대한 $\pi$의 MLE를 구하라.

## 풀이

우도함수 $L(\pi)$는 다음과 같다 (상수항 제외).
$$ L(\pi) \propto \pi^y (1-\pi)^{n-y} $$

로그 우도함수 $l(\pi) = \log L(\pi)$는:
$$ l(\pi) = y \log \pi + (n-y) \log (1-\pi) + C $$

$\pi$에 대해 미분하여 0이 되는 점을 찾는다.
$$ \frac{dl}{d\pi} = \frac{y}{\pi} - \frac{n-y}{1-\pi} = 0 $$

양변에 $\pi(1-\pi)$를 곱하여 정리하면:
$$ y(1-\pi) - (n-y)\pi = 0 $$
$$ y - y\pi - n\pi + y\pi = 0 $$
$$ y - n\pi = 0 $$
$$ n\pi = y $$

따라서 최대우도추정량은:
$$ \hat{\pi} = \frac{y}{n} $$

2계 미분값 확인:
$$ \frac{d^2l}{d\pi^2} = -\frac{y}{\pi^2} - \frac{n-y}{(1-\pi)^2} < 0 $$
(모든 $0 < \pi < 1$에 대해 음수이므로 위로 볼록, 즉 최댓값임이 보장된다.)
