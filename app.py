import dash
import dash_html_components as html
import dash_core_components as dcc


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([ html.H1('Retail User Interface'),


        html.Div([

         html.Div([

            html.H3('RMS Staging Tabel'),
            dcc.Graph(
        id='example-graph-1',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'ORDER_MFQUEU'},
                {'x': [1, 2, 3], 'y': [2, 6, 1], 'type': 'bar', 'name': 'ItemLoc_MFQUEUE'},
                {'x': [1, 2, 3], 'y': [3, 5, 0], 'type': 'bar', 'name': 'Item_MFQUEUE'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )], className="six columns"),

        html.Div([
            html.H3('SIM Staging Table'),
            dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'ASNIn'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Order'},
                {'x': [1, 2, 3], 'y': [0, 6, 3], 'type': 'line', 'name': 'Item'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )], className="six columns"),
    ], className="row")
])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=80,debug=True)
