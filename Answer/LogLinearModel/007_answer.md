# 7. Conditional Distribution of Independent Poisson Variables



## 문제 (English)

Suppose $X_1 \sim \text{Poisson}(\lambda_1), \dots, X_k \sim \text{Poisson}(\lambda_k)$ are independent random variables. Then, show the conditional distribution follows a multinomial distribution:

$$ P(Y_1=y_1, \dots, Y_k=y_k | Y_1+\dots+Y_k=n) $$

*(Note: The problem uses $Y$ in the probability expression but defines $X$ initially. I will assume $Y_i = X_i$.)*



---



## 해설 (Korean)



### 7.1 문제 정의 및 목표



서로 독립인 포아송 확률변수 $X_i \sim \text{Poisson}(\lambda_i)$ ($i=1,\dots,k$)가 있을 때, 그 합 $S = \sum_{i=1}^k X_i$가 $n$으로 주어졌다면, 각 $X_i$의 결합 분포(Joint Distribution)가 다항 분포(Multinomial Distribution)임을 증명하는 문제입니다.



### 7.2 증명 과정



**1. 합의 분포 (Distribution of the Sum)**

독립적인 포아송 확률변수의 합은 포아송 분포를 따릅니다.

$$ S = \sum_{i=1}^k X_i \sim \text{Poisson}(\Lambda), \quad \text{where } \Lambda = \sum_{i=1}^k \lambda_i $$

따라서 $S=n$일 확률은:

$$ P(S=n) = \frac{e^{-\Lambda} \Lambda^n}{n!} $$



**2. 결합 확률 (Joint Probability)**

$X_i$들이 독립이므로, $X_1=x_1, \dots, X_k=x_k$일 확률은 각 확률의 곱입니다.

$$ P(X_1=x_1, \dots, X_k=x_k) = \prod_{i=1}^k \frac{e^{-\lambda_i} \lambda_i^{x_i}}{x_i!} = \frac{e^{-\sum \lambda_i} \prod \lambda_i^{x_i}}{\prod x_i!} = \frac{e^{-\Lambda} \prod \lambda_i^{x_i}}{\prod x_i!} $$



**3. 조건부 확률 (Conditional Probability)**

조건부 확률의 정의 $P(A|B) = P(A \cap B) / P(B)$를 사용합니다.

여기서 사건 $A$는 $\{X_1=x_1, \dots, X_k=x_k\}$, 사건 $B$는 $\{\sum X_i = n\}$ 입니다.

단, $A$가 발생하면 $B$는 자동으로 만족되므로($\sum x_i = n$이라는 전제 하에), $A \cap B = A$ 입니다.



$$ P(X_1=x_1, \dots | S=n) = \frac{P(X_1=x_1, \dots, X_k=x_k)}{P(S=n)} $$



식을 대입하면:

$$ = \frac{\frac{e^{-\Lambda} \prod_{i=1}^k \lambda_i^{x_i}}{\prod_{i=1}^k x_i!}}{\frac{e^{-\Lambda} \Lambda^n}{n!}} $$



$e^{-\Lambda}$ 약분 후 정리:

$$ = \frac{n!}{\prod_{i=1}^k x_i!} \frac{\prod_{i=1}^k \lambda_i^{x_i}}{\Lambda^n} $$



여기서 $\Lambda^n$을 $\prod \Lambda^{x_i}$ (왜냐하면 $\sum x_i = n$)로 생각하여 각 항에 분배합니다.

$$ = \frac{n!}{x_1! \cdots x_k!} \prod_{i=1}^k \left( \frac{\lambda_i}{\Lambda} \right)^{x_i} $$



**4. 결론**

$\pi_i = \frac{\lambda_i}{\Lambda} = \frac{\lambda_i}{\sum \lambda_j}$ 라고 정의하면, 위 식은 다항 분포의 확률질량함수(PMF)와 정확히 일치합니다.

$$ \text{Multinomial}(n; \pi_1, \dots, \pi_k) $$

단, $\sum \pi_i = \frac{\sum \lambda_i}{\Lambda} = 1$ 을 만족합니다.



---



## 심화 학습 (Deep Understanding)



### 1. 로그선형모형과 다항 로짓 모형의 등가성

이 정리는 포아송 로그선형모형(Poisson Log-Linear Model)과 다항 로짓 모형(Multinomial Logit Model)이 본질적으로 같은 정보를 담고 있음을 보여줍니다.

- **포아송 관점:** 각 셀의 빈도 $n_{ij}$가 독립적인 포아송 분포를 따르며, 전체 표본 크기 $N$은 확률변수입니다.

- **다항 관점:** 전체 표본 크기 $N$이 고정되었다고 가정하면, 셀 빈도의 분포는 다항 분포를 따릅니다.

따라서 $N$에 대한 추론을 제외하면, 두 모형의 파라미터 추정값($\beta$)과 표준오차는 동일합니다.



### 2. 응용: 희귀 사건 시뮬레이션

다항 분포 난수를 생성하고 싶을 때, 각 범주별로 독립적인 포아송 난수를 생성한 뒤 그 합이 원하는 $n$이 될 때까지(또는 정규화하여) 사용하는 기법의 이론적 근거가 됩니다.
