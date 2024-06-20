from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df, all_brand

ram_counts = df['RAM'].value_counts().reset_index()
ram_counts.columns = ['RAM', 'count']
fig1 = px.pie(ram_counts, values='count', names='RAM', color_discrete_sequence=px.colors.sequential.Tealgrn)
fig1.update_layout(legend_title_text='Кол-во памяти, ГБ')

total_count = df['Storage'].value_counts().sum()
storage_counts = df['Storage'].value_counts().reset_index()
storage_counts.columns = ['Storage', 'count']
storage_counts['percentage'] = (storage_counts['count'] / total_count) * 100
storage_counts = storage_counts[storage_counts['percentage'] > 0.5]
fig2 = px.pie(storage_counts, values='count', names='Storage', color_discrete_sequence=px.colors.sequential.Tealgrn)
fig2.update_layout(legend_title_text='Кол-во памяти, ГБ')
                   
color_counts = df['Color'].value_counts().reset_index()
color_counts.columns = ['Color', 'count']
fig3 = px.bar(color_counts, x='Color', y='count', labels={'Color': 'Цвет', 'count': 'Кол-во смартфонов'}, color_discrete_sequence=['#76B1A2'])

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
                html.Div([
                html.H1("Анализ характеристик", style={'color' : '#4C7D6F'}),
                html.H5("Изучите информацию о тенденциях в характеристиках смартфонов"),
                html.Hr(style={'color': 'black'}),
            ], style={
                'textAlign': 'center',
                'margin': '0px 0px 30px 0px'
                })
        )
    ]), 

    dbc.Row([
        dbc.Col([
            html.H5('Распределение оперативной памяти', className='text-center', style={'color' : '#4C7D6F'}),
            dcc.Graph(
                id='RAM',
                figure=fig1
            )
        ], width=6),

         dbc.Col([
            html.H5('Распредедение встроенной памяти', className='text-center', style={'color' : '#4C7D6F'}),
            dcc.Graph(
                id='Storage',
                figure=fig2
            )
        ], width=6)
    ]),

    dbc.Row([
        html.H5('Распределение по цветамм', className='text-center', style={'color' : '#4C7D6F'}),
         dcc.Graph(
                id='Color',
                figure=fig3
            )
    ])  
])