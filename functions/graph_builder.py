import plotly
import plotly.graph_objs as go
import numpy as np

import json


def create_plot(names, values, title):
    fig = go.Figure(data=[go.Bar(
        x=values, y=names,
    )])
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    fig.update_layout(title_text=title)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON