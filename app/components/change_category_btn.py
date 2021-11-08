from dash import html
import dash_bootstrap_components as dbc

change_category_btn = html.Button(
    "Изменить категории",
    className="filled-button",
    n_clicks=0,
    id="change_category_btn"
)

change_category_modal = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Empty header")),
        dbc.ModalBody("Empty"),
        dbc.ModalFooter(
            dbc.Button(
                "Close",
                id="change_category_modal_close",
                n_clicks=0,
            )
        )
    ],
    id="change_category_modal",
    is_open=False
)

change_category = html.Div([change_category_btn, change_category_modal])
