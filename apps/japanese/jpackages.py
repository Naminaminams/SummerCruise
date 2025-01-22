import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  



packbackground = html.Div(
    [
        dbc.Carousel(
            items=[
                {
                    "key": "1",
                    "src": "/assets/backgrounds/resortbg4.jpg",
                    "img_style": {"height": "500px", "object-fit": "cover"}  # Set height and scale images
                }, 
            ],
            style={"max-height": "500px"}  # Limit the height of the carousel
        ),
        dbc.Card(
            [ 
                dbc.CardBody(
                    [
                        html.H2(html.B("料金"), className="card-title", style={'textAlign': 'center', 'fontFamily': "'Lobster'"}),
                        html.P(
                            [
                                "活動。ご宿泊。お食事。", 
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



package1 = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("ダイビング料金（表示はペソ）")),
                    ], 
                    xs=12, sm=12, md=5, lg=2,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [ 
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("エントリーフィー"), html.Td("P 350"), 
                                                 html.Td(html.Ul([ 
                                                    html.Li("飲料水・コーヒーは無料"), 
                                                    html.Li("ホットシャワー・タオルの使用"), 
                                                    html.Li("ご宿泊のお客様はエントリー費無料"), 
                                                    html.Li("７歳以下は半額、３歳以下は無料"),  
                                                    ]),  
                                                )
                                            ]
                                        ),
                                        html.Tr([html.Td("シュノーケルレンタル"), html.Td("P 350"), 
                                                 html.Td(html.Ul([ 
                                                    html.Li("３時間の料金"), 
                                                    html.Li("マスク・シュノーケル・ブーツ・フィン"),  
                                                    ]),  
                                                )
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
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)
 



package2 = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("ダイビング")),
                    ], 
                    xs=12, sm=12, md=5, lg=2,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [ 
                                html.Tbody(
                                    [
                                        html.Tr([html.Td([
                                                    html.P("体験ダイビング（ビーチ）"), 
                                                    html.P("体験ダイビング（ボート）"), 
                                                ]), 
                                                html.Td([
                                                    html.P("P 1,800"), 
                                                    html.P("P 2,800"),  
                                                    ]), 
                                                html.Td([ 
                                                    html.P("ダイビング経験不要、何方でも参加可能"), 
                                                    html.P("器材レンタル込み、マンツーマン対応"),  
                                                    ]),  
                                            ]
                                        ),
                                        html.Tr([html.Td([ 
                                                    html.P("ファンダイブ"), 
                                                    html.P("ビーチエントリー"),   
                                                    ]),  
                                                html.Td([ 
                                                    html.P("P 800"),  
                                                    ]),  
                                                html.Td([ 
                                                    html.P("タンク、ガイドダイバー込み"), 
                                                    html.P("器材レンタルは別途費用"),  
                                                    ]),   
                                            ]
                                        ),
                                        html.Tr([html.Td([ 
                                                    html.P("ファンダイブ/本"), 
                                                    html.P("サンルイス地区"),   
                                                    ]),  
                                                html.Td([ 
                                                    html.P("P 1,200"),  
                                                    ]),  
                                                html.Td([ 
                                                    html.P("タンク、ガイド、ボート費用込み"), 
                                                    html.P("器材レンタルは別途費用"),  
                                                    html.P("入海料250ペソ/日/人が別途必要"),  
                                                    ]),  
                                            ]
                                        ),
                                        html.Tr([html.Td([ 
                                                    html.P("器材レンタル/日"),  
                                                    ]),  
                                                html.Td([ 
                                                    html.P("P 1,000"),  
                                                    ]), 
                                                html.Td([ 
                                                    html.P("ダイビング器材フルセット１日の費用"),  
                                                    ]),  
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
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)
 
 

package3 = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("PADI認定コース")),
                        html.P("（マニュアル・Ｃカード申請費含む）　参加資格（12歳以上）")
                    ], 
                    xs=12, sm=12, md=5, lg=2,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [ 
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("スクーバダイバー"), html.Td("P12,800"), 
                                                 html.Td("１日、器材レンタル含む" )
                                            ]
                                        ),
                                        html.Tr([html.Td("オープンウォータ"), html.Td("P16,800"), 
                                                 html.Td("２日、器材レンタル含む" )
                                            ]
                                        ),
                                        html.Tr([html.Td("アドバンス"), html.Td("P16,800"), 
                                                 html.Td("２日、器材レンタル含む" )
                                            ]
                                        ),
                                        html.Tr([html.Td("レスキュー"), html.Td("P22,800"), 
                                                 html.Td("３日、EFR＆器材レンタル含む" )
                                            ]
                                        ),

                                        html.Tr([html.Td("ダイブマスター"), html.Td("P40,000"), 
                                                 html.Td([ 
                                                    html.P("最短７ 日間、器材レンタル＆教材費含む"), 
                                                    html.P("週末ベースでの講習も可能"), 
                                                    html.P("*年間メンバーシップ費用 (約$120/year)"), 
                                                    ]),  
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
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)
 
 

accomodations = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("ご宿泊")),
                    ], 
                    xs=12, sm=12, md=5, lg=2,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [ 
                                html.Thead(
                                    html.Tr(
                                        [
                                            html.Th(""),
                                            html.Th(" 料金（２名様）"),
                                            html.Th(" 追加マットレス"),
                                            html.Th(" シャワー＆トイレ"),
                                            html.Th(" エアコン"),
                                        ]
                                    )
                                ),
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("デラックス"), html.Td("P3,500"), 
                                                 html.Td("P500/人" ), html.Td("YES" ), html.Td("YES" )
                                            ]
                                        ),
                                        html.Tr([html.Td(" スタンダードA"), html.Td("P3,200"), 
                                                 html.Td("P500/人" ), html.Td("YES" ), html.Td("YES" )
                                            ]
                                        ),
                                        html.Tr([html.Td("スタンダードB"), html.Td("P2,500"), 
                                                 html.Td("P500/人" ), html.Td("共同（外）" ), html.Td("ファンのみ" )
                                            ]
                                        ),
                                        html.Tr([html.Td("エコノミー"), html.Td("P2,500"), 
                                                 html.Td("P500/人" ), html.Td("共同（外）" ), html.Td("YES" )
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
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)
 
 

meals = html.Div(
    [  
        dbc.Row(
            [ 
                dbc.Col(
                    [
                        html.H5(html.B("お食事")),
                    ], 
                    xs=12, sm=12, md=5, lg=2,
                ),
                dbc.Col(
                    [ 
                        dbc.Table(
                            [  
                                html.Tbody(
                                    [
                                        html.Tr([html.Td("朝食"), html.Td(""), 
                                                 html.Td("アラカルト" )
                                            ]
                                        ),
                                        html.Tr([html.Td("昼食"), html.Td(""), 
                                                 html.Td("アラカルト" )
                                            ]
                                        ),
                                        html.Tr([html.Td("夕食"), html.Td(""), 
                                                 html.Td("アラカルト" )
                                            ]
                                        ),
                                        html.Tr([html.Td("BBQ(スタンダード)/名 	"), html.Td("P500"), 
                                                 html.Td("BBQ（ポーク、チキン、野菜、肉類）ライス" )
                                            ]
                                        ),
                                        html.Tr([html.Td("BBQ テーブルレンタル"), html.Td("P500"), 
                                                 html.Td("BBQ テーブル・炭・皿類込み" )
                                            ]
                                        ),
                                        html.Tr([html.Td("瓶ビール"), html.Td("P80"), 
                                                 html.Td("")
                                            ]
                                        ),
                                        html.Tr([html.Td("ソフトドリンク"), html.Td("P50"), 
                                                 html.Td("")
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
            justify='center', 
            align='center',
            className="p-3"  
        ),
    ],
)

layout = html.Div(
    [  
        packbackground,
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    [
                        package1, 
                        package2,
                        package3,
                        html.H4("■上記講習費には、宿泊＆食事は含まれていません。",
                            className="text-center my-3"),
                        html.Hr(),
                        accomodations,
                        meals
                        
                    ],   
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)