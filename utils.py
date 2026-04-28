"""
Created on 2026-04-18
@author: Andrey

Description
-----------
This file has helper functions.
"""

#%% IMPORTS

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.stats import gaussian_kde

#%% FUNCTIONS

def churn_barplot(
        df: pd.DataFrame, 
        column_name: str,
        churn_col: str='Churn',
):
    # Group & count 
    counts = (
        df.groupby([column_name, churn_col])
        .size()
        .reset_index(name='count')
    )
    # Pivot
    pivot = (
        counts
        .pivot(index=column_name, columns=churn_col, values='count')
        .fillna(0)
    )
    
    # Create plot
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=pivot.index,
        y=pivot['Yes'],
        name='Churn = Yes',
        marker_color='crimson',
        hovertemplate=
            f"<b>{column_name}:</b>" + " %{x}<br>" +
            "<b>Churn:</b> Yes<br>" +
            "<b>Count:</b> %{y}<br><extra></extra>"
    ))

    fig.add_trace(go.Bar(
        x=pivot.index,
        y=pivot['No'],
        name='Churn = No',
        marker_color='steelblue',
        hovertemplate=
            f"<b>{column_name}:</b>" + " %{x}<br>" +
            "<b>Churn:</b> No<br>" +
            "<b>Count:</b> %{y}<br><extra></extra>"
    ))

    fig.update_layout(
        template='plotly_white',
        yaxis_title='<b>Count</b>',
        xaxis_title=f'<b>{column_name}</b>',
        showlegend=False
    )

    return fig



def nx2_figure(df, columns):
    n = len(columns)
    rows = (n + 1) // 2  # ceil division

    fig = make_subplots(
        rows=rows,
        cols=2,
        subplot_titles=columns
    )

    for i, col in enumerate(columns):
        row = i // 2 + 1
        col_pos = i % 2 + 1

        subfig = churn_barplot(df, col)

        for trace in subfig.data:
            fig.add_trace(trace, row=row, col=col_pos)

    # --- Dynamic height ---
    height_per_row = 250  # tweak this
    fig.update_layout(
        height=rows * height_per_row,
        template="plotly_white",
        showlegend=False,
        margin=dict(t=60, b=40)
    )

    return fig



def churn_kde_plot(df, column_name, churn_col='Churn'):
    fig = go.Figure()

    # Split data
    yes = df[df[churn_col] == 'Yes'][column_name].dropna()
    no = df[df[churn_col] == 'No'][column_name].dropna()

    # Create common x range
    x_min = min(df[column_name])
    x_max = max(df[column_name])
    x_vals = np.linspace(x_min, x_max, 200)

    # KDE
    kde_yes = gaussian_kde(yes)
    kde_no = gaussian_kde(no)

    y_yes = kde_yes(x_vals)
    y_no = kde_no(x_vals)

    # YES trace
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_yes,
        mode='lines',
        name='Churn = Yes',
        line=dict(color='crimson', width=2),
        fill='tozeroy',
        fillcolor='rgba(220, 20, 60, 0.25)',
        hovertemplate=
            f"<b>{column_name}:</b> %{{x:.2f}}<br>" +
            "<b>Churn:</b> Yes<br>" +
            f"<b>Density:</b> %{{y:.4f}}<extra></extra>"
    ))

    # NO trace
    fig.add_trace(go.Scatter(
        x=x_vals,
        y=y_no,
        mode='lines',
        name='Churn = No',
        line=dict(color='steelblue', width=2),
        fill='tozeroy',
        fillcolor='rgba(70, 130, 180, 0.25)',
        hovertemplate=
            f"<b>{column_name}:</b> %{{x:.2f}}<br>" +
            "<b>Churn:</b> No<br>" +
            f"<b>Density:</b> %{{y:.4f}}<extra></extra>"
    ))

    # Layout
    fig.update_layout(
        template='plotly_white',
        yaxis_title='<b>Density</b>',
        xaxis_title=f'<b>{column_name}</b>',
        title=dict(
            text=f'<b>Distribution of {column_name} by Churn</b>',
            x=0.5,
            xanchor='center',
            font=dict(size=20)
        ),
        legend=dict(
            x=1,
            y=1,
            xanchor='right',
            yanchor='top'
        )
    )

    return fig

# %%
