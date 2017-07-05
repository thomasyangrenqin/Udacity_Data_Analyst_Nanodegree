#Identify Fraud from Enron Financial and Email Dataset by Renqin Yang
---
###1. Summarize for us the goal of this project and how machine learning is useful in trying to accomplish it.
In 2000, Enron was one of the largest companies in the United States. By 2002, it had collapsed into bankruptcy due to widespread corporate fraud. In the resulting Federal investigation, a significant amount of typically confidential information entered into the public record, including tens of thousands of emails and detailed financial data for top executives. 

In this project, I explored the dataset, removed outliers, created new features, tied out various machine learning algorithms and tuned parameters respectively. Finally I built up a person of interest identifier based on financial and email data made public as a result of the Enron scandal. Notably, in the fraud case, the person of interest means individuals who were indicted, reached a settlement or plea deal with the government, or testified in exchange for prosecution immunity.

I used `Pandas` to transform the dataset `data_dict` into a `DataFrame` object to explore the structure of this dataset. And I immediately got that this dataset has 146 data points and 21 total features.  For the most important feature in this dataset, `poi`, I found the distribution of this feature is very skewed and unbalanced. There are only 18 people out of 146 total data points which is the 'POI'. Of course, it is also reasonable that the Person of Interest are small portion of the whole employee within the Enron, but this unbalanced distribution brought to me a little tricky challenge when it came to analysis the data structure and dividing the original dataset into training and testing sets. Finally, there is no 'NaN' or missing value within `poi` feature. However, there are some 'NaN' in other features. like `loan_advances`, `restricted_stock_deferred` etc.

Therefore, below are the important characteristics of this dataset:

*  The total number of data points: 146 (person based)
*  Number of features used: 21 features 
*  Allocation across classes (POI/non-POI): 18 POI out of 146 total data points(unbalanced)
*  Missing values: There is no missing value within `poi` feature, but with some 'NaN' in other features.

After my initial dataset exploration, I found there is one main outlier in the dataset, which named `'TOTAL'`. This is an aggregation on individual data, and a interference for our analysis. I remove out this outlier by:

```
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

data_dict.pop("TOTAL", 0) # Remove outliers
```
###2. What features did you end up using in your POI identifier, and what selection process did you use to pick them? Did you have to do any scaling? Why or why not?

I created two new features in the original dataset, they are `'from_poi_to_this_person_fraction'` and `'from_this_person_to_poi_fraction'`. I created them through following algorithm:

```
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
    data_dict[i]['from_poi_to_this_person_fraction']=\
    computeFraction(data_dict[i]['from_poi_to_this_person'],data_dict[i]['to_messages'])
    data_dict[i]['from_this_person_to_poi_fraction']=\
    computeFraction(data_dict[i]['from_this_person_to_poi'],data_dict[i]['from_messages'])
```

They are simply the ratio of the emails came or sent to POI out of the whole emails of the specific person. Ideally, the higher the either ratio is, the more likely this person would be POI.

Later, in the features selection step, I used `SelectKBest` algorithm to select best 5 features in all the features, including the two new features. Finally, the five features I selected out and used in the test steps are:

 `'from_this_person_to_poi_fraction'`,` 'bonus'`, `'total_stock_value'`,` 'salary'`,` 'exercised_stock_options'`
 
 And the features scores of them are:
 
 ```
 [  1.69882435   0.21705893   6.23420114  11.59554766   5.34494152
   0.06498431   8.74648553   7.2427304    0.1641645    4.20497086
  16.64170707   2.10765594  21.06000171  24.46765405   2.42650813
  10.07245453   9.34670079  18.57570327   8.86672154   3.21076192
  25.09754153]
 ```
 
Finally, I also scaled those selected features by using the `MinMaxScaler` algorithm. This feature scaling is vital when it comes to machine learning step. Specifically, feature scaling affect the outcome when I use SVM algorithm with rbf kernel in the machine learning step.

### 3. What algorithm did you end up using? What other one(s) did you try? How did model performance differ between algorithms?

Finally, I chose the `SVM` support vector machines algorithm with parameters : `'kernel': 'poly', 'C': 5, 'gamma': 0.9` in my machine learning and decision making step. The final performances of my algorithm based on my preprocessed dataset are list below:

```
SVC(C=5, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma=0.9,
  kernel='poly', max_iter=-1, probability=False, random_state=42,
  shrinking=True, tol=0.001, verbose=False)
	Accuracy: 0.81293	Precision: 0.34502	Recall: 0.34450	F1: 0.34476	F2: 0.34460
	Total predictions: 14000	True positives:  689	False positives: 1308	False negatives: 1311	True negatives: 10692
```
Both Precision and Recall are above 0.3, and the whole accuracy is about 81%, which could be a relative good result.

