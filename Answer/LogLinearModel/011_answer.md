# 11. MLE of Normal Mean (Known Variance)



## 문제 (English)

If $Y_1, \dots, Y_n \sim \text{i.i.d. } N(\mu, 1)$, find the MLE of $\mu$.



---



## 해설 (Korean)



### 11.1 우도함수 설정



정규분포 $N(\mu, 1)$의 확률밀도함수는 $f(y; \mu) = \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{(y-\mu)^2}{2} \right)$ 입니다.

$n$개의 독립 표본에 대한 우도함수는 다음과 같습니다.

$$ L(\mu) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi}} \exp\left( -\frac{(y_i-\mu)^2}{2} \right) $$

$$ L(\mu) = (2\pi)^{-n/2} \exp\left( -\frac{1}{2} \sum_{i=1}^n (y_i-\mu)^2 \right) $$



### 11.2 로그우도함수 미분



로그를 취하여 곱을 합으로 바꿉니다.

$$ \ell(\mu) = -\frac{n}{2} \log(2\pi) - \frac{1}{2} \sum_{i=1}^n (y_i - \mu)^2 $$



$\mu$에 대해 미분합니다.

$$ \frac{d \ell}{d \mu} = -\frac{1}{2} \sum_{i=1}^n 2(y_i - \mu)(-1) $$

$$ = \sum_{i=1}^n (y_i - \mu) $$

$$ = \sum_{i=1}^n y_i - n\mu $$



### 11.3 최적화 (MLE 도출)



$$ \sum_{i=1}^n y_i - n\hat{\mu} = 0 $$

$$ n\hat{\mu} = \sum_{i=1}^n y_i $$

$$ \hat{\mu} = \frac{1}{n} \sum_{i=1}^n y_i = \bar{y} $$



**답:** $\hat{\mu}_{MLE} = \bar{y}$ (표본 평균)



---



## 심화 학습 (Deep Understanding)



### 1. 최소제곱법(Least Squares)과의 관계

로그우도함수를 최대화하는 것은 오차 제곱합 $\sum (y_i - \mu)^2$을 최소화하는 것과 수학적으로 동일합니다. 이는 정규분포 가정 하에서 MLE와 LSE(Least Squares Estimator)가 일치함을 보여주는 가장 기본적인 예시입니다.



### 2. 분산이 미지수인 경우

만약 분산 $\sigma^2$도 미지수라면, $\mu$와 $\sigma^2$에 대해 편미분 연립방정식을 풀어야 합니다. 이때 $\hat{\mu}$는 여전히 $\bar{y}$이지만, $\hat{\sigma}^2$는 $S^2$ (표본분산, $n-1$로 나눔)가 아니라 $\frac{1}{n}\sum(y_i-\bar{y})^2$ (편의추정량)이 됩니다.
