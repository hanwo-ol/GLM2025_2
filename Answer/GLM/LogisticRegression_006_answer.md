---
title: "GLM Logistic Regression Homework 6"
author: "Jules"
date: "2025-02-18"
format:
  html:
    code-fold: true
---

# 문제 6

다음 표는 비전이성 골육종(nonmetastatic osteosarcoma) 연구 결과로, 3년 무병 생존(Disease-Free) 여부를 나타낸다. (A. M. Goorin et al., 1987).

| Lymphocytic Infiltration (LI) | Gender | Pathology (Osteoblastic) | Disease-Free (Yes) | Disease-Free (No) |
|---|---|---|---|---|
| High | Female | No | 3 | 0 |
| | | Yes | 2 | 0 |
| | Male | No | 4 | 0 |
| | | Yes | 1 | 0 |
| Low | Female | No | 5 | 0 |
| | | Yes | 3 | 2 |
| | Male | No | 5 | 4 |
| | | Yes | 6 | 11 |

a. 다른 변수 없이 각 예측 변수(LI, Gender, Pathology)를 개별적으로 사용했을 때, 각 변수가 유의한 효과를 가짐을 보여라.
b. 세 예측 변수를 모두 포함하는 주효과 로지스틱 회귀 모형을 적합해 보아라. 림프구 침윤(LI) 효과에 대한 ML 추정값이 무한대가 되는 이유를 설명하라.
c. 조건부 로지스틱 회귀(Conditional Logistic Regression)를 사용하여, (i) 다른 변수들을 통제한 상태에서 림프구 침윤(LI) 효과에 대한 정확 검정(Exact Test)을 수행하고, (ii) 효과에 대한 95% 신뢰구간을 구하라. 결과를 해석하라.

## 풀이

### a. 각 예측 변수의 개별 유의성 검정

각 변수에 대해 단변량 로지스틱 회귀 모형을 적합하고, 우도비 검정(Likelihood Ratio Test, LRT)을 수행하였다.

1.  **LI (High vs Low):**
    - High 그룹은 10명 모두 생존(Yes), Low 그룹은 19명 생존, 17명 사망.
    - LRT P-value: **0.0010** (< 0.05) → 유의함.

2.  **Gender (Male vs Female):**
    - LRT P-value: **0.0153** (< 0.05) → 유의함.

3.  **Pathology (Yes vs No):**
    - LRT P-value: **0.0186** (< 0.05) → 유의함.

따라서 세 변수 모두 개별적으로는 생존 여부에 유의한 영향을 미친다.

### b. 주효과 모형 적합 및 ML 추정값 무한대 원인

세 변수(LI, Gender, Pathology)를 모두 포함하여 로지스틱 회귀를 수행하면 LI High에 대한 계수 추정값이 매우 크게(사실상 무한대로) 나타난다.

**이유 (Complete Separation):**
데이터를 살펴보면 **LI가 High인 모든 환자(10명)가 Disease-Free=Yes**이다.
즉, LI=High라는 조건만 있으면 생존 여부를 완벽하게 예측할 수 있다.
$$ P(Y=1 | LI=\text{High}) = 1 \implies \text{logit}(\pi) \to \infty $$
이러한 **완전 분리(Complete Separation)** 현상 때문에 최대우도추정량(MLE)이 존재하지 않고(무한대로 발산), 표준오차 또한 매우 크게 추정되어 Wald 검정 결과가 유효하지 않게 된다.

### c. 조건부 로지스틱 회귀 (Exact Test)

다른 변수들(Gender, Pathology)의 조합으로 층(Strata)을 나눈 뒤, 각 층 내에서 LI와 생존의 연관성을 정확 검정(Exact CMH Test)으로 분석한다.

**층(Strata) 구성:**
1.  Female, No (Pathology)
2.  Female, Yes
3.  Male, No
4.  Male, Yes

**검정 결과 (R `mantelhaen.test` with exact option):**

**(i) 정확 검정 (Exact Test):**
- 검정통계량 $S=10$ (관측된 High 그룹의 생존자 수)
- **P-value:** **0.0596**

**(ii) 95% 신뢰구간:**
- 공통 오즈비(Common Odds Ratio) 추정값: $\infty$ (High 그룹 사망자가 0명이므로)
- 95% 신뢰구간: **$[0.898, \infty)$**

**해석:**
LI High 그룹의 생존율이 Low 그룹보다 월등히 높아 보이지만(표본 내에서는 100%), 정확 검정 결과 P-값이 0.05보다 약간 크다(0.06). 이는 표본 크기가 작아서 통계적 유의성을 확보하지 못한 경계선상의 결과이다.
95% 신뢰구간의 하한이 0.898로 1을 포함하고 있어, 보수적인 관점에서는 LI의 효과가 통계적으로 유의하지 않다고 결론 내릴 수 있다. 하지만 상한이 무한대이고 오즈비 추정값도 무한대인 점을 고려할 때, 실제 임상적으로는 강한 긍정적 효과가 있을 가능성이 매우 높다.

---
**검증 코드 (R)**

```r
# Data Setup
LI <- c(rep("High", 4), rep("Low", 4))
Gender <- c("Female", "Female", "Male", "Male", "Female", "Female", "Male", "Male")
Pathology <- c("No", "Yes", "No", "Yes", "No", "Yes", "No", "Yes")
Yes <- c(3, 2, 4, 1, 5, 3, 5, 6)
No <- c(0, 0, 0, 0, 0, 2, 4, 11)
data <- data.frame(LI, Gender, Pathology, Yes, No)

# Part a: LRT for univariate models
m_null <- glm(cbind(Yes, No) ~ 1, family = binomial, data = data)
p_vals <- numeric(3)
vars <- c("LI", "Gender", "Pathology")
for(i in 1:3){
  f <- as.formula(paste("cbind(Yes, No) ~", vars[i]))
  m <- glm(f, family = binomial, data = data)
  p_vals[i] <- pchisq(m_null$deviance - m$deviance, df=1, lower.tail=FALSE)
}
names(p_vals) <- vars
print(p_vals)

# Part c: Exact CMH Test
# Construct 2x2x4 Array (Row: LI High/Low, Col: Yes/No, Strata: 4 combinations)
arr <- array(dim = c(2, 2, 4))
# Fill manually based on data (High=Row1, Low=Row2; Yes=Col1, No=Col2)
# Strata 1 (F, N): High(3,0), Low(5,0)
arr[,,1] <- matrix(c(3,5,0,0), 2, 2)
# Strata 2 (F, Y): High(2,0), Low(3,2)
arr[,,2] <- matrix(c(2,3,0,2), 2, 2)
# Strata 3 (M, N): High(4,0), Low(5,4)
arr[,,3] <- matrix(c(4,5,0,4), 2, 2)
# Strata 4 (M, Y): High(1,0), Low(6,11)
arr[,,4] <- matrix(c(1,6,0,11), 2, 2)

res <- mantelhaen.test(arr, exact=TRUE)
print(res)
```
