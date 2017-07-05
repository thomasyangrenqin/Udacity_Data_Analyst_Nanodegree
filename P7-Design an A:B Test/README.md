## **Design and Analyze A/B Testing - Udacity Free Trial Screener**
---
By Renqin Yang

### **1. Experiment Design**
**1.1 Metric Choice**
> List which metrics you will use as invariant metrics and evaluation metrics here.

* Invariant metrics: Number of clicks, Number of cookies.
* Evaluation metrics: Gross conversion, Net conversion, Rentention

>For each metric, explain both why you did or did not use it as an invariant metric and why you did or did not use it as an evaluation metric. Also, state what results you will look for in your evaluation metrics in order to launch the experiment.

* **Number of clicks** (Number of unique cookies clicked the `'start free trial'` button): The clicks happen before the users see the experiment and independent from it. So, although the page asking the number of hours of the student's devotion after clicking `'Start free Trial'` button, the course overview page remains the same for both control & experiment group.
* **Number of cookies** (Number of unique users visited the course overview page): Cookies evenly distribute in control and experiment group. Again, the visits happen before the users see the experiment and thus independent from it.
* **Gross conversion** (Number of users who enrolled in the free trial/Number of users who clicked the `'Start Free Trial button'`): A good evaluation metrics since it directly depends on the effect of the experiment. In detail, in the experiment group the user can make a decision, if he has enough time to devote for course, he will be enrolled or not, he will continue with the free courseware without enrolling. Vice versa, for the control group, no pop-up would be displayed regardless of the time availability enrolls for the course. The underlying assumption would be the gross conversion in the control group is higher than experiment group. Therefore, it can be used as an evaluation metric to check if the experiment makes a significant difference in the enrollment.
*  **Retention** (Number of user-ids remaining enrolled for 14 days trial period and made their first payment/Number of users who enrolled in the free trial): As mentioned in gross conversion metric, in the experiment group, users are completely aware of the time commitment, they made a deliberate decision to enroll the course or to continue with the free courseware option. But for the control group, many users enroll for the courseware, since not many of them have the required time, the cancellation rate might be high and hence the retention rate will be low. Therefore, it also directly depends on the effect of the experiment, which makes it as a good evaluation metric.
* **Net conversion** (Number of user-ids remained enrolled for 14 days trial and at least make their first payment/Number of users clicked the `'Start Free Trial button'`): Similarly, for the experiment group, users aware of the time commitment requirement through the screener page and can make a decision to remain enrolled for the course past 14 days trial-period. However, on the control group side, they would be able to continue the payment without aware of the minimum time requirement. Therefore, it can be used as Evaluation metric. The net conversion is the final result after previous two evaluation metrics: gross conversion & retention and we expect to see whether having a `'5 or more hours per week'` button helps to increase the ratio of user making payment over total people see the start free trial page.

* *Click-through-probability* : Generally, it is a good invariant metric in many applications, since the clicks are occurred before the users see the experiment. Therefore it is does not depend on our test which is an excellent invariant metric. However, I believe the number of cookies and number of clicks are already sufficient to use as invariant metric and extra metric is nice to have but may not be as critical as the other two.
* *Number of User-ID* : The number of user-IDs is the number of users who have enrolled in the free trial. It could be used to detect an absolute difference in the number of enrollments between the control and experiment groups. Therefore, it would be a good evaluation metric. However, it is not the best metric as it is not normalized (so gross Conversion is definitively better), and gross conversion can indicate a relative difference between the number of enrollments, I will rather use gross conversion as an evaluation metric instead of Number of User-ID.

**Expected results** : the gross conversion will decrease significantly, which indicate the cost will be lower by introducing the new screener; while net conversion will not decrease significantly , which indicate the screener does not affect the revenues.


**1.2 Measuring Standard Deviation**
>List the standard deviation of each of your evaluation metrics

