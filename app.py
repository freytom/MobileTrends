import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, dcc, html
from pages import comparison, exrtainfo, info, about


external_stylesheets = [dbc.themes.MINTY]  # Вместо FLATLY выберите свою тему из https://bootswatch.com/
app = Dash(__name__, external_stylesheets=external_stylesheets,  use_pages=True)
app.config.suppress_callback_exceptions = True

# Задаем аргументы стиля для боковой панели. Мы используем position:fixed и фиксированную ширину
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "2rem 1rem",
    "background-color": "#4C7D6F", # Цвет фона боковой панели меняем на тот, который больше всего подходит436D61
}

# Справа от боковой панели размешается основной дашборд. Добавим отступы
CONTENT_STYLE = {
    "margin-left": "17rem",
    "margin-right": "1rem",
    "padding": "2rem 1rem",
    #"background-color": "#EBECF1"
}

sidebar = html.Div(
    [
        html.H2("Мобильные тренды" , className="display-6", style={'color' : 'white', 'font-style': 'bold'}),
        html.Hr(style={'color' : 'white'}),
        html.P([
             "Учебный проект студентов группы БСБО-15-21 ",
             html.Br(),
             "Крамаренко А.Д. и",
             html.Br(),
             "Прокопенко Д.А."
             ],className="lead", style={'color' : "#9EFFE3"}
             ),
        html.Hr(style={'color' : 'white'}),
        html.H5("Меню", style={'textAlign': 'center', 'color' : 'white'}),
        dbc.Nav(
            [
                dbc.NavLink("Информация о проекте", href="/page-1", active="exact"),
                dbc.NavLink("Анализ брендов", href="/page-2", active="exact"),
                dbc.NavLink("Анализ характеристик", href="/page-3", active="exact"),           
                dbc.NavLink("Сравнение смартфонов", href="/page-4", active="exact"),
            ],
            vertical=True,
            pills=True,
            style={'font-size': '20px'}
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return about.layout
    elif pathname == "/page-1":
        return about.layout
    elif pathname == "/page-2":
        return info.layout
    elif pathname == "/page-3":
        return exrtainfo.layout
    elif pathname == "/page-4":
        return comparison.layout
    # Если пользователь попытается перейти на другую страницу, верните сообщение 404. Мы изменим её в следующей практической.
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
        style={'margin' : '0px 0px 0px 40px'}
    )

if __name__ == '__main__':
    app.run_server(debug=True)
