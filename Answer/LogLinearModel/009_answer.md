# 9. Discrete MLE for Binomial Distribution

## 문제 (English)
Suppose $Y \sim B(n, \pi)$, where $n$ takes values 2 or 3, and $\pi$ takes values $1/2$ or $1/3$ (inferred from OCR "!0 or !1"). In this case, for each combination of $n$ and $\pi$, determine the maximum likelihood estimate.

*(Note: The OCR text said "!0 or !1", likely meaning $1/2, 1/3$ or similar discrete set. I will define the parameter space as $\Theta = \{(n, \pi) : n \in \{2, 3\}, \pi \in \{0.5, 1/3\}\}$ and solve for a generic observed $y$.)*

---

## 해설 (Korean)

### 9.1 문제 정의

관측값 $y$가 주어졌을 때, 모수 공간 $\Theta = \{ (2, 0.5), (2, 1/3), (3, 0.5), (3, 1/3) \}$ 중에서 우도(Likelihood)를 최대화하는 쌍 $(n, \pi)$를 찾는 문제입니다.
이항분포의 확률질량함수는 다음과 같습니다.
$$ P(Y=y | n, \pi) = \binom{n}{y} \pi^y (1-\pi)^{n-y} $$
단, $y > n$인 경우 확률은 0입니다.

### 9.2 가능한 $y$ 값에 따른 MLE 분석

관측 가능한 $y$는 $0, 1, 2, 3$ 중 하나입니다. (단, $n=2$인 모형에서는 $y=3$이 불가능)

**Case 1: $y=3$**
- $n=2$인 모델들은 우도가 0입니다.
- $n=3$인 모델만 비교하면 됩니다.
  - $(3, 0.5): L = \binom{3}{3} (0.5)^3 = 0.125$
  - $(3, 1/3): L = \binom{3}{3} (1/3)^3 \approx 0.037$
- **MLE:** $(n=3, \pi=0.5)$

**Case 2: $y=2$**
- $(2, 0.5): L = \binom{2}{2} (0.5)^2 = 0.25$
- $(2, 1/3): L = \binom{2}{2} (1/3)^2 \approx 0.111$
- $(3, 0.5): L = \binom{3}{2} (0.5)^2 (0.5)^1 = 3 \times 0.125 = 0.375$
- $(3, 1/3): L = \binom{3}{2} (1/3)^2 (2/3)^1 = 3 \times \frac{2}{27} = \frac{6}{27} \approx 0.222$
- **MLE:** $(n=3, \pi=0.5)$ (값: 0.375)

**Case 3: $y=1$**
- $(2, 0.5): L = \binom{2}{1} (0.5)(0.5) = 0.5$
- $(2, 1/3): L = \binom{2}{1} (1/3)(2/3) = 4/9 \approx 0.444$
- $(3, 0.5): L = \binom{3}{1} (0.5)(0.25) = 0.375$
- $(3, 1/3): L = \binom{3}{1} (1/3)(4/9) = 12/27 \approx 0.444$
- **MLE:** $(n=2, \pi=0.5)$ (값: 0.5)

**Case 4: $y=0$**
- $(2, 0.5): L = (0.5)^2 = 0.25$
- $(2, 1/3): L = (2/3)^2 = 4/9 \approx 0.444$
- $(3, 0.5): L = (0.5)^3 = 0.125$
- $(3, 1/3): L = (2/3)^3 = 8/27 \approx 0.296$
- **MLE:** $(n=2, \pi=1/3)$ (값: 0.444)

### 9.3 요약

| 관측값 $y$ | MLE $(n, \pi)$ |
| :---: | :---: |
| 0 | $(2, 1/3)$ |
| 1 | $(2, 0.5)$ |
| 2 | $(3, 0.5)$ |
| 3 | $(3, 0.5)$ |

---

## R Code (검증)

```r
# 모수 공간 정의
params <- list(
  c(n=2, pi=0.5),
  c(n=2, pi=1/3),
  c(n=3, pi=0.5),
  c(n=3, pi=1/3)
)

# 우도 계산 함수
calc_likelihood <- function(y, n, pi) {
  if (y > n) return(0)
  dbinom(y, size = n, prob = pi)
}

# 각 y에 대해 MLE 찾기
y_vals <- 0:3
results <- data.frame()

for (y in y_vals) {
  liks <- sapply(params, function(p) calc_likelihood(y, p['n'], p['pi']))
  best_idx <- which.max(liks)
  best_param <- params[[best_idx]]

  results <- rbind(results, data.frame(
    y = y,
    MLE_n = best_param['n'],
    MLE_pi = round(best_param['pi'], 3),
    Max_Likelihood = round(max(liks), 3)
  ))
}

print(results)
```

---

## 심화 학습 (Deep Understanding)

### 1. 프로파일 우도(Profile Likelihood)
이 문제는 $n$과 $\pi$가 모두 미지의 모수일 때, 이산형 모수 공간에서의 최대우도추정을 다루고 있습니다. 일반적으로 $n$을 모를 때의 추정은 매우 불안정(unstable)한 것으로 알려져 있습니다. 하지만 위처럼 모수 공간이 매우 제한적일 때는 전수 조사(Exhaustive Search)를 통해 명확한 해를 구할 수 있습니다.

### 2. 관측값과 모수의 관계
결과를 보면 $y$가 작을수록 작은 $n$과 작은 $\pi$를, $y$가 클수록 큰 $n$과 큰 $\pi$를 선호하는 경향이 있습니다. 특히 $y=2$일 때 $n=2$ (성공률 100%)보다 $n=3$ (성공률 67%)을 더 선호하는 것은, $\pi=0.5$라는 조건 하에서는 $n=3$에서 2가 나올 확률이 $n=2$에서 2가 나올 확률보다 더 높기 때문입니다($0.375 > 0.25$). 이는 직관과 다를 수 있는 흥미로운 결과입니다.