[Data link](https://docs.google.com/spreadsheets/d/1MYNUtC47Pg8hdoCjOXaHqF-thheGpUshrFA21BAJnNc/edit#gid=0)

* Calculation:
```
Gross conversion(3200 clicks within 40000 page views): se = sqrt(0.20625*(1-0.20625)/3200) = 0.00715
For 50000 page views, we have new_se = 0.00715 * sqrt(40000/5000) = 0.0202 

Retention: se = sqrt((0.53*(1-0.53)/660) * sqrt(40000/5000))) = 0.549

Net conversion(3200 clicks within 40000 page views): se = sqrt(0.1093125*(1-0.1093125)/3200) = 0.0055159 
For 50000 page views, we have new_se = 0.00715 * sqrt(40000/5000) = 0.0156 
```
* Final Results:
```
Gross conversion: 0.0202
Retention: 0.0549
Net conversion: 0.0156
```

>For each of your evaluation metrics, indicate whether you think the analytic estimate would be comparable to the the empirical variability, or whether you expect them to be different (in which case it might be worth doing an empirical estimate if there is time). Briefly give your reasoning in each case.

Both Gross Conversion and Net Conversion used number of cookies as denominator, which is also the unit of diversion. In this case, the unit of diversion is equal to unit of analysis, which indicates the analytical estimate would be comparable to the empirical variability.

For Retention, the denominator is 'Number of users enrolled the courseware' which is not similar as the Unit of Diversion. Therefore the analytical an the empirical estimates are different.


**1.3 Sizing**

* **Number of Samples vs. Power**

>Indicate whether you will use the Bonferroni correction during your analysis phase, and give the number of pageviews you will need to power you experiment appropriately.

No, I did not use Bonferronicorrection during my analysis phase. The metrics in the test has high correlation (covariant) and the Bonferroni correction will be too conservative to it.

During the back-of-the-envelope calculation, I realized that the retention might not be a good evaluation metric for my analysis. Because the amount of page view for retention as evaluation metrics would need almost half year for testing even if we direct 50% of traffic to that experiment. Therefore, I decided just use Gross Conversion and Net Conversion as evaluation metrics. By using [Evan Miller](http://www.evanmiller.org/ab-testing/sample-size.html), the result can be referred below:
```
Probability of enrolling, given click:
20.625% Baseline conversion rate, 1% Minimum Detectable Effect.
Samples needed: 25,835

Probability of payment, given click:
10.93125% Baseline conversion rate, 0.75% Minimum Detectable Effect.
Samples needed: 27,413 (chosen)

Therefore, pageview/group = 27413/0.08 = 342662.5
Total pageview = 342662.5*2 = 685325
*Note1 : only 0.08 pageview leads to click.
*Note2: double pageview because we need total pageview for both experiment and control group
```

* **Duration vs. Exposure**

>Indicate what fraction of traffic you would divert to this experiment and, given this, how many days you would need to run the experiment.

With daily traffic of 40000, I'd direct 100% of my traffic (40000) to the experiment, which means it would take us approximately 17 days (685325/40000 = 17) for the experiment.

>Give your reasoning for the fraction you chose to divert. How risky do you think this experiment would be for Udacity?

I believe this experiment would not affect whole operation of existing paying customers as well as highly motivated students and also would not affect Udacity content. During the experiment, no student going to be exposed anything beyond minimal risk. Neither personal, financial nor otherwise sensitive data will be collected, and no student can be hurt either. Therefore, the whole experiment would not considered as highly risky.  So I decided to direct 100% of traffic to the experiment.


### **2. Experiment Analysis**
[Data link](https://docs.google.com/spreadsheets/d/1Mu5u9GrybDdska-ljPXyBjTpdZIUev_6i7t4LRDfXM8/edit#gid=0)

**2.1 Sanity Checks**

>For each of your invariant metrics, give the 95% confidence interval for the value you expect to observe, the actual observed value, and whether the metric passes your sanity check.

Calculation:
```
1. Number of cookies:
Total Control group pageview: 345543
Total Experiment group pageview: 344660 
Total pageview: 690203
Probability of cookie in control or experiment group: 0.5
SE = sqrt(0.5*(1-0.5)*(1/345543+1/344660) = 0.0006018
Margin of error (m) = SE * 1.96 = 0.0011796
Confidence Interval = [0.5-m,0.5+m] = [0.4988,0.5012]
Observed value  = 344660/690203 = 0.5006

2. Number of clicks: 
Total Control group clicks: 28378
Total Experiment group cliks: 28325
Total pageview: 56703
Probability of cookie in control or experiment group: 0.5
SE = sqrt(0.5*(1-0.5)*(1/28378+1/28325) = 0.0021
Margin of error (m) = SE * 1.96 = 0.0041
Confidence Interval = [0.5-m,0.5+m] = [0.4959,0.5041]
Observed value  = 28378/56703 = 0.50046
```
Result
```
Number of cookies: [0.4988,0.5012]; observed .5006; Pass Sanity Check
Number of clicks : [0.4959,0.5041]; observed .50046; Pass Sanity Check
```

**2.2 Result Analysis**

* **Effect Size Tests**

>For each of your evaluation metrics, give a 95% confidence interval around the difference between the experiment and control groups. Indicate whether each metric is statistically and practically significant.

* Gross Conversion:

|                  | Control Group | Experiment   |
|------------------|---------------|--------------|
| Clicks           | 17293         | 17260        |
| Enrolment        | 3785          | 3423         |
| Gross Conversion | 0.2188746892  | 0.1983198146 |

Calculation:
```
SE = 0.004371675385
m = SE * 1.96 = 0.00856848375
Pooled Probability = 0.2086
D hat = -0.02055
Confidence Interval = [-0.0291,-0.0120]
```
Result:
```
Gross conversion CI: [-.0291, -.0120]
Statistically significant (CI doesn't contain zero)
Practically significant (CI doesn't contain d_min value)
```

* Net Conversion:

|                | Control Group | Experiment   |
|----------------|---------------|--------------|
| Clicks         | 17293         | 17260        |
| Enrolment      | 2033          | 1945         |
| Net Conversion | 0.1175620193  | 0.1126882966 |

Calculation:
```
SE = 0.003434133513
m = SE * 1.96 = 0.0067
Pooled Probability = 0.2086
D hat = -0.0049
Confidence Interval = [-0.0116,-0.0018]
```
Result:
```
Net conversion CI: (-0.0116, 0.0018)
Not statistically significant (CI contains zero)
Not practically significant (CI contain d_min = +/- 0.0075)
```


* **Sign Tests**

>For each of your evaluation metrics, do a sign test using the day-by-day data, and report the p-value of the sign test and whether the result is statistically significant.

* Gross Conversion:
```
Number of success: 4
Number of trials: 23
Probability: 0.5
Two-tailed p-value : 0.0026
```
p-value = 0.0026 < alpha level = 0.025. Therefore, we agree with the initial hypothesis, that the data is statistically and practically significant.

* Net Conversion:
```
Number of success: 10
Number of trials: 23
Probability: 0.5
Two-tailed p-value : 0.6776
```
p-value = 0.6776 > alpha level = 0.025. Therefore, we agree with the initial hypothesis, that the net conversion CI is both statistically and practically insignificant.


* **Summary**

>State whether you used the Bonferroni correction, and explain why or why not. If there are any discrepancies between the effect size hypothesis tests and the sign tests, describe the discrepancy and why you think it arose.

I did not use Bonferroni correction in my work because the metrics in the test has high correlation (covariant) , The Bonferroni correction is designed to limit the risk of Type I errors in multiple comparisons. Therefore the Bonferroni correction will be too conservative to it. We would only launch if all evaluation metrics must show a significant change. In that case, there would be no need to use Bonferroni correction.


**2.3 Recommendation**:

>Make a recommendation and briefly describe your reasoning.

The analysis of gross conversion indicates that the experiment successfully reduced the number of students who did enroll in the free trial, without having enough time to finish the course. On the other hand, the analysis of net conversion results ended up being statistically and practically insignificant while the confidence interval does include the negative number of the practical significance boundary, which means that it's possible that this number went down by an amount that would hurt the business - decrease the revenue. If we consider the initial hypothesis, it does not increase numbers of paid users, which fails the initial goal of launching this feature and likely to be unacceptable risk to launch. Therefore, I would **not** launch the experiment, and I would suggest to try to improve net conversion.


### **3. Follow-up experiment**

>Give a high-level description of the follow up experiment you would run, what your hypothesis would be, what metrics you would want to measure, what your unit of diversion would be, and your reasoning for these choices.

Many lesson videos on Udacity are followed by a set of problems at the end. There will be a hint box after students submit their answer, telling students whether their answer is right. If their answer is wrong, the box will contain some instruction about the error, mainly focusing on which part of question you are wrong. However, in a scenario like that, as a student, I am more willing to know the way how to solve the problem, instead of merely the position where I was wrong.

To address this issue, I would suggest to add more detailed instruction about the error, like reviewing which part of the previous video or some website could help you solve the problem.

My **hypothesis** is that the change would help students to get over their difficulties easier, and therefore, **it would reduce the number of students who cancel early in the course**. 

I would use **user-ID** as the **unit of diversion**, as the change would only be visible to users whose are enrolled in a course.

I would use **user-ID** as an **invariant metric**, and the **number of payments divided by the number of user-IDs** as an **evaluation metric**.

### **References:**

* [Evan Miller](http://www.evanmiller.org/ab-testing/sample-size.html)
* [GraphPad](http://graphpad.com/quickcalcs/binomial1.cfm)

