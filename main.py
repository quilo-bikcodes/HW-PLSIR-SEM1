import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import threading

iris_dataframe = pd.read_csv('iris.csv')

def showlineplt(i):
    plt.figure(figsize=(15,5))
    plt.plot(iris_dataframe[i])
    plt.title('Iris Da  taset')
    plt.xlabel('Flower Name')
    plt.ylabel(i)
    plt.show()

def showDatasetStats(data):
    return data.describe()
def seabn(data):
    tmp = data.drop('Id', axis=1)
    g = sns.pairplot(tmp, hue='Species', markers='+')
    plt.show()

def species_count(data):
    return data['Species'].value_counts()
def linepltSepalLengthCm():
    showlineplt('SepalLengthCm')
def linepltSepalWidthCm():
    showlineplt('SepalWidthCm')
def linepltPetalLengthCm():
    showlineplt('PetalLengthCm')
def linepltPetalWidthCm():
    showlineplt('PetalWidthCm')


def showsbplt(category):
    g = sns.violinplot(y='Species', x=category, data=iris_dataframe, inner='quartile')
    plt.show()

def sbpltSepalLengthCm():
    showsbplt('SepalLengthCm')
def sbpltSepalWidthCm():
    showsbplt('SepalWidthCm')
def sbpltPetalLengthCm():
    showsbplt('PetalLengthCm')
def sbpltPetalWidthCm():
    showsbplt('PetalWidthCm')

linepltSepalLengthCm()
# pltSepalWidthCm()
# pltPetalLengthCm()
# pltPetalWidthCm()
# sbpltSepalLengthCm()
# sbpltSepalWidthCm()
# sbpltPetalLengthCm()
# sbpltPetalWidthCm()


# stats = showDatasetStats(iris_dataframe)
# print(stats)
# count_spieces = species_count(iris_dataframe)
# print(count_spieces)

# seabn(iris_dataframe)
# print(iris_dataframe)
# print(iris_dataframe.info())
