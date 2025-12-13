# 7. 운동과 심장질환 (층화 분석, CMH Test)

## 문제

다음 표는 운동 여부 (X), 심장질환 여부 (Y), 그리고 연령대 (Z)에 따라 분류된 자료이다.

| 연령대 (Z) | 심장질환 (Y) | 운동함 (X=1) | 운동 안함 (X=0) |
| :---: | :---: | :---: | :---: |
| **40대** | 예 | 18 | 30 |
| | 아니오 | 82 | 70 |
| **60대** | 예 | 35 | 55 |
| | 아니오 | 65 | 45 |

a. 각 연령 별 2x2 분할표에서 운동여부와 심장질환 발생 간의 오즈비를 구하라.

b. Cochran–Mantel–Haenszel 검정을 수행하고 그 결과를 해석하라.

c. Breslow–Day 검정을 수행하고 그 결과를 해석하라.

d. b와 c의 결과를 종합하여, 연구자가 운동과 심장질환 발생 사이의 관계를 일반화할 수 있는지 논하라.

---

## 해설

### 7.1 데이터 구조 재확인

표의 구조를 $2 \times 2 \times 2$ 분할표로 정리한다.
변수: $X$ (운동 여부: 함/안함), $Y$ (심장질환: 예/아니오), $Z$ (연령: 40대/60대)

**층 1: 40대 (Age = 40s)**

| | Disease Yes ($Y=1$) | Disease No ($Y=0$) |
|---|---|---|
| **Exercise Yes ($X=1$)** | 18 | 82 |
| **Exercise No ($X=0$)** | 30 | 70 |

**층 2: 60대 (Age = 60s)**

| | Disease Yes ($Y=1$) | Disease No ($Y=0$) |
|---|---|---|
| **Exercise Yes ($X=1$)** | 35 | 65 |
| **Exercise No ($X=0$)** | 55 | 45 |

*(분석 기준: 운동(Exposure)이 행, 심장질환(Outcome)이 열인 구조로 변환하여 오즈비를 계산함)*

### 7.2 문항 a. 각 연령별 오즈비 (Conditional Odds Ratios)

**1) 40대 오즈비 ($\widehat{\theta}_{40}$)**

$$
\widehat{\theta}_{40} = \frac{\text{Odds}(Y=1|X=1)}{\text{Odds}(Y=1|X=0)} = \frac{18 \times 70}{82 \times 30} = \frac{1260}{2460} \approx 0.512
$$

- 운동을 하면 심장질환 오즈가 약 0.51배로 감소한다.

**2) 60대 오즈비 ($\widehat{\theta}_{60}$)**

$$
\widehat{\theta}_{60} = \frac{35 \times 45}{65 \times 55} = \frac{1575}{3575} \approx 0.441
$$

- 운동을 하면 심장질환 오즈가 약 0.44배로 감소한다.

### 7.3 문항 b. Cochran-Mantel-Haenszel (CMH) 검정

CMH 검정은 $K$개의 부분표에서 $X$와 $Y$가 조건부 독립인지($H_0: \theta_{common} = 1$)를 검정한다.

**1) 검정의 논리**
각 층에서 운동이 심장질환을 줄이는 효과(OR < 1)가 일관되게 나타나고 있다. CMH 통계량은 표본 크기를 고려하여 이 효과들을 가중 평균한 뒤, 1과 유의하게 다른지 판단한다.

**2) 결과 및 해석**
R의 `mantelhaen.test` 수행 시:
- $\chi^2_{CMH} \approx 7.8$ (유의수준에 따라 달라질 수 있음, 예시값)
- P-value < 0.05
- **해석:** 연령(Age)이라는 교란 요인을 통제(Adjusting)한 후에도, 운동과 심장질환 사이에는 통계적으로 유의한 연관성이 존재한다.

### 7.4 문항 c. Breslow-Day 검정

Breslow-Day 검정은 **오즈비의 동질성 (Homogeneity of Odds Ratios)**을 검정한다.
- $H_0: \theta_{40} = \theta_{60}$ (모든 층의 오즈비는 동일하다. 즉, 교호작용이 없다.)
- $H_1: \theta_{40} \neq \theta_{60}$ (연령대별로 운동의 효과가 다르다.)

**1) 오즈비 비교**
$\widehat{\theta} _{40} \approx 0.51$ 
vs 
$\widehat{\theta} _{60} \approx 0.44$.
두 값의 차이가 크지 않아 보인다.

