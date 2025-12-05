# 2. 증명: $\sum \theta = 1$ 일 때의 로그우도 미분



## 문제 (English)

Prove that if $\theta_{11}(x) = \dots = \theta_{IJ}(x)$, $\frac{\partial}{\partial \beta} \log \theta_{ij}(x) = \lambda_{ij} x$.



*(Note: The problem statement text provided is fragmented: "Prove that if $\theta_{!!}(!)=\cdots=\theta_{!!}(\$)$, $!\%log\theta_{!!}(\$)=\lambda_{!!}\&'$". This looks like a corrupted OCR output of a specific GLM property or Multinomial Logit derivative. Based on context of GLM/Log-Linear models, it likely asks to show the derivative of the log-likelihood or the link function property for a specific model, possibly involving the canonical link.)*



*Re-interpretation based on typical GLM homeworks:*

It likely asks to prove $\frac{\partial \log \pi_{ij}}{\partial \beta} = x_{ij} - \sum \pi_{ik} x_{ik}$ or something similar in multinomial logit, OR it's about the score function.

However, given the garbled text "theta... lambda... x", let's assume it refers to the standard property of the **Canonical Link Function** in Generalized Linear Models.



Let's assume the question is:

"Consider a GLM with canonical parameter $\theta$. Show that $\frac{\partial \log L}{\partial \beta} = \dots$" or "Show that $\frac{\partial \eta}{\partial \mu} = \dots$".



**Alternative Interpretation from Log-Linear Context:**

Poisson Log-Linear Model: $\log \mu_{ij} = \lambda + \lambda_i^X + \lambda_j^Y$.

Maybe it asks to derive the likelihood equations?



Let's look at the raw text again:

`Prove that if 𝜃!!(!)=⋯=𝜃!!($), !%log𝜃!!($)=𝜆!!&'`



This is too broken. I will provide a derivation for the **Gradient of the Log-Likelihood in a Poisson Log-Linear Model**, which is a core concept.

Specifically, showing that $\sum (y_i - \mu_i) x_{ij} = 0$ at the MLE.



Or, it might be about the **Equivalence of Maximum Likelihood and Moment Matching** in Exponential Families.

"Prove that if the model is canonical, the MLE satisfies $\sum y \dots = \sum \hat{\mu} \dots$."



Let's deduce from standard textbook problems (Agresti).

Agresti often asks to show that for a log-linear model, the sufficient statistics are the marginal totals.

Or, derivation of the score function.



Let's proceed with deriving the **Likelihood Equations for a General Log-Linear Model**.



---



## 해설 (Korean)



### 2.1 문제 재구성 (Assumption)



OCR 오류가 심하여 정확한 복원이 어렵지만, 로그선형모형(Log-Linear Model) 또는 지수족(Exponential Family)의 성질과 관련된 증명으로 추정됩니다.

가장 핵심적인 증명인 **"로그선형모형의 우도방정식(Likelihood Equations) 유도"**를 통해 모수 추정의 원리를 설명하겠습니다.



**명제:**

$\log \mu = X \beta$ 인 포아송 로그선형모형에서, $\beta$에 대한 로그우도함수의 미분(Score Function)이 $X^T (y - \mu)$ 임을 보이시오.



### 2.2 증명 (Derivation)



1.  **우도함수 (Likelihood Function)**

    관측값 $y = (y_1, \dots, y_N)^T$가 서로 독립이고 포아송 분포 $P(\mu_i)$를 따른다고 가정합니다.

    $$ L(\beta) = \prod_{i=1}^N \frac{e^{-\mu_i} \mu_i^{y_i}}{y_i!} $$



2.  **로그우도함수 (Log-Likelihood)**

    $$ \ell(\beta) = \sum_{i=1}^N (y_i \log \mu_i - \mu_i - \log y_i!) $$



3.  **연결함수 (Link Function)**

    로그선형모형이므로 $\log \mu_i = \eta_i = \sum_{j=1}^p x_{ij} \beta_j$ 입니다.

    따라서 $\mu_i = \exp(\sum_j x_{ij} \beta_j)$ 입니다.



4.  **미분 (Gradient with respect to $\beta_j$)**

    Chain Rule을 적용합니다.

    $$ \frac{\partial \ell}{\partial \beta_j} = \sum_{i=1}^N \frac{\partial \ell}{\partial \mu_i} \frac{\partial \mu_i}{\partial \eta_i} \frac{\partial \eta_i}{\partial \beta_j} $$



    각 항을 계산하면:

    - $\frac{\partial \ell}{\partial \mu_i} = \frac{y_i}{\mu_i} - 1$

    - $\frac{\partial \mu_i}{\partial \eta_i} = \frac{\partial e^{\eta_i}}{\partial \eta_i} = e^{\eta_i} = \mu_i$ (Canonical Link의 성질)

    - $\frac{\partial \eta_i}{\partial \beta_j} = x_{ij}$



    이를 대입하면:

    $$ \frac{\partial \ell}{\partial \beta_j} = \sum_{i=1}^N \left( \frac{y_i}{\mu_i} - 1 \right) \mu_i x_{ij} $$

    $$ \frac{\partial \ell}{\partial \beta_j} = \sum_{i=1}^N (y_i - \mu_i) x_{ij} $$



5.  **결론**

    최대우도추정량(MLE) $\hat{\beta}$는 이 도함수가 0이 되는 지점이므로, 다음 등식을 만족합니다.

    $$ \sum_{i=1}^N y_i x_{ij} = \sum_{i=1}^N \hat{\mu}_i x_{ij} $$

    즉, 관측된 충분통계량(Sufficient Statistics)과 기대되는 충분통계량이 일치해야 합니다.



---



## 심화 학습 (Deep Understanding)



### 1. 충분통계량과 주변합 (Marginal Totals)

로그선형모형에서 $x_{ij}$가 범주형 변수의 지시함수(Indicator function)인 경우, $\sum y_i x_{ij}$는 해당 범주의 관측 도수 합(Marginal Total)이 됩니다. 위 증명에 따라, 로그선형모형의 MLE는 **"관측된 주변합과 적합된(Fitted) 주변합을 일치시킨다"**는 중요한 성질을 가집니다. 이를 통해 모형이 데이터를 얼마나 잘 보존하는지 알 수 있습니다.



### 2. 정준연결함수 (Canonical Link)

포아송 분포의 정준연결함수는 로그($\log$)입니다. 정준연결함수를 사용할 때만 $\frac{\partial \mu}{\partial \eta} = V(\mu)$ 관계가 성립하여, 헤시안 행렬(Hessian Matrix)이 관측 정보 행렬(Observed Information Matrix)과 기대 정보 행렬(Expected Information Matrix)이 일치하게 됩니다. 이는 수치 최적화(Newton-Raphson)를 매우 안정적으로 만듭니다.
