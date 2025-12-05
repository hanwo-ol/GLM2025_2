# 14. Local Government Survey (Confidence Interval)



## 문제 (English)

In a public opinion survey evaluating the local government system, out of 500 respondents, 165 gave a positive response. Construct a 95% confidence interval for the proportion of people in the entire population who have a positive opinion about the local government system.

($p = 165/500 = 0.33$, $s.e.(p) = 0.012$)



---



## 해설 (Korean)



### 14.1 통계량 계산



- 표본 크기 ($n$): 500

- 긍정 응답 수 ($y$): 165

- 표본 비율 ($\hat{p}$): $165 / 500 = 0.33$



표준오차 ($s.e.(\hat{p})$):

Wald 방식의 표준오차 공식을 사용합니다.

$$ s.e. = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.33 \times 0.67}{500}} = \sqrt{\frac{0.2211}{500}} = \sqrt{0.0004422} \approx 0.0210 $$



*(주의: 문제 지문에 $s.e.(p)=0.012$라고 되어 있으나, 직접 계산한 값 $0.021$과 다릅니다. $0.012$는 $n$이 훨씬 크거나 다른 수치일 때 나옵니다. 예를 들어 $n \approx 1500$이면 $0.012$가 됩니다. 여기서는 주어진 데이터($n=500, p=0.33$)를 기준으로 직접 계산한 표준오차를 사용하여 풀이합니다.)*

*혹시 $s.e.$ 계산 오류?* $\sqrt{0.33 \times 0.67 / 500} \approx 0.021$.

만약 $s.e.=0.012$를 따르려면 $n$이 약 1535명이어야 합니다. 문제의 $n=500$을 신뢰하고 직접 계산합니다.



### 14.2 95% 신뢰구간 (Wald Interval)



95% 신뢰수준에 해당하는 $Z$값($z_{0.025}$)은 1.96입니다.



$$ \hat{p} \pm 1.96 \times s.e.(\hat{p}) $$

$$ 0.33 \pm 1.96 \times 0.0210 $$

$$ 0.33 \pm 0.0412 $$



하한: $0.33 - 0.0412 = 0.2888$

상한: $0.33 + 0.0412 = 0.3712$



**답:** 95% 신뢰구간은 약 **(0.289, 0.371)**, 즉 **28.9% ~ 37.1%** 입니다.



---



## R Code (검증)



```r

# 데이터

n <- 500

y <- 165

p_hat <- y/n



# 1. Wald Interval (Manual)

se_wald <- sqrt(p_hat * (1 - p_hat) / n)

ci_wald <- c(p_hat - 1.96 * se_wald, p_hat + 1.96 * se_wald)



cat("Calculated SE:", se_wald, "\n")

cat("Wald CI:", ci_wald, "\n")



# 2. Score Interval (Wilson) - More robust

# prop.test uses Wilson score interval implicitly usually or similar approximation

ci_prop <- prop.test(y, n)$conf.int

cat("Wilson Score CI (prop.test):", ci_prop, "\n")

```



---



## 심화 학습 (Deep Understanding)



### 1. Wald 신뢰구간의 한계

$\hat{p} \pm z \sqrt{\hat{p}(1-\hat{p})/n}$ 공식(Wald Interval)은 간단하지만, $n$이 작거나 $p$가 0 또는 1에 가까울 때 커버리지 확률(Coverage Probability)이 95%보다 낮아지는 문제가 있습니다.



### 2. 대안: 윌슨 스코어 구간 (Wilson Score Interval)

이러한 문제를 해결하기 위해, 신뢰구간을 구할 때 표준오차 분모에 모비율 $p$를 그대로 두고 2차 방정식을 푸는 **Score Interval (Wilson Interval)**이 권장됩니다.

$$ \tilde{p} = \frac{y + z^2/2}{n + z^2} $$

Agresti-Coull 구간도 이와 유사하게 "성공 2회, 실패 2회"를 데이터에 추가하여 계산하는 방식으로, 성능이 우수합니다.
