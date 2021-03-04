# -*- coding: utf-8 -*-

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

user_stats, chkdout_stats, changelists_ds, full_info_df = logic_handler()
# user_stats['n of files'] = user_stats['n of files'].astype(str).astype(int)
# user_stats['Rating'] = user_stats['n of files'].apply(lambda x:
#                                                             '⭐⭐⭐' if x > 100 else (
#                                                             '⭐⭐' if x > 50 else (
#                                                             '⭐' if x > 10 else '')))

colors = {
    'background': '#111111',
    'text': '#111111'
}
app = dash.Dash()

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')


app.layout = html.Div(children=[
    html.H1(children='P4V Nanion Monitor',
    style= {
        'textAlign': 'center'
    }),
    html.H2(children = chkdout_stats,
    style= {
        'color': colors['text'],
        'textAlign': 'left'
    }),
    #! Table user stats
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
    ),
    html.H2(children='Last 10 Submitted Changelists'),
    #! Table changelist
    dash_table.DataTable(
        id='Last 10 Changelists',
        # style_data={
        # 'whiteSpace': 'normal',
        # 'height': 'auto',
        # 'lineHeight': '30px'
        # },
        columns=[{"name": i, "id": i} for i in changelists_ds.columns],
        style_data_conditional=[
            {'if': {'column_id': 'change_n'},
            'width': '200px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'date'},
            'width': '200px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'user'},
            'width': '200px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'description'},
            'width': '400px',
            'textAlign': 'left'
            },
        ],
        data=changelists_ds.to_dict('records'),
        fill_width=False
    ),
    html.H2(children='Files Checked Out in Parallel'),
    #! Table potential conflicts
    dash_table.DataTable(
        id='Files Checked Out in Parallel',
        # style_data={
        # 'whiteSpace': 'normal',
        # 'height': 'auto',
        # 'lineHeight': '30px'
        # },
        columns=[{"name": i, "id": i} for i in full_info_df.columns],
        style_cell_conditional=[
            {'if': {'column_type': 'text'},
            'backgroundColor': 'red'
            },
            {'if': {'column_id': 'path'},
            'width': '400px',
            'textAlign': 'left'
            },
            {'if':{'column_id': 'johannes.stiehler'},
            'width': '100px',
            'textAlign': 'center',
            #'backgroundColor': 'red'
            },
            {'if': {'column_id': 'igor.pugliesi'},
            'width': '100px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'peter.prinzen'},
            'width': '100px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'danil.konowalow'},
            'width': '100px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'kilian.frhler'},
            'width': '100px',
            'textAlign': 'center'
            },
            {'if': {'column_id': 'Timo_Stengel'},
            'width': '100px',
            'textAlign': 'center'
            },
        ],
        data=full_info_df.to_dict('records'),
        fill_width=False,
    ),
    #! Blank header
    html.H2(children='End')
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
#     #app.run_server(host= '0.0.0.0', port=5000,debug=False)