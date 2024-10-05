from dash import Dash, html, dcc
import dash

# Tailwind CSS
external_scripts = [
    {'src': 'https://cdn.tailwindcss.com'}
]

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    external_scripts=external_scripts
)

app.layout = html.Div(children=[
    html.Div(className='mx-auto max-w-7xl px-2 py-4 bg-blue-400', children=[
        html.Div(className='flex flex-col items-center gap-3', children=[
            html.Div(className='w-48 aspect-square overflow-hidden rounded-full', children=[
                html.Img(className='w-full h-full object-cover', src="assets/logo.jpg")
            ]),
            dcc.Link(html.H1(className='font-bold text-3xl text-white', children="Interfaz Gráfica"), href='/')
        ])
    ]), 
    html.Div(className='mx-auto max-w-7xl px-2 py-4', children=[
        html.Div(className='flex gap-6 justify-center', children=[
            dcc.Link(html.Button('Edo 1er Orden', className='px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700'), href='/'),
            dcc.Link(html.Button('Edo 2er Orden', className='px-4 py-2 bg-blue-600 text-white rounded-xl hover:bg-blue-700'), href='/Edo2')
        ])
    ]),
    html.Div(className='mx-auto max-w-7xl px-2 py-4', children=[
        dash.page_container
    ]),
    html.Div(className='mx-auto max-w-7xl h-[16rem] mt-6 px-2 py-4 bg-blue-800', children=[
        html.Div(className='h-full flex flex-col justify-center items-center gap-3 text-white', children=[
            html.P(children=[
                html.Strong("Alumno: "),
                html.Span("Linares Rojas, Ander Rafael")
            ]),
            html.P(children=[
                html.Strong("Código: "),
                html.Span("22140367")
            ])
        ]),

    ]), 
])

if __name__ == '__main__':
    app.run_server(debug=True)
