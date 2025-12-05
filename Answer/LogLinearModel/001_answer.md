# 1. 독립성 관계의 증명과 반례



## 문제 (English)

Check whether each statement is true:

(1) $X, Y, Z$: mutual independence $\implies$ joint independence

(2) $Y \perp (X, Z)$ (joint independence) $\implies X \perp Y|Z$ and $Y \perp Z|X$

(3) $X \perp Y|Z$ and $Y \perp Z|X \implies X \perp Y$ and $Y \perp Z$



---



## 해설 (Korean)



### 1.1 문항 (1) 상호 독립이면 결합 독립인가?



**거짓 (False)**



상호 독립(Mutual Independence)은 $P(X,Y,Z) = P(X)P(Y)P(Z)$를 의미합니다.

결합 독립(Joint Independence)은 예를 들어 $Y \perp (X,Z)$라면 $P(Y, X, Z) = P(Y) P(X, Z)$를 의미합니다.



상호 독립이 성립하면:

$$ P(Y, X, Z) = P(Y)P(X)P(Z) $$

이때 $X$와 $Z$가 독립($P(X,Z) = P(X)P(Z)$)이라면 결합 독립도 성립합니다.

하지만 일반적인 정의에서 "상호 독립"은 보통 모든 부분집합의 독립을 포함하는 가장 강력한 조건입니다.

만약 문제의 의도가 "Pairwise independence $\implies$ Joint independence"를 묻는 것이라면 거짓이지만, "Mutual independence $\implies$ Joint independence"는 **참(True)**입니다.



*재검토:*

통계학에서 Mutual Independence는 $P(X,Y,Z) = P(X)P(Y)P(Z)$를 만족함을 말합니다.

이 경우, $P(X, Z) = \sum_y P(X, y, Z) = P(X)P(Z)$가 되어 마진도 독립입니다.

따라서 $P(Y, X, Z) = P(Y) [P(X)P(Z)] = P(Y) P(X, Z)$가 성립하므로 $Y \perp (X, Z)$입니다.

즉, 상호 독립은 결합 독립을 포함합니다.

**답: True**



### 1.2 문항 (2) 결합 독립이면 조건부 독립인가?



**참 (True)**



가정: $Y \perp (X, Z) \iff P(Y, X, Z) = P(Y) P(X, Z)$



보여야 할 것 1: $X \perp Y | Z$

$$ P(X, Y | Z) = \frac{P(X, Y, Z)}{P(Z)} = \frac{P(Y) P(X, Z)}{P(Z)} = P(Y) P(X | Z) $$

그런데 $P(Y|Z) = P(Y,Z)/P(Z) = P(Y)P(Z)/P(Z) = P(Y)$ (왜냐하면 $Y \perp Z$이므로).

따라서 $P(X, Y | Z) = P(Y|Z) P(X|Z)$ 가 성립합니다.



보여야 할 것 2: $Y \perp Z | X$

동일한 논리로 성립합니다.

**답: True**



### 1.3 문항 (3) 조건부 독립이면 주변 독립인가?



**거짓 (False)**



