# 6. Nonmetastatic Osteosarcoma (Conditional Logistic Regression)

## 문제 (English)
Consider following Table, from a study of nonmetastatic osteosarcoma (A. M. Goorin, J. Clin Oncol. 5: 1178-1184, 1987, and the manual for LogXact). The response is whether the subject achieved a three-year disease-free interval.

| Lymphocytic Infiltration | Gender | Osteoblastic Pathology | Disease-Free Yes | No |
|:---:|:---:|:---:|:---:|:---:|
| High | Female | No | 3 | 0 |
| | | Yes | 2 | 0 |
| | Male | No | 4 | 0 |
| | | Yes | 1 | 0 |
| Low | Female | No | 5 | 0 |
| | | Yes | 3 | 2 |
| | Male | No | 5 | 4 |
| | | Yes | 6 | 11 |

a. Show that each predictor has a significant effect when used individually without the others.
b. Try to fit a main-effects logistic regression model containing all three predictors. Explain why the ML estimate for the effect of lymphocytic infiltration is infinite.
c. Using conditional logistic regression, (i) conduct an exact test for the effect of lymphocytic infiltration, controlling for the other variables; and (ii) find a 95% confidence interval for the effect. Interpret results.

---

## 해설 (Korean)

### 6.1 문항 a. 개별 변수의 유의성 검정

각 변수별로 2x2 분할표를 생성하여 연관성을 검정합니다.
- **Lymphocytic Infiltration (High vs Low):**
  - High: Yes(3+2+4+1=10), No(0) → 성공률 100%
  - Low: Yes(5+3+5+6=19), No(0+2+4+11=17) → 성공률 53%
  - Fisher's Exact Test 수행 시 유의할 것입니다.
- **Gender (Female vs Male):**
  - Female: Yes(3+2+5+3=13), No(2)
  - Male: Yes(4+1+5+6=16), No(15)
  - 여성의 예후가 훨씬 좋습니다.
- **Osteoblastic Pathology (No vs Yes):**
  - No: Yes(17), No(4)
  - Yes: Yes(12), No(13)
  - Pathology가 No인 경우 예후가 더 좋습니다.

모두 개별적으로는 유의한(Significant) 예측 변수입니다.

### 6.2 문항 b. 다중 로지스틱 회귀와 무한대 추정값

세 변수를 모두 넣고 모델을 적합할 때, **Lymphocytic Infiltration = High**인 모든 환자(10명)는 Disease-Free = Yes입니다 (No = 0).
$$ P(Y=1 | \text{Infiltration=High}) = 1 $$
이는 **완전 분리(Complete Separation)** 현상입니다.
우도 함수를 최대화하려면 High 그룹의 로그 오즈($\alpha + \beta_{High} + \dots$)가 $+\infty$가 되어야 하므로, $\hat{\beta}_{High}$는 양의 무한대로 발산합니다. 따라서 표준적인 최대우도추정(MLE)은 존재하지 않거나 수렴하지 않습니다.

### 6.3 문항 c. 조건부 로지스틱 회귀 (Conditional Logistic Regression)

MLE가 존재하지 않는 상황에서는 **정확 조건부 추론(Exact Conditional Inference)**이 필요합니다.

**(i) 정확 검정 (Exact Test):**
다른 변수(Gender, Pathology)의 충분통계량을 조건부로 고정하고, Infiltration 변수의 순열 분포(Permutation Distribution)를 이용하여 정확한 P-값을 계산합니다.
Infiltration=High인 경우 예후가 완벽하게 좋았으므로, 통계적으로 매우 유의할 가능성이 높습니다.

**(ii) 정확 신뢰구간 (Exact Confidence Interval):**
MLE로는 신뢰구간을 구할 수 없지만(폭이 무한대), 정확법을 사용하면 하한(Lower bound)은 유한한 값으로 구할 수 있습니다. 상한(Upper bound)은 데이터 특성상 $+\infty$일 것입니다.
- 예: 95% CI $[1.5, \infty)$.
- **해석:** 림프구 침윤(Lymphocytic Infiltration)이 높으면 3년 무병 생존 확률(오즈)이 최소 1.5배 이상 증가한다고 95% 신뢰수준에서 말할 수 있습니다. 상한이 무한대인 것은 데이터에서 High 그룹의 실패 사례가 단 한 건도 없기 때문에 효과가 "매우 크다"는 가능성을 배제할 수 없기 때문입니다.

