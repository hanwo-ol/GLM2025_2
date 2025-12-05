# 10. MLE of Binomial Proportion

## 문제 (English)
If $Y \sim B(n, \pi)$ and we observe $Y=y$ with known $n$, find the MLE of $\pi$.

---

## 해설 (Korean)

### 10.1 우도함수 설정

이항분포의 확률질량함수는 다음과 같습니다.
$$ f(y; \pi) = \binom{n}{y} \pi^y (1-\pi)^{n-y} $$
여기서 $n$과 $y$는 상수이고, $\pi$가 변수입니다.
우도함수 $L(\pi)$는 다음과 같습니다.
$$ L(\pi) \propto \pi^y (1-\pi)^{n-y} $$

### 10.2 로그우도함수 미분

계산의 편의를 위해 로그를 취합니다.
$$ \ell(\pi) = \log L(\pi) = y \log \pi + (n-y) \log (1-\pi) + C $$
(여기서 $C$는 $\pi$와 무관한 상수항 $\log \binom{n}{y}$ 입니다.)

$\pi$에 대해 미분합니다 (Score Function).
$$ \frac{d \ell}{d \pi} = \frac{y}{\pi} - \frac{n-y}{1-\pi} $$

### 10.3 최적화 (MLE 도출)

미분값이 0이 되는 지점 $\hat{\pi}$를 찾습니다.
$$ \frac{y}{\hat{\pi}} - \frac{n-y}{1-\hat{\pi}} = 0 $$
$$ \frac{y}{\hat{\pi}} = \frac{n-y}{1-\hat{\pi}} $$
$$ y(1-\hat{\pi}) = \hat{\pi}(n-y) $$
$$ y - y\hat{\pi} = n\hat{\pi} - y\hat{\pi} $$
$$ n\hat{\pi} = y $$
$$ \hat{\pi} = \frac{y}{n} $$

**이계도함수 판정 (Second Derivative Test):**
$$ \frac{d^2 \ell}{d \pi^2} = -\frac{y}{\pi^2} - \frac{n-y}{(1-\pi)^2} $$
모든 $y \in [0, n]$에 대해 이 값은 항상 음수($<0$)이므로, 구한 해는 극대값이자 최대값입니다.

**답:** $\hat{\pi}_{MLE} = \frac{y}{n}$ (표본 비율)

---

## 심화 학습 (Deep Understanding)

### 1. 경계값(Boundary) 문제
만약 $y=0$이거나 $y=n$인 경우, 미분 방정식의 해가 $\pi=0$ 또는 $\pi=1$이 되어 로그 항이 정의되지 않을 수 있습니다. 하지만 극한값 관점에서 접근하거나, 원래의 우도함수 $\pi^y (1-\pi)^{n-y}$를 직접 고려하면 경계값에서도 $L(\pi)$가 최대화됨을 알 수 있습니다.
- $y=0 \implies L(\pi) = (1-\pi)^n$ (감소함수) $\to$ Max at $\pi=0$.
- $y=n \implies L(\pi) = \pi^n$ (증가함수) $\to$ Max at $\pi=1$.

### 2. 불편성(Unbiasedness)과 효율성(Efficiency)
이 추정량 $\hat{\pi} = Y/n$은 불편추정량($E[\hat{\pi}] = \pi$)이며, 크라메르-라오 하한(Cramer-Rao Lower Bound)을 달성하는 유효추정량(Efficient Estimator)입니다. 또한 지수족(Exponential Family)의 성질에 따라 충분통계량의 평균과 일치합니다.
