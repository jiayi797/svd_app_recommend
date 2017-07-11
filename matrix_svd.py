#coding=utf-8

from sklearn.decomposition import TruncatedSVD
from sklearn.utils.extmath import randomized_svd
from matplotlib import pyplot as plt
from numpy import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from pandas import DataFrame
from sklearn.random_projection import sparse_random_matrix
import gc
from sklearn.preprocessing import OneHotEncoder
FilePath = '../extra/final/'
TrainFile = 'train.csv'
CleanedTrainFile = 'cleaned_train.csv'
TestFile = 'test.csv'
AdFile = 'ad.csv'
User_basic_File = 'user.csv'
AppCategoriesFile = 'app_categories.csv'
UserInstallAppsFile = 'user_installedapps.csv'
UserAppActionsFile = 'user_app_actions.csv'
PositionFile = 'position.csv'


# install_data = pd.read_csv(FilePath+UserInstallAppsFile)
# print 'haha'
# train_data = pd.read_csv(FilePath+'train.csv')
# train_data = train_data[(train_data['clickTime']>=28000000)&(train_data['clickTime']<=31000000)]
# test_data = pd.read_csv(FilePath+'test.csv')
# install_data_user = install_data[['userID']]
# train_data_user = train_data[['userID']]
# train_data_user = train_data_user.drop_duplicates()
# test_data_user = test_data[['userID']]
# test_data_user = test_data_user.drop_duplicates()
# train_data_user = pd.merge(train_data_user,test_data_user,on='userID',how='outer')
# train_data_user =  train_data_user.drop_duplicates()

# #从install中拿到这些用户
# # print train_data_user

# train_data_user = pd.merge(train_data_user,install_data,on=['userID'],how='left')
# train_data_user = train_data_user.dropna()

# train_data_user.to_csv('installed_cleaned.csv',index=False)


# print train_data_user
#
install_data = pd.read_csv('installed_cleaned_test.csv')

install_data = install_data.groupby('userID')['appID'].agg(lambda x:','.join(x)).reset_index()
print install_data
# print install_data
# enc = OneHotEncoder()
# train_test_matrix = enc.fit_transform(install_data[['appID']])
# feature_list = []
# idx = 0

# start_idx = enc.feature_indices_[idx]
# end_idx = enc.feature_indices_[idx + 1]
# for active in enc.active_features_:
#     if active >= start_idx and active < end_idx:
#         active = 'appID_' + str(active-start_idx)
#         feature_list.append(active)
# idx += 1
# print train_test_matrix.toarray()
# print feature_list
















# x = pd.get_dummies(train_data_user['appID'])
# install_data = train_data_user.join(x)
# del train_data_user
# gc.collect()
# install_data.drop('appID',axis=1,inplace=True)
# install_data = install_data.groupby(['userID']).agg('sum').reset_index()
# install_data.index = install_data['userID'].tolist()
# install_data.drop('userID',inplace=True,axis=1)
# # print install_data.shape
# # svd = TruncatedSVD(n_components=5, n_iter=7, random_state=42)
# # U = svd.fit(install_data)
# U, Sigma, VT = randomized_svd(install_data,n_components=10)
# U = DataFrame(U)
# # print U
# U.to_hdf(FilePath+'user_matrix_from_install','all')