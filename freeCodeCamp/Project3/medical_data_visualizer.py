import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import data
df = pd.read_csv('medical_examination.csv')

# 2. Add 'overweight' column
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (df['BMI'] > 25).astype(int)

# 3. Normalize data
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Categorical plot
def draw_cat_plot():
    # 5. Create DataFrame for cat plot
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
    )

    # 6. Group and reformat the data to split by 'cardio'
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Draw the catplot
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar',
        data=df_cat
    )

    # 8. Save figure
    fig.savefig('catplot.png')
    return fig


# 9. Heat map
def draw_heat_map():
    # 10. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11. Calculate the correlation matrix
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 14. Draw the heatmap
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        ax=ax
    )

    # 15. Save figure
    fig.savefig('heatmap.png')
    return fig
