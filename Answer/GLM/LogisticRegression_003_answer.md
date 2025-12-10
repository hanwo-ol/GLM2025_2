---
title: "GLM Logistic Regression Homework 3"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 3

낙태 합법화에 대한 개인의 의견($Y$, 1=찬성)을 성별($h$), 종교($i$), 정당($j$)에 따라 분석한 로지스틱 회귀모형 결과가 다음과 같다.

$$ \text{logit}[P(Y=1)] = \alpha + \beta^G_h + \beta^R_i + \beta^P_j $$

보고된 모수 추정값은 다음과 같다. (Sum-to-zero 제약조건 사용)
- **절편:** $\alpha = 0.62$
- **성별 (G):** $\beta^G_1 = 0.08$ (여성), $\beta^G_2 = -0.08$ (남성)
- **종교 (R):** $\beta^R_1 = -0.16$ (개신교), $\beta^R_2 = -0.25$ (가톨릭), $\beta^R_3 = 0.41$ (유대교)
- **정당 (P):** $\beta^P_1 = 0.87$ (민주당), $\beta^P_2 = -1.27$ (공화당), $\beta^P_3 = 0.40$ (무소속)

a. 종교에 따라 찬성 오즈(odds)가 어떻게 달라지는지 해석하라.
b. 현재 법률을 찬성할 확률이 가장 높은 그룹과 가장 낮은 그룹의 확률을 추정하라.
c. 만약 제약조건을 $\beta^G_1 = \beta^R_1 = \beta^P_1 = 0$ (첫 번째 레벨을 기준)으로 변경한다면 추정값은 어떻게 변하는가?

## 풀이

### a. 종교에 따른 찬성 오즈의 해석

다른 변수들이 동일할 때, 종교 간의 오즈비(Odds Ratio)를 통해 효과를 비교할 수 있다. 오즈비는 $\exp(\beta^R_A - \beta^R_B)$로 계산된다.

1.  **유대교 vs 개신교:**
    $$ OR_{J vs P} = \exp(0.41 - (-0.16)) = \exp(0.57) \approx \mathbf{1.77} $$
    유대교인은 개신교인에 비해 찬성할 오즈가 약 1.77배 높다.

2.  **유대교 vs 가톨릭:**
    $$ OR_{J vs C} = \exp(0.41 - (-0.25)) = \exp(0.66) \approx \mathbf{1.93} $$
    유대교인은 가톨릭교인에 비해 찬성할 오즈가 약 1.93배 높다.

3.  **개신교 vs 가톨릭:**
    $$ OR_{P vs C} = \exp(-0.16 - (-0.25)) = \exp(0.09) \approx \mathbf{1.09} $$
    개신교인은 가톨릭교인에 비해 찬성할 오즈가 약 1.09배 높다 (큰 차이 없음).

**결론:** 유대교 신자들이 낙태 합법화에 찬성할 성향이 가장 강하며, 가톨릭 신자들이 가장 약하다.

### b. 찬성 확률이 가장 높은/낮은 그룹 추정

확률 $P(Y=1) = \frac{1}{1 + e^{-\eta}}$이므로, 선형 예측자 $\eta$가 최대일 때 확률이 가장 높고, 최소일 때 가장 낮다.

$$ \eta = \alpha + \beta^G_h + \beta^R_i + \beta^P_j $$

**1. 가장 높은 확률 (Most Likely):**
각 범주에서 가장 큰 계수를 선택한다.
- 성별: 여성 ($\beta^G_1 = 0.08$)
- 종교: 유대교 ($\beta^R_3 = 0.41$)
- 정당: 민주당 ($\beta^P_1 = 0.87$)

$$ \eta_{max} = 0.62 + 0.08 + 0.41 + 0.87 = 1.98 $$
$$ \hat{\pi}_{max} = \frac{e^{1.98}}{1 + e^{1.98}} \approx \mathbf{0.879} \text{ (87.9\%)} $$
(그룹: 여성, 유대교, 민주당원)

