import matplotlib.pyplot as plt # type: ignore
import pandas as pd
import seaborn as sns # type: ignore
from datetime import datetime

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()


    fig = sns.catplot(
        data=df_bar,
        x="year",
        y="value",
        hue="month",
        kind="bar",
        height=6,
        aspect=1.5,
        palette="tab10"
    )
    fig.set_axis_labels("Years", "Average Page Views")
    fig._legend.set_title("Months")

    fig.savefig('bar_plot.png')
    return fig.fig

def draw_box_plot():
    df_box = df.copy().reset_index()
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig('box_plot.png')
    return fig