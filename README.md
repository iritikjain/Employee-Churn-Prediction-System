# Employee Churn Prediction System

## Employee Churn Predictor

## Introduction

Employee Churn is defined as the percentage of employees leaving an organization over a specific period of time.
The churn rate is frequently referred to as employee attrition rate or employee turnover rate. Employee churn rate indicates how frequently the company’s employees quit their jobs within a given period. Note that employee churn rates can significantly vary among companies and industries.

## Major Factors Contributing To Employee Churn -

- Lack Of Growth Plan And Opportunities
- Skewed Work-Life Balance
- Bad Workplace Culture
- Dissatisfactory Appraisals
- Low Staff Morale

## Did You Know ?

According to the Society of Human Resources Management's (SHRM) 2018 Employee Recognition Report, employee churn is the number one challenge for most organizations globally. A staggering 29% of these organizations admitted to being stressed about finding replacements. Although a certain level of employee turnover is normal in any organization, however, high rates of employee churn can be a costly affair.

## Problem Statement

In today's world, many organizations focus on maintaining their reputation, business standards and performance. So to achieve this, they first train their newly joined employees and spend huge amount on these trainings. But usually most of these employees switch their jobs within a short span of joining. In most cases employees with niche skills are harder to replace. This affects the ongoing work and productivity of existing employees. Again acquiring new employees as a replacement has its huge costs such as hiring costs and training costs. Also, the new employee will take time to learn skills to be at par of technical or business expertise knowledge of the older employee. Organizations can simply tackle this problem by applying Machine Learning techniques to predict employee churn, which helps them in taking necessary actions such as negotiating with the employees, mentoring and guiding to retain them.

## Project Description

This project aims to solve the above mentioned problem by using Azure Machine Learning Service. It uses Two-Class Decision Forest module to create a machine learning model based on the random decision forests algorithm. The dataset used to train and test the model have the following attributes - Employee ID, Satisfaction Level, Last Evaluation Score, Number Of Projects, Average Monthly Hours, Time Spent In The Company, Accidents While Working, Promotion In Last 5 Years, Department, Salary Range and Left. Here, the target attribute is "Left" which have two values either 0 or 1 where 0 indicates "have not left the company" and 1 indicates "have left the company". The entire dataset is split into 80% and 20% ratio where 80% of dataset is used for training the model and the rest 20% is used for testing the model. The accuracy of this ML model is 98.70%. So, this ML Model is then deployed as a web service using Azure Machine Learning. The project takes the above mentioned attributes except the target attribute "Left" as an input via a form. Then the data is passed to the ML Model Web Service and the model evaluates the data and sends back the prediction of whether the employee will leave the company or not. This prediction is displayed on the webpage to the end user. In this way, the organizations can take necessary actions for the employees who are on the verge of leaving the company.

## Tech Stack

- Azure Machine Learning
- Azure Container Instance
- Azure Web App Service
- HTML, CSS, Bootstrap
- Flask (Python)

## Outputs


![image](https://user-images.githubusercontent.com/85997443/157715624-76a144b4-6b34-4973-9dbc-64b2f333152a.png)


![image](https://user-images.githubusercontent.com/85997443/157715698-7ddc2701-06a6-4f80-9883-2b735b803f8a.png)


![image](https://user-images.githubusercontent.com/85997443/157715733-a3e88355-b469-48f1-b008-b358ce182e3c.png)


![image](https://user-images.githubusercontent.com/85997443/157715806-c9ed4854-fc1b-4bc7-adaf-4054ab1f2c2c.png)


## Thank You For Reading!
