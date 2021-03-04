from stats_handler import user_stats
import dash, dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

from handler import logic_handler

#! N of checked out files per user
#? All Checked out Files
#? Conflicting Files
#? Last 5 check outs

user_stats, chkdout_stats = logic_handler()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app = dash.Dash()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


app.layout = html.Div(children=[
    html.H1(children='P4V Nanion Monitor'),
    html.H2(children = chkdout_stats,
    style= {
        'color': colors['text']
    }),

    dash_table.DataTable(
        id='Parallel check outs',
        # style_data={
        # 'whiteSpace': 'normal',
        # 'height': 'auto',
        # 'lineHeight': '30px'
        # },
        columns=[{"name": i, "id": i} for i in user_stats.columns],
        style_cell_conditional=[
            {'if': {'column_id': 'user'},
            'width': '200px',
            'textAlign': 'left'
            },
            {'if': {'column_id': 'n of files'},
            'width': '200px',
            'textAlign': 'center'
            },
        ],
        data=user_stats.to_dict('records'),
        fill_width=False
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
#     #app.run_server(host= '0.0.0.0', port=5000,debug=False)