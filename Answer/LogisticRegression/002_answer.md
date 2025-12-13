# 2. Kyphosis Risk Factors (Logistic Regression Analysis)

## 문제 (English)
Hastie and Tibshirani 1990, p. 282 described a study to determine risk factors for kyphosis, severe forward flexion of the spine following corrective spinal surgery. The age in months at the time of the operation for the 18 subjects for whom kyphosis was present were 12, 15, 42, 52, 59, 73, 82, 91, 96, 105, 114, 120, 121, 128, 130, 139, 139, 157 and for 22 of the subjects for whom kyphosis was absent were 1, 1, 2, 8, 11, 18, 22, 31, 37, 61, 72, 81, 97, 112, 118, 127, 131, 140, 151, 159, 177, 206.

a. Fit a logistic regression model using age as a predictor of whether kyphosis is present. Test whether age has a significant effect.

b. Plot the data. Note the difference in dispersion on age at the two levels of kyphosis.

c. Fit the model $\text{logit}[\pi(x)] = \alpha + \beta_1 x + \beta_2 x^2$. Test the significance of the squared age term, plot the fit, and interpret.

---

## 해설 (Korean)

### 2.1 문항 a. 단순 로지스틱 회귀 적합 및 검정

반응변수 $Y$를 Kyphosis 유무(Present=1, Absent=0), 설명변수 $x$를 Age(개월 수)로 설정합니다.

$$ \text{logit}(\pi) = \alpha + \beta x $$

**가설 검정:**
- $H_0: \beta = 0$ (나이는 척추후만증 발생에 영향이 없다)
- $H_1: \beta \neq 0$

R의 `glm()` 함수를 사용하여 추정하고, Wald Test($Z$-statistic) 또는 Likelihood Ratio Test로 유의성을 확인합니다.
데이터를 보면 Kyphosis가 있는 그룹(12~157)과 없는 그룹(1~206)의 나이 분포가 겹쳐 있어, 선형 효과만으로는 뚜렷한 구분이 어려울 수 있습니다.

### 2.2 문항 b. 데이터 시각화 및 산포(Dispersion) 관찰

데이터를 산점도로 그립니다 ($x$: Age, $y$: Kyphosis 0/1).
- **Kyphosis Present (1):** 100개월(약 8~9세) 전후에 몰려 있는 경향이 있을 수 있습니다.
- **Kyphosis Absent (0):** 아주 어리거나(1~30개월), 아주 나이가 많은(150~200개월) 경우에 주로 분포할 수 있습니다.
- **산포 차이:** 'Absent' 그룹은 나이의 범위(Range)와 분산(Variance)이 매우 큰 반면, 'Present' 그룹은 중간 대역에 집중되어 있어 분산이 상대적으로 작아 보일 수 있습니다. 이는 단순 선형 관계가 아님을 시사합니다.

### 2.3 문항 c. 이차항(Squared Term) 추가 및 해석

단순 선형 모델로는 중간 대역에서 발병률이 높고 양 끝단에서 낮은(뒤집힌 U자형) 패턴을 설명할 수 없습니다. 따라서 이차항 $x^2$을 추가합니다.

$$ \text{logit}[\pi(x)] = \alpha + \beta_1 x + \beta_2 x^2 $$

**가설 검정:**
- $H_0: \beta_2 = 0$ (이차항 효과 없음)
- $H_1: \beta_2 \neq 0$ (이차항 효과 있음, 비선형 관계)

**해석:**
만약 $\beta_2$가 유의하고 음수($<0$)라면, 2차 함수 그래프는 위로 볼록한 형태(Concave down)가 됩니다. 즉, **나이가 아주 어리거나 아주 많으면 발병 확률이 낮고, 특정 중간 연령대에서 발병 위험이 가장 높음**을 의미합니다. 이는 생물학적으로 "성장기 급등(Growth spurt)" 시기나 특정 수술 적기 등과 관련이 있을 수 있습니다.

---

## R Code 및 실습

```r
# 데이터 입력
age_present <- c(12, 15, 42, 52, 59, 73, 82, 91, 96, 105, 114, 120, 121, 128, 130, 139, 139, 157)
age_absent <- c(1, 1, 2, 8, 11, 18, 22, 31, 37, 61, 72, 81, 97, 112, 118, 127, 131, 140, 151, 159, 177, 206)

# 데이터 프레임 생성 (Y=1: Present, Y=0: Absent)
df <- data.frame(
  Age = c(age_present, age_absent),
  Kyphosis = c(rep(1, length(age_present)), rep(0, length(age_absent)))
)

# a. 단순 로지스틱 회귀
fit1 <- glm(Kyphosis ~ Age, family = binomial, data = df)
summary(fit1)

# b. 데이터 시각화
plot(df$Age, df$Kyphosis, pch = 16, col = ifelse(df$Kyphosis==1, "red", "blue"),
     xlab = "Age (months)", ylab = "Kyphosis Presence",
     main = "Kyphosis vs Age")
curve(predict(fit1, data.frame(Age=x), type="response"), add=TRUE, col="green", lwd=2)

# c. 이차항 포함 모형
fit2 <- glm(Kyphosis ~ Age + I(Age^2), family = binomial, data = df)
summary(fit2)

# 이차항 유의성 검정 (Likelihood Ratio Test)
lrt <- 2 * (logLik(fit2) - logLik(fit1))
p_val_sq <- pchisq(lrt, df = 1, lower.tail = FALSE)
cat("LRT for Squared Term P-value:", p_val_sq, "\n")

# 곡선 추가
curve(predict(fit2, data.frame(Age=x), type="response"), add=TRUE, col="purple", lwd=2)
legend("right", legend=c("Linear", "Quadratic"), col=c("green", "purple"), lwd=2)
```

---

## 심화 학습 (Deep Understanding)

### 1. 비선형성 탐지 (Detecting Non-linearity)
로지스틱 회귀분석에서 설명변수 $X$와 로그 오즈(Log Odds) 간의 관계가 선형이라는 가정은 매우 강력합니다. 이 문제처럼 데이터의 분포가 양극단(Absent)과 중앙(Present)으로 나뉘는 경우, 선형 모델은 "나이가 많을수록 위험하다" 또는 "적을수록 위험하다" 중 하나로만 결론을 강제하려 하므로 실제 패턴을 놓치게 됩니다.
이차항($X^2$) 추가, 스플라인(Spline) 회귀, 또는 범주형 변환(Categorization) 등을 통해 비선형성을 모델링하는 것이 필수적입니다.

### 2. 과적합(Overfitting)과 희소 데이터
데이터 포인트가 총 40개(18+22)로 많지 않습니다. 여기서 변수를 추가($X^2$)하는 것은 모델의 복잡도를 높여 과적합 위험을 증가시킬 수 있습니다. 하지만 시각적으로 패턴이 너무나 명확하므로(가운데만 볼록), 여기서는 이차항 추가가 타당한 선택입니다. 만약 $P$차 다항식까지 계속 추가한다면 문제가 되겠지만, 2차항은 해석 가능한 최소한의 비선형 확장이기 때문입니다.
