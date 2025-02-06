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
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/map_car.jpg", 
                                    style={
                                        "width": "100%", 
                                        "height": "auto", 
                                        "position": "relative"
                                    }
                                ),
                                
                            ],
                            style={
                                "position": "relative",
                                "text-align": "center"
                            }
                        ),
                    ],
                    width={"size": 12, "offset": 0},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
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
                        html.P("1 時間おきに出ています。運賃は 250 ペソ。3~時間程度の乗車。"),
                        html.P("※カウンターチケットでの事前購入は不要で運賃は発車後に車内で支払います。"),
                        html.Br(),

                        html.H4("レメリー ⇒ ナルダパーキング（トライシクル移動）"),
                        html.P("バスを降りたらトライシクルに乗り換えます。"),
                        html.P("降車時に 250 ペソを支払います。乗車時間約 30 分"),
                        html.P("トライシクル乗車前に携帯に連絡をください。"),
                        html.P(html.B("0969-241-7880 TAKAGAKI")),
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
                        html.P("0969-241-7880 TAKAGAKI"),
                        html.Br(),

                        html.H6("Paki dalhin ako sa Parking ni NARDA sa SanLuis Balite"),
                        html.P("バリテ村（ナルダパーキング）まで行けますか"),
                        html.H6("Ang bayad ko simula Lemery hanggang SanLuis Balite 250 lamang."),
                        html.P("バリテ村までの料金は 250 ペソでよいですか"),
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

                        html.H6("ビヌクボクパーキング⇒海の家"),
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
                        html.P(html.B("0969-241-7880 TAKAGAKI"),
                            className="text-center my-3"),
                        
                        dbc.Button("地図を開く", color="light", href="https://www.google.com/maps/dir//RWF6%2BM5F+Binukbok+Parking+Area,+Batangas/@13.824083,120.9068588,814m/data=!3m1!1e3!4m17!1m7!3m6!1s0x33bd083a59a12ae7:0x3afeb59f11b3702c!2sBinukbok+Parking+Area!8m2!3d13.8241976!4d120.9104208!16s%2Fg%2F11dxl8t656!4m8!1m0!1m5!1m1!1s0x33bd083a59a12ae7:0x3afeb59f11b3702c!2m2!1d120.9104208!2d13.8241976!3e2?entry=ttu&g_ep=EgoyMDI0MTAwOS4wIKXMDSoASAFQAw%3D%3D",   
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "180px",
                                    "margin": "20px 0"  
                                },
                                target="_blank"
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