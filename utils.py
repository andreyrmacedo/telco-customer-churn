"""
Created on 2026-04-18
@author: Andrey

Description
-----------
This file has helper functions.
"""

#%% IMPORTS

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
            f"<b>{column_name}:</b>" + "%{x}<br>" +
            "<b>Churn:</b> Yes<br>" +
            "<b>Count:</b> %{y}<br><extra></extra>"
    ))

    fig.add_trace(go.Bar(
        x=pivot.index,
        y=pivot['No'],
        name='Churn = No',
        marker_color='steelblue',
        hovertemplate=
            f"<b>{column_name}:</b>" + "%{x}<br>" +
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
    height_per_row = 300  # tweak this
    fig.update_layout(
        height=rows * height_per_row,
        template="plotly_white",
        showlegend=False,
        margin=dict(t=60, b=40)
    )

    return fig
