---
title: "GLM Log-Linear Model Homework 11-14"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 11

$Y_1, \dots, Y_n \overset{i.i.d.}{\sim} N(\mu, 1)$ 일 때, $\mu$의 최대우도추정량(MLE)을 구하라.

## 풀이

정규분포의 확률밀도함수(PDF)는 다음과 같다.
$$ f(y_i; \mu) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{(y_i - \mu)^2}{2} \right) $$

우도함수(Likelihood Function)는 결합확률밀도함수이다.
$$ L(\mu) = \prod_{i=1}^n f(y_i; \mu) = (2\pi)^{-n/2} \exp\left( -\frac{1}{2} \sum_{i=1}^n (y_i - \mu)^2 \right) $$

로그 우도함수(Log-Likelihood Function)는 다음과 같다.
$$ l(\mu) = \log L(\mu) = -\frac{n}{2} \log(2\pi) - \frac{1}{2} \sum_{i=1}^n (y_i - \mu)^2 $$

$\mu$에 대해 미분하여 0이 되는 점을 찾는다.
$$ \frac{dl}{d\mu} = - \frac{1}{2} \sum_{i=1}^n 2(y_i - \mu)(-1) = \sum_{i=1}^n (y_i - \mu) = 0 $$
$$ \sum_{i=1}^n y_i - n\mu = 0 $$
$$ n\mu = \sum_{i=1}^n y_i $$

따라서 최대우도추정량은 표본평균이다.
$$ \hat{\mu}_{MLE} = \frac{1}{n} \sum_{i=1}^n Y_i = \bar{Y} $$

---

# 문제 12

$Y_1, \dots, Y_n \overset{i.i.d.}{\sim} \text{Poisson}(\lambda)$ 일 때, $P(Y_1=0)$의 최대우도추정량(MLE)을 구하라.

## 풀이

먼저 $\lambda$의 MLE를 구한다.
포아송 분포의 확률질량함수는 $P(Y_i=y) = \frac{e^{-\lambda} \lambda^y}{y!}$ 이다.

로그 우도함수:
$$ l(\lambda) = \sum_{i=1}^n (y_i \log \lambda - \lambda - \log y_i!) = (\sum y_i) \log \lambda - n\lambda - \sum \log y_i! $$

미분하여 0이 되는 점:
$$ \frac{dl}{d\lambda} = \frac{\sum y_i}{\lambda} - n = 0 \implies \hat{\lambda}_{MLE} = \bar{Y} $$

우리가 구하고자 하는 것은 $\theta = P(Y_1=0) = e^{-\lambda}$ 의 MLE이다.
최대우도추정량의 **불변성(Invariance Property)**에 의해, 함수 $g(\lambda) = e^{-\lambda}$의 MLE는 $\lambda$의 MLE를 대입한 값과 같다.

따라서:
$$ \widehat{P(Y_1=0)}_{MLE} = e^{-\hat{\lambda}_{MLE}} = e^{-\bar{Y}} $$

---

# 문제 13

임신 중절(낙태) 합법화에 대한 설문조사 결과가 다음과 같다.
- 귀무가설 $H_0: \pi = 0.5$
- 대립가설 $H_1: \pi < 0.5$
- 시카고 대학 조사 결과: 응답자 $n=893$명 중 찬성 $y=400$명, 반대 493명.

어떤 결론을 내릴 수 있는가?

## 풀이

**1. 표본비율 계산:**
$$ \hat{p} = \frac{400}{893} \approx 0.4479 $$

**2. 검정통계량 (Z-score):**
귀무가설 하에서 모비율 $p_0 = 0.5$ 이므로 표준오차는 다음과 같다.
$$ SE_0 = \sqrt{\frac{p_0(1-p_0)}{n}} = \sqrt{\frac{0.5 \times 0.5}{893}} = \sqrt{\frac{0.25}{893}} \approx 0.01673 $$

$$ Z = \frac{\hat{p} - p_0}{SE_0} = \frac{0.4479 - 0.5}{0.01673} \approx -3.11 $$

**3. P-값 (P-value):**
대립가설이 $\pi < 0.5$ (단측 검정)이므로, $Z < -3.11$ 일 확률을 구한다.
$$ P(Z < -3.11) \approx 0.0009 $$

**4. 결론:**
P-값이 유의수준 0.05 (또는 0.01)보다 매우 작으므로 **귀무가설을 기각한다.**
즉, 낙태 합법화에 찬성하는 비율은 과반수(50%)보다 통계적으로 유의하게 낮다고 할 수 있다.

---

# 문제 14

지방자치제도에 대한 여론조사에서 500명 중 165명이 긍정적인 반응을 보였다. 전체 모집단에서 긍정적인 의견을 가진 사람의 비율에 대한 95% 신뢰구간을 구하라.
(문제에 제시된 통계량: $p=0.33$, $s.e.(p) \approx 0.012$ 라고 적혀있으나, 실제 계산된 표준오차는 약 0.021이다. 여기서는 직접 계산한 값을 사용한다.)

## 풀이

**1. 표본비율:**
$$ \hat{p} = \frac{165}{500} = 0.33 $$

**2. 표준오차 (Standard Error):**
$$ SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.33 \times 0.67}{500}} = \sqrt{\frac{0.2211}{500}} \approx 0.0210 $$

**3. 95% 신뢰구간:**
$$ \hat{p} \pm 1.96 \times SE $$
$$ 0.33 \pm 1.96 \times 0.0210 $$
$$ 0.33 \pm 0.0412 $$

$$ \text{CI} = [0.2888, 0.3712] $$

따라서 전체 모집단의 긍정적 의견 비율은 약 **28.9%에서 37.1% 사이**에 있을 것으로 95% 신뢰수준에서 추정된다.

---
**검증 코드 (Python)**

```python
import numpy as np
from scipy.stats import norm

# 문제 13
n_13 = 893
x_13 = 400
p_hat_13 = x_13 / n_13
p_0 = 0.5
se_0 = np.sqrt(p_0 * (1 - p_0) / n_13)
z_13 = (p_hat_13 - p_0) / se_0
p_val_13 = norm.cdf(z_13)

print(f"Prob 13: p_hat={p_hat_13:.4f}, z={z_13:.4f}, p-value={p_val_13:.4f}")

# 문제 14
n_14 = 500
x_14 = 165
p_hat_14 = x_14 / n_14
se_14 = np.sqrt(p_hat_14 * (1 - p_hat_14) / n_14)
ci_lower = p_hat_14 - 1.96 * se_14
ci_upper = p_hat_14 + 1.96 * se_14

print(f"Prob 14: p_hat={p_hat_14:.2f}, SE={se_14:.4f}")
print(f"Prob 14 CI: [{ci_lower:.4f}, {ci_upper:.4f}]")
```

**출력:**
```
Prob 13: p_hat=0.4479, z=-3.1121, p-value=0.0009
Prob 14: p_hat=0.33, SE=0.0210
Prob 14 CI: [0.2888, 0.3712]
```
