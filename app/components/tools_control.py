from dash import dcc
tool_list = [
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

def render_tab(tab):
    return dcc.Tab(
        **tab,
        className="custom-tab",
        selected_className="custom-tab--selected b-border"
    )

def get_list_item_by_value(list, value):
    for item in list:
        if item.get("value") == value:
            return item
    return {}

def check_value_in_list(list, value):
    return value if get_list_item_by_value(list, value) else list[0].get("value")

def render_menu_items(key, value):
    item_list = get_list_item_by_value(tool_list, key).get("children")
    if item_list:
        return ([render_tab(tab) for tab in item_list], check_value_in_list(item_list, value))

tools_menu_selector = dcc.Dropdown(
    options=[create_option(item) for item in tool_list],
    value="competitor_analysis",
    id="tools_menu_selector",
    clearable=False,
    searchable=False,
    className="tools_menu_selector"
)

tools_menu = dcc.Tabs(
    id="tools_menu",
    className="d-flex align-items-center lr-border",
    parent_className="flex-grow-1"
)