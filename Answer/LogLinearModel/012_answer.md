# 12. MLE of Poisson Probability P(Y=0)



## 문제 (English)

If $Y_1, \dots, Y_n \sim \text{i.i.d. } \text{Poisson}(\lambda)$, Find the MLE of $P(Y_1=0)$.



---



## 해설 (Korean)



### 12.1 목표 설정



구하고자 하는 모수는 $\theta = P(Y_1=0)$ 입니다.

포아송 분포의 확률질량함수 $P(Y=y) = \frac{e^{-\lambda} \lambda^y}{y!}$ 에서 $y=0$을 대입하면:

$$ \theta = e^{-\lambda} $$

따라서 $\lambda$의 MLE인 $\hat{\lambda}$를 구한 뒤, MLE의 불변성(Invariance Property)을 이용하여 $\hat{\theta}$를 구할 수 있습니다.



### 12.2 $\lambda$의 MLE 도출



우도함수:

$$ L(\lambda) = \prod_{i=1}^n \frac{e^{-\lambda} \lambda^{y_i}}{y_i!} = \frac{e^{-n\lambda} \lambda^{\sum y_i}}{\prod y_i!} $$

로그우도함수:

$$ \ell(\lambda) = -n\lambda + (\sum y_i) \log \lambda - \sum \log y_i! $$

미분 및 최적화:

$$ \frac{d \ell}{d \lambda} = -n + \frac{\sum y_i}{\lambda} = 0 $$

$$ \hat{\lambda} = \frac{\sum y_i}{n} = \bar{y} $$



### 12.3 불변성(Invariance Property) 적용



MLE의 중요한 성질 중 하나는 **불변성**입니다. 만약 $\hat{\lambda}$가 $\lambda$의 MLE이고 $g(\cdot)$가 일대일 함수(또는 그보다 넓은 조건)라면, $g(\lambda)$의 MLE는 $g(\hat{\lambda})$입니다.



구하고자 하는 값은 $g(\lambda) = e^{-\lambda}$ 이므로:

$$ \widehat{P(Y=0)} = e^{-\hat{\lambda}} = e^{-\bar{y}} $$



**답:** $e^{-\bar{y}}$



---



## R Code (검증)



```r

# 데이터 생성 (lambda=2)

set.seed(123)

y <- rpois(100, lambda = 2)



# 1. 이론적 MLE 계산

lambda_hat <- mean(y)

mle_theta <- exp(-lambda_hat)



# 2. 수치적 최적화로 검증 (Direct Optimization)

# theta = P(Y=0) = exp(-lambda) => lambda = -log(theta)

# Likelihood function in terms of theta

neg_log_lik <- function(theta, y) {

  lambda <- -log(theta)

  if(lambda < 0) return(Inf)

  # Poisson log-likelihood

  -sum(dpois(y, lambda, log=TRUE))

}



opt <- optimize(neg_log_lik, interval=c(0.001, 0.999), y=y)



cat("Theoretical MLE:", mle_theta, "\n")

cat("Numerical MLE:", opt$minimum, "\n")

```



---



## 심화 학습 (Deep Understanding)



### 1. 최소분산 비편향 추정량(MVUE)와의 비교

$e^{-\bar{y}}$는 MLE이지만 편의(Biased) 추정량입니다. (왜냐하면 $E[e^{-\bar{Y}}] \neq e^{-E[\bar{Y}]}$ due to Jensen's inequality).

포아송 분포에서 $\theta = e^{-\lambda}$의 비편향 추정량(MVUE)은 다음과 같이 주어집니다.

$$ T = \left( \frac{n-1}{n} \right)^{\sum y_i} $$

표본 크기 $n$이 커지면 $(1 - 1/n)^{n\bar{y}} \approx (e^{-1})^{\bar{y}} = e^{-\bar{y}}$가 되어 MLE에 수렴합니다.



### 2. 점근적 성질

MLE인 $e^{-\bar{y}}$는 일치성(Consistency)과 점근적 정규성(Asymptotic Normality)을 가집니다. 델타 방법(Delta Method)을 이용하면 이 추정량의 분산을 근사할 수 있습니다.

$$ \text{Var}(\hat{\theta}) \approx [g'(\lambda)]^2 \text{Var}(\hat{\lambda}) = (-e^{-\lambda})^2 \frac{\lambda}{n} = \frac{\lambda e^{-2\lambda}}{n} $$