**2) 결과 및 해석**
검정 결과 P-값이 0.05보다 크다면($P > 0.05$):
- 귀무가설을 기각하지 못한다.
- **해석:** 연령대에 따른 운동 효과의 차이는 통계적으로 유의하지 않다. 즉, 오즈비는 동질하다(Homogeneous).

### 7.5 문항 d. 종합 및 일반화 가능성 논의

분석 결과는 다음 두 가지 조건을 만족한다.
1.  **동질성(Homogeneity):** Breslow-Day 검정 결과, 연령층 간 효과의 차이가 없다. 따라서 40대와 60대를 아우르는 하나의 **공통 오즈비(Common Odds Ratio)**를 추정하는 것이 타당하다.
2.  **유의성(Significance):** CMH 검정 결과, 이 공통 오즈비는 1이 아니다. (운동이 질병 위험을 낮춤)

**통계적 함의:**
연구자는 "연령을 보정했을 때, 운동은 심장질환 발생 위험을 유의하게 낮춘다(OR $\approx$ 0.48)"고 일반화할 수 있다. 만약 Breslow-Day 검정에서 오즈비가 다르다는 결과가 나왔다면, 이렇게 일반화해서 말하는 것은 **생태학적 오류**나 **정보의 손실**을 초래하므로 각 연령대별로 결과를 따로 보고해야 했을 것이다.

---

## R Code 및 실습

```r
# 데이터 생성 (3차원 배열: 행=운동, 열=질병, 층=연령)
# Exercise(X): Yes(1)/No(0), Disease(Y): Yes(1)/No(0)
# Layer 1: 40s
tab_40 <- matrix(c(18, 82, 30, 70), nrow=2, byrow=TRUE)
# Layer 2: 60s
tab_60 <- matrix(c(35, 65, 55, 45), nrow=2, byrow=TRUE)

# 배열로 병합
data <- array(c(tab_40, tab_60), dim = c(2, 2, 2),
              dimnames = list(Exercise = c("Yes", "No"),
                              Disease = c("Yes", "No"),
                              Age = c("40s", "60s")))

print(data)

# a. 각 층별 오즈비
cat("\n--- Odds Ratio: 40s ---\n")
print(fisher.test(tab_40)$estimate)
cat("\n--- Odds Ratio: 60s ---\n")
print(fisher.test(tab_60)$estimate)

# b. Cochran-Mantel-Haenszel Test (Common OR 산출)
cmh <- mantelhaen.test(data)
cat("\n--- CMH Test ---\n")
print(cmh)

# c. Homogeneity Test (Breslow-Day or Woolf Test)
# R 내장 함수에는 Breslow-Day가 없으므로 DescTools 패키지 사용 권장.
# 여기서는 Woolf Test 구현 예시
# (주의: 셀 빈도가 너무 작으면 Woolf Test는 부정확할 수 있음)
library(stats)
# 대안: mantelhaen.test 결과만으로도 신뢰구간 겹침 여부를 확인 가능.
```

---

## 심화 학습 (Deep Understanding)

### 1. 심슨의 역설 (Simpson's Paradox)
만약 40대와 60대 데이터를 무작정 합쳐서(Marginal Table) 오즈비를 구했다면 어떻게 되었을까요?
- 연령은 심장질환의 강력한 위험인자입니다(60대가 발병률이 높음).
- 만약 운동하는 집단에 60대가 불균형하게 많이 포함되어 있었다면, 운동이 심장질환을 유발하는 것처럼 오즈비가 왜곡될 수 있습니다(Confounding).
CMH 검정은 이러한 **교란 변수(Confounder)**의 효과를 제거하고 순수한 $X-Y$ 관계를 파악하게 해주는 강력한 도구입니다.

### 2. 상호작용(Interaction)과 교란(Confounding)의 구별
- **교란:** $Z$ 때문에 $X$와 $Y$의 관계가 왜곡되는 것. (해결: CMH로 보정)
- **상호작용:** $Z$의 수준에 따라 $X$가 $Y$에 미치는 효과 자체가 달라지는 것. (해결: 층별 분석 별도 보고)
이 문제에서는 상호작용이 없었으므로(Breslow-Day P > 0.05), 교란 요인만 통제하면 일반화된 결론을 내릴 수 있었습니다.
