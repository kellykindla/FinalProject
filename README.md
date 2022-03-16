# Housing Prices and Neighborhood Safety in Austin

# Background: 
Housing prices in Austin have seen a sharp increase in recent years. According to the Austin Board of Realtors January 2022 report, the meadian house price in Austin Round Rock area is $476,000, up 30% from last January 2021. Simultaneously, in recent years there are reports of increased crime in Austin. According to KVUE, there were 60 homicides in Austin in 2021, the highest in 61 years that the police has kept records. Taking both things into consideration, we wonder if the crime rates are impacting at all what areas are seeing the most house sales and the price they are listed at. 

# Question: 
Can we predict, from reported crime data, the price of a house in a certain area in Austin?
Will crime rates in Austin affect house prices by zipcode? 
Will crime rates and house prices vary per zipcode depending on the year?
Is there a difference between pre-pandemic and post-pandemic house prices and crime rates in Austin? 

# Technologies: 
Python will be used to clean up data and conduct the machine learning analysis. Further information pertaining to the technologies used for this assignment are found in the [technology.md file](technology.md). 

# Data: 
We are using an [Austin house listing data set](https://www.kaggle.com/ericpierce/austinhousingprices) from [kaggle.com](https://www.kaggle.com/) along with [crime reports dataset](https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu) from [austintexas.gov](https://www.austintexas.gov/). We plan to add up crimes per zipcode and merge with the housing dataset, so each listing will have a crime frequency number to help with our analysis. A simple entity relationship diagram is found below:

<img width="277" alt="ERD" src="https://user-images.githubusercontent.com/92558842/158086740-83a18bb9-e932-4d36-8c9e-8d80254170be.png">

# Machine Learning Model: 
With the housing and crime data we will train a logistic regression model to try and predict the home price in a given zipcode.

# Database: 
A PostgreSQL database will be used to store the cleaned Austin house listing and crime reports datasets. A SQL query will be written to join the two datasets before importing to Python to use in the machine learning model. The following dependencies will be used to import and export data, and connect to the PostgreSQL database: sqlalchemy and psycopg2.

# Communication Protocols: 
Our team consists of: Francisco Azares, Kelly Kindla, Nayely Gutierrez, and Philip Leung. Our primary form of communication will be through Slack. If we are unable to reach a team member, we have a form containing everyones email and phone number. The secondary form of communication will be text and final will be email. We have established our GitHub and have created a Google Drive folder containing all project documents that everyone has access to. 