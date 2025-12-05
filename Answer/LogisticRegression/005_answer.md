# 5. Penicillin Effectiveness (Separation & Exact Tests)



## 문제 (English)

Following Table, refers to the effectiveness of immediately injected or $1 \frac{1}{2}$-hour-delayed penicillin in protecting rabbits against lethal injection with $\beta$-hemolytic streptococci.



| Penicillin Level | Delay | Response Cured | Died |

|:---:|:---:|:---:|:---:|

| 1/8 | None | 0 | 6 |

| | 1 1/2 h | 0 | 5 |

| 1/4 | None | 3 | 3 |

| | 1 1/2 h | 0 | 6 |

| 1/2 | None | 6 | 0 |

| | 1 1/2 h | 2 | 4 |

| 1 | None | 5 | 1 |

| | 1 1/2 h | 6 | 0 |

| 4 | None | 2 | 0 |

| | 1 1/2 h | 5 | 0 |



a. Let $X=$ delay, $Y=$ whether cured, and $Z=$ penicillin level. Fit the logit model $\text{logit}(\pi_{ik}) = \alpha + \beta x_i + \beta_k^Z (i=1,2, k=1,\dots,5)$. Argue that the pattern of 0 cell counts suggests that (with no intercepts) $\beta_1^Z = -\infty$ and $\beta_5^Z = \infty$ (assuming ordinal levels). What does your software report?

b. Using the logit model, conduct the likelihood-ratio test of $XY$ conditional independence and interpret.

c. Test $XY$ conditional independence using the Cochran Mantel Haenszel test and interpret.

d. Estimate the $XY$ conditional odds ratio using (i) ML with the logit model, and (ii) the Mantel Haenszel estimate and interpret.

e. The small cell counts make large-sample analyses questionable. Conduct small sample inference and interpret.



---



## 해설 (Korean)



### 5.1 문항 a. 완전 분리(Complete Separation) 문제



가장 낮은 Penicillin Level (1/8)에서는 Cured(성공)가 0건이고, 가장 높은 Level (4)에서는 Died(실패)가 0건입니다.

- **Level 1/8 ($k=1$):** 성공률 0% ($\pi = 0$). Logit은 $\ln(0/1) = -\infty$. 따라서 해당 레벨의 효과 $\beta_1^Z$는 $-\infty$로 추정되려 합니다.

- **Level 4 ($k=5$):** 성공률 100% ($\pi = 1$). Logit은 $\ln(1/0) = \infty$. 따라서 해당 레벨의 효과 $\beta_5^Z$는 $\infty$로 추정되려 합니다.



**소프트웨어 보고:**

R의 `glm`과 같은 표준 패키지는 수렴하지 못하거나(Algorithm did not converge), 계수 추정값이 비정상적으로 큰 값(예: $\pm 20$)과 매우 큰 표준오차(SE)를 보고합니다. 이는 **Hauck-Donner 효과**나 **Separation** 현상 때문입니다.



### 5.2 문항 b. 우도비 검정 (Likelihood Ratio Test)



$H_0: \beta_{\text{delay}} = 0$ (Delay 효과 없음) vs $H_1: \beta_{\text{delay}} \neq 0$.



이 검정은 모형 전체의 우도(Likelihood)를 비교하는 것이므로, 특정 파라미터가 무한대로 발산하더라도 $G^2$ 통계량 자체는 유효한 값으로 수렴할 수 있습니다.

R에서 `anova(model_reduced, model_full, test="Chisq")`를 수행하면, Delay 변수의 유의성을 검정할 수 있습니다. 아마도 Delay가 있으면 치료율이 떨어지는 음의 효과가 유의하게 나올 것입니다.



### 5.3 문항 c. Cochran-Mantel-Haenszel (CMH) Test



CMH 검정은 로지스틱 회귀와 달리 반복적인 최적화 과정(Iterative method)이 필요 없으므로, Separation 문제에서 자유롭습니다.

$Z$(Penicillin Level)를 층(Stratum)으로 하여 $X$(Delay)와 $Y$(Cured)의 독립성을 검정합니다.

- 귀무가설: 모든 Penicillin Level에서 Delay는 Cure Rate에 영향을 주지 않는다.

- 결과: $P < 0.05$로 유의하게 나올 것으로 예상됩니다 (Delay가 있으면 치료율 감소).



### 5.4 문항 d. 조건부 오즈비 추정 (Conditional Odds Ratio)



**(i) ML with Logit Model:**

Separation 때문에 MLE $\hat{\beta}_{\text{delay}}$가 불안정할 수 있습니다. 하지만 Delay 변수 자체는 Separation을 일으키지 않는다면(0/1이 섞여 있다면), 유한한 값을 가질 수도 있습니다. 만약 Level 1/8과 4를 제외한 데이터만으로 추정되거나, 과도하게 큰 값이 나올 수 있습니다.



