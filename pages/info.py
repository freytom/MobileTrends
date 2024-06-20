from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
from data import df, all_brand

brand_counts = df['Brand'].value_counts().reset_index()
brand_counts.columns = ['Brand', 'count']
brand_counts = brand_counts.sort_values(by='count', ascending=False).head(10)
fig1 = px.pie(brand_counts, values='count', names='Brand', color_discrete_sequence=px.colors.sequential.Tealgrn)
fig1.update_layout(legend_title_text='Название бренда')

expensive = df[['Smartphone', 'Final Price']]
expensive = expensive.rename(columns={'Smartphone': 'Модель телефона', 'Final Price': 'Цена'})
expensive = expensive.sort_values(by='Цена', ascending=False).head(8)

avg_price_per_brand = df.groupby('Brand')['Final Price'].mean().reset_index()
# Сначала сортируем данные
sorted_brands = avg_price_per_brand.sort_values('Final Price', ascending=False)

# Теперь создаем диаграмму, передав отсортированный список брендов
fig3 = px.bar(sorted_brands, x='Brand', y='Final Price', 
              labels={'Brand': 'Бренд', 'Final Price': 'Средняя цена по бренду, USD'},
              category_orders={'Brand': sorted_brands['Brand'].tolist()},
              color_discrete_sequence=['#76B1A2'])
#fig3 = px.bar(avg_price_per_brand, x='Brand', y='Final Price', labels={'Brand': 'Бренд', 'Final Price': 'Средняя цена по бренду, USD'}, color_discrete_sequence=['#76B1A2'])

#fig3.update_traces(marker_color='#456788')

layout = dbc.Container([
    dbc.Row ([
        dbc.Col(
                html.Div([
                html.H1("Анализ брендов", style={'color' : '#4C7D6F'}),
                html.H5("Изучите информацию о популярных брендах и их ценовому сегменту"),
                html.Hr(style={'color': 'black'}),
            ], style={'textAlign': 'center'})
        )
    ]), 

    dbc.Row([
        dbc.Col([
            html.H5('Популярные бренды смартфонов', className='text-center', style={'color' : '#4C7D6F'}),
            dcc.Graph(
                id='Brand',
                figure=fig1
            )
        ]),

        dbc.Col([
            html.H5('Топ дорогих смартфонов', className='text-center', style={'color' : '#4C7D6F'}),
            dbc.Table.from_dataframe(
                expensive, 
                striped=True, 
                bordered=True, 
                hover=True, 
                index=False
            )
        ]),


        dbc.Row([
            html.H5('Средняя цена по брендам', className='text-center', style= {'margin': '0px 0px 0px 0px', 'color' : '#4C7D6F'}),
            dcc.Graph(
                id='avgPrice',
                figure=fig3,
                style= {'margin': '0px 0px 0px 0px'}
            )
        ])
    ])
])
