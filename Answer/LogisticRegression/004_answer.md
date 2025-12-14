# 4. Draft Position and All-Star Probability

## 문제 (English)
A study for several professional sports of the effect of a player’s draft position $d$ ($d=1,2,3,\dots$) of selection from the pool of potential players in a given year on the probability $\pi$ of eventually being named an all-star used the model

$$ \text{logit}(\pi) = \alpha + \beta \log d $$

(S.M. Berry, Chance, 14:53-57, 2001).

a. Show that $\pi(1-\pi)^E = e^{\alpha} d^{\beta}$. (Note: The provided text says $\pi(1-\pi)^E$, but based on context it likely implies Odds or a typo.

+ Let's inspect the math.
+ Logit is $\log(\pi/(1-\pi))$. So $\pi/(1-\pi) = e^{\alpha+\beta \log d} = e^\alpha (e^{\log d})^\beta = e^\alpha d^\beta$.
+ The original text seems to have a typo "E" instead of nothing or $-1$.
+ Let's assume it asks to show the Odds relationship: $\text{Odds} = e^\alpha d^\beta$.)

b. In the United States, Berry reported $\hat{\alpha}=2.3$ and $\hat{\beta}=-1.1$ for pro basketball and $\hat{\alpha}=0.7$ and $\hat{\beta}=-0.6$ for pro baseball. This suggests that in basketball a first draft picks with high $d$ are relatively less likely to be all-stars. Explain why.

---

## 해설 (Korean)

### 4.1 문항 a. 수식 유도

문제의 모델은 로그 오즈(Log Odds)가 $d$의 로그값에 선형적으로 비례한다고 가정합니다.

$$ \ln \left( \frac{\pi}{1-\pi} \right) = \alpha + \beta \ln d $$

양변에 지수함수(Exponential)를 취하면:

$$ \frac{\pi}{1-\pi} = \exp(\alpha + \beta \ln d) $$

$$ \frac{\pi}{1-\pi} = e^{\alpha} \cdot e^{\beta \ln d} $$

로그의 성질 $a \ln x = \ln (x^a)$와 $e^{\ln k} = k$를 이용하면:

$$ \frac{\pi}{1-\pi} = e^{\alpha} \cdot d^{\beta} $$

문제 원문의 $\pi(1-\pi)^E$는 $\pi / (1-\pi)$ 즉, **오즈(Odds)**를 의미하는 것으로 보입니다 (오타 추정: E가 exponent $-1$을 의미하거나 Odds의 O를 잘못 표기했을 가능성).
따라서 **오즈(Odds)**는 드래프트 순위 $d$의 거듭제곱(Power function) 형태를 따릅니다.

### 4.2 문항 b. 농구와 야구의 비교 해석

주어진 계수:
- **농구 (Basketball):** $\alpha = 2.3, \beta = -1.1$

$$ \text{Odds}_{BK} = e^{2.3} d^{-1.1} \approx 9.97 \times \frac{1}{d^{1.1}} $$

- **야구 (Baseball):** $\alpha = 0.7, \beta = -0.6$

$$ \text{Odds}_{BB} = e^{0.7} d^{-0.6} \approx 2.01 \times \frac{1}{d^{0.6}} $$

**해석:**
1.  **초기 기대치 ($\alpha$):** $d=1$(드래프트 1순위)일 때의 오즈는 농구가 $e^{2.3} \approx 10$으로 야구 $e^{0.7} \approx 2$보다 훨씬 높습니다. 즉, 농구 1순위는 올스타가 될 확률이 매우 높습니다.
2.  **감소 속도 ($\beta$):** $\beta$의 절댓값은 순위 $d$가 뒤로 밀릴 때 오즈가 얼마나 급격히 떨어지는지를 나타냅니다.
    - 농구($-1.1$)는 야구($-0.6$)보다 절댓값이 큽니다.
    - 이는 $d$가 증가함에 따라 성공 확률이 **훨씬 더 가파르게 감소함**을 의미합니다.
    - 즉, 농구에서는 드래프트 상위 순번과 하위 순번의 실력 격차가 매우 크며, 예측 가능성이 높습니다. 반면 야구는 하위 순번에서도 올스타가 나올 확률이 상대적으로 천천히 줄어듭니다(예측이 더 어렵고 의외성이 많음).

**결론:**
농구에서 높은 숫자 $d$(하위 픽)를 가진 선수들은 야구의 동일 순번 선수들에 비해 올스타가 될 가능성이 상대적으로 더 희박합니다. 이는 농구가 야구보다 개인의 신체적 능력(키, 운동신경 등) 의존도가 높아 스카우팅 실패 확률이 낮거나, 주전 선수의 수가 적어 진입 장벽이 높기 때문일 수 있습니다.

---

## R Code 및 실습

```r
# 파라미터 정의
alpha_bk <- 2.3; beta_bk <- -1.1
alpha_bb <- 0.7; beta_bb <- -0.6

# 드래프트 순위 벡터
d <- 1:100

# 오즈 계산
odds_bk <- exp(alpha_bk) * d^beta_bk
odds_bb <- exp(alpha_bb) * d^beta_bb

# 확률 변환
prob_bk <- odds_bk / (1 + odds_bk)
prob_bb <- odds_bb / (1 + odds_bb)

# 시각화
plot(d, prob_bk, type = "l", col = "red", lwd = 2, ylim = c(0, 1),
     xlab = "Draft Position (d)", ylab = "Probability of All-Star",
     main = "Draft Position Effect: Basketball vs Baseball")
lines(d, prob_bb, col = "blue", lwd = 2)
legend("topright", legend = c("Basketball", "Baseball"), col = c("red", "blue"), lwd = 2)

# d=10, d=50 비교
cat("Basketball Prob (d=1, 10, 50):", prob_bk[c(1, 10, 50)], "\n")
cat("Baseball Prob (d=1, 10, 50):", prob_bb[c(1, 10, 50)], "\n")
```

---

## 심화 학습 (Deep Understanding)

### 1. 멱법칙(Power Law) 분포
오즈가 $A \cdot d^{\beta}$ 형태를 띤다는 것은 드래프트 순위와 성공 확률 사이에 **멱법칙(Power Law)** 관계가 성립함을 의미합니다. 이는 자연계나 사회 현상(소득 분배, 도시 인구 등)에서 흔히 발견되는 분포입니다. 농구의 $\beta \approx -1$은 Zipf's Law와 유사한 급격한 불평등 구조를 보여줍니다.

### 2. 스포츠 분석(Sports Analytics)의 함의
이 결과는 드래프트 픽의 가치(Trade Value)를 산정하는 데 사용될 수 있습니다. 농구에서는 1라운드 상위 픽의 가치가 압도적으로 높으므로 트레이드 시 하위 픽 여러 장보다 상위 픽 1장이 더 중요할 수 있습니다. 반면 야구는 "복권 긁기" 전략으로 하위 픽을 많이 모으는 전략이 상대적으로 유효할 수 있음을 시사합니다.
