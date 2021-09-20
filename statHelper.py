import math

class DataSet():
    def __init__(self, list):
        self.list = sorted(list)
        self.n = len(self.list)
    def mean(self):
        return sum(self.list) / self.n
    def median(self):
        if self.n % 2 == 1:
            return self.list[int((self.n - 1) / 2)]
        else:
            return (self.list[int(self.n / 2)] + self.list[int(self.n / 2 - 1)]) / 2
    def q1(self):
        if self.n % 2 == 1:
            halfway = int((self.n - 1) / 2)
        else:
            halfway = int((self.n / 2 - 1))
        lowerHalf = DataSet(self.list[:halfway])
        return lowerHalf.median()
    def q3(self):
        if self.n % 2 == 1:
            halfway = int((self.n - 1) / 2)
        else:
            halfway = int((self.n / 2))
        upperHalf = DataSet(self.list[halfway:])
        return upperHalf.median()
    def popVar(self):
        mean = self.mean()
        summing = 0
        for n in self.list:
            summing += (n - mean) ** 2
        return summing / self.n
    def popStd(self):
        return math.sqrt(self.popVar())
    def sampVar(self):
        mean = self.mean()
        summing = 0
        for n in self.list:
            summing += (n - mean) ** 2
        return summing / (self.n - 1)
    def sampStd(self):
        return math.sqrt(self.sampVar())
    def max(self):
        return self.list[-1]
    def min(self):
        return self.list[0]
    def fs(self):
        return self.q3() - self.q1()
    def freqDic(self):
        dic = {}
        for n in self.list:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        return dic
    def relFreqDic(self):
        dic = self.freqDic()
        for n in dic:
            dic[n] = dic[n] / self.n
        return dic

def perm(n, k):
    return math.factorial(n) / math.factorial(n - k)

def comb(n, k):
    return perm(n, k) / math.factorial(k)

class PMF():
    def __init__(self, dic):
        self.dic = dic
    def CDF(self, x):
        summing = 0
        for n in self.dic:
            if n > x:
                break
            else:
                summing += self.dic[n]
        return summing
    def E(self):
        summing = 0
        for key, value in self.dic.items():
            summing += key * value
        return summing
    def var(self):
        summing = 0
        for key, value in self.dic.items():
            summing += key **2 * value
        return summing - (self.E() ** 2)
    def std(self):
        return math.sqrt(self.var())

class BRV():
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.q = 1 - p
    def b(self, x):
        return comb(self.n, x) * self.p ** x * self.q ** (self.n - x)
    def B(self, x):
        count = 0
        summing = 0
        while count <= x:
            summing += self.b(count)
            count += 1
        return summing
    def E(self):
        return self.n * self.p
    def var(self):
        return self.n * self.p * self.q
    def std(self):
        return math.sqrt(self.var())

class HRV():
    def __init__(self, n, M, N):
        self.n = n
        self.M = M
        self.N = N
        self.p = M / N
        self.q = 1 - self.p
    def h(self, x):
        return (comb(self.M, x)*comb(self.N - self.M, self.n - x)) / comb(self.N, self.n)
    def H(self, x):
        count = 0
        summing = 0
        while count <= x:
            summing += self.h(count)
            count += 1
        return summing
    def E(self):
        return self.n * self.p
    def var(self):
        return ((self.N - self.n) / (self.N - 1)) * self.n * self.p * self.q
    def std(self):
        return math.sqrt(self.var())

class NBRV():
    def __init__(self, r, p):
        self.r = r
        self.p = p
        self.q = 1 - p
    def nb(self, x):
        return comb(x + self.r - 1, self.r - 1) * self.p ** self.r * self.q ** x
    def NB(self, x):
        count = 0
        summing = 0
        while count <= x:
            summing += self.nb(count)
            count += 1
        return summing
    def E(self):
        return self.r * self.q / self.p
    def var(self):
        return self.r * self.q / (self.p ** 2)
    def std(self):
        return math.sqrt(self.var())

class PPD():
    def __init__(self, u):
        self.u = u
    def p(self, x):
        return math.e ** (-1 * self.u) * self.u ** x / math.factorial(x)
    def P(self, x):
        count = 0
        summing = 0
        while count <= x:
            summing += self.p(count)
            count += 1
        return summing
    def E(self):
        return self.u
    def var(self):
        return self.u
    def std(self):
        return math.sqrt(self.var())

class PP():
    def __init__(self, a):
        self.a = a
    def pp(self, t, k):
        return math.e ** (-1 * self.a * t) * (self.a * t) ** k / math.factorial(k)
    def PP(self, t, k):
        count = 0
        summing = 0
        while count <= k:
            summing += self.pp(t, count)
            count += 1
        return summing
    def E(self, t):
        return self.a * t
    def var(self, t):
        return self.a * t
    def std(self, t):
        return math.sqrt(self.var(t))

class Exponential():
    def __init__(self, _lambda):
        self._lambda = _lambda
    def f(self, x):
        if x >= 0:
            return self._lambda * math.e ** (-self._lambda * x)
        else:
            return 0
    def F(self, x):
        if x >= 0:
            return 1 - math.e ** (-self._lambda * x)
        else:
            return 0
    def E(self):
        return 1 / self._lambda
    def var(self):
        return 1 / (self._lambda ** 2)
    def std(self):
        return 1 / self._lambda

class Gamma():
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
    def f(self, x):
        if x >= 0:
            return (x**(self.alpha - 1) * math.e**(-x/self.beta)) / (self.beta**self.alpha * math.gamma(self.alpha))
        else:
            return 0

class Chi_Squared(Gamma):
    def __init__(self, v):
        self.alpha = v / 2
        self.beta = 2

class Weibull():
    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta
    def f(self, x):
        if x >= 0:
            return (self.alpha / self.beta ** self.alpha) * x ** (self.alpha - 1) * math.e ** (-x / self.beta)
        else:
            return 0
    def F(self, x):
        if x >= 0:
            return 1 - math.e ** (-1 * (x / self.beta) ** self.alpha)
        else:
            return 0
