# 7. Conditional Independence Testing in 2x2x2 Table



## 문제 (English)

Suppose that $\pi_{ijk}$ in a $2 \times 2 \times 2$ table is, by row, $(0.15, 0.10 / 0.10, 0.15)$ when $Z=1$ and $(0.10, 0.15 / 0.15, 0.10)$ when $Z=2$. For testing conditional $XY$ independence with logit models having $Y$ as a response, explain why the likelihood-ratio test comparing models $X+Z$ and $Z$ is not consistent but the likelihood-ratio test of fit of the $XY$ conditional independence model is.



*(Note: The probability notation $(p_{11}, p_{12} / p_{21}, p_{22})$ usually refers to cell probabilities $P(X=i, Y=j | Z=k)$ or joint probabilities. Given the context of "logit models having Y as a response", we should interpret these values carefully. However, looking at the pattern, it seems to define the joint structure.)*



---



## 해설 (Korean)



### 7.1 데이터 구조 및 오즈비 분석



주어진 확률 구조를 $2 \times 2$ 표로 나타내면 다음과 같습니다.



**Z=1 층:**

$$

\begin{pmatrix} 0.15 & 0.10 \\ 0.10 & 0.15 \end{pmatrix}

$$

- 오즈비 $OR_1 = \frac{0.15 \times 0.15}{0.10 \times 0.10} = \frac{0.0225}{0.01} = 2.25$



**Z=2 층:**

$$

\begin{pmatrix} 0.10 & 0.15 \\ 0.15 & 0.10 \end{pmatrix}

$$

- 오즈비 $OR_2 = \frac{0.10 \times 0.10}{0.15 \times 0.15} = \frac{0.01}{0.0225} \approx 0.444$ ($= 1/2.25$)



### 7.2 조건부 독립성 검정 ($XY \perp Z$)



조건부 독립성은 모든 층에서 $OR=1$이어야 함을 의미합니다.

하지만 실제 오즈비는 $Z=1$에서 $2.25$, $Z=2$에서 $0.44$로 1이 아니며, 서로 역수 관계입니다. 즉, $X$와 $Y$는 각 층에서 강한 연관성을 가집니다(방향은 반대).



### 7.3 모형 비교 (LRT comparing $X+Z$ and $Z$)



로지스틱 회귀모형 $X+Z$ (Main Effects Model)는 오즈비가 $Z$에 따라 변하지 않는다(Homogeneous Odds Ratio)고 가정합니다.

$$ \text{logit}[P(Y=1)] = \alpha + \beta_X X + \beta_Z Z $$

이 모형은 모든 층에서 공통된 오즈비 $e^{\beta_X}$를 추정합니다.

데이터에서 $OR_1 = 2.25$, $OR_2 = 0.44$이므로, 이들의 기하평균적인 공통 오즈비는 약 1 ($2.25 \times 0.44 \approx 1$)에 가까울 것입니다.

따라서 $X+Z$ 모형을 적합하면 $\hat{\beta}_X \approx 0$이 됩니다.



이 경우, $X+Z$ 모형과 $Z$ 모형(Null model regarding X)을 비교하는 우도비 검정(LRT)은 **"평균적인 오즈비가 1인가?"**를 검정하게 됩니다.

실제로는 연관성이 강하지만 방향이 반대여서 상쇄되므로, LRT 통계량은 0에 가까워지고 귀무가설($\beta_X=0$)을 기각하지 못합니다. 즉, **일치성(Consistency)이 없습니다.** (거짓인 귀무가설을 기각하지 못함).



### 7.4 적합도 검정 (Goodness-of-Fit Test of Conditional Independence Model)



반면, 조건부 독립 모형($XY$ conditional independence model) 자체의 적합도 검정($G^2$ of Fit)은 관측된 데이터가 "오즈비=1"인 구조와 얼마나 다른지를 봅니다.

- 모형 가정: $OR_1 = 1, OR_2 = 1$

