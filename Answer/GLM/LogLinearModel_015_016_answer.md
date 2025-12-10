---
title: "GLM Log-Linear Model Homework 15-16"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 15

기존의 최고 치료율은 0.3이다. 새로운 항암제를 $n=13$명의 환자에게 투여한 결과, $y=7$명이 완치되었다. 새로운 항암제가 기존보다 더 효과적인지 검정하라. (P-값과 mid-P 값을 모두 계산하라)

## 풀이

**가설 설정:**
- 귀무가설 $H_0: \pi = 0.3$
- 대립가설 $H_1: \pi > 0.3$ (우측 단측 검정)

**1. 정확 P-값 (Exact P-value):**
이항분포 $B(13, 0.3)$ 하에서 $Y \ge 7$일 확률을 구한다.
$$ P(Y \ge 7) = \sum_{k=7}^{13} \binom{13}{k} (0.3)^k (0.7)^{13-k} $$
$$ \approx 0.0624 $$

**해석:** 유의수준 0.05에서 P-값이 0.0624이므로 귀무가설을 기각할 수 없다. (효과가 있다고 단정하기 어렵다)

**2. Mid-P 값:**
이산형 분포의 불연속성을 보정하기 위한 방법으로, 관측된 값의 확률의 절반만을 포함한다.
$$ \text{mid-P} = \frac{1}{2} P(Y=7) + P(Y > 7) $$
$$ P(Y=7) \approx 0.0442 $$
$$ P(Y > 7) = P(Y \ge 8) \approx 0.0182 $$

$$ \text{mid-P} = 0.5 \times 0.0442 + 0.0182 = 0.0221 + 0.0182 = 0.0403 $$

**해석:** Mid-P 값은 0.0403으로 유의수준 0.05보다 작다. 이 기준으로는 새로운 항암제가 효과적일 가능성을 지지한다.

**결론:**
표본 수가 작아($n=13$) 검정력에 한계가 있으며, 사용하는 P-값의 정의에 따라 결론이 달라질 수 있는 경계선상의 결과이다. 더 많은 데이터 수집이 권장된다.

---

# 문제 16

$X_1, \dots, X_n \overset{i.i.d.}{\sim} N(\mu, \sigma_0^2)$ 이고 $\sigma_0$는 알려져 있을 때, 가설 $H_0: \mu = \mu_0$ vs $H_1: \mu \neq \mu_0$ 에 대한 Wald, Score, Likelihood Ratio 검정통계량을 구하라.

## 풀이

정규분포의 로그 우도함수(상수항 제외)는 다음과 같다.
$$ l(\mu) = -\frac{n}{2\sigma_0^2} (\bar{X} - \mu)^2 $$

최대우도추정량(MLE)은 $\hat{\mu} = \bar{X}$ 이며, 정보량(Fisher Information)은 $I(\mu) = \frac{n}{\sigma_0^2}$ 이다.

**1. Wald 검정통계량 ($W$):**
$$ W = (\hat{\mu} - \mu_0)^2 I(\hat{\mu}) = (\bar{X} - \mu_0)^2 \frac{n}{\sigma_0^2} = \left( \frac{\bar{X} - \mu_0}{\sigma_0 / \sqrt{n}} \right)^2 $$

**2. Score 검정통계량 ($S$):**
스코어 함수 $U(\mu) = \frac{\partial l}{\partial \mu} = \frac{n(\bar{X} - \mu)}{\sigma_0^2}$.
귀무가설 하에서 스코어 함수 값은 $U(\mu_0) = \frac{n(\bar{X} - \mu_0)}{\sigma_0^2}$.
$$ S = \frac{[U(\mu_0)]^2}{I(\mu_0)} = \frac{\left( \frac{n(\bar{X} - \mu_0)}{\sigma_0^2} \right)^2}{\frac{n}{\sigma_0^2}} = \frac{n^2 (\bar{X} - \mu_0)^2}{\sigma_0^4} \cdot \frac{\sigma_0^2}{n} = \frac{n(\bar{X} - \mu_0)^2}{\sigma_0^2} $$
$$ = \left( \frac{\bar{X} - \mu_0}{\sigma_0 / \sqrt{n}} \right)^2 $$

**3. 우도비 검정통계량 (Likelihood Ratio, $-2\log\Lambda$):**
$$ -2\log\Lambda = -2 (l(\mu_0) - l(\hat{\mu})) $$
$$ = -2 \left[ -\frac{n}{2\sigma_0^2} (\bar{X} - \mu_0)^2 - \left( -\frac{n}{2\sigma_0^2} (\bar{X} - \bar{X})^2 \right) \right] $$
(두 번째 항은 0이므로)
$$ = -2 \left[ -\frac{n}{2\sigma_0^2} (\bar{X} - \mu_0)^2 \right] = \frac{n(\bar{X} - \mu_0)^2}{\sigma_0^2} $$
$$ = \left( \frac{\bar{X} - \mu_0}{\sigma_0 / \sqrt{n}} \right)^2 $$

**결론:**
정규분포(분산 알려짐)의 평균에 대한 검정에서 Wald, Score, Likelihood Ratio 검정통계량은 모두 동일하며, 이는 $Z$-검정 통계량의 제곱과 같다.

---
**검증 코드 (Python)**

```python
from scipy.stats import binom

# 문제 15
n = 13
y = 7
pi_0 = 0.3

# Exact P-value: P(Y >= 7)
p_val_exact = 1 - binom.cdf(6, n, pi_0)
print(f"Exact P-value: {p_val_exact:.4f}")

# Mid-P value: 0.5 * P(Y=7) + P(Y>7)
prob_equal = binom.pmf(7, n, pi_0)
prob_greater = 1 - binom.cdf(7, n, pi_0)
mid_p = 0.5 * prob_equal + prob_greater
print(f"Mid-P value: {mid_p:.4f}")
```

**출력:**
```
Exact P-value: 0.0624
Mid-P value: 0.0403
```
