# 16. Wald, Score, and Likelihood Ratio Tests for Normal Mean



## 문제 (English)

Let $X_1, \dots, X_n \sim \text{i.i.d. } N(\mu, \sigma_0^2)$, Find the Wald, Score, and Likelihood Ratio test statistics for the hypotheses:

$H_0: \mu = \mu_0$ vs $H_1: \mu \neq \mu_0$, with $\sigma_0$ known.



---



## 해설 (Korean)



### 16.1 기본 설정



- 로그우도함수:

  $$ \ell(\mu) = -\frac{n}{2}\log(2\pi\sigma_0^2) - \frac{1}{2\sigma_0^2}\sum_{i=1}^n(x_i - \mu)^2 $$

- 1차 미분 (Score Function):

  $$ U(\mu) = \ell'(\mu) = \frac{1}{\sigma_0^2}\sum(x_i - \mu) = \frac{n(\bar{x} - \mu)}{\sigma_0^2} $$

- 2차 미분 및 피셔 정보량 (Fisher Information):

  $$ \ell''(\mu) = -\frac{n}{\sigma_0^2} $$

  $$ I(\mu) = -E[\ell''(\mu)] = \frac{n}{\sigma_0^2} $$

- MLE: $\hat{\mu} = \bar{x}$



### 16.2 Wald 통계량 ($W$)



Wald 검정은 MLE $\hat{\mu}$와 귀무가설값 $\mu_0$의 차이를 표준오차로 표준화한 것입니다.

$$ W = (\hat{\mu} - \mu_0)^2 I(\hat{\mu}) $$

$$ W = (\bar{x} - \mu_0)^2 \frac{n}{\sigma_0^2} = \left( \frac{\bar{x} - \mu_0}{\sigma_0/\sqrt{n}} \right)^2 $$



이는 표준정규분포를 따르는 $Z$ 통계량의 제곱과 같습니다.



### 16.3 Score 통계량 ($S$)



Score 검정은 귀무가설값 $\mu_0$에서의 기울기(Score) 크기를 봅니다.

$$ S = \frac{[U(\mu_0)]^2}{I(\mu_0)} $$

$$ U(\mu_0) = \frac{n(\bar{x} - \mu_0)}{\sigma_0^2} $$

$$ I(\mu_0) = \frac{n}{\sigma_0^2} $$



대입하면:

$$ S = \frac{\left[ \frac{n(\bar{x} - \mu_0)}{\sigma_0^2} \right]^2}{\frac{n}{\sigma_0^2}} = \frac{n^2(\bar{x} - \mu_0)^2}{\sigma_0^4} \times \frac{\sigma_0^2}{n} = \frac{n(\bar{x} - \mu_0)^2}{\sigma_0^2} $$

$$ S = \left( \frac{\bar{x} - \mu_0}{\sigma_0/\sqrt{n}} \right)^2 $$



### 16.4 우도비 통계량 (Likelihood Ratio Statistic, $G^2$)



$$ \lambda = -2 [\ell(\mu_0) - \ell(\hat{\mu})] $$



로그우도의 차이 계산:

$$ \ell(\hat{\mu}) - \ell(\mu_0) = \left[ -\frac{1}{2\sigma_0^2}\sum(x_i - \bar{x})^2 \right] - \left[ -\frac{1}{2\sigma_0^2}\sum(x_i - \mu_0)^2 \right] $$

여기서 $\sum(x_i - \mu_0)^2 = \sum(x_i - \bar{x} + \bar{x} - \mu_0)^2 = \sum(x_i - \bar{x})^2 + n(\bar{x} - \mu_0)^2$ 임을 이용합니다.

$$ \ell(\hat{\mu}) - \ell(\mu_0) = -\frac{1}{2\sigma_0^2} \left[ \sum(x_i - \bar{x})^2 - \left( \sum(x_i - \bar{x})^2 + n(\bar{x} - \mu_0)^2 \right) \right] $$

$$ = -\frac{1}{2\sigma_0^2} [ -n(\bar{x} - \mu_0)^2 ] = \frac{n(\bar{x} - \mu_0)^2}{2\sigma_0^2} $$



따라서 검정 통계량은:

$$ G^2 = 2 \times \frac{n(\bar{x} - \mu_0)^2}{2\sigma_0^2} = \frac{n(\bar{x} - \mu_0)^2}{\sigma_0^2} $$

$$ G^2 = \left( \frac{\bar{x} - \mu_0}{\sigma_0/\sqrt{n}} \right)^2 $$



### 16.5 결론



정규분포의 평균에 대한 추론(분산이 알려진 경우)에서는 **Wald, Score, Likelihood Ratio 통계량이 모두 동일**합니다.

$$ W = S = G^2 = Z^2 $$

이들은 모두 자유도 1인 카이제곱 분포 $\chi^2(1)$을 따릅니다.



---



## 심화 학습 (Deep Understanding)



### 1. 세 통계량의 기하학적 의미

- **Wald:** 우도함수의 최댓값($\hat{\mu}$)에서 $x$축 거리($\hat{\mu} - \mu_0$)를 2차 곡률(정보량)로 가중치 둔 것. (가로축 기준)

- **Score:** 귀무가설($\mu_0$) 지점에서의 기울기. (기울기 기준)

- **Likelihood Ratio:** 최댓값과 귀무가설값의 $y$축(로그우도) 높이 차이. (세로축 기준)



정규분포의 로그우도함수는 완벽한 2차 곡선(Parabola)이므로, 이 세 가지 관점이 수학적으로 정확히 일치하는 결과가 나옵니다. 하지만 비선형적인 일반화 선형 모형(GLM) 등에서는 세 값이 서로 다를 수 있으며, 표본이 작을 때는 우도비 검정($G^2$)이 가장 신뢰할 만합니다.
