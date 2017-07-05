
# coding: utf-8

# In[31]:

import pickle
import numpy as np
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data


features_list = ['poi'] 

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_dict.pop("TOTAL", 0) # Remove outliers

# Building new features 'from_poi_to_this_person_fraction'
# and 'from_this_person_to_poi_fraction' 

def computeFraction( poi_messages, all_messages ):
    """ given a number messages to/from POI (numerator) 
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """
    if poi_messages == 'NaN' or all_messages == 'NaN':
        fraction = 0
    else:
        fraction = float(poi_messages)/all_messages


    return fraction

for i in data_dict:
    data_dict[i]['from_poi_to_this_person_fraction']=    computeFraction(data_dict[i]['from_poi_to_this_person'],data_dict[i]['to_messages'])
    data_dict[i]['from_this_person_to_poi_fraction']=    computeFraction(data_dict[i]['from_this_person_to_poi'],data_dict[i]['from_messages'])

my_dataset = data_dict

# find out all features
all_features=set()
for i in my_dataset:
    for l in my_dataset[i]:
         all_features.add(l)
            
# Move out label 'poi' and uncovertible feature 'email_address'            
all_features.remove('poi')
all_features.remove('email_address')

# Fill the features_list
for i in all_features:
    features_list.append(i)
    
### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)
    
# Using selectKBest method to select best five features from all features
from sklearn.feature_selection import SelectKBest
selector=SelectKBest(k=5)
selector.fit(features,labels)

# Finding out which five features are selected
select_indices=selector.get_support(indices=True)+1
select_features=[]
for i in select_indices:
    select_features.append(features_list[i])
print('The five selected features are:')
print(select_features)

# Print out the feature scores 
print('The scores of all features are(respectively):')
print(selector.scores_)

# redefine the features_list
features_list=['poi']
for i in select_features:
    features_list.append(i)
    
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)
# split the dataset into training and testing set
from sklearn.cross_validation import StratifiedShuffleSplit
cv = StratifiedShuffleSplit(labels, 1000, random_state = 42)
for train_idx, test_idx in cv: 
    features_train = []
    features_test  = []
    labels_train   = []
    labels_test    = []
    for ii in train_idx:
        features_train.append( features[ii] )
        labels_train.append( labels[ii] )
    for jj in test_idx:
        features_test.append( features[jj] )
        labels_test.append( labels[jj] )

# Features scaling
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
features_train=scaler.fit_transform(features_train)
features_test=scaler.fit_transform(features_test)

# Provided to give you a starting point. Try a variety of classifiers.
# First try:
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
svc=SVC(random_state=42)
parameters={'kernel':['rbf','sigmoid','poly'],'C':np.arange(1,16,1),'gamma':np.arange(0.1,1,0.1)}
clf1=GridSearchCV(svc,parameters)
clf1.fit(features_train,labels_train)

# print out best results and parameters
print('\n The results:')
import pandas as pd
print(pd.DataFrame(clf1.cv_results_))
print('\n The best parameters are:')
best_params=clf1.best_params_
print(best_params)

clf=SVC(kernel=best_params['kernel'],        C=best_params['C'],        gamma=best_params['gamma'],        random_state=42)
clf.fit(features_train,labels_train)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)


# In[32]:

import tester 
tester.main()


# In[ ]:



