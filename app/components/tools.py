from dash import html
from dash import dcc

from components.show_more_filters_btn import show_more_filters_btn
from components.change_category_btn import change_category


tabs_list = [
    {"label": "Ниша", "value": "niche"},
    {"label": "Бренды", "value": "brands"},
    {"label": "Размеры", "value": "sizes"},
    {"label": "Свойства предмета", "value": "properties"},
    {"label": "Динамика в нише", "value": "dynamics"},
    {"label": "Связанные поиски", "value": "related_searches"},
    {"label": "+", "value": "plus"},
]

filter_list = {
    "first_color_dropdown": {
        "options": [
            {"label": "Белый", "value": "0"},
            {"label": "Чёрный", "value": "1"},
            {"label": "Горох", "value": "2"},
        ],
        "placeholder": "Первый цвет",
    },
    "gender_dropdown": {
        "options": [
            {"label": "Mужской", "value": "m"},
            {"label": "Женский", "value": "f"},
            {"label": "Унисекс", "value": "u"},
        ],
        "placeholder": "Пол",
    },
    "brand_dropdown": {
        "options": [
            {"label": "Hand brand", "value": "0"},
            {"label": "Brand & Co", "value": "1"},
            {"label": "Brand & Son", "value": "2"},
        ],
        "placeholder": "Бренд", }
}


def render_dropdown(data):
    return dcc.Dropdown(
        **data,
        className="tools_widget_dropdown"
    )


def create_filter(filterId):
    data = filter_list.get(filterId)
    if data:
        return render_dropdown(data)


show_more_filters_btn = html.Button(
    "Показать ещё",
    className="outlined-button"
)

filters = [
    create_filter("brand_dropdown"),
    create_filter("first_color_dropdown"),
    create_filter("gender_dropdown"),
    show_more_filters_btn,
]


def create_tab(kwargs):
    return dcc.Tab(
        **kwargs,
        className="custom-tab",
        selected_className="custom-tab--selected"
    )


content_tabs = dcc.Tabs(
    [create_tab(tab) for tab in tabs_list],
    id="content_control",
    value="niche",
    className="width-fit-content"
)

analitic_tools = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        change_category,
                        *filters,
                    ],
                    className="d-grid gap-3 h-100 tool-box",
                ),
                content_tabs,
            ],
            className="gradient-background"
        ),
        html.Div(id="content_view")
    ],
    className="d-flex flex-column justify-content-between h-100"
)
