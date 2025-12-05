# 15. Anticancer Drug Test (Exact Test & Mid-P)



## 문제 (English)

The previous highest cure rate is 0.3. A new anticancer drug was tested on $n=13$ patients, and $y=7$ were cured ($\ge 5$-year survival). Test whether the new drug is more effective than the old one. Compute both the p-value and the mid-p value.



---



## 해설 (Korean)



### 15.1 가설 설정



- 귀무가설 ($H_0$): $\pi = 0.3$ (신약의 효과는 기존과 같다)

- 대립가설 ($H_1$): $\pi > 0.3$ (신약의 효과가 더 좋다, 단측 검정)

- 관측 데이터: $n=13, y=7$



### 15.2 P-값 계산 (Exact Binomial Test)



표본 크기가 작으므로($n=13$) 정규 근사 대신 이항분포를 이용한 정확 검정을 수행합니다.

P-값은 귀무가설 하에서 관측된 값 $y=7$ 이상이 나올 확률입니다.



$$ P(Y \ge 7 | n=13, \pi=0.3) = \sum_{k=7}^{13} \binom{13}{k} (0.3)^k (0.7)^{13-k} $$



계산:

- $P(Y=7) = \binom{13}{7} (0.3)^7 (0.7)^6 \approx 1716 \times 0.0002187 \times 0.1176 \approx 0.04415$

- $P(Y=8) = \binom{13}{8} (0.3)^8 (0.7)^5 \approx 1287 \times 0.0000656 \times 0.1680 \approx 0.01419$

- $P(Y=9) \approx 0.00337$

- ...

- 합계 $P(Y \ge 7) \approx 0.0624$ (R의 `pbinom` 이용 권장)



**Exact P-value:** $\approx 0.0624$



### 15.3 Mid-P 값 계산



이산형 분포에서의 P-값은 보수적(Conservative)인 경향이 있어, 제1종 오류 확률이 유의수준보다 낮아집니다. 이를 보정하기 위해 관측값 확률의 절반만을 포함하는 **Mid-P Value**를 사용합니다.



$$ \text{Mid-P} = P(Y > 7) + \frac{1}{2} P(Y=7) $$

$$ = [P(Y \ge 7) - P(Y=7)] + 0.5 \times P(Y=7) $$

$$ = P(Y \ge 7) - 0.5 \times P(Y=7) $$



값 대입:

- $P(Y \ge 7) \approx 0.0624$

- $P(Y=7) \approx 0.0442$



$$ \text{Mid-P} \approx 0.0624 - 0.5 \times 0.0442 = 0.0624 - 0.0221 = 0.0403 $$



**Mid-P Value:** $\approx 0.0403$



### 15.4 결론



- **Exact P-value (0.0624):** 유의수준 0.05에서 귀무가설을 기각할 수 없습니다. 효과가 입증되지 않았습니다.

- **Mid-P Value (0.0403):** 유의수준 0.05에서 귀무가설을 기각할 수 있습니다. 효과가 있다고 볼 여지가 있습니다.



이처럼 표본이 작을 때 어떤 P-값을 쓰느냐에 따라 결론이 달라질 수 있습니다. 보수적인 관점에서는 기각 실패이지만, 탐색적 관점에서는 추가 연구가 필요함을 시사합니다.



---



## R Code (검증)



```r

n <- 13

y <- 7

pi_0 <- 0.3



# 1. Exact Binomial Test

# P(Y >= 7) = 1 - P(Y <= 6)

p_exact <- 1 - pbinom(6, size = n, prob = pi_0)



# 2. Mid-P Value

prob_y <- dbinom(y, size = n, prob = pi_0)

p_mid <- p_exact - 0.5 * prob_y



cat("Exact P-value:", round(p_exact, 5), "\n")

cat("Mid-P value:", round(p_mid, 5), "\n")



# binom.test 함수 (Exact)

print(binom.test(y, n, p = pi_0, alternative = "greater"))

```



---



## 심화 학습 (Deep Understanding)



### 1. Mid-P Value의 통계적 성질

Mid-P 값은 귀무가설 하에서 그 기대값이 정확히 0.5가 되는 성질(즉, 균일분포에 더 가깝게 근사)이 있습니다. 따라서 점근적으로 제1종 오류율을 명목 유의수준($\alpha$)에 더 가깝게 유지합니다. 반면 Exact P-value는 이산성 때문에 실제 오류율이 $\alpha$를 초과하지 않도록 보장하지만, 너무 낮아질 수 있어 검정력(Power) 손실이 발생합니다.



### 2. 임상시험에서의 의사결정

이 사례처럼 P-값이 경계선(0.04~0.06)에 있을 때, 단순히 "기각 실패"로 끝내기보다는 효과 크기(Effect Size, 여기서는 $7/13 \approx 0.54$ vs $0.3$)와 표본 크기를 고려해야 합니다. 13명 중 과반수가 완치되었다는 것은 임상적으로 매우 의미 있는 신호일 수 있으므로, 더 큰 규모의 후속 연구가 강력히 권장됩니다.
