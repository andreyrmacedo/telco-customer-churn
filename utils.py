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
            "<b>Gender:</b> %{x}<br>" +
            "<b>Churn:</b> Yes<br>" +
            "<b>Count:</b> %{y}<br><extra></extra>"
    ))

    fig.add_trace(go.Bar(
        x=pivot.index,
        y=pivot['No'],
        name='Churn = No',
        marker_color='steelblue',
        hovertemplate=
            "<b>Gender:</b> %{x}<br>" +
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


