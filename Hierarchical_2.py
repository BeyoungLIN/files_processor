import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch #用于进行层次聚类，画层次聚类图的工具包
import scipy.spatial.distance as ssd
from scipy.cluster.vq import vq,kmeans,whiten
import numpy as np

points = [45, 51, 52, 53, 53, 54, 55, 62, 64, 72, 77, 77, 77, 80, 80, 80, 80, 80, 80, 80, 80, 81, 81]