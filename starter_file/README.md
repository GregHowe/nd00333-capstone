# Heart Failure Prediction

About 18 million people die from cardiovascular diseases, with heart failure being one of the most frequent causes, amounting to 31% of the death toll anually.

The goal of this project is to predict whether a person will survive or not after a heart failure event, using a dataset of patients health records.
We will train a model using Hyperparameter tuning, and a model using AutoML. Then, we'll compare the results and deploy the best model to the Azure cloud.


## Dataset

### Overview

The Heart Failure Prediction dataset was downloaded from Kaggle. However, the dataset was originally built for the following paper:
Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020)
The dataset was collected "at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015".

It contains twelve(12) feature columns and one (1) class column, and 299 rows (records), for 194 men and 105 women, between 40 and 95 years old. All of them had already suffered a heart failure event in the past.

### Task

The goal is to predict if a person will survive a heart failure event before the next follow-up visit to the doctor's office, based on the following features:
- Age: in years
- Anaemia: whether the person has (1) or not (0) anaemia
- Creatinine phospokinase: level of this substance in the blood or another blood fluid
- Diabetes: whether the person has (1) or not (0) diabetes
- Ejection fraction: percentage of blood the left ventricle pumps out with each heart contraction. Less than 40% is risky. Normal values are between 50% and 75%.
- High blood pressure: whether the person has (1) or not (0) high blood pressure
- Platelets: level of this substance in the blood or another blood fluid
- Serum creatinine: level of this substance in the blood or another blood fluid. Waste product of the creatinine. Useful to check whether the kidney is working properly. High levels indicate renal dysfunction.
- Serum sodium: level of this substance in the blood or another blood fluid
- Sex: 1 is men, 0 is women
- Smoking: whether the person smokes (1) or not (0)
- Time: follow-up visit to the doctor in days.

### Access

The dataset CSV file is hosted in a Github repo. Thus, we need to access it as raw content, using a URL that starts with: "https://raw.githubusercontent.com"
Next, we use the Azure ML Dataset library to download and convert the CSV file to a dataset that can be used by the Jupyter notebook running on an Azure ML compute instance.

## Automated ML

Settings:
- 20 is the experiment_timeout_minutes
- It can have 4 concurrent iterations at max
- The primary metric to monitor is the accuracy.

Configuration:
- The task is classification
- The label column is DEATH_EVENT
- It will use automatic featurization: the features will be generated automatically
- It will have early stopping enabled
- The task will be run in a CPU cluster called simba_cluster, vm_size Standard_D2_V2, with 4 nodes.

### Results

34 different models were trained and compared
The best model used the VotingEnsemble algorithm, reaching an accuracy of 87.30 %.
Ten-fold cross validation was used.
All the columns were used for training.

According to (1), serum creatinine and ejection fraction are the most relevant features and are enough to predict if a patient with heart failure will survive or not. Thus, using a dataset with only these two columns would provide better results, increased accuracy and higher performance.


AutoML experiment RunDetails
![AutoML experiment RunDetails]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-RunDetails.png)

AutoML best model
![AutoML best model]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-BestModel.png)

AutoML Voting Ensemble model
![AutoML Voting Ensemble model]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-VotingEnsembleBestModel.png)

## Hyperparameter Tuning

I used a logistic regression model with an SKLearn estimator. I used it because it is a very popular method for binary classification tasks, and because I had used in another project. In short, this algorithm predicts the probability of events. In our case, it would predict the probability of a patient surviving a heart failure event.

The hyperparameters were:
- C (Inverse of regularization strength), with a uniform range from 0.001 to 1.0. Smaller values mean stronger regularization, which means the prediction error on new data will be lower.
- max_iter (maximun number of iterations to converge), with 3 possible values: 50, 100 and 200. Converge: find a solution to the problem.


### Results

The best model reached an accuracy of 76.66% and used the following hyperparameters:
- Regularization Strength: 0.13655501543763932
- Max iterations: 100

Similar to the AutoML model, we could have used only two columns (ejection fraction, serum creatinine) to train the model, reaching superior accuracy and performance.
In both cases, having a bigger dataset could also help improving the results. However, collecting and build a medical records dataset is costly, time-consuming and can only be done by hihgly trained and specialized proffesionals.


Hyperdrive RunDetails
![Hyperdrive RunDetails]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdrive-RunDetails.png)

Hyperdrive best model
![Hyperdrive best model]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdrive-BestModel.png)

Hyperdrive best model in ML Studio
![Hyperdrive best model in ML Studio]
(https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdriver-BestModelMLStudio.png)

## Model Deployment

*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
https://www.youtube.com/watch?v=wZj6kmEjMHw

*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

## References
(1) Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16, https://doi.org/10.1186/s12911-020-1023-5 (2020)
