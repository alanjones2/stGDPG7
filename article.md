# How to Visualize the Economic Impact of the Pandemic using Jupyter Notebooks and Streamlit

## Are we back on track after the shock of the COVID pandemic. We can use OECD data, Python, a simple regression model and Jupyter Notebooks to find out and create an interactive Streamlit app to show the results.

![](images/app-screen.png)


In most countries, GDP dropped like a stone in the first quarter of 2020. Lockdowns and illness meant that industry ground to a halt.

Under normal circumstances GDP tends to grow over time but when there are exceptional events like the one we are going through now and the financial crash of 2008, it doesn't. It falls - dramatically.

GDP is an indicator of the overall wealth of a country; when it is high employment tends to be higher and citizens are generally wealthier. But shocks, such as the one we are experiencing now, don't necessarily mean that the underlying economic factors have changed. So, will our economies recover to the level that they would have been if the panademic had not occurred? Indeed, as some politicians imply, have they already done so?

It really depends on how you look at it - what you are measuring and over what period. 

We are going to look at how growth might have continued without the effects of 2008 and the pandemic using a regression model trained with data from the intervening years. We can then compare the current state of affairs with the modelled one.

### OECD data

I have used data from the OECD to produce some visualizations with Plotly that may help clarify the situation. 

I did my first analysis in a Jupyter notebook in order to address some specific questions. Then I created a Streamlit app (which you can see in the image above) that enables the user to interactively engage with the data (this is a proptotype which will be updated soon).

_The Notebook, Streamlit app and data files will all be made available for download - see links at end._

I decided to look only at the the G7 countries as this was a more doable than to try and tackle the whole world. And the OECD helpfully provide GPD and economic growth data over a period from 2007 to the end of 2021. This conveniently covers the 2008 financial melt-down as well as the current situation.

As you might expect the OECD data is free for anyone to use as long as you reference it correctly. So, to be clear, the data set is from the OECD's _Quarterly National Accounts_ and is referenced fully at the end of this article.

The data is a combination of three time series:

- VIXOBSA: Volume index, OECD reference year 2015, seasonally adjusted
- GPSA: Growth rate based on seasonally adjusted volume data, percentage change from previous quarter
- GYSA: Growth rate based on seasonally adjusted volume data,  percentage change from same quarter of previous year


The original OECD data can be found [here](https://stats.oecd.org/Index.aspx?QueryId=77241) but for convenience I have split the data into three separate tables: _GPSA.csv_, _GYSA.csv_ and _IXOBSA.csv_ and created individual Pandas dataframes to hold that data.

If you want to follow along in a Jupyter notebook, then you'll need to import the libraries first.

    import pandas as pd
    import matplotlib
    import matplotlib.pyplot as plt

The we can create the dataframes.

    # GPSA
    gpsa = pd.read_csv('GPSA.csv', index_col='Country')    

    # GYSA
    gysa = pd.read_csv('GYSA.csv', index_col='Country')  

    # VIXOBSA       
    vixobsa = pd.read_csv('VIXOBSA.csv', index_col='Country')


Here is a snapshot of the VIXOBSA table.

![](images/vixobsa-snapshot.png)

You can see that the columns represent the four quarters of each year starting in 2007. And the rows are for the 7 countries in the G7 group.

Each entry represents the GDP for a quarter. So, in the second row at _Q1-2007_ (first quarter, 2007) we see that France's GDP was 95 and over time it gradually increases. But if we look further into that year, we see that the numbers start going down again beginning in Q4 2008.

The numbers, by the way are not a total number of dollars ar any other currency but are relative to 2015. The average GDP for 2015 is taken to be 100 and then each quarter is calculated relative to that: thus if the figure for a particular quarter is 95, then that represents a value that is 95% of the  average in 2015. Representing GDP in this way means we can plot the numbers of all countries on a graph and see the relative growth of each one on the same scale.

And here is a line graph of GDP for the G7 over the period 2007 to 2021.

![](images/vixobsa-line-all-years.png)

And here is the code that generated it.

    vixobsa.T.plot(figsize=(15,5))

Note that I have used a transposed dataframe to make the plot so that the x axis is time and the y axis the countries.


You can see that between the beginning of 2010 up until recently, GDP has been rising in most countries (with the notable exeception of Italy).

Then the pandemic struck and GDP plummeted to levels not seen since 2008/9. And while there was a quick recovery GDP did not bounce back to its previous levels, rather it shot up initially and then began to rise more slowly.

Let's zoom in a little to see it in a little more detail.

    # track GDP over the last 3 years
    vixobsa.T[-12:].plot(figsize=(15,5), grid=True)

![](images/vixobsa-line-2019-2021.png)

It's easier to see now that GDP is rising again and is approaching, or even exceeding, pre-pandemic levels.

Here is a line graph of GPSA of all countries for the entire time period.

![](images/gpsa-line-all-years.png)

And you can see from this that the change in GPSA at the beginning of the pandemic was vastly greater than during the 2008 financial crash.

    # from worst of pandemic to end 2020
    (vixobsa['Q4-2021']-vixobsa['Q2-2020']).plot.bar(
        title='Difference in GDP Q2 2020 to Q4 2021')


But that shows us percentage change over a short period - each quarter 

GPSA
Each entry represents the percentage difference in GDP for a quarter compared with the previous quarter in the same year. So, in the second row at _Q1-2008_ (first quarter, 2008) we see that France's GDP was 0.4% higher than in the fourth quarter of 2007. But if we look further into that year, we see that the numbers are negative meaning that GDP had dropped compared to the previous quarters.



### Reference
1. OECD (2022), _Quarterly National Accounts  : G7 GDP for EI copy_, URL: https://stats.oecd.org/Index.aspx?QueryId=77241 (accessed on 26/02/2022)
