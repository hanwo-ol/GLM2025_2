# 6. Bug Occurrence Probability (Poisson Distribution)

## 문제 (English)
Suppose, on average, there is 1 bug per 500 lines of code. If a programmer writes five programs, each with 300 lines, what is the probability that 2 or fewer bugs occur in total?

---

## 해설 (Korean)

### 6.1 문제 분석

버그 발생은 단위(코드 라인 수)당 발생하는 희귀 사건이므로 **포아송 분포(Poisson Distribution)**를 따릅니다.
- 단위 비율(Rate): $\lambda_{unit} = \frac{1}{500} = 0.002$ (버그/라인)

전체 코드의 양(Exposure):
- 5개의 프로그램 $\times$ 300 라인 = 1,500 라인

### 6.2 파라미터 $\lambda$ 계산

전체 1,500 라인에서 예상되는 평균 버그 수($\lambda_{total}$)는:
$$ \lambda_{total} = \text{Rate} \times \text{Exposure} $$
$$ \lambda_{total} = \frac{1}{500} \times 1500 = 3 $$

따라서 총 버그 수 $X$는 평균이 3인 포아송 분포를 따릅니다.
$$ X \sim \text{Poisson}(3) $$

### 6.3 확률 계산

구하고자 하는 것은 "2개 이하($2$ or fewer)의 버그가 발생할 확률"입니다.
$$ P(X \le 2) = P(X=0) + P(X=1) + P(X=2) $$

포아송 확률질량함수: $P(X=k) = \frac{e^{-\lambda} \lambda^k}{k!}$

1.  $P(X=0) = \frac{e^{-3} 3^0}{0!} = e^{-3} \approx 0.04979$
2.  $P(X=1) = \frac{e^{-3} 3^1}{1!} = 3 e^{-3} \approx 0.14936$
3.  $P(X=2) = \frac{e^{-3} 3^2}{2!} = \frac{9}{2} e^{-3} = 4.5 e^{-3} \approx 0.22404$

합계:
$$ P(X \le 2) = e^{-3} (1 + 3 + 4.5) = 8.5 e^{-3} $$
$$ \approx 8.5 \times 0.049787 \approx 0.42319 $$

**답: 약 0.4232 (42.32%)**

---

## R Code (검증)

```r
# 파라미터 설정
rate <- 1 / 500
total_lines <- 5 * 300
lambda <- rate * total_lines

cat("Total Expected Bugs (Lambda):", lambda, "\n")

# 누적 확률 계산 P(X <= 2)
prob <- ppois(2, lambda = lambda)

cat("Probability P(X <= 2):", prob, "\n")
```

---

## 심화 학습 (Deep Understanding)

### 1. 오프셋(Offset)의 개념
일반화 선형 모형(GLM)에서 포아송 회귀를 할 때, 관측 단위(노출, Exposure)가 다를 경우 이를 보정해주어야 합니다.
$$ \log(\mu) = \alpha + \beta x + \log(\text{exposure}) $$
여기서 $\log(\text{exposure})$ 항을 **오프셋(Offset)**이라고 부르며, 계수를 1로 고정합니다. 이 문제에서도 라인 수(1,500)가 Exposure로 작용하여 평균($\mu$)을 결정하는 핵심 요소가 되었습니다.

### 2. 가산성(Additivity)
포아송 분포의 합은 다시 포아송 분포가 됩니다. 만약 각 프로그램(300라인)마다 $X_i \sim \text{Pois}(0.6)$인 확률변수가 5개 있고 서로 독립이라면, 총합 $\sum X_i$는 $\text{Pois}(5 \times 0.6 = 3)$을 따릅니다. 이를 이용해 전체 문제를 하나의 큰 분포로 단순화하여 풀 수 있었습니다.
