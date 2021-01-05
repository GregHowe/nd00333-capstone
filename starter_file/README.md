*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Heart Failure Prediction
*TODO:* Write a short introduction to your project.
About 18 million people die from cardiovascular diseases, with heart failure being one of the most frequent causes.
It amounts to 31% of the death toll anually.

The goal of this project is to predict whether a person will survive or not after a heart failure event.
We will train a model using Hyperparameter tuning, and a model using AutoML. Then, we'll compare the results and deploy the best model to the Azure cloud.


## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.
The Heart Failure Prediction dataset was downloaded from Kaggle. However, the dataset was originally built for the following paper:
Davide Chicco, Giuseppe Jurman: Machine learning can predict survival of patients with heart failure from serum creatinine and ejection fraction alone. BMC Medical Informatics and Decision Making 20, 16 (2020)
The dataset was collected "at the Faisalabad Institute of Cardiology and at the Allied Hospital in Faisalabad (Punjab, Pakistan), during April–December 2015".

It contains twelve(12) feature columns and one (1) class column, and 299 rows (records).

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.
The goal is to predict if a person will survive heart failure event based on the following features:
- Age: in years
- Anaemia: whether the person has (1) or not (0) anaemia
- Creatinine phospokinase: level of this substance in the blood or another blood fluid
- Diabetes: whether the person has (1) or not (0) diabetes
- Ejection fraction
- High blood pressure: whether the person has (1) or not (0) high blood pressure
- Platelets: level of this substance in the blood or another blood fluid
- Serum creatinine: level of this substance in the blood or another blood fluid
- Serum sodium: level of this substance in the blood or another blood fluid
- Sex: 1 is men, 0 is women
- Smoking: whether the person smokes (1) or not (0)
- Time: follow-up visit to the doctor in days. NOT USED.

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
