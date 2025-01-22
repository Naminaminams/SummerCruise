from dash import dcc, html
import dash_bootstrap_components as dbc
import dash
import dash_leaflet as dl

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
   


locbackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/resortbg4.jpg",
                    "img_style": {"height": "250px", "object-fit": "cover"}  # Set height and scale images
                }, 
            ],
            style={"max-height": "500px"}  # Limit the height of the carousel
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("サマークルーズ（海の家）"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                "どうやってそこに行くのですか", 
                            ], 
                            className="card-text",
                            style={'textAlign': 'center'}
                        ),   
                        
                    ]
                )
            ],
            style={ 
                "position": "absolute",
                "boxShadow": "0 4px 8px rgba(0, 0, 0, 0.2)",   
                "bottom": "40px",  
                "left": "50%",  
                "transform": "translateX(-50%)",  
                "zIndex": 1,  
                "width": "50%",   
                "opacity": 0.8,  
            },
        ),
    ],
    style={"position": "relative", "max-height": "500px"}  # Make parent container relative
)


map = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        dl.Map(
                            [
                                dl.TileLayer(),  
                                dl.Marker(  # Marker for Manila
                                    position=[14.5995124, 120.9842195],
                                    children=dl.Tooltip("Manila, Metro Manila"),
                                ),
                                dl.Marker(  # Marker for Summer Cruise Diving Resort
                                    position=[13.8234639, 120.9064561],
                                    children=dl.Tooltip("Summer Cruise Diving Resort"),
                                ),
                            ],
                            style={"height": "50vh", "width": "100%"},
                            center=[14.2, 120.7],  # Center the map between Manila and the resort
                            zoom=9,
                        ),

                    ], 
                    xs=12, sm=12, md=10, lg=8,  # Adjust column size as needed
                ), 
            ],
            justify="center", 
            align="center",
            className="p-3",  
        ),
    ],
)
   
commute = html.Div(
    [
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H4("バスでの移動方法"),
                        html.P("パサイ⇒レメリー（バス移動）"),
                        html.Br(),
                    ],
                    className="text-center"  # Centers the text horizontally within the column
                )
            ],
            className="justify-content-center align-items-center"  # Centers the content both vertically and horizontally in the row
        ),
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/1.jpg",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/2.jpg",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
            ]
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.P("Gil Puyat 駅(パサイ)降りてすぐのバスターミナルからレメリー行のバスが"),
                        html.P("2 時間おきに出ています。運賃は 200 ペソ。3 時間程度の乗車。"),
                        html.P("※カウンターチケットでの事前購入は不要で運賃は発車後に車内で支払います。"),
                        html.Br(),

                        html.H4("レメリー ⇒ ナルダパーキング（トライシクル移動）"),
                        html.P("パバスを降りたらトライシクルに乗り換えます。ドライバにこの紙を見せてください"),
                        html.P("降車時に 150 ペソを支払います。乗車時間約 30 分"),
                        html.P("トライシクル乗車前に携帯に連絡をください。"),
                        html.P(html.B("Takagaki: 0928-554-9185")),
                    ],
                    className="text-center"  # Centers the text horizontally within the column
                )
            ],
            className="justify-content-center align-items-center"  # Centers the content both vertically and horizontally in the row
        ),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/3.jpg",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/4.jpg",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
            ]
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [

                        html.Br(),

                        html.P("パバスを降りたらトライシクルに乗り換えます。ドライバにこの紙を見せてください"),
                        html.P("降車時に 150 ペソを支払います。乗車時間約 30 分"),
                        html.P("トライシクル乗車前に携帯に連絡をください。"),
                        html.P("Takagaki 0928-554-9185"),
                        html.Br(),

                        html.H6("Paki dalhin ako sa Parking ni NARDA sa SanLuis Balite"),
                        html.P("バリテ村（ナルダパーキング）まで行けますか"),
                        html.H6("Ang bayad ko simula Lemery hanggang SanLuis Balite 150 lamang."),
                        html.P("バリテ村までの料金は 150 ペソでよいですか"),
                    ],
                    className="text-center"  # Centers the text horizontally within the column
                )
            ],
            className="justify-content-center align-items-center"  # Centers the content both vertically and horizontally in the row
        ),

        
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/5.jpg",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    html.Img(
                        src="/assets/pictures/loc/6.png",
                        style={
                            "width": "100%",
                            "height": "250px",
                            "object-fit": "cover",
                            "position": "relative"
                        }
                    ),
                    width={"size": 6},
                    xs=8, sm=8, md=6, lg=6,
                    className="d-flex justify-content-center align-items-center"
                ),
            ]
        ),
        dbc.Row(
            [ 
                dbc.Col(
                    [

                        html.Br(),

                        html.H6("ナダルパーキング⇒海の家"),
                        html.P("弊社スタッフが待機しております。ボートで海の家まで向かいます"), 

                        html.Br(),

                        html.H4("海の家周辺マップ"),

                    ],
                    className="text-center"  # Centers the text horizontally within the column
                )
            ],
            className="justify-content-center align-items-center"  # Centers the content both vertically and horizontally in the row
        )
    ]
)







layout = html.Div(
    [  
        locbackground,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        map, 
                        html.P("車でマニラから2時間30分ほどの距離です。",
                            className="text-center my-3"),
                        html.P("駐車場に到着しましたら携帯にご連絡をください。",
                            className="text-center my-3"),
                        html.P("バスでお越しになられる方はアクセス方法をまとめたPDFを印刷しご利用ください。",
                            className="text-center my-3"),
                        
                        dbc.Button(
                            "地図を見る",  # Button text
                            href="https://maps.app.goo.gl/K6yuSpV5ZkQkzuqaA",
                            style={
                                'margin-left': 'auto',  # Push to the rightmost part
                                'padding': '5px 15px',
                                'font-size': '14px',
                                "border": "1px solid black", 
                                "border-radius": "10px",      
                                "color": "black",   
                                "width": "150px", 
                            },
                            target="_blank"  # Opens the link in a new tab
                        ),
                        html.Br(),
                        html.Hr(),
                        html.Div(
                            commute, 
                                className="text-center" 
                        ),
                        html.Br(),
                        html.Br(),
                    ],
                    xs=12, sm=12, md=8, lg=8,  
                    className="text-center" 
                )
            ],
            justify='center',   
            align='center',    
        )
    ]
)