반례: 심슨의 역설(Simpson's Paradox) 상황을 생각할 수 있습니다.

$Z$층별로 보면 $X$와 $Y$가 독립이지만, $Z$를 합치면(Marginalize) $X$와 $Y$가 종속이 될 수 있습니다.



예를 들어, 로그선형모형 $(XY, XZ, YZ)$ (No 3-way interaction, but all 2-way associations) 상황을 고려하면:

- $X \perp Y | Z$가 성립하지 않습니다 (이 모형은 조건부 종속).

- 문제의 조건은 $X \perp Y | Z$ (즉 $XY$ 항 없음) 이고 $Y \perp Z | X$ (즉 $YZ$ 항 없음) 인 모형, 즉 $(XZ, Y)$ 모형입니다.

- 이 경우 $Y$는 $X$와도 조건부 독립, $Z$와도 조건부 독립입니다. 즉 $Y$는 $(X, Z)$ 결합 분포와 독립입니다.

- 따라서 $Y \perp X$ 그리고 $Y \perp Z$가 성립합니다.



*재검토:*

조건 "$X \perp Y|Z$ and $Y \perp Z|X$"는 로그선형모형 표기법으로 $(XZ, Y)$ 모형을 의미하는가?

- $X \perp Y|Z \iff$ $XY$ 항 없음.

- $Y \perp Z|X \iff$ $YZ$ 항 없음.

- 두 조건을 모두 만족하면 로그선형모형은 $(XZ, Y)$ 형태가 됩니다.

- 즉, $P(X, Y, Z) = g(X, Z) h(Y)$ 꼴로 분해됩니다.

- 이 경우 $Y$는 $X, Z$와 결합 독립이므로, 당연히 주변 독립($X \perp Y$ and $Y \perp Z$)도 성립합니다.



**잠깐, 반례가 있는가?**

만약 $Z$가 이산형이 아니라 연속형이거나 특수한 구조라면?

일반적으로 "조건부 독립 $\implies$ 주변 독립"은 성립하지 않지만, **이 문제의 특정 조건($Y$가 $Z$와도, $X$와도 조건부 독립)** 하에서는 $Y$가 고립되므로 성립합니다.

하지만 문제의 (3)번이 일반적인 명제($A \perp B | C \implies A \perp B$)를 묻는 것이 아니라, 두 가지 조건부 독립이 겹친 상황을 묻는 것입니다.



그러나 문제를 다시 보면:

$X \perp Y | Z$ (No direct X-Y link)

$Y \perp Z | X$ (No direct Y-Z link)

그래픽 모형(Graphical Model)으로 그리면 $Z - X - Y$ (Markov Chain) 구조가 아니라, $Y$에 연결된 선이 $X$에서도 $Z$에서도 끊긴 상태입니다. 즉 $X-Z$ 만 연결되어 있고 $Y$는 고립점(Isolated node)입니다.

따라서 $Y$는 $(X, Z)$와 독립입니다.



**결론:**

이 명제는 **참(True)**입니다. (로그선형모형 $(XZ, Y)$에 해당).



*혹시 다른 해석?*

만약 $X \perp Y | Z$ 만 있다면 주변독립 보장 못함.

만약 $Y \perp Z | X$ 만 있다면 주변독립 보장 못함.

둘 다 있으면 $Y$는 아무와도 연결되지 않음 -> 주변 독립 성립.



---



## R Code (검증)



```r

# 3번 명제 시뮬레이션

# 3-way contingency table 생성 (XZ만 연관, Y는 독립)

# Model (XZ, Y) 생성

X <- rep(1:2, each=200)

Z <- rep(1:2, times=200)

# X와 Z는 연관됨 (예: X=Z일 확률 높음)

idx <- (X == Z)

# Y는 완전 랜덤 (독립)

Y <- rbinom(400, 1, 0.5)



# 데이터 프레임

df <- data.frame(X, Y, Z)



# 조건부 독립성 확인

# Cochran-Mantel-Haenszel Test for X, Y given Z

cmh_XY_Z <- mantelhaen.test(table(X, Y, Z)) # should be non-significant

# CMH Test for Y, Z given X

cmh_YZ_X <- mantelhaen.test(table(Y, Z, X)) # should be non-significant



# 주변 독립성 확인

chisq_XY <- chisq.test(table(X, Y))

chisq_YZ <- chisq.test(table(Y, Z))



print(cmh_XY_Z)

print(cmh_YZ_X)

print(chisq_XY)

print(chisq_YZ)

```



---



## 심화 학습 (Deep Understanding)



### 1. 로그선형모형의 계층적 구조

로그선형모형에서 조건부 독립성은 해당 변수들 간의 교호작용 항($\lambda_{XY}$ 등)이 0임을 의미합니다.

- (1) $(X, Y, Z)$ Mutual Indep $\iff$ $\lambda_X, \lambda_Y, \lambda_Z$ 만 존재 (1-way terms only).

- (2) $(Y, XZ)$ Joint Indep $\iff$ $\lambda_Y, \lambda_{XZ}$ 및 하위항 존재. $\lambda_{XY}, \lambda_{YZ}, \lambda_{XYZ}$는 모두 0.

- (3) 조건 $(XZ, Y)$ $\iff$ $\lambda_{XY}=0, \lambda_{YZ}=0$ (그리고 $\lambda_{XYZ}=0$). 남는 최고차항은 $\lambda_{XZ}$와 $\lambda_Y$. 이는 $Y$가 완전히 분리된 모형을 의미하므로 주변 독립도 성립합니다.



### 2. Collapsibility (압축 가능성)

어떤 변수 $Z$에 대해 주변화(Marginalization) 했을 때 변수 간의 관계가 보존되려면 Collapsibility 조건이 필요합니다. 3번의 경우 $Y$가 $X, Z$ 모두와 독립이므로, $Z$를 무시하고 $X, Y$만 보더라도 독립성이 유지됩니다.
