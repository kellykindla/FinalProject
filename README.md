# Housing Prices and Neighborhood Safety in Austin

## Background: 
Housing prices in Austin have seen a sharp increase in recent years. According to the Austin Board of Realtors January 2022 report, the meadian house price in the Austin-Round Rock area is $476,000, up 30% from last January of 2021. Simultaneously, in recent years there have been reports of increased crime in Austin. According to KVUE, there were 60 homicides in Austin in 2021, the highest in 61 years that the police has kept records. Taking both things into consideration, we wonder if the crime rates are impacting, at all, what areas are seeing the most house sales and the price they are listed at. 

## Question: 
Can we predict, from reported crime data, the price of a house in a certain area in Austin?

Will crime rates in Austin affect house prices by zipcode? 

Will crime rates and house prices vary per zipcode depending on the year?

Is there a difference between pre-pandemic and post-pandemic house prices and crime rates in Austin? 

## Technologies: 
Python will be used to clean up data and conduct the machine learning analysis. Further information pertaining to the technologies used for this assignment are found in the [technology.md file](technology.md). 

## Data: 
The data used for this project comes from an [Austin House Listing dataset](https://www.kaggle.com/ericpierce/austinhousingprices) found on [kaggle.com](https://www.kaggle.com/), along with a [crime reports dataset](https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu) from [austintexas.gov](https://www.austintexas.gov/). The Austin House Listing dataset contains information pertaining to the housing market from 2018 to 2021. We chose this dataset as it listed houses from multiple zip codes around Austin and it offered insight on the features of each listing, such as: if the house was in a homeowners association, the nearby schools, and the latest listing price. We hope to connect this dataset to the crime reports dataset on zip code and determine if the latest listing price for a home could be predicted by the number of crimes in a zip code. The crime reports dataset contains records of incidents that the Austin Police Department responded to and reported. This dataset is updated weekly; however, the dataset used for this analysis was last updated on 7 March 2022. The raw dataset contains 2.41 million rows of data from 2002 to 2022. We will filter this dataset to contain reported crimes from 2018 to 2021. A entity relationship diagram for our project is shown below. This diagram displays the relationships between the datasets; furthermore, the columns we will remove from each dataset in efforts to reduce noise are listed in red. 

<img width="273" alt="ERD" src="https://user-images.githubusercontent.com/92558842/158905458-85cf337a-3f74-4d9e-a139-2b9c5419d47b.png">

## Machine Learning Model: 
For our analysis, we are aiming to find the relationship between two continuous variables— the number of crimes per zip code and the latest listing price for houses in Austin between 2018 and 2021. With this, we will implement a Linear Regression, supervised Machine Learning model in which the model will find the best fit linear line between the independent variable- the number of crimes per zip code- and the dependent variable- the latest listing price. 

After our preliminary attempt at our Machine Learning model, we found a low R-squared score of 0.02 which suggests a low correlation between the datasets. The pairwise correlation of the columns of our merged dataset shows the following: 

<img width="364" alt="Screen Shot 2022-03-17 at 4 48 09 PM" src="https://user-images.githubusercontent.com/92558842/158905519-90621dde-2422-4887-9aec-9ac4ac079009.png">

To refactor and improve our model, we may attempt to train the model on other independent variables (such as homeowners association presence or the count of nearby schools). In other efforts to improve our model, we will attempt a multiple linear regression where we have multiple independent variables (such as the weight of a crime, time of day, or property tax rate) along with the number of crimes per zip code to predict the latest price listing of a home in Austin. 

## Database: 
A PostgreSQL database will be used to store the cleaned Austin house listing and crime reports datasets. A SQL query will be written to join the two datasets before importing to Python to use in the machine learning model. The following dependencies will be used to import and export data, and connect to the PostgreSQL database: sqlalchemy and psycopg2.

## Communication Protocols: 
Our team consists of: Francisco Azares, Kelly Kindla, Nayely Gutierrez, and Philip Leung. Our primary form of communication will be through Slack. If we are unable to reach a team member, we have a form containing everyones email and phone number. The secondary form of communication will be text and final form will be email. We have established our GitHub and have created a Google Drive folder containing all project documents that everyone has access to. 
