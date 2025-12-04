# 3. Abortion Opinion Survey (Dummy Variables & Interpretation)

## 문제 (English)
Let $Y$ denote a subject’s opinion about current laws legalizing abortion (1=support), for gender $h$ ($h=1$, female; $h=2$, male), religious affiliation $i$ ($i=1$, Protestant; $i=2$, Catholic, $i=3$, Jewish), and political party affiliation $j$ ($j=1$, Democrat; $j=2$, Republican; $j=3$, Independent). For survey data, software for fitting the model
$$ \text{logit}[P(Y=1)] = \alpha + \beta_h^G + \beta_i^R + \beta_j^P $$
reports $\hat{\alpha} = 0.62$, $\hat{\beta}_1^G = 0.08$, $\hat{\beta}_2^G = -0.08$, $\hat{\beta}_1^R = -0.16$, $\hat{\beta}_2^R = -0.25$, $\hat{\beta}_3^R = 0.41$, $\hat{\beta}_1^P = 0.87$, $\hat{\beta}_2^P = -1.27$, $\hat{\beta}_3^P = 0.40$.

a. Interpret how the odds of support depends on religion.
b. Estimate the probability of support for the group most (least) likely to support current laws.
c. If, instead, parameters used constraints $\beta_1^G = \beta_1^R = \beta_1^P = 0$, report the estimates.

---

## 해설 (Korean)

### 3.1 모형 구조 및 제약조건 확인

주어진 계수들을 보면, 각 변수의 계수 합이 0이 되는 **Effect Coding (Sum-to-zero constraint)** 방식이 사용되었음을 알 수 있습니다.
- Gender: $0.08 + (-0.08) = 0$
- Religion: $-0.16 + (-0.25) + 0.41 = 0$
- Party: $0.87 + (-1.27) + 0.40 = 0$

이는 ANOVA 등에서 주로 사용하는 방식으로, 각 계수는 '전체 평균(Grand Mean)' 대비 해당 집단의 편차를 나타냅니다.

### 3.2 문항 a. 종교(Religion)에 따른 오즈 해석

종교 효과 $\beta_i^R$는 다음과 같습니다.
- Protestant ($i=1$): $\hat{\beta}_1^R = -0.16$
- Catholic ($i=2$): $\hat{\beta}_2^R = -0.25$
- Jewish ($i=3$): $\hat{\beta}_3^R = 0.41$

오즈비(Odds Ratio) 관점에서 해석하려면 기준(Reference)이 필요하지만, 여기서는 절대적인 효과 크기를 비교할 수 있습니다.
- **Jewish** 집단은 평균적인 오즈보다 $e^{0.41} \approx 1.51$배 높은 오즈를 가집니다 (찬성 경향이 강함).
- **Protestant**와 **Catholic**은 각각 $e^{-0.16} \approx 0.85$, $e^{-0.25} \approx 0.78$배로 평균보다 낮은 찬성 오즈를 보입니다.

**Protestant 대비 Jewish의 오즈비:**
$$ OR_{J \text{ vs } P} = \exp(0.41 - (-0.16)) = \exp(0.57) \approx 1.77 $$
해석: 유대교인은 개신교인에 비해 낙태 합법화를 지지할 오즈가 약 1.77배 높습니다.

### 3.3 문항 b. 찬성 확률이 가장 높은/낮은 집단 추정

$$ \text{logit}(\pi) = 0.62 + \beta^G + \beta^R + \beta^P $$
$\pi$를 최대화하려면 $\beta$ 값들을 가장 큰 것끼리 조합해야 합니다.

**1) 가장 찬성할 것 같은 그룹 (Highest Probability)**
- Gender: Female ($0.08$) > Male ($-0.08$)
- Religion: Jewish ($0.41$) > P ($-0.16$) > C ($-0.25$)
- Party: Democrat ($0.87$) > I ($0.40$) > R ($-1.27$)

**조합:** Female, Jewish, Democrat
$$ \hat{\eta}_{\max} = 0.62 + 0.08 + 0.41 + 0.87 = 1.98 $$
$$ \hat{\pi}_{\max} = \frac{e^{1.98}}{1+e^{1.98}} \approx 0.8787 $$
약 **87.9%** 확률로 찬성합니다.

**2) 가장 찬성하지 않을 것 같은 그룹 (Lowest Probability)**
- 조합: Male ($-0.08$), Catholic ($-0.25$), Republican ($-1.27$)
$$ \hat{\eta}_{\min} = 0.62 - 0.08 - 0.25 - 1.27 = -0.98 $$
$$ \hat{\pi}_{\min} = \frac{e^{-0.98}}{1+e^{-0.98}} \approx 0.2729 $$
약 **27.3%** 확률로 찬성합니다.

### 3.4 문항 c. Reference Coding ($\beta_1 = 0$) 으로의 변환