- 실제 데이터: $OR_1 = 2.25, OR_2 = 0.44$



이 검정은 각 층별로 편차를 계산하여 합산하므로($\sum (O-E)^2/E$), 방향이 반대여도 상쇄되지 않고 오차가 누적됩니다.

따라서 적합도 검정 통계량은 매우 커질 것이며, 귀무가설(독립이다)을 올바르게 기각하게 됩니다. 즉, **일치성(Consistent)**을 가집니다.



**결론:**

상호작용(Interaction)이 존재하여 오즈비의 방향이 엇갈리는 경우($Z$에 따른 이질성), 주효과 모형($X+Z$)에 기반한 검정은 연관성을 놓칠 수 있습니다(검정력 상실). 반면, 포화 모형(Saturated Model) 대비 조건부 독립 모형의 적합도 검정은 이러한 이질성을 감지해낼 수 있습니다.



---



## R Code 및 실습



```r

# 데이터 생성 (3차원 배열)

# Z=1

tab1 <- matrix(c(15, 10, 10, 15), nrow=2, byrow=TRUE) * 10 # 가상의 빈도

# Z=2

tab2 <- matrix(c(10, 15, 15, 10), nrow=2, byrow=TRUE) * 10



data <- array(c(tab1, tab2), dim=c(2,2,2))



# 1. Cochran-Mantel-Haenszel Test (유사하게 평균 효과 검정)

cmh <- mantelhaen.test(data)

cat("CMH Estimate:", cmh$estimate, "\n") # 1에 가까움

cat("CMH P-value:", cmh$p.value, "\n")   # 유의하지 않음



# 2. Breslow-Day Test (동질성 검정 - Interaction 확인)

# install.packages("DescTools")

# library(DescTools)

# BreslowDayTest(data) -> 매우 유의함 (이질적임)



# 3. GLM을 이용한 LRT 비교

# 데이터 프레임 변환

df <- data.frame(

  Z = c(1,1,1,1, 2,2,2,2),

  X = c(1,0,1,0, 1,0,1,0),

  Y = c(1,1,0,0, 1,1,0,0), # Y=1(Col1), Y=0(Col2)

  Freq = c(150, 100, 100, 150, 100, 150, 150, 100)

)

# 주의: 이 데이터 프레임 구조는 GLM fit을 위해 Y를 count로 합쳐야 함.

# 간단히 설명하면:

# Model 1 (Z only): Y ~ Z

# Model 2 (X + Z): Y ~ X + Z

# LRT(Model 1 vs Model 2) -> Not Significant (평균 효과 0)



# Model Independence (Y ~ X + Z + X:Z 에서 X, X:Z 제거한 것과 비교?

# 적합도 검정은 Saturated Model과 Independence Model(X, Z만으로 Y설명 불가) 비교.

# Deviance of Independence Model -> Very Large (Significant Lack of Fit)

```



---



## 심화 학습 (Deep Understanding)



### 1. 심슨의 역설의 극단적 형태

이 예제는 심슨의 역설(Simpson's Paradox) 중에서도 **상쇄 효과(Cancellation Effect)**가 완벽하게 일어나는 특수한 경우입니다. 층별 효과는 강력하지만($2.25$와 $0.44$), 이를 무시하고(Marginalize) 보거나 잘못된 모형(Main effect only)을 쓰면 아무런 효과가 없는 것처럼 보입니다.



### 2. 모형 선택의 중요성

통계적 검정이 "유의하지 않다"고 해서 "효과가 없다"고 단정지으면 안 되는 이유입니다. 모형의 가정(여기서는 오즈비의 동질성)이 위배되었을 가능성을 항상 염두에 두어야 합니다. 따라서 분석 전 **상호작용 항(Interaction Term)** $X \times Z$의 유의성을 먼저 검정하거나, Breslow-Day 검정을 수행하는 절차가 필수적입니다.
