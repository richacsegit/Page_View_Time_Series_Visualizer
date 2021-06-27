import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",
                  parse_dates= True,
                  index_col= "date")

# Clean data
df = df[(df['value']>= df['value'].quantile(0.025)) & 
        (df['value']<= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax= plt.subplots()
    ax.plot(df.index, df['value'], c= 'red')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()

    df_bar['year']= pd.DatetimeIndex(df_bar.index).year
    df_bar['month']= pd.DatetimeIndex(df_bar.index).month

    df_bar= df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar= df_bar.unstack()

    # Draw bar plot

    fig= df_bar.plot(kind ="bar", figsize = (15,10)).figure
    plt.legend(fontsize= 12, title="Months", labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xlabel("Years", fontsize= 12)
    plt.ylabel("Average Page Views", fontsize= 12)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()

    df_box['year'] = pd.DatetimeIndex(df_box.index).year
    df_box['month'] = pd.DatetimeIndex(df_box.index).strftime('%b') 

    df_box['month_num']= pd.DatetimeIndex(df_box.index).month
    df_box= df_box.sort_values(by= 'month_num')

    # Draw box plots (using Seaborn)

    fig, (ax1, ax2)= plt.subplots(1,2, figsize= (18,10))

    sns.boxplot(x= df_box['year'], y= df_box['value'], ax= ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    sns.boxplot(x= df_box['month'], y= df_box['value'], ax= ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
