import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  
 

roombackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/bg2.png",
                    "img_style": {"height": "250px", "object-fit": "cover"}  # Set height and scale images
                }, 
            ],
            style={"max-height": "500px"}  # Limit the height of the carousel
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("Rooms"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                "マニラ近郊サンルイスでご宿泊！",
                                html.Br(),  
                                "海の景色を眺めながらリラックス"
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

   

standardpics = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/rooms/room1.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/rooms/room3.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/rooms/room5.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)

standard= html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [ 
                        dbc.Table(
                            [  
                                html.Tbody(
                                    [
                                        html.Tr([
                                            html.Td("スタンダード"),  
                                            html.Td( html.Ul([ 
                                                    html.Li("クイーンサイズとシングルサイズのベッド"),
                                                    html.Li("ホットシャワー"),
                                                    html.Li("水洗トイレ"),
                                                    html.Li("プライベートテラス"), 
                                                    html.Li("エアコンあり。"), 
                                                ]))
                                            ]
                                        ),
                                        html.Tr([html.Td("包括的"), 
                                            html.Td("ブランケット、シーツ、枕、バスタオル")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックイン"), 
                                            html.Td("13:00～")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックアウト"), 
                                            html.Td("～12:00")
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),  
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)
 

  
economy = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [ 
                        dbc.Table(
                            [  
                                html.Tbody(
                                    [
                                        html.Tr([
                                            html.Td("エコノミー"),  
                                            html.Td( html.Ul([ 
                                                    html.Li("クイーンサイズとシングルサイズのベッド"),
                                                    html.Li("ホットシャワー"),
                                                    html.Li("水洗トイレ"),
                                                    html.Li("プライベートテラス"), 
                                                    html.Li("ファンルーム"), 
                                                ]))
                                            ]
                                        ),
                                        html.Tr([html.Td("包括的"), 
                                            html.Td("ブランケット、シーツ、枕、バスタオル")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックイン"), 
                                            html.Td("13:00～")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックアウト"), 
                                            html.Td("～12:00")
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),  
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)


groupics = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/rooms/room10.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.CardImg(src="/assets/pictures/rooms/room21.jpg", style={"maxHeight": "180px", "objectFit": "cover"}), 
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)  

group = html.Div(
    [ 
        dbc.Row(
            [ 
                dbc.Col(
                    [ 
                        dbc.Table(
                            [  
                                html.Tbody(
                                    [
                                        html.Tr([
                                            html.Td("広い部屋"),  
                                            html.Td( html.Ul([ 
                                                    html.Li("クィーンサイズ x 1 + シングルサイズ x 1、ホットシャワー"),
                                                    html.Li("水洗トイレ"),
                                                    html.Li("プライベートテラス"),
                                                    html.Li("ロフトルーム"),   
                                                    html.Li("8人用"),  
                                                    html.Li("ルーム 10, 11, 23 はエアコン付きと扇風機。"), 
                                                ]))
                                            ]
                                        ),
                                        html.Tr([html.Td("包括的"), 
                                            html.Td("ブランケット、シーツ、枕、バスタオル")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックイン"), 
                                            html.Td("13:00～")
                                            ]
                                        ),
                                        html.Tr([html.Td("チェックアウト"), 
                                            html.Td("～12:00")
                                            ]
                                        ),
                                    ]
                                ),
                            ],
                            bordered=True,
                            hover=True,
                            responsive=True,
                            striped=True,
                        ),
                    ],
                    xs=12, sm=12, md=8, lg=5,
                ),  
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
    ]
)


layout = html.Div(
    [
        roombackground,
        html.Br(),
        html.Div(
                dbc.Button("View Map", color="primary"),
                style={'display': 'flex', 'justify-content': 'center'}  # Center the button
            ),
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        standard,
                        html.Br(),
                        standardpics,
                        html.Br(),
                        economy,
                        html.Br(),
                        groupics,
                        html.Br(),
                        group,
                        
                         
                    ],  
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)