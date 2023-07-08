import csv
import itertools

import pandas as pd
from scipy import stats

mtcars = pd.read_csv(r"data2.csv")
values = ['학업스트레스','사회적지지','자기효능감','대학만족','중도탈락의도']
print("남성 vs 여성")
for i in values:
    firstgroup = mtcars.query('성별 == "남성"')[i]
    secondgroup = mtcars.query('성별 == "여성"')[i]
    t, p = stats.ttest_ind(firstgroup, secondgroup)
    print(f"{i}: t = {t}, p = {p}")
print("")
print("1,2학년 vs 3,4학년")
for i in values:
    firstgroup = mtcars.query('학년 < 3')[i]
    secondgroup = mtcars.query('학년 > 2')[i]
    t, p = stats.ttest_ind(firstgroup, secondgroup)
    print(f"{i}: t = {t}, p = {p}")


print("피어슨 상관관계")
mtcars.drop("학년",axis=1,inplace=True)
print(mtcars.corr(method='pearson',numeric_only=True))