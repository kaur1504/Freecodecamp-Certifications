import pandas as pd
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
import numpy as np

data=pd.read_csv("medical_examination.csv")
data['overweight']=(data['weight']/((data['height']/100)**2)>25).astype(int)
data['cholestrol']=(data['cholestrol']>1).astype(int)
data['gluc']=(data['gluc']>1).astype(int)

def draw_cat_plot():
    data_cat=pd.melt(
        data,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    data_cat = (
        data_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    fig = sns.catplot(
        x='variable', y='total', hue='value', col='cardio',
        data=data_cat, kind='bar'
    )

    return fig


def draw_heat_map():
    df_heat = data[
        (data['ap_lo'] <= data['ap_hi']) &
        (data['height'] >= data['height'].quantile(0.025)) &
        (data['height'] <= data['height'].quantile(0.975)) &
        (data['weight'] >= data['weight'].quantile(0.025)) &
        (data['weight'] <= data['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 12))

    sns.heatmap(
        corr, mask=mask, annot=True, fmt=".1f", center=0.0, square=True,
        linewidths=0.5, cbar_kws={"shrink": 0.5}
    )

    return fig