# 5. Injury vs Non-injury Accidents (Binomial Probability)



## 문제 (English)

In a certain area, the average number of injury accidents is 1, and the average number of non-injury accidents is 3. If a total of 10 accidents occurred, what is the probability that 2 of them were injury accidents?



---



## 해설 (Korean)



### 5.1 문제 분석 및 분포 설정



사고 발생 건수는 포아송 분포(Poisson Distribution)를 따르는 것이 일반적입니다.

- 부상 사고(Injury)의 평균 발생률: $\lambda_1 = 1$

- 비부상 사고(Non-injury)의 평균 발생률: $\lambda_2 = 3$



두 종류의 사고가 서로 독립적으로 발생한다고 가정하면, 전체 사고 발생률은 $\lambda = \lambda_1 + \lambda_2 = 1 + 3 = 4$ 입니다.



### 5.2 조건부 확률 분포의 유도



문제는 "총 10건의 사고가 발생했을 때($N=10$)", 그중 "부상 사고가 2건($k=2$)일 확률"을 묻고 있습니다.

서로 독립인 두 포아송 확률변수 $X_1 \sim \text{Poisson}(\lambda_1)$과 $X_2 \sim \text{Poisson}(\lambda_2)$의 합이 $N = X_1 + X_2$로 주어졌을 때, $X_1$의 조건부 분포는 **이항 분포(Binomial Distribution)**를 따릅니다.



$$ X_1 | (X_1 + X_2 = N) \sim \text{Binomial}(N, p) $$

여기서 성공 확률 $p$는 다음과 같습니다.

$$ p = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{1}{1 + 3} = \frac{1}{4} = 0.25 $$



### 5.3 확률 계산



따라서 문제는 $B(10, 0.25)$ 분포에서 $X=2$일 확률을 구하는 것입니다.



$$ P(X=2) = \binom{10}{2} p^2 (1-p)^{10-2} $$

$$ = \frac{10 \times 9}{2} (0.25)^2 (0.75)^8 $$

$$ = 45 \times 0.0625 \times (0.75)^8 $$



계산:

- $(0.75)^8 \approx 0.10011$

- $P(X=2) \approx 45 \times 0.0625 \times 0.10011 \approx 0.2815$



**답: 약 0.2815 (28.15%)**



---



## R Code (검증)



```r

# 파라미터 설정

lambda1 <- 1

lambda2 <- 3

N <- 10

k <- 2



# 이항 확률 p 계산

p <- lambda1 / (lambda1 + lambda2)



# 이항분포 확률 계산 (dbinom)

prob <- dbinom(k, size = N, prob = p)



cat("Probability P(X=2 | N=10):", prob, "\n")



# 검증: 포아송 분포 정의를 이용한 직접 계산

# P(X1=k, X2=N-k) / P(X1+X2=N)

prob_direct <- (dpois(k, lambda1) * dpois(N-k, lambda2)) / dpois(N, lambda1+lambda2)

cat("Direct Poisson Calculation:", prob_direct, "\n")

```



---



## 심화 학습 (Deep Understanding)



### 1. 포아송 과정의 분해와 결합 (Splitting and Superposition)

이 문제는 포아송 과정의 기본적인 성질을 보여줍니다.

- **결합(Superposition):** 독립적인 포아송 과정들의 합은 합쳐진 비율($\lambda_{sum}$)을 가진 포아송 과정이 됩니다.

- **조건부 분포:** 총 사건 수가 주어졌을 때, 각 유형의 사건 수는 전체 비율 대비 해당 비율($\lambda_i / \lambda_{sum}$)을 성공 확률로 하는 이항 분포(또는 다항 분포)를 따릅니다.

이 성질은 로지스틱 회귀분석이나 로그선형모형에서 포아송 분포 가정과 다항 분포 가정이 서로 호환(Equivalent)됨을 보이는 이론적 기초입니다. 즉, 전체 표본 크기 $N$을 고정하면 포아송 로그선형모형은 다항 로짓 모형과 동일한 추론 결과를 낳습니다.



### 2. 분할표 분석으로의 확장

사고 유형(부상/비부상)을 $2 \times 1$ 분할표로 생각할 수 있습니다. 관측 도수가 $(2, 8)$일 때, 귀무가설 $H_0: p=0.25$에 대한 정확 검정(Exact Binomial Test)을 수행하는 것과 논리적으로 같습니다.