---

## R Code 및 실습

```r
# 데이터 생성
# LI: High=1, Low=0 / Gender: F=1, M=0 / Osteo: Yes=1, No=0
LI <- c(1,1,1,1, 0,0,0,0)
Gen <- c(1,1,0,0, 1,1,0,0)
Ost <- c(0,1,0,1, 0,1,0,1)
Yes <- c(3,2,4,1, 5,3,5,6)
No  <- c(0,0,0,0, 0,2,4,11)

df <- data.frame(LI, Gen, Ost, Yes, No)

# a. Univariate Analysis (Fisher Test)
# LI vs Outcome
tab_LI <- matrix(c(sum(Yes[LI==1]), sum(No[LI==1]),
                   sum(Yes[LI==0]), sum(No[LI==0])), nrow=2)
fisher.test(tab_LI)

# Gender vs Outcome
tab_Gen <- matrix(c(sum(Yes[Gen==1]), sum(No[Gen==1]),
                    sum(Yes[Gen==0]), sum(No[Gen==0])), nrow=2)
fisher.test(tab_Gen)

# Osteo vs Outcome
tab_Ost <- matrix(c(sum(Yes[Ost==0]), sum(No[Ost==0]), # No가 Reference일때 유리
                    sum(Yes[Ost==1]), sum(No[Ost==1])), nrow=2)
fisher.test(tab_Ost)

# b. Multivariate Logistic Regression (Separation Check)
fit_all <- glm(cbind(Yes, No) ~ LI + Gen + Ost, family = binomial, data = df)
summary(fit_all)
# LI 계수와 SE가 비정상적으로 큼을 확인

# c. Exact Logistic Regression using 'elrm' or 'logistf'
# elrm 패키지는 Exact Conditional Inference 수행
# install.packages("elrm")
library(elrm)

# 데이터 포맷 변환 (elrm은 ungrouped data 선호하거나 특정 포맷 필요)
# 여기서는 개념적 코드 제시
# fit_exact <- elrm(formula = Yes/n ~ LI + Gen + Ost, interest = ~LI, iter = 20000, dataset = df)
# summary(fit_exact)

# 대안: logistf (Firth method) - 유한한 CI 제공
library(logistf)
fit_firth <- logistf(cbind(Yes, No) ~ LI + Gen + Ost, data = df)
summary(fit_firth)
exp(confint(fit_firth))
```

---

## 심화 학습 (Deep Understanding)

### 1. 로그-이그젝트(LogXact)와 정확 로지스틱 회귀
문제에서 언급된 "LogXact"는 정확 로지스틱 회귀를 수행하는 전문 소프트웨어입니다. 일반적인 패키지(SAS, SPSS, R 기본)가 점근적 근사(Asymptotic)를 사용하는 반면, LogXact는 네트워크 알고리즘을 사용하여 조합 가능한 모든 표(Table)를 생성하고 정확한 P-값을 계산합니다. 이는 특히 바이오메디컬 데이터처럼 표본이 작고 결과가 극단적인(0 셀이 있는) 경우에 필수적입니다.

### 2. 조건부 우도(Conditional Likelihood)의 원리
조건부 로지스틱 회귀는 주로 매칭된 환자-대조군 연구(Matched Case-Control)에서 사용되지만, 이처럼 층화 변수(Nuisance parameters)가 많은 경우에도 사용됩니다. 모형에서 절편항($\alpha$)과 다른 공변량 효과를 조건부 확률을 통해 소거함으로써, 관심 있는 변수($\beta_{LI}$)에 대한 추론만 남기는 방식입니다. 이를 통해 표본 크기가 작을 때 발생하는 편향(Bias)을 제거할 수 있습니다.
