---
title: "GLM Logistic Regression Homework 1"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 1

Labeling Index (LI)는 환자에게 tritiated thymidine을 투여한 후 측정되는 세포 활동의 지표이다. 다음 표는 다양한 LI 값에 대해 암 수술을 받은 환자 수(Cases)와 회복된 환자 수(Remissions; 1 = Yes)를 보여준다. 이 데이터를 사용하여 암 수술 후 회복 여부와 LI 간의 관계를 알아보기 위해 로지스틱 회귀분석을 수행하라.

**Data Summary**

| LI | Cases ($n_i$) | Remissions ($y_i$) |
|:---:|:---:|:---:|
| 8 | 2 | 0 |
| 10 | 2 | 0 |
| 12 | 3 | 0 |
| 14 | 3 | 0 |
| 16 | 3 | 0 |
| 18 | 1 | 1 |
| 20 | 3 | 2 |
| 22 | 2 | 1 |
| 24 | 1 | 0 |
| 26 | 1 | 1 |
| 28 | 1 | 1 |
| 32 | 1 | 0 |
| 34 | 1 | 1 |
| 38 | 3 | 2 |

a. LI = 8과 LI = 26인 환자에 대해 추정된 회복 확률($\hat{\pi}$)과 95% 신뢰구간을 구하라.
b. LI = 8과 LI = 26일 때 $\hat{\pi}$의 변화율(rate of change)을 계산하라.
c. LI의 효과에 대한 오즈비(Odds Ratio)의 95% 신뢰구간을 구하라.
d. LI의 효과에 대한 우도비 검정(Likelihood Ratio Test)을 수행하기 위해, 귀무가설 하에서의 우도와 대립가설 하에서의 우도를 구하고 검정을 수행하라.

## 풀이

### 로지스틱 회귀모형 적합

회복 확률을 $\pi(x)$라고 할 때, 로지스틱 회귀모형은 다음과 같다.

$$ \text{logit}[\pi(x)] = \log\left(\frac{\pi(x)}{1-\pi(x)}\right) = \alpha + \beta x $$

여기서 $x$는 LI 값이다.
최대우도추정법(MLE)을 통해 추정된 회귀계수는 다음과 같다.

- $\hat{\alpha} = -3.7771$ (Standard Error: 1.379)
- $\hat{\beta} = 0.1449$ (Standard Error: 0.059)

따라서 추정된 로짓 함수는:

$$ \text{logit}[\hat{\pi}(x)] = -3.7771 + 0.1449 x $$

### a. 회복 확률 $\hat{\pi}$ 및 95% 신뢰구간 추정

특정 $x$ 값에서의 추정 확률 $\hat{\pi}(x)$는 다음과 같다.

$$ \hat{\pi}(x) = \frac{\exp(\hat{\alpha} + \hat{\beta}x)}{1 + \exp(\hat{\alpha} + \hat{\beta}x)} $$

신뢰구간은 선형 예측자 $\hat{\eta} = \hat{\alpha} + \hat{\beta}x$에 대한 신뢰구간을 구한 후, 이를 다시 확률 스케일로 변환하여 구한다.
$\text{Var}(\hat{\eta}) = \text{Var}(\hat{\alpha}) + x^2 \text{Var}(\hat{\beta}) + 2x \text{Cov}(\hat{\alpha}, \hat{\beta})$

**(1) LI = 8 일 때**
- 선형 예측자: $\hat{\eta} = -3.7771 + 0.1449(8) \approx -2.618$
- 추정 확률: $\hat{\pi} = \frac{e^{-2.618}}{1 + e^{-2.618}} \approx \mathbf{0.0680}$ (6.8%)
- 95% 신뢰구간: $\mathbf{[0.0112, 0.3193]}$

**(2) LI = 26 일 때**
- 선형 예측자: $\hat{\eta} = -3.7771 + 0.1449(26) \approx -0.011$
- 추정 확률: $\hat{\pi} = \frac{e^{-0.011}}{1 + e^{-0.011}} \approx \mathbf{0.4973}$ (49.7%)
- 95% 신뢰구간: $\mathbf{[0.2521, 0.7438]}$

### b. $\hat{\pi}$의 변화율 (Rate of Change)

로지스틱 곡선에서의 순간 변화율(기울기)은 다음과 같이 계산된다.

$$ \frac{\partial \pi(x)}{\partial x} = \beta \pi(x) (1 - \pi(x)) $$

**(1) LI = 8 일 때**
$$ \text{Rate} = 0.1449 \times 0.0680 \times (1 - 0.0680) \approx \mathbf{0.0092} $$
즉, LI가 8일 때 LI가 1단위 증가하면 회복 확률은 약 0.9% 증가한다.

**(2) LI = 26 일 때**
$$ \text{Rate} = 0.1449 \times 0.4973 \times (1 - 0.4973) \approx \mathbf{0.0362} $$
즉, LI가 26일 때 LI가 1단위 증가하면 회복 확률은 약 3.6% 증가한다. (확률이 0.5 근처일 때 변화율이 가장 크다)

