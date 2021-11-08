from dash import html

from components.logo import logo
from components.settings_btn import settings_btn
from components.tools_control import tools_menu_selector, tools_menu

header = html.Div(
    [
        logo, tools_menu_selector, tools_menu, settings_btn
    ],
    className="app-header d-flex align-items-center"
)

main_layout = html.Div([
    header,
    html.Div(
        id="tool_widget",
    ),
])