**(ii) Mantel-Haenszel Estimate:**

$\hat{\theta}_{MH} = \frac{\sum (n_{11k} n_{22k} / n_k)}{\sum (n_{12k} n_{21k} / n_k)}$ 공식을 사용합니다.

0이 포함된 층은 기여도가 0이 되어 자연스럽게 제외되거나 계산에 포함되어도 문제가 없습니다. 이 값이 훨씬 신뢰할 수 있는 추정치입니다.



### 5.5 문항 e. 소표본 추론 (Exact Inference)



표본 수가 매우 적고 0이 많으므로 점근적 근사(Asymptotic approach)는 부적절합니다.

**정확 로지스틱 회귀 (Exact Logistic Regression)** 또는 **Exact CMH Test**를 수행해야 합니다.

- 조건부 정확 검정(Conditional Exact Test)을 통해 Delay 변수의 정확한 P-값과 신뢰구간을 구합니다.

- 결과적으로 Delay는 치료 확률을 유의하게 낮춘다는 결론을 얻게 될 것입니다.



---



## R Code 및 실습



```r

# 데이터 생성

# Penicillin Level을 Factor로 처리

Penicillin <- factor(c("1/8", "1/8", "1/4", "1/4", "1/2", "1/2", "1", "1", "4", "4"),

                     levels=c("1/8", "1/4", "1/2", "1", "4"))

Delay <- factor(rep(c("None", "1.5h"), 5), levels=c("None", "1.5h"))

Cured <- c(0, 0, 3, 0, 6, 2, 5, 6, 2, 5)

Died <- c(6, 5, 3, 6, 0, 4, 1, 0, 0, 0)

Total <- Cured + Died



data <- data.frame(Penicillin, Delay, Cured, Died)



# a. GLM Fit (Warning Expected)

fit_glm <- glm(cbind(Cured, Died) ~ Penicillin + Delay, family = binomial, data = data)

summary(fit_glm)

# 해석: Penicillin1/8 계수 등이 매우 작거나 큼, SE 폭발.



# b. Likelihood Ratio Test for Delay

fit_reduced <- glm(cbind(Cured, Died) ~ Penicillin, family = binomial, data = data)

anova(fit_reduced, fit_glm, test = "Chisq")



# c. CMH Test

# Array 형태로 변환 (2x2x5)

# 행: Delay, 열: Response(Cured/Died), 층: Penicillin

table_array <- array(dim = c(2, 2, 5))

for(i in 1:5) {

  idx <- which(data$Penicillin == levels(data$Penicillin)[i])

  # Delay None vs 1.5h

  # Row1: None, Row2: 1.5h

  # Col1: Cured, Col2: Died

  sub <- data[idx, ]

  mat <- matrix(c(sub$Cured[1], sub$Died[1],

                  sub$Cured[2], sub$Died[2]), nrow=2, byrow=TRUE)

  table_array[,,i] <- mat

}

dimnames(table_array) <- list(Delay=c("None", "1.5h"), Response=c("Cured", "Died"), Penicillin=levels(Penicillin))



cmh_test <- mantelhaen.test(table_array)

print(cmh_test)



# d. Odds Ratio Estimates

cat("MLE OR (Delay):", exp(coef(fit_glm)["Delay1.5h"]), "\n")

cat("MH OR:", cmh_test$estimate, "\n")



# e. Exact Logistic Regression (logistf or elrm package)

# 여기서는 logistf (Firth's penalization) 사용 예시

# install.packages("logistf")

library(logistf)

fit_exact <- logistf(cbind(Cured, Died) ~ Penicillin + Delay, data = data)

summary(fit_exact)

exp(coef(fit_exact)["Delay1.5h"])

```



---



## 심화 학습 (Deep Understanding)



### 1. Firth's Penalized Likelihood

완전 분리(Complete Separation)가 발생했을 때 표준 MLE는 무한대로 발산합니다. 이를 해결하기 위해 Jeffreys Prior를 도입한 **Firth의 방법**을 많이 사용합니다. 이는 우도 함수에 벌점항(Penalty)을 추가하여 계수를 수축(Shrinkage)시키고, 유한한 추정값과 신뢰구간을 제공합니다. 문항 e의 "Small sample inference"에 적합한 현대적인 대안입니다.



### 2. 정확 검정(Exact Test)의 논리

정확 검정은 충분통계량(Sufficient Statistic)에 기초한 조건부 분포를 이용합니다. 불필요한 모수(Nuisance Parameter, 여기서는 각 Penicillin Level의 효과)를 조건부로 고정시킴으로써 제거하고, 관심 모수(Delay)에 대해서만 정확한 확률 계산을 수행합니다. 이는 표본이 작고 층이 많은 데이터(Sparse data)에서 점근적 방법보다 훨씬 타당합니다.