### c. LI 효과에 대한 오즈비(Odds Ratio)의 95% 신뢰구간

LI에 대한 오즈비 추정값은 $\exp(\hat{\beta})$이다.

$$ \widehat{OR} = \exp(0.1449) \approx \mathbf{1.156} $$

95% 신뢰구간은 $\exp(\hat{\beta} \pm 1.96 \times SE(\hat{\beta}))$로 구한다.
$SE(\hat{\beta}) \approx 0.059$

$$ \text{CI} = \exp(0.1449 \pm 1.96 \times 0.059) = [\exp(0.029), \exp(0.261)] $$
$$ \text{95\% CI} = \mathbf{[1.029, 1.299]} $$

신뢰구간이 1을 포함하지 않으므로 LI의 효과는 유의하다.

### d. 우도비 검정 (Likelihood Ratio Test)

귀무가설 $H_0: \beta = 0$ (LI는 회복에 영향이 없다) vs 대립가설 $H_1: \beta \neq 0$.

1.  **귀무가설 하에서의 로그 우도 ($L_0$):**
    상수항만 있는 모형($\text{logit}(\pi) = \alpha$)의 로그 우도이다.
    $$ \log L_0 \approx -14.296 $$

2.  **대립가설 하에서의 로그 우도 ($L_1$):**
    적합된 로지스틱 모형의 로그 우도이다.
    $$ \log L_1 \approx -10.146 $$

3.  **검정통계량 ($G^2$):**
    $$ G^2 = -2 (\log L_0 - \log L_1) = -2 (-14.296 - (-10.146)) $$
    $$ G^2 = -2 (-4.15) = \mathbf{8.299} $$

4.  **검정 결과:**
    검정통계량 $G^2$는 자유도 1인 카이제곱 분포를 따른다 ($\chi^2_1$).
    유의수준 $\alpha=0.05$에서 기각역은 $\chi^2_{1, 0.95} = 3.84$이다.
    $8.299 > 3.84$ 이므로 귀무가설을 기각한다.

    **P-값:** $P(\chi^2_1 > 8.299) \approx \mathbf{0.004}$

    **결론:** LI 변수는 회복 확률을 설명하는 데 통계적으로 유의한 기여를 한다.

---
**검증 코드 (R)**

이 솔루션은 R을 사용하여 검증되었습니다. 사용된 R 코드와 출력 결과는 다음과 같습니다.

```r
# Data Entry
LI <- c(8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 34, 38)
Cases <- c(2, 2, 3, 3, 3, 1, 3, 2, 1, 1, 1, 1, 1, 3)
Remissions <- c(0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 1, 2)
Failures <- Cases - Remissions

# Create DataFrame
data <- data.frame(LI, Cases, Remissions, Failures)

# Fit Logistic Regression Model (GLM)
model <- glm(cbind(Remissions, Failures) ~ LI, family = binomial(link = "logit"), data = data)

# ---------------------------------------------------------
# Coefficients
# ---------------------------------------------------------
print(coef(model))

# ---------------------------------------------------------
# Part a: Probability and 95% CI
# ---------------------------------------------------------
new_data <- data.frame(LI = c(8, 26))
preds <- predict(model, newdata = new_data, type = "link", se.fit = TRUE)
lower_logit <- preds$fit - 1.96 * preds$se.fit
upper_logit <- preds$fit + 1.96 * preds$se.fit
prob_est <- plogis(preds$fit)
lower_prob <- plogis(lower_logit)
upper_prob <- plogis(upper_logit)
print(data.frame(LI=new_data$LI, Prob=prob_est, Lower=lower_prob, Upper=upper_prob))

# ---------------------------------------------------------
# Part c: Odds Ratio and 95% CI
# ---------------------------------------------------------
beta <- coef(model)["LI"]
se_beta <- summary(model)$coefficients["LI", "Std. Error"]
or_est <- exp(beta)
or_ci <- exp(beta + c(-1, 1) * 1.96 * se_beta)
print(c(OR=or_est, CI=or_ci))

# ---------------------------------------------------------
# Part d: Likelihood Ratio Test
# ---------------------------------------------------------
null_model <- glm(cbind(Remissions, Failures) ~ 1, family = binomial(link = "logit"), data = data)
lrt_stat <- -2 * (as.numeric(logLik(null_model)) - as.numeric(logLik(model)))
p_val_lrt <- pchisq(lrt_stat, df = 1, lower.tail = FALSE)
print(c(LRT_Stat=lrt_stat, P_Value=p_val_lrt))
```

**R 출력 결과 요약:**

```
Coefficients:
(Intercept)           LI
 -3.7771402    0.1448632

Part a (Probabilities):
  LI      Prob      Lower     Upper
1  8 0.0680155 0.01124483 0.3193427
2 26 0.4972580 0.25208643 0.7437887

Part c (Odds Ratio):
      OR.LI     CI1     CI2
1.155883 1.029019 1.298380

Part d (LRT):
   LRT_Stat     P_Value
8.298835848 0.003966922
```
