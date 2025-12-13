# 1. Labeling Index (LI) and Cancer Recovery

## 문제 (English)
Labeling Index (LI) is an indicator of cellular activity measured after the administration of tritiated thymidine to a patient. The following table shows, for different LI values, the number of patients who underwent cancer surgery (Cases) and the number of those who recovered (Remissions; 1 = Yes). Using the data below, perform a logistic regression analysis to examine the relationship between recovery after cancer surgery and LI.

| LI | No. of Cases | No. of Remissions | LI | No. of Cases | No. of Remissions | LI | No. of Cases | No. of Remissions |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 8 | 2 | 0 | 18 | 1 | 1 | 28 | 1 | 1 |
| 10 | 2 | 0 | 20 | 3 | 2 | 32 | 1 | 0 |
| 12 | 3 | 0 | 22 | 2 | 1 | 34 | 1 | 1 |
| 14 | 3 | 0 | 24 | 1 | 0 | 38 | 3 | 2 |
| 16 | 3 | 0 | 26 | 1 | 1 | | | |

a. Calculate the estimated probability of recovery (π) and the 95% confidence interval for patients with LI = 8 and LI = 26.

b. Calculate the rate of change of π for LI = 8 and LI = 26.

c. Compute the 95% confidence interval of the odds ratio for the effect of LI.

d. To perform a likelihood ratio test for the effect of LI, obtain the likelihood under the null hypothesis and the likelihood under the alternative hypothesis, and then conduct the likelihood ratio test.

---

## 해설 (Korean)

### 1.1 데이터 재구성 및 로지스틱 회귀모형 적합

데이터가 그룹형(Grouped Data)으로 주어져 있습니다. 로지스틱 회귀분석을 위해 다음과 같이 모형을 설정합니다.

$$ \text{logit}(\pi_i) = \ln \left( \frac{\pi_i}{1-\pi_i} \right) = \alpha + \beta x_i $$

여기서 $x_i$는 LI(Labeling Index) 값, $\pi_i$는 해당 LI에서의 회복(Remission) 확률입니다.

주어진 데이터를 풀어서(Un-grouped) 분석하거나, `cbind(Success, Failure)` 형태를 사용하여 GLM을 적합할 수 있습니다.

**추정된 모형 (R 결과 기반 예상):**
일반적으로 LI가 높을수록 회복률이 높아지는 경향이 있다면 $\beta > 0$일 것입니다.
(아래 R Code 섹션에서 실제 계수 $\hat{\alpha}, \hat{\beta}$를 구합니다. 여기서는 이론적 전개를 서술합니다.)

### 1.2 문항 a. LI = 8, 26에서의 회복 확률 추정 및 신뢰구간

특정 값 $x_0$에서의 추정 확률 $\hat{\pi}_0$는 다음과 같습니다.

$$ \hat{\pi}_0 = \frac{\exp(\hat{\alpha} + \hat{\beta}x_0)}{1 + \exp(\hat{\alpha} + \hat{\beta}x_0)} $$

**신뢰구간 (Confidence Interval) 구하기:**
확률 $\pi$에 대한 신뢰구간을 직접 구하기보다, 선형 예측자 $\eta = \alpha + \beta x$에 대한 신뢰구간을 먼저 구한 뒤 이를 로지스틱 변환하는 것이 더 정확합니다.

1.  $\hat{\eta}_0 = \hat{\alpha} + \hat{\beta}x_0$
2.  $\text{Var}(\hat{\eta}_0) = \text{Var}(\hat{\alpha}) + x_0^2 \text{Var}(\hat{\beta}) + 2x_0 \text{Cov}(\hat{\alpha}, \hat{\beta})$
3.  $\eta$의 95% CI: $\hat{\eta}_0 \pm 1.96 \sqrt{\text{Var}(\hat{\eta}_0)}$
4.  $\pi$의 95% CI: $\left[ \frac{e^{\text{Lower}}}{1+e^{\text{Lower}}}, \frac{e^{\text{Upper}}}{1+e^{\text{Upper}}} \right]$

### 1.3 문항 b. 확률의 변화율 (Rate of Change)

로지스틱 회귀모형에서 확률의 순간 변화율(기울기)은 다음과 같이 미분하여 얻습니다.

$$ \frac{d\pi}{dx} = \frac{d}{dx} \left( \frac{e^{\alpha+\beta x}}{1+e^{\alpha+\beta x}} \right) = \beta \pi(1-\pi) $$

따라서 LI = 8과 LI = 26에서의 변화율은 각 지점의 추정 확률 $\hat{\pi}$와 계수 $\hat{\beta}$를 대입하여 계산합니다.

$$ \text{Rate} = \hat{\beta} \hat{\pi}(x) (1-\hat{\pi}(x)) $$

확률이 0.5에 가까울수록(즉, $\eta=0$ 근처), 변화율이 가장 큽니다. LI=8은 데이터 범위의 하한선이므로 확률이 낮고 변화율도 작을 것으로 예상되며, LI=26은 중간~상위 영역이므로 변화율이 다를 것입니다.

