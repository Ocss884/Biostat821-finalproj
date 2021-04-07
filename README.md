# **US Covid-19 Vaccination Visualization Project**  
The US Covid-19 Vaccinations is a simple web application presenting the recent progress of COVID-19 vaccinations in United States for each state based on data from CDC.  

## **Features Intended to Implement**  
1. Interactive US Map: Create an interative US map visualizing the current total doses allocation by state/territory.
2. Time slider: Provide a slider for vaccine allocation history.
3. Horizontal bar Plot: Visualize the trend of the dose allocation against new cases in each state and the US overall.
4. Bubble by Companies: Visualize the allocation of Pfizer, Moderna, and Johnson & Johnson vaccines in each state; Create a drop-down list for user's choices of interest.
5. Stats Table: Present the proportion of people who have finished two doses of vaccinations in each state; Create a drop-down list for user's choices of interest for states.

## **Data Source**  
All data are obtained from [Data.CDC.gov](https://data.cdc.gov/browse?category=Vaccinations)

## **Member and Contribution**  
* Web building, Server setting: Junrong Lin [@Ocss884](https://github.com/Ocss884)
* Data analysis, Visualization: Lucy Lin [@lucylin1997](https://github.com/lucylin1997), Wenyue Zhuo [@jennyzz17](https://github.com/jennyzz17)

## Architecture  
This application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) framwork and SQLite database. [Ploty](https://plotly.com/) and [mpld3](https://mpld3.github.io/) are used for visualization.
