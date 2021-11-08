from dash.dependencies import Input, Output, State

from app import app
from components.tools_control import render_menu_items
from components.tools import analitic_tools
from components.data_table import data_table_niche

@app.callback(Output("tools_menu", "children"),
              Output("tools_menu", "value"),
              Input("tools_menu_selector", "value"),
              State("tools_menu", "value"))
def change_tools_menu_select(key, value):
    return render_menu_items(key, value)

@app.callback(Output("tool_widget", "children"),
              Input("tools_menu", "value"))
def change_tools_menu_item(value):
    if value == "analytics":
        return analitic_tools

@app.callback(Output("content_view", "children"),
              Input("content_control", "value"))
def change_content(value):
    if value == "niche":
        return data_table_niche

@app.callback(
    Output("change_category_modal", "is_open"),
    [
        Input("change_category_btn", "n_clicks"),
        Input("change_category_modal_close", "n_clicks"),
    ],
    [State("change_category_modal", "is_open")],
)
def handle_toggle_change_category_modal(open, close, is_open):
    if open or close:
        return not is_open
    return is_open