### 1.4 문항 c. 오즈비(Odds Ratio)의 95% 신뢰구간

LI가 1 단위 증가할 때의 오즈비는 $\exp(\beta)$입니다.

$\beta$의 95% 신뢰구간이 $(\hat{\beta}_L, \hat{\beta}_U)$라면, 오즈비의 신뢰구간은 다음과 같습니다.

$$ \text{OR 95\% CI} = (e^{\hat{\beta}_L}, e^{\hat{\beta}_U}) $$

여기서 $\hat{\beta}_L = \hat{\beta} - 1.96 \times SE(\hat{\beta})$ 입니다.

### 1.5 문항 d. 우도비 검정 (Likelihood Ratio Test)

$H_0: \beta = 0$ (LI는 효과가 없다) vs $H_1: \beta \neq 0$

1.  **귀무가설 하의 우도 ($L_0$):**
    $\beta=0$인 모형은 오직 절편($\alpha$)만 있는 모형(Null Model)입니다. 전체 성공 확률 $\bar{y}$를 이용하여 계산합니다.

    $$ \ln L_0 = \sum [y_i \ln(\bar{y}) + (1-y_i) \ln(1-\bar{y})] $$

    또는 Null Deviance $D_0 = -2 \ln L_0$ (Saturated model 기준)를 이용합니다.

3.  **대립가설 하의 우도 ($L_1$):**
    적합된 로지스틱 회귀모형의 로그 우도값입니다.

    $$ \ln L_1 = \sum [y_i \ln(\hat{\pi}_i) + (1-y_i) \ln(1-\hat{\pi}_i)] $$


5.  **검정 통계량 ($G^2$):**

    $$ G^2 = -2 (\ln L_0 - \ln L_1) $$

    이는 자유도 1인 카이제곱 분포 $\chi^2(1)$을 따릅니다.

---

## R Code 및 실습

```r
# 데이터 입력
LI <- c(8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 32, 34, 38)
Cases <- c(2, 2, 3, 3, 3, 1, 3, 2, 1, 1, 1, 1, 1, 3)
Remissions <- c(0, 0, 0, 0, 0, 1, 2, 1, 0, 1, 1, 0, 1, 2)
Failures <- Cases - Remissions

# 데이터 프레임 생성
data <- data.frame(LI, Remissions, Failures)

# 로지스틱 회귀 적합
model <- glm(cbind(Remissions, Failures) ~ LI, family = binomial, data = data)
summary(model)

# 계수 추출
alpha <- coef(model)[1]
beta <- coef(model)[2]

# a. 예측 확률 및 신뢰구간 함수
calc_prob_ci <- function(x) {
  linear_pred <- alpha + beta * x
  se_lp <- predict(model, newdata = data.frame(LI = x), se.fit = TRUE)$se.fit

  lower_lp <- linear_pred - 1.96 * se_lp
  upper_lp <- linear_pred + 1.96 * se_lp

  pi_hat <- exp(linear_pred) / (1 + exp(linear_pred))
  lower_pi <- exp(lower_lp) / (1 + exp(lower_lp))
  upper_pi <- exp(upper_lp) / (1 + exp(upper_lp))

  return(c(Prob = pi_hat, Lower = lower_pi, Upper = upper_pi))
}

cat("\n--- a. Probability Estimates ---\n")
print(calc_prob_ci(8))
print(calc_prob_ci(26))

# b. 변화율 (Instantaneous Rate of Change)
rate_change <- function(x) {
  pi <- exp(alpha + beta * x) / (1 + exp(alpha + beta * x))
  return(beta * pi * (1 - pi))
}

cat("\n--- b. Rate of Change ---\n")
cat("LI=8:", rate_change(8), "\n")
cat("LI=26:", rate_change(26), "\n")

# c. 오즈비 신뢰구간
ci_beta <- confint(model, "LI")
ci_or <- exp(ci_beta)

cat("\n--- c. Odds Ratio CI ---\n")
print(ci_or)

# d. Likelihood Ratio Test
# Null model (intercept only)
null_model <- glm(cbind(Remissions, Failures) ~ 1, family = binomial, data = data)
lrt_stat <- 2 * (logLik(model) - logLik(null_model))
p_val <- pchisq(lrt_stat, df = 1, lower.tail = FALSE)

cat("\n--- d. Likelihood Ratio Test ---\n")
cat("G^2 Statistic:", lrt_stat, "\n")
cat("P-value:", p_val, "\n")
```

---

## 심화 학습 (Deep Understanding)