문제에서 제시한 제약조건 $\beta_1^G = \beta_1^R = \beta_1^P = 0$은 첫 번째 범주를 기준(Reference, Baseline)으로 삼는 **Dummy Coding (Treatment Coding)** 방식입니다.

기존 모델: $\text{Logit} = \alpha_{sum} + \beta^{sum}$
새 모델: $\text{Logit} = \alpha_{ref} + \beta^{ref}$

두 모델이 동일한 예측값을 내야 하므로, 각 범주의 Logit 값을 비교하여 파라미터를 변환합니다.

**새로운 절편 ($\alpha_{ref}$):**
모든 범주가 1번(Female, Protestant, Democrat)일 때의 값이어야 합니다.
기존 모델에서의 (1,1,1) Logit 값:
$$ 0.62 + 0.08 + (-0.16) + 0.87 = 1.41 $$
따라서 $\hat{\alpha}_{ref} = 1.41$

**새로운 계수들 ($\beta^{ref}$):**
기준 집단(1번) 대비 다른 집단의 차이입니다.
- **Gender (Male vs Female):** $(-0.08) - (0.08) = -0.16$. ($\hat{\beta}_2^{G, ref} = -0.16$)
- **Religion (Cath vs Prot):** $(-0.25) - (-0.16) = -0.09$. ($\hat{\beta}_2^{R, ref} = -0.09$)
- **Religion (Jew vs Prot):** $(0.41) - (-0.16) = 0.57$. ($\hat{\beta}_3^{R, ref} = 0.57$)
- **Party (Rep vs Dem):** $(-1.27) - (0.87) = -2.14$. ($\hat{\beta}_2^{P, ref} = -2.14$)
- **Party (Ind vs Dem):** $(0.40) - (0.87) = -0.47$. ($\hat{\beta}_3^{P, ref} = -0.47$)

**정리:**
- $\alpha = 1.41$
- $\beta_2^G = -0.16$
- $\beta_2^R = -0.09, \beta_3^R = 0.57$
- $\beta_2^P = -2.14, \beta_3^P = -0.47$
- (나머지 $\beta_1$들은 0)

---

## R Code 및 실습

```r
# 주어진 계수 (Sum-to-zero)
alpha <- 0.62
beta_G <- c(0.08, -0.08) # F, M
beta_R <- c(-0.16, -0.25, 0.41) # P, C, J
beta_P <- c(0.87, -1.27, 0.40) # D, R, I

# b. Max / Min Prob calculation
logit_max <- alpha + max(beta_G) + max(beta_R) + max(beta_P)
prob_max <- exp(logit_max) / (1 + exp(logit_max))

logit_min <- alpha + min(beta_G) + min(beta_R) + min(beta_P)
prob_min <- exp(logit_min) / (1 + exp(logit_min))

cat("Max Probability (Female, Jewish, Democrat):", prob_max, "\n")
cat("Min Probability (Male, Catholic, Republican):", prob_min, "\n")

# c. Parameter Transformation
# Reference group: index 1 (Female, Protestant, Democrat)
intercept_ref <- alpha + beta_G[1] + beta_R[1] + beta_P[1]

# New coefficients (Difference from ref)
beta_G_ref <- beta_G - beta_G[1]
beta_R_ref <- beta_R - beta_R[1]
beta_P_ref <- beta_P - beta_P[1]

cat("\n--- Transformed Parameters (Reference Coding) ---\n")
cat("Intercept:", intercept_ref, "\n")
cat("Gender (Male):", beta_G_ref[2], "\n")
cat("Religion (Catholic):", beta_R_ref[2], "\n")
cat("Religion (Jewish):", beta_R_ref[3], "\n")
cat("Party (Republican):", beta_P_ref[2], "\n")
cat("Party (Independent):", beta_P_ref[3], "\n")
```

---

## 심화 학습 (Deep Understanding)

### 1. 코딩 방식(Contrast Coding)의 이해
통계 패키지마다 기본 코딩 방식이 다릅니다.
- **R (`contr.treatment`):** 첫 번째 레벨을 0으로 둡니다. (문제 c의 방식)
- **SAS (`param=effect`):** 계수의 합을 0으로 둡니다. (문제 원본 방식)
어떤 방식을 쓰더라도 예측된 확률($\hat{\pi}$)이나 모형의 적합도(Deviance)는 동일합니다. 단지 계수($\beta$)의 해석(Interpretation)만 달라질 뿐입니다. 이를 이해하는 것은 여러 소프트웨어 결과를 비교하거나 논문을 읽을 때 필수적입니다.

### 2. 제약조건의 자유도
범주가 $k$개일 때 추정해야 할 모수는 $k-1$개입니다. 따라서 정보의 양은 동일하며, 수학적으로 두 파라미터 공간은 일대일 대응(Isomorphic)합니다.
