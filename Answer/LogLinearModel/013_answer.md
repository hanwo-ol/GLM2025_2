# 13. Abortion Legalization Survey (Hypothesis Testing)

## 문제 (English)
A survey was conducted on whether to legalize abortion for pregnant women.
$H_0: \pi=0.5$ vs $H_1: \pi < 0.5$
At the University of Chicago, among 893 respondents, 400 were in favor and 493 were opposed. What conclusion can be drawn?

---

## 해설 (Korean)

### 13.1 가설 설정 및 데이터

- 귀무가설 ($H_0$): $\pi = 0.5$ (찬반 비율이 같다)
- 대립가설 ($H_1$): $\pi < 0.5$ (찬성 비율이 과반보다 적다, 단측 검정)
- 표본 크기 ($n$): 893
- 찬성 수 ($y$): 400
- 표본 비율 ($\hat{\pi}$): $400 / 893 \approx 0.4479$

### 13.2 검정 통계량 (Score Test / Z-test)

표본 크기가 충분히 크므로 정규 근사(Normal Approximation)를 사용합니다. 귀무가설 하에서 분산은 $p_0(1-p_0)/n$을 사용합니다(Score Test 방식).

$$ z = \frac{\hat{\pi} - \pi_0}{\sqrt{\frac{\pi_0(1-\pi_0)}{n}}} $$

$$ \pi_0 = 0.5, \quad \sqrt{\frac{0.5 \times 0.5}{893}} = \sqrt{\frac{0.25}{893}} \approx \sqrt{0.000279955} \approx 0.01673 $$

$$ z = \frac{0.4479 - 0.5}{0.01673} = \frac{-0.0521}{0.01673} \approx -3.11 $$

### 13.3 P-값 및 결론

단측 검정($H_1: \pi < 0.5$)이므로 $Z < -3.11$일 확률을 구합니다.
표준정규분포표에서 $P(Z < -3.11) \approx 0.0009$ 입니다.

**결론:**
유의확률(P-value)이 0.0009로, 통상적인 유의수준 0.05 또는 0.01보다 훨씬 작습니다.
따라서 **귀무가설을 기각**합니다.
데이터는 낙태 합법화에 대한 찬성 비율이 과반수(50%)보다 통계적으로 유의하게 낮다는 강력한 증거를 제공합니다.

---

## R Code (검증)

```r
# 데이터
n <- 893
y <- 400
pi_0 <- 0.5

# 1. Prop.test (Score test with continuity correction by default)
# correct=FALSE to match manual calculation
test_res <- prop.test(y, n, p = pi_0, alternative = "less", correct = FALSE)

# 2. Manual Z-test
se <- sqrt(pi_0 * (1 - pi_0) / n)
z_stat <- (y/n - pi_0) / se
p_val <- pnorm(z_stat)

cat("Z-statistic:", z_stat, "\n")
cat("P-value:", p_val, "\n")
print(test_res)
```

---

## 심화 학습 (Deep Understanding)

### 1. Wald 검정 vs Score 검정
위에서 사용한 식은 분모에 $\pi_0$를 사용했으므로 **Score 검정**에 해당합니다. 만약 분모에 $\hat{\pi}$를 사용했다면 **Wald 검정**이 됩니다.
$$ Z_{Wald} = \frac{\hat{\pi} - \pi_0}{\sqrt{\hat{\pi}(1-\hat{\pi})/n}} $$
일반적으로 비율 검정에서 $H_0$가 참일 때의 분포를 더 정확히 반영하는 Score 검정이 선호됩니다. Wald 검정은 $\pi$가 0이나 1에 가까울 때 성능이 떨어질 수 있습니다.

### 2. 연속성 수정 (Continuity Correction)
이항분포(이산형)를 정규분포(연속형)로 근사할 때 발생하는 오차를 줄이기 위해 분자에 $1/2n$을 더하거나 빼주는 보정을 할 수 있습니다. 표본이 893명으로 매우 크기 때문에 보정 효과는 미미하지만, R의 `prop.test`는 기본적으로 이를 수행합니다.
