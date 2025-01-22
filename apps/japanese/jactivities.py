import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  


activitiesbackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/resortbgwide.jpg",
                    "img_style": {"height": "500px", "object-fit": "cover"}  
                }, 
            ],
            style={"max-height": "500px"}   
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("活動"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                """ビーチフロントを散策する!""",
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

  
snorkelcard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("シュノーケリング")),  
                            html.Br(),
                            html.P(html.B("スキンダイビング")), 
                            html.Ul([
                                html.Li("エントリーフィー	P350"),
                                html.Li("ご宿泊のお客様はエントリー費無料"),
                                html.Li("７歳以下は半額、３歳以下は無料"),
                                html.Li("飲料水・コーヒーは無料"),
                                html.Li("ホットシャワー・タオルの使用"),
                                html.Li("シュノーケルレンタル	P300	(３時間の料金)"), 
                                html.Li("(マスク・シュノーケル・ブーツ・フィン) "), 
                            ]),  
                            html.Br(),
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/activities/activity1.jpg", 
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
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)
 
 

familycard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("釣り")), 
                            html.Ul([
                                html.Li("ギアレンタル P2,500"), 
                                html.Li("餌を含む ✔"),   
                                html.Li("ボートを含む ✔"),  
                            ]),  

                            html.P(html.B("アイランドホッピング")), 
                            html.Ul([
                                html.Li("ボート代 1人当たり P400"), 
                            ]), 
                            html.Br(), 
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/activities/activity3.JPG", 
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
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)
 



Introdivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("PADIオープンウォーターコー ")), 
                            html.P(html.B("ダイビング経験不要、何方でも参加可能")), 
                            html.Ul([ 
                                html.Li("体験ダイビング（ビーチ）P1,800"), 
                                html.Li("体験ダイビング（ボート）P3,600"),  
                                html.Li("１時間程度の座学授業を5レッスン ✔ "),  
                                html.Li("限定水域練習（浅場）ｘ５ダイブ（30分～40分/ダイブ） ✔ "), 
                                html.Li("海洋実習ｘ４ダイブ。（30分～40分/ダイブ） ✔"),
                                html.Li("食事は含まれません"),
                            ]),  
                            html.Br(),
                             
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/activities/activity4.jpg", 
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
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)





opendivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("PADI認定コース ")),  
                            html.Ul([ 
                                html.Li("オープンウォータ (ビーチエントリー) P16,800"),  
                                html.Li("アカデミックレッスン5 回とオープンウォーターレッスン2回 ✔ "),  
                                html.Li("ダイビング器材フルセット１日の費用 ✔ "), 
                                html.Li("マニュアル・Ｃカード申請費含む ✔ "),  
                                html.Li("参加資格（12歳以上）"),
                                html.Li("食事は含まれません"),
                            ]),  
                            html.Br(), 
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/activities/activity5.jpg", 
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
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)




advanceddivecard = html.Div(
    [ 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [ 
                            html.P(html.B("PADI認定コース")),   
                            html.Ul([ 
                                html.Li(" アドバンス （ビーチ）P16,800"),  
                                html.Li("アカデミックレッスン5 回とオープンウォーターレッスン5回 ✔ "),  
                                html.Li("ダイビング器材フルセット１日の費用 ✔ "), 
                                html.Li("マニュアル・Ｃカード申請費含む ✔ "),  
                                html.Li("参加資格（12歳以上）"),
                                html.Li("食事は含まれません"),
                            ]),  
                            html.Br(), 
                        ],
                        className="d-flex flex-column align-items-start"  # Left-align content
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src="/assets/pictures/activities/activity6.jpg", 
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
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)


 





 


picture_cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/boatdive.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/couple.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/turtle.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/dive1.png", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/dive2.png", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/activities/dive3.png", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)

















layout = html.Div(
    [
        activitiesbackground,
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("Swimming, Snorkeling, Skin Diving"), style={'textAlign': 'center'}),
                        snorkelcard,
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("Family Bonding Activities"), style={'textAlign': 'center'}),
                        familycard, 
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("SCUBA Diving"), style={'textAlign': 'center'}),
                        Introdivecard, 
                        html.Br(),
                        html.Br(),
                        html.H3(html.B("SCUBA Diving Certification"), style={'textAlign': 'center'}),
                        opendivecard, 
                        html.Br(),
                        html.Br(),
                        advanceddivecard, 
                        html.Br(),
                        html.Br(), 
                        picture_cards,
                        html.Br(),
                        html.Br(),
 
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)