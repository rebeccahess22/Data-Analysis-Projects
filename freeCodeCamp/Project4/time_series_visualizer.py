import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
df['date']= pd.to_datetime(df['date'])
df.set_index('date', inplace=True)


def draw_line_plot():
    # Draw line plot
     # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Set custom x-ticks
    ticks = pd.date_range(start='2016-07-01', periods=8, freq='6MS')
    ax.set_xticks(ticks)
    ax.set_xticklabels(ticks.strftime('%Y-%m'))


    plt.show()




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()


    # Create a pivot table  
    #whatever the x axis is will be the index
    df_bar = df_bar.pivot_table(index='year', columns='month', values='value', aggfunc='mean')
    # Reorder the months
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar.reindex(columns=months_order)
    fig, ax = plt.subplots(figsize=(12, 6))
    df_bar.plot(kind='bar', ax=ax, color=sns.color_palette("pastel"))

    ax.set_title('Average Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    plt.legend(title='Months', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Patch np.float if needed
    np.float = float

    # Prepare data
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month_name().str.slice(0, 3)
    df_box['month'] = pd.Categorical(
        df_box['month'],
        categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        ordered=True
    )

    # Create single figure with two subplots side-by-side
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', palette='pastel', fliersize=0.5, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_yticks(np.arange(0, 200001, 20000))
    axes[0].set_ylim(0, 200000)

    # Month-wise box plot
    sns.boxplot(data=df_box, x='month', y='value', palette='pastel', fliersize=0.5, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_yticks(np.arange(0, 200001, 20000))
    axes[1].set_ylim(0, 200000)

    # Final adjustments
    plt.tight_layout()

    # Save and return figure
    fig.savefig('box_plot.png')
    return fig