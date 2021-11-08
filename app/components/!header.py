from dash import dcc, html

from components.logo import logo

menu_items_list = [
    {
        "label": "Конкурентный анализ",
        "value": "competitor_analysis",
        "children": [
            {"label": "Аналитика", "value": "analytics"},
            {"label": "Бренды", "value": "brands"},
            {"label": "Товары", "value": "goods"},
            {"label": "Новинки", "value": "new_items"},
            {"label": "Поисковые запросы", "value": "search_queries"}
        ],
    },
    {
        "label": "Другой инструмент",
        "value": "another_tool",
        "children": [
            {"label": "Вкладка I", "value": "tab_1"},
            {"label": "Вкладка II", "value": "tab_2"},
            {"label": "Вкладка III", "value": "tab_3"},
        ],
    }
]


def create_option(data):
    return {"label": data.get("label"), "value": data.get("value")}


tools_selector = dcc.Dropdown(
    options=[create_option(item) for item in menu_items_list],
    value="competitor_analysis",
    id="tools_selector",
    clearable=False,
    searchable=False,
    className="tools_selector"
)

menu_items = dcc.Tabs(
    id="header_menu",
    value="analytics",
    className="d-flex align-items-center lr-border"
)


def get_children_of_list_item(list, key):
    for item in list:
        if item.get("value") == key:
            return item.get("children")
    return []


def render_tab(tab):
    return dcc.Tab(
        **tab,
        className="custom-tab",
        selected_className="custom-tab--selected b-border"
    )


def render_menu_items(key):
    item_list = get_children_of_list_item(menu_items_list, key)
    return [render_tab(tab) for tab in item_list]


settings_btn = html.Button(
    html.I(className="bi bi-gear"),
    className="settings-btn",
)

header = html.Div(
    [logo, tools_selector, menu_items, settings_btn],
    className="app-header d-flex align-items-center justify-content-between"
)