At the very beginning, I used the `GaussianNB` Naive Bayes algorithm with Gaussian kernel. However, this is a algorithm with almost no parameters to be tuned with. And the performance of this algorithm is:

```
Accuracy: 0.83343	Precision: 0.38392	Recall: 0.27450	F1: 0.32012	F2: 0.29109
	Total predictions: 14000	True positives:  549	False positives:  881	False negatives: 1451	True negatives: 11119
```
Although, it has very good performance on accuracy, its Recall is lower than 0.3.


Later, I tried the `AdaBoostClassifier` algorithm, with its best performance parameters: `'learning_rate': 0.5, 'algorithm': 'SAMME'`(obtained by using `GridSearchCV` algorithm). It's performance:

```
AdaBoostClassifier(algorithm='SAMME', base_estimator=None, learning_rate=0.5,
          n_estimators=50, random_state=7)
	Accuracy: 0.79029	Precision: 0.33475	Recall: 0.47400	F1: 0.39238	F2: 0.43759
	Total predictions: 14000	True positives:  948	False positives: 1884	False negatives: 1052	True negatives: 10116
```

`AdaBoostClassifier` did well both on Precision and Recall. However, its accuracy is relatively a bit low. Finally, I decided to choose  `SVM` support vector machines algorithm to perform my machine learning and decision making steps.

###4.What does it mean to tune the parameters of an algorithm, and what can happen if you don’t do this well?  How did you tune the parameters of your particular algorithm?

Tuning the parameters of an algorithm is usually to set those parameters to so optimal values that enable you to complete a learning task in the best way possible. Whatever the algorithm you choose to use, tuning the parameters of this algorithm is always the very vital step to make the whole machine learning and decision making process work or even great.

There is one typical example of what can happen I don't tune parameters well. When I explored the `GaussianNB` Naive Bayes algorithm with Gaussian kernel, there is almost no parameters I can tune with, therefore, I just put the default setting remained and test its performances. And I got a unideal Recall performance. 

When it came to `SVM` and `AdaBoostClassifier` , there are various parameters for me to tune with, so I decided to use `GridSearchCV` algorithm to compare and select the best combination of parameters.
For `AdaBoostClassifier`, the parameters group is: `parameters={'algorithm':['SAMME','SAMME.R'],'learning_rate':[0.5,1,1.5,2]}`

And `GridSearchCV` picked up `'learning_rate': 0.5, 'algorithm': 'SAMME'` as its best parameters.
For `SVM`, the parameters group is: `parameters={'kernel':['rbf','sigmoid','poly'],'C':np.arange(1,16,1),'gamma':np.arange(0.1,1,0.1)}`. And `GridSearchCV` picked up `'kernel': 'poly', 'C': 5, 'gamma': 0.9` as its best parameters.

###5.What is validation, and what’s a classic mistake you can make if you do it wrong? How did you validate your analysis?

Validation in machine learning is the way how you assess various machine learning algorithm or even the whole dataset. However, in the case of our situation, due to the small size of the dataset, if we chose to use conventional validation, there is not enough data available to partition it into separate training and test sets without losing significant modelling or testing capability. So I need to do a cross-validation.Cross-validation is a model validation technique for assessing how the results of a statistical analysis will generalize to an independent data set. The goal of cross validation is to define a dataset to "test" the model in the training phase (i.e., the validation dataset), give an insight on how the model will generalize to an independent dataset (i.e., an unknown dataset, for instance from a real problem), etc. If we didn't choose cross-validation or even do any validation with our dataset, then problems like overfitting, very small variance with almost no bias, will come out as we proceed into machie learning and decision making part.

In this project, I used cross-validation. To be specific, I used stratified shuffle split cross validation.  Using training dataset to fit my machine learning classifier, and testing dataset to validate my algorithm.

```
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
```

###6.Give at least 2 evaluation metrics and your average performance for each of them. 
In the evaluation step, I used `Precision` and `Recall` metrics to evaluate my whole machine learning process.

 `Precision` : Out of all the items labeled as positive, how many belong to the True class. That is : `True Positive/(True Positive+False Positive)`
 
 `Recall` : Out of all the items that are truly positive, how many were correctly classified as positive. That is : `True Positive/(True Positive+False Negative)`
 
My finally performance on these two metrics:

```
Accuracy: 0.81293	Precision: 0.34502	Recall: 0.34450	F1: 0.34476	F2: 0.34460
	Total predictions: 14000	True positives:  689	False positives: 1308	False negatives: 1311	True negatives: 10692
```