**2. 가장 낮은 확률 (Least Likely):**
각 범주에서 가장 작은 계수를 선택한다.
- 성별: 남성 ($\beta^G_2 = -0.08$)
- 종교: 가톨릭 ($\beta^R_2 = -0.25$)
- 정당: 공화당 ($\beta^P_2 = -1.27$)

$$ \eta_{min} = 0.62 - 0.08 - 0.25 - 1.27 = -0.98 $$
$$ \hat{\pi}_{min} = \frac{e^{-0.98}}{1 + e^{-0.98}} \approx \mathbf{0.273} \text{ (27.3\%)} $$
(그룹: 남성, 가톨릭, 공화당원)

### c. 제약조건 변경 ($\beta^G_1 = \beta^R_1 = \beta^P_1 = 0$) 시 추정값

기존 모형(Sum-to-zero)과 새로운 모형(Corner-point, 첫 번째 레벨 기준)은 동일한 예측값을 주어야 한다.
새로운 파라미터를 $\alpha^*, \beta^*$라고 하자. 기준 레벨(1)에 대해 계수가 0이 되어야 하므로, 기존 모수에서 각 변수의 첫 번째 레벨 계수($\beta^X_1$)를 빼주는 방식으로 변환된다. 절편은 그만큼 더해진다.

$$ \beta^{*X}_k = \beta^X_k - \beta^X_1 $$
$$ \alpha^* = \alpha + \beta^G_1 + \beta^R_1 + \beta^P_1 $$

**계산:**

1.  **새로운 절편 ($\alpha^*$):**
    $$ \alpha^* = 0.62 + 0.08 + (-0.16) + 0.87 = \mathbf{1.41} $$

2.  **성별 (기준: 여성):**
    - $\beta^{*G}_1 = 0.08 - 0.08 = 0$
    - $\beta^{*G}_2 = -0.08 - 0.08 = \mathbf{-0.16}$ (남성)

3.  **종교 (기준: 개신교):**
    - $\beta^{*R}_1 = -0.16 - (-0.16) = 0$
    - $\beta^{*R}_2 = -0.25 - (-0.16) = \mathbf{-0.09}$ (가톨릭)
    - $\beta^{*R}_3 = 0.41 - (-0.16) = \mathbf{0.57}$ (유대교)

4.  **정당 (기준: 민주당):**
    - $\beta^{*P}_1 = 0.87 - 0.87 = 0$
    - $\beta^{*P}_2 = -1.27 - 0.87 = \mathbf{-2.14}$ (공화당)
    - $\beta^{*P}_3 = 0.40 - 0.87 = \mathbf{-0.47}$ (무소속)

**결과 요약:**
- $\alpha = 1.41$
- 성별: $0, -0.16$
- 종교: $0, -0.09, 0.57$
- 정당: $0, -2.14, -0.47$

---
**검증 코드 (R)**

이 문제는 데이터 적합이 아닌 모수 변환 문제이므로, R을 사용하여 대수적 검증을 수행할 수 있다.

```r
# Original Parameters
alpha <- 0.62
bg <- c(0.08, -0.08)       # Female, Male
br <- c(-0.16, -0.25, 0.41)# Prot, Cath, Jew
bp <- c(0.87, -1.27, 0.40) # Dem, Rep, Ind

# Task a: Odds Ratios
cat(sprintf("OR Jew/Prot: %.4f\n", exp(br[3] - br[1])))
cat(sprintf("OR Jew/Cath: %.4f\n", exp(br[3] - br[2])))

# Task b: Probabilities
eta_max <- alpha + max(bg) + max(br) + max(bp)
eta_min <- alpha + min(bg) + min(br) + min(bp)
cat(sprintf("Max Prob: %.4f\n", plogis(eta_max)))
cat(sprintf("Min Prob: %.4f\n", plogis(eta_min)))

# Task c: Parameter Transformation
alpha_new <- alpha + bg[1] + br[1] + bp[1]
bg_new <- bg - bg[1]
br_new <- br - br[1]
bp_new <- bp - bp[1]

cat("\nNew Parameters:\n")
cat(sprintf("Alpha: %.2f\n", alpha_new))
cat("Gender:", bg_new, "\n")
cat("Religion:", br_new, "\n")
cat("Party:", bp_new, "\n")
```
