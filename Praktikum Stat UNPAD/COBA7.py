import numpy as np
##1##
#RATA-RATA
x = np.arange(10)
y = [1,2,3,9,5,6,7,8,9,10]
np.mean(x)
np.mean(y)
#MEDIAN
np.median(x)
np.median(y)
#RANGE
np.ptp(x)
np.ptp(y)
#STD DEVIASI
np.std(x)
np.std(y)
np.std(x, ddof=1) #degrees of freedom (int) def 0
#VARIANS
np.var(x)
np.var(y)
np.var(x, ddof=1) #degrees of freedom (int) def 0

##2##
#GENERATE NORMAL BAKU n=100
np.random.normal(size=100)
#GENERATE BINOMIAL n=10, p=.05, size=100
np.random.binomial(10,.05,100)
#GENERATE EXP scale/theta=5, size=5
np.random.exponential(5,100)

##3##
from scipy import stats
#BERNOULLI
#N adalah random value~Bernoulli, p=.4
N = stats.bernoulli(.4)
#P(N = 0)
N.pmf(0)
#P(N = 1)
N.pmf(1)
#BINOMIAL
#K adalah random value~Binomial, n=10, p=.4
K = stats.binom(10,.4)
#P(K = 0)
K.pmf(0)
#P(K = 3)
K.pmf(3)
#P(K <= 3) / fungsi distribusi kumulatif (cdf)
K.cdf(3)

##4##
#NORMAL
#X adalah random value~Normal, mean=60, sd=10
X = stats.norm(60,10)
#P( X <= 67)
X.cdf(67)
#GAMMA
#Y adalah random value~Gamma, alpha=3, theta=10
Y = stats.gamma(3,10)
#P( X <= 11)
Y.cdf(11)
#EXPONENTIAL
#E adalah random value~Exponential, theta=10
E = stats.expon(10)
#P (X <= 11)
E.cdf(11)