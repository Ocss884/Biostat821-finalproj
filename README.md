# **US Covid-19 Vaccination Visualization Project**  
The US Covid-19 Vaccinations is a simple web application presenting the recent progress of COVID-19 vaccinations in United States for each state based on data from CDC.  

## **Features intend to implement**  
1. Interactive US Map: Create an interative US map visualizing the current total doses allocation by state/territory.
2. Time slider: Provide a slider for vaccine allocation history
4. Horizontal bar Plot: Visualizing the trend of the dose allocation against new cases in US and each state
5. Bubble by Companies: Visualizing the allocation of Pfizer, Moderna, and Johnson & Johnson vaccine in each state. Create a drop-down list for user's choice of interest.
6. Table: Presenting the proportion of people who have finished two doses of vaccinations for each state

## **About the data**  
All data are from [Data.CDC.gov](https://data.cdc.gov/browse?category=Vaccinations)

## **Member and contribution**  
* Web building, Server setting: Junrong Lin [@Ocss884](https://github.com/Ocss884)
* Data analysis, Visualization: Lucy Lin [@lucylin1997](https://github.com/lucylin1997), Wenyue Zhuo [@jennyzz17](https://github.com/jennyzz17)

## Architecture  
This application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) framwork and SQLite database. [Ploty](https://plotly.com/) and [mpld3](https://mpld3.github.io/) are used for visualization.
