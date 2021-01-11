# Heart Failure Prediction

About 18 million people die from cardiovascular diseases, with heart failure being one of the most frequent causes, amounting to 31% of the death toll anually.

The goal of this project is to predict whether a person will survive or not after a heart failure event, using a dataset of patients health records.
We will train a model using Hyperparameter tuning, and a model using AutoML. Then, we'll compare the results and deploy the best model to the Azure cloud.


## Dataset

### Overview

The Heart Failure Prediction dataset was downloaded from Kaggle. However, the dataset was originally built for [1] and collected "at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015".

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

The dataset CSV file is hosted in a Github repo. Thus, we need to access it as raw content, using a URL that starts with: "https://raw.githubusercontent.com".

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
![AutoML experiment RunDetails](https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-RunDetails.png)

AutoML best model
![AutoML best model](https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-BestModel.png)

AutoML Voting Ensemble model
![AutoML Voting Ensemble model](https://github.com/jhonatantirado/nd00333-capstone/blob/master/AutoML-VotingEnsembleBestModel.png)

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
![Hyperdrive RunDetails](https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdrive-RunDetails.png)

Hyperdrive best model
![Hyperdrive best model](https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdrive-BestModel.png)

Hyperdrive best model in ML Studio
![Hyperdrive best model in ML Studio](https://github.com/jhonatantirado/nd00333-capstone/blob/master/Hyperdriver-BestModelMLStudio.png)


## Best Models Comparison

The table below compares the accuracy obtained by the best models generated by AutoML and Hyperdrive. We can see the Voting Ensemble model reached an accuracy 11% superior to the one reached by the Logistic regression model. In my experience with Azure ML, AutoML always generates better models, and usually the best models are based on the Voting Ensemble algorithm, which provides better results than the Logistic Regression model. The collective wisdom of multiple models/algorithms performs better than the one of a single model (Logistic Regression). This is the key difference between both models.

Model | Accuracy
------------ | -------------
Auto ML - Voting Ensemble| 87.30%
Hyperdrive - Logistic Regression | 76.66%

## Model Deployment

The AutoML Voting Ensemble model was deployed to an Azure Container Instance programmatically.

To query the model and predict a new instance, we should send a POST request to the score endpoint.

POST http://a10dc4c0-4353-4824-9eb8-293d64e7fe81.southcentralus.azurecontainer.io/score


The input can predict several data instances in parallell since the input payload supports multiple data instances.

Sample input/payload:

```
{
  "data": [
    {
      "age": 36,
      "anaemia": 0,
      "creatinine_phosphokinase": 200,
      "diabetes": 0,
      "ejection_fraction": 30,
      "high_blood_pressure": 0,
      "platelets": 120000,
      "serum_creatinine": 1.1,
      "serum_sodium": 135,
      "sex": 1,
      "smoking": 0,
      "time": 7
    },
    {
      "age": 39,
      "anaemia": 0,
      "creatinine_phosphokinase": 300,
      "diabetes": 0,
      "ejection_fraction": 50,
      "high_blood_pressure": 0,
      "platelets": 200000,
      "serum_creatinine": 0.9,
      "serum_sodium": 250,
      "sex": 0,
      "smoking": 0,
      "time": 1
    }
  ]
}
```

The content type should be set in the headers:
- Content-Type: 'application/json'

Also, if authentication is enabled, we should include key in the header as follows:
- Authorization: Bearer {key}

The request can be submitted using clients like POSTMAN, or directly from code as in [endpoint.py](https://github.com/jhonatantirado/nd00333-capstone/blob/master/starter_file/endpoint.py)

Best model endpoint is in Healthy deployment status![Best model endpoint is in Healthy deployment status](https://github.com/jhonatantirado/nd00333-capstone/blob/master/ModelEnpointActive.png)

Scoring URI Swagger documentation![Scoring URI Swagger documentation](https://github.com/jhonatantirado/nd00333-capstone/blob/master/SwaggerDocumentation.png)

## Future Improvements
- According to (1), serum creatinine and ejection fraction are the most relevant features and are enough to predict if a patient with heart failure will survive or not. Thus, using a dataset with only these two columns would provide better results, increased accuracy and higher performance.
- Also, having a bigger dataset could also help improving the results. However, collecting and build a medical records dataset is costly, time-consuming and can only be done by hihgly trained and specialized proffesionals.
- We could also scale the data prior to training the Logistic Regression model.
- Another improvement would be to do a model grid search, comparing Random Forest, Support Vector Machine and Logistic Regression models, for the Hyperdrive experiment.
- Deploy the best model to an Azure Kubernetes Cluster, to provide greater scalability and performance for production workloads.
- Consume the scoring endpoint from a web or mobile application

## Screen Recording

[Capstone Project by Jhonatan Tirado](https://www.youtube.com/watch?v=fQRlLeOf72E)

The screencast includes the following:

- A working model: heart-failure-prediction-automl-model
- Demo of the deployed  model: heartfailurepredictionautomlv2
- Demo of a sample request sent to the endpoint and its response: using the [endpoint.py](https://github.com/jhonatantirado/nd00333-capstone/blob/master/starter_file/endpoint.py) script and the Jupyter notebook
- Demo of any additional feature of your model: Application Insights

## References
[1] Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16, [DOI link](https://doi.org/10.1186/s12911-020-1023-5) (2020)
