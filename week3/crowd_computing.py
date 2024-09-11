from statistics import mean
from scipy import stats
estimates = [100,120,130,150,180,200,210,250,290,300,3000,300,300,400,500,450,480,550,600,700,800,900,100,1500,1200,2000,1800,540,1100]
print(len(estimates))
estimates.sort()
print(stats.trim_mean(estimates,0.1))
# tv=int(len(estimates)*0.1)
# estimates=estimates[tv:]
# estimates=estimates[:len(estimates)-tv]
# print(mean(estimates))