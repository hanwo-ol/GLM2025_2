# 8. Likelihood Function of Uniform Distribution



## 문제 (English)

Let $X \sim U(0, \theta)$, then draw the likelihood function of $\theta$ when the observed value of $X$ is $x$.



---



## 해설 (Korean)



### 8.1 균일분포의 확률밀도함수



확률변수 $X$가 균일분포 $U(0, \theta)$를 따를 때, 확률밀도함수(PDF)는 다음과 같습니다.

$$ f(x; \theta) = \begin{cases} \frac{1}{\theta} & \text{if } 0 \le x \le \theta \\ 0 & \text{otherwise} \end{cases} $$

이를 지시함수(Indicator function) $I(\cdot)$를 사용하여 표현하면 더 명확합니다.

$$ f(x; \theta) = \frac{1}{\theta} I(0 \le x \le \theta) $$



### 8.2 우도함수 (Likelihood Function)



관측된 값이 $x$ 하나일 때, 우도함수 $L(\theta)$는 $\theta$에 대한 함수로서 $f(x; \theta)$와 같습니다.

$$ L(\theta) = \frac{1}{\theta} I(x \le \theta) $$

(단, $\theta > 0$ 이며, $x$는 이미 관측되었으므로 $x \ge 0$ 상수로 취급합니다. $\theta$는 반드시 $x$보다 크거나 같아야 합니다. 만약 $\theta < x$라면 확률밀도는 0이 됩니다.)



**그래프 개형:**

- 정의역: $\theta \in [x, \infty)$

- 치역: $L(\theta) = 1/\theta$ (감소함수)

- $\theta < x$인 구간에서는 $L(\theta) = 0$.



따라서 우도함수는 $\theta = x$에서 최댓값 $1/x$를 갖고, $\theta$가 증가함에 따라 $1/\theta$ 곡선을 따라 0으로 수렴하는 형태입니다.



**최대우도추정량 (MLE):**

우도함수 $L(\theta)$를 최대화하는 값은 정의된 구간의 하한인 $\hat{\theta} = x$ 입니다.

(만약 표본이 여러 개 $X_1, \dots, X_n$라면 $\hat{\theta} = \max(X_i)$가 됩니다.)



---



## R Code (시각화)



```r

# 데이터 관측값 예시

x_obs <- 2



# 우도함수 정의

likelihood <- function(theta, x) {

  ifelse(theta < x, 0, 1/theta)

}



# 그래프 그리기

theta_vals <- seq(0, 10, by = 0.01)

lik_vals <- likelihood(theta_vals, x_obs)



plot(theta_vals, lik_vals, type = "l", lwd = 2, col = "blue",

     main = paste("Likelihood Function for U(0, theta) given x =", x_obs),

     xlab = "theta", ylab = "L(theta)")

abline(v = x_obs, col = "red", lty = 2)

text(x_obs, 0.1, paste("MLE =", x_obs), pos = 4, col = "red")

```



---



## 심화 학습 (Deep Understanding)



### 1. 정칙 조건(Regularity Conditions)의 위배

이 문제는 최대우도추정의 일반적인 이론(미분 가능성, Score equation = 0)이 적용되지 않는 대표적인 사례입니다.

- 우도함수의 지지집합(Support)인 $[0, \theta]$가 모수 $\theta$에 의존하므로, $\theta$에 대해 미분할 수 없는 지점($x$)에서 최댓값이 발생합니다.

- 따라서 MLE의 점근 분포가 정규분포를 따르지 않으며(Asymptotic Normality 위배), 표준오차를 구하는 방식도 피셔 정보(Fisher Information)를 이용할 수 없습니다.



### 2. 충분통계량

여러 표본이 있을 때 $T = \max(X_i)$는 $\theta$에 대한 충분통계량입니다. 우도함수가 $L(\theta) = \theta^{-n} I(\max(x_i) \le \theta)$ 꼴이 되기 때문입니다.