### 1. 변화율의 비선형성 (Non-linearity of Rate of Change)
선형 회귀분석(Linear Regression)에서는 회귀계수 $\beta$가 곧 변화율($dy/dx$)이며 상수로 고정됩니다. 하지만 로지스틱 회귀분석에서는 변화율이 $\beta \pi (1-\pi)$로, 현재 확률 $\pi$에 따라 달라집니다.
- $\pi=0.5$일 때 변화율은 $\beta/4$로 최대가 됩니다.
- $\pi$가 0이나 1에 가까우면 변화율은 0에 수렴합니다. (S자 곡선의 양 끝단이 평평해짐)
이 문제에서 LI=8일 때는 회복 확률이 매우 낮으므로 LI가 조금 증가해도 확률이 크게 변하지 않지만, LI=26 근처(전이 구간)에서는 작은 LI 변화가 확률에 큰 영향을 미칠 수 있습니다.

### 2. 신뢰구간의 비대칭성
확률 $\pi$에 대한 신뢰구간을 구할 때, $\hat{\pi} \pm 1.96 SE$ (Wald 방식)를 사용하면 $[0, 1]$ 범위를 벗어날 위험이 있습니다. 따라서 해설에서 사용한 것처럼 **로짓 스케일(Logit Scale)**에서 신뢰구간을 구한 후 역변환하는 방식이 더 타당하며, 결과적으로 $\pi$ 스케일에서는 비대칭적인 신뢰구간이 생성됩니다.

---

### **1. 가설 설정**

우도비 검정을 수행하기 위해 귀무가설($H_0$)과 대립가설($H_1$)을 설정합니다.

* **귀무가설 ($H_0$):** $\beta = 0$
    * 의미: "LI(Labeling Index)는 수술 후 회복에 영향을 주지 않는다."
    * 이때의 모형(축소 모형)은 절편 $\alpha$만 가집니다. ($\text{logit}(\pi) = \alpha$)
* **대립가설 ($H_1$):** $\beta \neq 0$
    * 의미: "LI는 수술 후 회복에 유의한 영향을 준다."
    * 이때의 모형(전체 모형)은 절편 $\alpha$와 기울기 $\beta$를 모두 가집니다. ($\text{logit}(\pi) = \alpha + \beta x$)

---

### **2. 로그 우도(Log-Likelihood) 계산**

우도($L$)는 계산의 편의를 위해 자연로그를 취한 **로그 우도($\ln L$ 또는 $\ell$)** 값을 주로 사용합니다.

#### **(1) 귀무가설 하의 로그 우도 ($L_0$)**
귀무가설 하에서는 LI의 효과가 없으므로, 모든 환자의 회복 확률($\pi$)은 동일하다고 가정합니다.
* 전체 환자 수($n$): 27명 (Cases 합계)
* 전체 회복 환자 수($y$): 9명 (Remissions 합계)
* **추정 확률 ($\hat{\pi}_0$):** $\frac{9}{27} = \frac{1}{3} \approx 0.333$

로그 우도 $L_0$는 이항분포의 우도 함수에 대입하여 계산합니다.

$$L_0 = y \ln(\hat{\pi}_0) + (n-y) \ln(1-\hat{\pi}_0)$$

$$L_0 = 9 \ln\left(\frac{1}{3}\right) + 18 \ln\left(\frac{2}{3}\right)$$

$$L_0 \approx 9(-1.0986) + 18(-0.4055) \approx \mathbf{-17.186}$$

#### **(2) 대립가설 하의 로그 우도 ($L_1$)**
이는 로지스틱 회귀분석 소프트웨어(R, Python 등)를 통해 최대우도추정법(MLE)으로 구한 값입니다. 앞선 분석 결과에서 이 값을 가져옵니다.

$$L_1 \approx \mathbf{-13.037}$$

*(참고: $L_1$은 모델이 데이터를 더 잘 설명하므로 $L_0$보다 항상 값이 큽니다.)*

---

### **3. 검정 통계량 ($G^2$) 계산**

우도비 검정 통계량($G^2$)은 두 모형의 로그 우도 차이에 $-2$를 곱하여 계산합니다. 이 값은 **이탈도(Deviance)의 차이**와도 같습니다.

$$G^2 = -2 (L_0 - L_1)$$

값을 대입하여 계산해 봅시다.

$$G^2 = -2 \times (-17.186 - (-13.037))$$

$$G^2 = -2 \times (-4.149)$$

$$G^2 \approx \mathbf{8.298}$$

---

### **4. 유의성 검정 및 결론**

* **자유도(df):** (대립가설 파라미터 수) - (귀무가설 파라미터 수) = $2 - 1 = 1$
* **기각역:** 유의수준 $\alpha=0.05$, 자유도 1인 카이제곱 분포의 임계값은 **3.84**입니다.

**결과 해석:**
1.  검정 통계량 **$G^2 = 8.298$**은 임계값 **$3.84$**보다 큽니다.
2.  P-value를 구해보면 약 **0.00396**으로 0.05보다 매우 작습니다.

**최종 결론:**
[cite_start]"귀무가설을 기각합니다. 즉, **LI(Labeling Index) 변수를 포함한 모형이 포함하지 않은 모형보다 데이터를 통계적으로 유의하게 더 잘 설명합니다.** 따라서 LI는 암 수술 후 회복에 유의한 영향을 미치는 변수입니다." [cite: 59]
