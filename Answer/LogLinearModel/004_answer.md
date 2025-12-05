# 4. Poisson Log-Linear Model Proofs



## 문제 (English)

Consider the following Poisson log-linear model for an $I \times J$ contingency table:

$$ \log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y $$

Prove the following:

(1) $\log \theta_{ij} = \lambda + \lambda_i^X + \lambda_j^Y$ (Wait, standard notation for independent model implies OR is 1. The problem likely asks to show something related to odds ratio or probablities. The OCR text says: `(1) log*!"*#"=𝜆+&−𝜆,&`).

*Re-reading OCR*: `log(pi_ij / pi_ik) ...`? No.

Let's deduce typical homework.

Standard Independence Model: $\log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y$.

Property 1: $\log \mu_{ij} = \alpha_i + \beta_j$ (Additivity).

Property 2: The Odds Ratio $\theta = 1$ for all $2 \times 2$ subtables.

Property 3: $\pi_{ij} = \pi_{i+} \pi_{+j}$.



Looking at OCR again: `(1) log*!"*#"=𝜆+&−𝜆,&`.

Maybe $\log (\mu_{ij} / \mu_{ik}) = \lambda_j^Y - \lambda_k^Y$?

Or $\log \pi_{i|j} = \dots$?



Let's look at `(2) If all 𝜆)'=0, then 𝜋-)=!.`.

If all $\lambda_j^Y = 0$, then $\mu_{ij} = \exp(\lambda + \lambda_i^X)$.

This means $\mu_{ij}$ does not depend on $j$.

Thus, the distribution across columns is uniform (equi-probability) given row $i$.

So $\pi_{j|i} = 1/J$. This matches `𝜋-)=!.` (likely $\pi_{j|i} = 1/J$).



Let's derive these two properties based on the **Independence Model (Main Effects Model)**.



**(1) Log-Odds or Log-Ratio derivation**

**(2) Uniform distribution condition**



---



## 해설 (Korean)



### 4.1 기본 설정



$I \times J$ 분할표에서 포아송 로그선형모형(독립성 모형)은 다음과 같습니다.

$$ \log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y $$

여기서 제약조건 $\sum \lambda_i^X = \sum \lambda_j^Y = 0$ (또는 $\lambda_1=0$)이 필요합니다.



### 4.2 문항 (1) 로그 비율의 유도



문제의 깨진 텍스트 `log*!"*#"=𝜆+&−𝜆,&`는 두 셀의 기대도수 비율에 대한 로그를 묻는 것으로 추정됩니다.

예를 들어 $\log(\mu_{ij} / \mu_{ik})$를 구해봅시다.

$$ \log \mu_{ij} - \log \mu_{ik} = (\lambda + \lambda_i^X + \lambda_j^Y) - (\lambda + \lambda_i^X + \lambda_k^Y) $$

$$ = \lambda_j^Y - \lambda_k^Y $$

즉, 같은 행(row $i$) 내에서 열 $j$와 열 $k$의 기대도수 비율은 행 효과($\lambda_i^X$)에 의존하지 않고 오직 열 효과($\lambda^Y$)의 차이로만 결정됩니다. 이는 독립성 모형의 특징입니다.



또는 오즈비(Odds Ratio) $\theta$의 로그:

$$ \log \theta = \log \left( \frac{\mu_{11}\mu_{22}}{\mu_{12}\mu_{21}} \right) = (\lambda_1^X + \lambda_1^Y + \lambda_2^X + \lambda_2^Y) - (\lambda_1^X + \lambda_2^Y + \lambda_2^X + \lambda_1^Y) = 0 $$

따라서 $\theta = 1$ (독립).



### 4.3 문항 (2) $\lambda_j^Y = 0$ 일 때의 결과



**조건:** 모든 $j$에 대해 $\lambda_j^Y = 0$.

**모형:** $\log \mu_{ij} = \lambda + \lambda_i^X$.

즉, $\mu_{ij} = \exp(\lambda + \lambda_i^X)$.



이 식은 기대도수 $\mu_{ij}$가 열 인덱스 $j$에 의존하지 않음을 의미합니다. 즉, 모든 열에서 빈도가 동일합니다.

$$ \mu_{i1} = \mu_{i2} = \dots = \mu_{iJ} $$



조건부 확률(Conditional Probability) $P(Y=j | X=i)$를 구해봅시다.

$$ \pi_{j|i} = \frac{\mu_{ij}}{\sum_{k=1}^J \mu_{ik}} = \frac{\exp(\lambda + \lambda_i^X)}{\sum_{k=1}^J \exp(\lambda + \lambda_i^X)} $$

분모는 $J \times \exp(\lambda + \lambda_i^X)$ 입니다.

$$ \pi_{j|i} = \frac{\exp(\lambda + \lambda_i^X)}{J \exp(\lambda + \lambda_i^X)} = \frac{1}{J} $$



**결론:**

만약 열 효과($\lambda_j^Y$)가 모두 0이라면, 주어진 행에서 각 열에 속할 확률은 모두 $1/J$로 동일합니다(Equiprobable).



---



## R Code (검증)



```r

# 데이터 생성 및 검증

# I=3, J=4

# Lambda X 설정, Lambda Y = 0

lambda_X <- c(0.5, -0.2, -0.3)

# lambda_X 합이 0이 되도록 조정 (필수는 아니지만 일반적)

lambda_X <- lambda_X - mean(lambda_X)



mu <- matrix(0, nrow=3, ncol=4)

for(i in 1:3) {

  for(j in 1:4) {

    # Model: log(mu) = 2 + lambda_X[i] + 0

    mu[i, j] <- exp(2 + lambda_X[i])

  }

}



print("Expected Frequencies (mu):")

print(mu)



# Conditional Probabilities

pi_j_given_i <- prop.table(mu, margin = 1)

print("Conditional Probabilities (Row-wise):")

print(pi_j_given_i)



# Check if all are 1/J = 1/4 = 0.25

if (all(abs(pi_j_given_i - 0.25) < 1e-6)) {

  cat("\nVerification: All conditional probabilities are 1/J = 0.25\n")

}

```



---



## 심화 학습 (Deep Understanding)



### 1. 모형 파라미터의 해석과 독립성

로그선형모형의 장점은 파라미터 $\lambda$가 오즈비나 상대위험도와 직접적인 관련이 있다는 것입니다. 독립성 모형($XY$ 항 없음)에서 $\lambda_{ij}^{XY} = 0$은 모든 로컬 오즈비가 1임을 보장합니다. 문항 (2)와 같은 상황은 열 변수 $Y$가 아무런 효과가 없다는 것, 즉 $Y$의 분포가 균등(Uniform)하다는 매우 강력한 제약입니다.



### 2. 적합도 검정과의 관계

이러한 이론적 속성은 모형 적합도 검정($G^2$ 또는 Pearson $\chi^2$)의 기초가 됩니다. 관측된 데이터가 $\pi_{j|i} = 1/J$ 패턴에서 벗어난 정도를 측정함으로써, "선호도 차이가 없는가?"(Equiprobability test)와 같은 가설을 검정할 수 있습니다.
