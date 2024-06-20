from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df, all_brand

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
                html.Div([
                html.H1("Сравнение смартфонов", style={'color' : '#4C7D6F'}),
                html.H5("Выберите два интересующих вас смартфона и ознакомьтесь с характеристиками"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
      )
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.B('Смартфон 1', style={'color' : '#4C7D6F'})
        ], style={'textAlign': 'center', 'margin' : '0px 0px 20px 0px'}),

        dbc.Col([
            html.B('Смартфон 2', style={'color' : '#4C7D6F'})
        ], style={'textAlign': 'center'}),
    ]),

    dbc.Row ([
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.P("Бренд:", style={'font-weight': 'bold', 'color' : '#4C7D6F'})
                ], width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id = 'crossfilter-brand1',
                 # заполняем дропдаун уникальными значениями континентоы из датасета
                        options = [{'label': i, 'value': i} for i in all_brand],
                 # значение континента, выбранное по умолчанию
                        value = all_brand[0],
                 # возможность множественного выбора
                        multi = False
                     )
                ], width=10)
            ], style = {
            'backgroundColor': 'rgb(143, 232, 207)',
            'padding': '10px 10px 10px 10px'
        }),

            dbc.Row([
                dbc.Col([
                    html.P("Модель:", style={'font-weight': 'bold', 'color' : '#4C7D6F'})
                ], width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id = 'crossfilter-model1',
                        multi = False
                    )
                ], width=10)
            ], style = {
            'backgroundColor': 'rgb(143, 232, 207)',
            'padding': '10px 10px 10px 10px'
            })  
        ], style = {
            'border': 'thin lightgrey solid',
            'margin': '0px 0px 30px 10px'
            }),

        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.P("Бренд:", style={'font-weight': 'bold', 'color' : '#4C7D6F'})
                ], width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id = 'crossfilter-brand2',
                 # заполняем дропдаун уникальными значениями континентоы из датасета
                        options = [{'label': i, 'value': i} for i in all_brand],
                 # значение континента, выбранное по умолчанию
                        value = all_brand[0],
                 # возможность множественного выбора
                        multi = False
                     )
                ], width=10)
            ], style = {
            'backgroundColor': 'rgb(143, 232, 207)',
            'padding': '10px 10px 10px 10px'
        }),

            dbc.Row([
                dbc.Col([
                    html.P("Модель:", style={'font-weight': 'bold', 'color' : '#4C7D6F'})
                ], width=2),
                dbc.Col([
                    dcc.Dropdown(
                        id = 'crossfilter-model2',
                        multi = False
                    )
                ], width=10)
            ], style = {
            'backgroundColor': 'rgb(143, 232, 207)',
            'padding': '10px 10px 10px 10px'
             }),  
        ], style = {
            'border': 'thin lightgrey solid',
            'margin': '0px 10px 30px 30px'
            })  
        ]),

    dbc.Row([
        dbc.Col([
            html.H6("Характеристики", className='text-center')
        ]),

        dbc.Col([
            html.H6("Характеристики", className='text-center')
        ]),
    ], style= {'margin': '10px 0px 20px 0px'}),

    dbc.Row([
        dbc.Col(
            dbc.Table(
            id='table-container1'
            )
        ),
        dbc.Col(
            dbc.Table(
            id='table-container2'
            )
        )
    ])
    

    ])      

#подтягиваем данные в дропдаун с выбором модели 1го смартфона
@callback( 
    [Output('crossfilter-model1', 'options'),
    Output('crossfilter-model1', 'value'),
    ],
    Input('crossfilter-brand1', 'value')
)
def update_region(brand):
    all_brand=df[(df['Brand'] == brand)]['Smartphone'].unique()
    dd_model1 = [{'label': i, 'value': i} for i in all_brand]
    dd_model_value1 = all_brand[0]
    return dd_model1, dd_model_value1


#подтягиваем данные в дропдаун с выбором модели 2го смартфона
@callback(
    [Output('crossfilter-model2', 'options'),
    Output('crossfilter-model2', 'value'),
    ],
    Input('crossfilter-brand2', 'value')
)
def update_region(brand):
    all_brand=df[(df['Brand'] == brand)]['Smartphone'].unique()
    dd_model2 = [{'label': i, 'value': i} for i in all_brand]
    dd_model_value2 = all_brand[0]
    return dd_model2, dd_model_value2


#создаём таблицу 1го смартфона и подтягиваем в неё данные
@callback(
    Output('table-container1', 'children'),
    Input('crossfilter-model1', 'value')
)
def update_table(dd_model_value2):

    df_phone2=df[(df['Smartphone'] == dd_model_value2)]

    df_phone2.sort_values(by='Smartphone')

    data = [
        ('Полное название', df_phone2.iloc[0]['Smartphone']),
        ('Оперативная память, ГБ', df_phone2.iloc[0]['RAM']),
        ('Встроенная память, ГБ', df_phone2.iloc[0]['Storage']),
        ('Цвет', df_phone2.iloc[0]['Color']),
        ('Цена, USD', df_phone2.iloc[0]['Final Price'])
    ]
    
    table1 = dbc.Table(
        [html.Thead(html.Tr([html.Th('Параметр'), html.Th('Значение')]))] +
        [html.Tbody([
            html.Tr([
                html.Td(parameter),
                html.Td(value)
            ]) for parameter, value in data
        ])],
        bordered=True,
        style={'border': '1px solid black', 'border-color' : '#4C7D6F'}
    )
    
    return table1


#создаём таблицу 2го смартфона и подтягиваем в неё данные
@callback(
    Output('table-container2', 'children'),
    Input('crossfilter-model2', 'value')
)
def update_table(dd_model_value2):

    df_phone2=df[(df['Smartphone'] == dd_model_value2)]

    data = [
        ('Полное название', df_phone2.iloc[0]['Smartphone']),
        ('Оперативная память, ГБ', df_phone2.iloc[0]['RAM']),
        ('Встроенная память, ГБ', df_phone2.iloc[0]['Storage']),
        ('Цвет', df_phone2.iloc[0]['Color']),
        ('Цена, USD', df_phone2.iloc[0]['Final Price'])
    ]
    
    table2 = dbc.Table(
        [html.Thead(html.Tr([html.Th('Параметр'), html.Th('Значение')]))] +
        [html.Tbody([
            html.Tr([
                html.Td(parameter),
                html.Td(value)
            ]) for parameter, value in data
        ])],
        bordered=True,
        style={'border': '1px solid black', 'border-color' : '#4C7D6F'}
    )
    
    return table2