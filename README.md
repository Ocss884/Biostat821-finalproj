# **US Covid-19 Vaccination Visualization Project**  
The US Covid-19 Vaccinations is a simple web application presenting the recent progress of COVID-19 vaccinations in United States for each state based on data from CDC.  

## **Features Intended to Implement**  
1. Interactive US Map: Create an interative US map visualizing the current total doses allocation by state/territory.
2. Time slider: Plot the comparison of vaccine allocations between Pfizer and Moderna with a slider showing the allocaion history.
3. Horizontal bar Plot: Visualize the trend of the dose allocation against new cases in each state and the US overall.
4. Bubble Plot by Companies: Visualize the allocation of Pfizer, Moderna, and Johnson & Johnson vaccines in each state; Create a drop-down list for user's choices of interest.
5. Stats Table: Present the proportion of people who have finished two doses of vaccinations in each state; Create a drop-down list for user's choices of interest for states.

## Directory Tree
```
┣run.py
┣main
    └──static
        ├──img
        ├──assets
            ├──css
            ├──img
            ├──js
            ├──vendor
    ├──templates
        ├──base.html
        ├──index.html
        ├──table.html
        ├──figure
            ├──moderna.html
            ├──pfizer.html
    ├──generator
        ├──map
        ├──db
    ├──__init__.py
    ├──route.py
    ├──vaccine.db
```

## Serve locally
Enter the root directory. Command `export FLASK_APP=main` in linux environment and run `flask run`

## **Data Source**  
All data are obtained from [Data.CDC.gov](https://data.cdc.gov/browse?category=Vaccinations)

## **Member and Contribution**  
* Web building, Server setting: Junrong Lin [@Ocss884](https://github.com/Ocss884)
* Data analysis, Visualization: Lucy Lin [@lucylin1997](https://github.com/lucylin1997), Wenyue Zhuo [@jennyzz17](https://github.com/jennyzz17)

## Architecture  
This application uses [Flask](https://flask.palletsprojects.com/en/1.1.x/) framwork, SQLite database and deployed in [Heroku](www.heroku.com). [Ploty](https://plotly.com/) is used for visualization.
