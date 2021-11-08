import dash

BOOTSTRAP = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.0/font/bootstrap-icons.css",
]

app = dash.Dash(
    __name__,
    external_stylesheets=BOOTSTRAP,
    suppress_callback_exceptions=True,
)