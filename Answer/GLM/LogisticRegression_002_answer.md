---
title: "GLM Logistic Regression Homework 2"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 2

Hastie and Tibshirani (1990)는 척추 교정 수술 후 심각한 척추 전만증(kyphosis) 발생의 위험 요인을 결정하기 위한 연구를 기술하였다. 수술 당시의 나이(개월) 데이터는 다음과 같다.

- **Kyphosis 존재 (Y=1, 18명):** 12, 15, 42, 52, 59, 73, 82, 91, 96, 105, 114, 120, 121, 128, 130, 139, 139, 157
- **Kyphosis 없음 (Y=0, 22명):** 1, 1, 2, 8, 11, 18, 22, 31, 37, 61, 72, 81, 97, 112, 118, 127, 131, 140, 151, 159, 177, 206

a. 나이(Age)를 예측 변수로 하여 로지스틱 회귀 모형을 적합하라. 나이가 유의한 효과를 가지는지 검정하라.
b. 데이터를 시각화하라(Plot). Kyphosis 유무에 따른 나이 분포의 차이(산포 등)를 기술하라.
c. $logit[\pi(x)] = \alpha + \beta_1 x + \beta_2 x^2$ 모형을 적합하라. 제곱항($x^2$)의 유의성을 검정하고, 적합된 모형을 시각화 및 해석하라.

## 풀이

### a. 로지스틱 회귀 모형 적합 (Linear Term)

나이($x$)에 대한 선형 로지스틱 회귀 모형은 다음과 같다.

$$ \text{logit}[\pi(x)] = \alpha + \beta x $$

R을 사용하여 모형을 적합한 결과는 다음과 같다.

- **절편 ($\hat{\alpha}$):** -0.573 (SE: 0.602, p-value: 0.342)
- **나이 계수 ($\hat{\beta}$):** 0.0043 (SE: 0.0058, p-value: 0.463)

**유의성 검정:**
나이의 계수 $\hat{\beta}$에 대한 Wald 검정 결과 p-value가 **0.463**으로 유의수준 0.05보다 훨씬 크다. 따라서 **나이는 Kyphosis 발생 여부를 설명하는 데 통계적으로 유의한 선형 효과를 가지지 않는다.**

### b. 데이터 시각화 및 분포 해석

데이터의 분포를 살펴보면 다음과 같은 특징이 있다.

- **Kyphosis 없음(Y=0):** 매우 어린 나이(1개월)부터 고령(206개월)까지 **넓게 퍼져 있다**.
- **Kyphosis 존재(Y=1):** 주로 **중간 나이대(12~157개월)**에 몰려 있으며, 아주 어리거나 아주 나이가 많은 환자는 적다.

이러한 분포의 차이(Y=1 그룹이 중간에 밀집됨)는 나이와 발병 확률 간에 단순한 선형 관계가 아닌, **비선형(곡선) 관계**가 존재할 가능성을 시사한다. 즉, 너무 어리거나 나이가 많으면 위험이 낮고, 특정 중간 나이대에서 위험이 높은 형태일 수 있다.

### c. 2차항(Quadratic Term) 포함 모형 적합

나이의 제곱항($x^2$)을 포함한 모형은 다음과 같다.

$$ \text{logit}[\pi(x)] = \alpha + \beta_1 x + \beta_2 x^2 $$

적합 결과는 다음과 같다.

- **절편 ($\hat{\alpha}$):** -2.046 (p-value: 0.040)
- **나이 ($\hat{\beta}_1$):** 0.0600 (p-value: 0.025)
- **나이 제곱 ($\hat{\beta}_2$):** -0.000328 (p-value: 0.036)

**제곱항의 유의성 검정:**
$\hat{\beta}_2$에 대한 Wald 검정 p-value는 **0.036**으로 유의수준 0.05에서 유의하다. 또한, 선형 모형과 비교한 우도비 검정(LRT) 결과도 $\chi^2 = 6.276, p = 0.012$로 2차항 추가가 통계적으로 유의함을 보여준다.

**해석:**
$\hat{\beta}_2 < 0$ (음수)이므로, 이 모형은 **역 U자형(Inverted U-shape)** 곡선을 그린다.
이는 나이가 증가함에 따라 Kyphosis 발생 확률이 증가하다가, 특정 시점을 지나면 다시 감소함을 의미한다.

**최대 위험 나이 계산:**
확률이 최대가 되는 나이는 선형 예측자의 미분값이 0이 되는 지점이다.
$$ \frac{\partial}{\partial x} (\hat{\alpha} + \hat{\beta}_1 x + \hat{\beta}_2 x^2) = \hat{\beta}_1 + 2\hat{\beta}_2 x = 0 $$
$$ x_{peak} = -\frac{\hat{\beta}_1}{2\hat{\beta}_2} = -\frac{0.0600}{2(-0.000328)} \approx \mathbf{91.5 \text{개월}} $$

따라서, 생후 약 91.5개월(약 7~8세) 무렵에 척추 교정 수술 후 Kyphosis가 발생할 위험이 가장 높다.

---
**검증 코드 (R)**

```r
# Data Entry
present <- c(12, 15, 42, 52, 59, 73, 82, 91, 96, 105, 114, 120, 121, 128, 130, 139, 139, 157)
absent <- c(1, 1, 2, 8, 11, 18, 22, 31, 37, 61, 72, 81, 97, 112, 118, 127, 131, 140, 151, 159, 177, 206)
data <- data.frame(kyphosis = c(rep(1, length(present)), rep(0, length(absent))),
                   age = c(present, absent))

# Part a: Linear Model
model_a <- glm(kyphosis ~ age, family = binomial, data = data)
print(summary(model_a))

# Part c: Quadratic Model
data$age2 <- data$age^2
model_c <- glm(kyphosis ~ age + age2, family = binomial, data = data)
print(summary(model_c))

# LRT for Quadratic Term
lrt_stat <- model_a$deviance - model_c$deviance
p_val <- pchisq(lrt_stat, df=1, lower.tail=FALSE)
cat(sprintf("LRT Statistic: %.4f, P-value: %.4f\n", lrt_stat, p_val))
```
