from dash import dash_table
from dash.dash_table import FormatTemplate
from dash.dash_table.Format import Format, Group, Symbol

percentage = FormatTemplate.percentage(0)

money = Format(
    group=Group.yes,
    groups=3,
    group_delimiter=" ",
    decimal_delimiter=",",
    symbol=Symbol.yes,
    symbol_suffix=" руб."
)

group = Format(group_delimiter=" ", group=Group.yes, groups=3)
table_columns = [
    {"name": "Категория", "id": "category"},
    {
        "name": "Товаров в продаже",
        "id": "on_sale",
        "format": group,
        "type": "numeric"
    },
    {
        "name": "Заказано за период",
        "id": "ordered",
        "format": group,
        "type": "numeric"
    },
    {
        "name": "Выгрузка по заказам за период",
        "id": "orders_unloading",
        "format": money,
        "type": "numeric"
    },
    {
        "name": "Товаров без заказов",
        "id": "no_orders",
        "format": percentage,
        "type": "numeric"
    },
    {"name": "Оборачиваемость продаваемых", "id": "turnover"},
]

total = {
    "orders_unloading": 8014948116,
    "on_sale": 1350476,
    "ordered": 5658257,
}

data = [
    {
        "category": "Аксессуары\n\t>\tСумки и рюкзаки",
        "on_sale": 267662,
        "ordered": 1033247,
        "orders_unloading": 1802177683,
        "no_orders": 0.46,
        "turnover": 104,
    },
    {
        "category": "Аксессуары\n\t>\tГоловные уборы",
        "on_sale": 230368,
        "ordered": 1338519,
        "orders_unloading": 833656306,
        "no_orders": 0.44,
        "turnover": 132,
    },
    {
        "category": "Аксессуары\n\t>\tОчки и футляры",
        "on_sale": 75670,
        "ordered": 367695,
        "orders_unloading": 479650410,
        "no_orders": 0.34,
        "turnover": 99,
    },
    {
        "category": "Аксессуары\n\t>\tЧехлы",
        "on_sale": 255847,
        "ordered": 1082186,
        "orders_unloading": 479650410,
        "no_orders": 0.6,
        "turnover": 148,
    },
    {
        "category": "Аксессуары\n\t>\tБижутерия",
        "on_sale": 195639,
        "ordered": 684737,
        "orders_unloading": 283110500,
        "no_orders": 0.5,
        "turnover": 136,
    },
    {
        "category": "Аксессуары\n\t>\tРемни и пояса",
        "on_sale": 48336,
        "ordered": 269808,
        "orders_unloading": 169032196,
        "no_orders": 0.39,
        "turnover": 157,
    },
    {
        "category": "Аксессуары\n\t>\tПлатки и шарфы",
        "on_sale": 78776,
        "ordered": 263888,
        "orders_unloading": 167015882,
        "no_orders": 0.45,
        "turnover": 127,
    },
    {
        "category": "Аксессуары\n\t>\tКошельки и кредитницы",
        "on_sale": 73432,
        "ordered": 209442,
        "orders_unloading": 144916458,
        "no_orders": 0.52,
        "turnover": 147,
    },
    {
        "category": "Аксессуары\n\t>\tЧасы и ремешки",
        "on_sale": 49160,
        "ordered": 161588,
        "orders_unloading": 121316388,
        "no_orders": 0.62,
        "turnover": 102,
    },
    {
        "category": "Аксессуары\n\t>\tЧемоданы и дорожные сумки",
        "on_sale": 8047,
        "ordered": 29845,
        "orders_unloading": 91047036,
        "no_orders": 0.59,
        "turnover": 101,
    },
    {
        "category": "Аксессуары\n\t>\tПерчатки и варежки",
        "on_sale": 44438,
        "ordered": 137945,
        "orders_unloading": 7633484,
        "no_orders": 0.51,
        "turnover": 197,
    },
]


def data_bars(column):
    bounds = [i / 100 for i in range(101)]
    ranges = [total[column] * i for i in bounds]
    styles = []
    for i in range(1, 101):
        start = ranges[i - 1]
        end = ranges[i]
        percentage = bounds[i] * 100
        styles.append({
            'if': {
                'filter_query': (
                    '{{{column}}} >= {start}' +
                    (' && {{{column}}} < {end}' if (i < 100) else '')
                ).format(column=column, start=start, end=end),
                'column_id': column
            },
            'background': (
                """
                    linear-gradient(90deg,
                    #BFDBFA 0%,
                    #BFDBFA {percentage}%,
                    white {percentage}%,
                    white 100%)
                """.format(percentage=percentage)
            ),
            'paddingBottom': 2,
            'paddingTop': 2
        })

    return styles


style_data_conditional = [{
    "if": {"column_id": "category"},
    "whiteSpace": "pre-line",
    "textAlign": "left"
}]
style_data_conditional.extend(data_bars("on_sale"))
style_data_conditional.extend(data_bars("ordered"))
style_data_conditional.extend(data_bars("orders_unloading"))

data_table_niche = dash_table.DataTable(
    columns=table_columns,
    data=data,
    style_data_conditional=style_data_conditional,
    style_cell={
        "overflow": "hidden",
        "textOverflow": "ellipsis",
    },
    style_header={"whiteSpace": "normal"},
    filter_action="native",
    sort_action="native",
)
