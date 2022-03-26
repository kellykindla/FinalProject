# Housing Prices and Neighborhood Safety in Austin

## Background: 
Housing prices in Austin have seen a sharp increase in recent years. According to the [Austin Board of Realtors January 2022 report](https://www.abor.com/january-2022-central-texas-housing-market-report), the median house price in the Austin-Round Rock area is $476,000, up 30% from last January of 2021. Simultaneously, in recent years there have been reports of increased crime in Austin. According to [KVUE, there were 60 homicides in Austin in 2021](https://www.kvue.com/article/news/local/austin-homicide-record-number-2021/269-e3c419af-9722-456f-9b5d-c044944e128d), the highest in 61 years that the police has kept records. Taking both things into consideration, we wonder if the crime rates are impacting, at all, what areas are seeing the most house sales and the price they are listed at. 

## Question: 
- Can we predict, from reported crime data, the price of a house in a certain area in Austin?
- Will crime rates in Austin affect house prices by zip code? 
- Will crime rates and house prices vary per zip code depending on the year?
- Is there a difference between pre-pandemic and post-pandemic house prices and crime rates in Austin? 

## Technologies: 
Python will be used to clean up data and conduct the machine learning analysis. Further information pertaining to the technologies used for this assignment are found in the [technology.md file](technology.md). 

## Data: 
The data used for this project comes from an [Austin House Listing dataset](https://www.kaggle.com/ericpierce/austinhousingprices) found on [kaggle.com](https://www.kaggle.com/), along with a [crime reports dataset](https://data.austintexas.gov/Public-Safety/Crime-Reports/fdj4-gpfu) from [austintexas.gov](https://www.austintexas.gov/). The Austin House Listing dataset contains information pertaining to the housing market from 2018 to 2021. We chose this dataset as it listed houses from multiple zip codes around Austin and it offered insight on the features of each listing, such as: if the house was in a homeowner's association, the nearby schools, and the latest listing price. We hope to connect this dataset to the crime reports dataset on zip code and determine if the latest listing price for a home could be predicted by the number of crimes in a zip code. The crime reports dataset contains records of incidents that the Austin Police Department responded to and reported. This dataset is updated weekly; however, the dataset used for this analysis was last updated on 7 March 2022. The raw dataset contains 2.41 million rows of data from 2002 to 2022. We will filter this dataset to contain reported crimes from 2018 to 2021. An entity relationship diagram for our project is shown below. This diagram displays the relationships between the datasets; furthermore, the columns we will remove from each dataset in efforts to reduce noise are listed in red. 

<img width="273" alt="ERD" src="https://user-images.githubusercontent.com/92558842/158905458-85cf337a-3f74-4d9e-a139-2b9c5419d47b.png">

## Machine Learning Model: 
## Our Model: 
We are trying to find the relationship between two or more continuous variables in efforts to determine if crimes in Austin have an effect on the housing prices between 2018 and 2021. We will implement a Multiple Linear Regression, supervised Machine Learning model in which the model will find the best fit linear line between the dependent variable- the latest listing price and the independent variables- the number of crimes per zip code, the hour the crime occurred, and a multitude of variables related to the house. This model best fits our data as our data has labels and has the potential to learn, based on the input variables, what the output (latest listing price) might be. Furthermore, by using an ordinary least squares regression technique to evaluate our regression model, we are able to estimate the coefficients of the linear regression equation to identify the relationship and impact each variable has on the latest listing price. 

## Data Preprocessing: 
** insert preprocessing information and images 

## Model Accuracy: 
To accomplish our model, our data was grouped by zip code to count the occurrence of crimes and this DataFrame was merged to the housing data. An initial attempt of our model showed a low adjusted r-squared score of 0.38. In efforts to improve our model, we encoded zip codes so each could be evaluated in the model. Furthermore, columns that initially showed insignificant p-values (greater than 0.05) were dropped. Our data was split into training and testing sets and was further scaled to improve accuracy. We used sklearn’s LinearRegression to perform our model and statsmodels.api to display the OLS Regression results. After refactoring, our adjusted r-squared score is 0.556 and we find that for each crime occurrence, the latest listing price increase by 6302.9761. 

<img width="705" alt="MLM" src="https://user-images.githubusercontent.com/92558842/160219021-ebcbe85f-3aa2-4417-912c-262b369b06fe.png">

## Further Investigation 
If time permitted, we would like to investigate the effect crime grouped by year had on our model. To do this, we would have liked to run four models, one for each year— 2018, 2019, 2020, and 2021 in order to investigate the impact each variable had on the latest listing price for each house by zip code by year. If time permitted, it also could have been beneficial to encode each categorical variable to determine it’s impact on the latest listing price. Similarly, it would be interesting to include more crime data to determine if it impacts the latest listing price in any way or changes the weight of the crime occurrence variable.  

## Database: 
A PostgreSQL database will be used to store the cleaned Austin house listing and crime reports datasets. A SQL query will be written to join the two datasets before importing to Python to use in the machine learning model. The following dependencies will be used to import and export data, and connect to the PostgreSQL database: sqlalchemy and psycopg2.

## Communication Protocols: 
Our team consists of: Francisco Azares, Kelly Kindla, Nayely Gutierrez, and Philip Leung. Our primary form of communication will be through Slack. If we are unable to reach a team member, we have a form containing everyone's email and phone number. The secondary form of communication will be text and final form will be email. We have established our GitHub and have created a Google Drive folder containing all project documents that everyone has access to. 
