import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('FreeCodeCamp\Data analysis\\boilerplate-page-view-time-series-visualizer\\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
  (df['value'] >= df['value'].quantile(0.025)) &
  (df['value'] <= df['value'].quantile(0.975))
  ]


def draw_line_plot():

    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax = plt.plot(df.index, 'value', data=df, color='r', linewidth=1)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame(
        {
            'Years':df.index.year,
            'Months':[m.month_name() for m in df.index],
            'value':df['value']
        }
    ).groupby(['Years', 'Months'])['value'].mean().unstack()

    df_bar = df_bar[['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

    # Draw bar plot
    
    fig = df_bar.plot.bar(
        figsize=(9,7),
        ylabel='Average Page Views'
    ).figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['num_month'] = df_box['date'].dt.month

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    ax[0] = sns.boxplot(
        x='year',
        y='value',
        data=df_box,
        ax=ax[0],
        linewidth=1
    )
    ax[1] = sns.boxplot(
        x='month',
        y='value',
        data=df_box.sort_values('num_month'),
        ax=ax[1],
        linewidth=1
    )

    ax[0].set_ylabel('Page Views')
    ax[0].set_xlabel('Year')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[1].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
