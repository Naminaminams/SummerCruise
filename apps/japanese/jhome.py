import hashlib

import dash
from dash import callback_context, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app
from apps import dbconnect as db
from apps import commonmodules as cm
  



homepagebackground = dbc.Carousel(
    items=[
        {
            "key": "1",
            "src": "/assets/backgrounds/resortbg.jpg",
            "header": "ようこそ", 
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
        {
            "key": "2",
            "src": "/assets/backgrounds/resortbg2.jpg",
            "header": "Summer Cruise Diving Resort",
            "caption": "旅先でのあなたの家",
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
        {
            "key": "3",
            "src": "/assets/backgrounds/resortbg3.jpg", 
            "img_style": {"height": "500px", "object-fit": "cover"}  # Set max height and scale images
        },
    ],
    style={"max-height": "500px"}  # Ensure carousel doesn't exceed the height
)



images = [
    "/assets/pictures/diningarea.jpg",
    "/assets/pictures/pool.jpg",
    "/assets/pictures/functionarea.jpg",
    "/assets/pictures/booths.jpg",
    "/assets/pictures/relax.jpg",
    "/assets/pictures/kitchen.jpg" 
]


def content(image_url, header_text, description_text):
    return dbc.Card(
        [
            dbc.CardImg(src=image_url, style={"maxHeight": "180px", "objectFit": "cover"}),
            dbc.CardHeader(
                html.H5(header_text, className="card-title fw-bold")
            ),
            dbc.CardBody(
                html.P(description_text, className="card-text")
            ),
        ],
        style={
            "maxWidth": "18rem", 
            "margin": "auto", 
            "overflow": "hidden"  # Hide overflow content
        }
    )


ammenities_cards = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        content(images[0], "ダイニングエリア", "屋外ダイニングを楽しむ事ができ、屋外ラウン。"),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[1], "天然塩水プール", "(4.5m~)."),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[2], "ファンクションエリア", "様々な レッスンに使える広々とした空間。"),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        content(images[3], "個別のブース", "プライベート空間くつろげる。"),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[4], "リラックスできるスペース", "多くのオープンスペースがあり、景色、海風、日差しを楽しむことができます。"),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
                dbc.Col(
                    dbc.Card(
                        content(images[5], "BBQ", "刺身とバーベキューをお楽しみください"),
                        style={"width": "18rem", "margin": "auto"}
                    ),
                    width="auto",  # Adjust column width to fit content
                    style={"padding": "0.5rem"},  # Reduce padding between columns
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ), 
    ]
)







 



def review(image_url, header_text, description_text, small_text):
    return dbc.Card(
        dbc.Row(
            [
                dbc.Col(
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    dbc.CardImg(src=image_url, className="img-fluid", 
                                                style={"maxWidth": "100px", "borderRadius": "50%"}),
                                    html.Small(small_text, className="card-text text-muted text-center"),
                                ],
                                className="d-flex flex-column align-items-center"  # Center image and small text
                            ),
                            html.Br(),
                            html.H5(header_text, className="card-title text-center"),  # Center header
                            html.P(description_text, className="card-text text-center"),  # Center description
                        ]
                    ),
                    className="col-md-12",
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
        className="mb-3",
        style={"maxWidth": "540px"},
    )





review_cards = html.Div(
    [
        dbc.Row(
            [
                
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review2.jpg", 
                        "Staff are all friendly and approachable.", 
                        """
                            First time here and we really enjoyed the activities and accommodation. Staff are all friendly and approachable.
                            We came here for the intro class, and lahat ng coaches ay mababait. They welcome questions 
                            and we learned a lot from them. Even yung coaches na hindi assigned sa inyo, mabait rin and willing to help you.
                        """, 
                        "Joshua Forcadela"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review1.jpg", 
                        "Our experience at Summer Cruise was truly sulit and unforgettable. We almost did not want to leave! Nakakabitin!", 
                        """
                            Summer Cruise Diving Resort is one of the must-visit destinations in San Luis, Batangas. 
                            There are multiple ways to get there and for us commuters, it's via bus and tricycle. 
                            Just make sure to arrive at Summer Cruise's parking area before 4 pm to catch the boat to the resort itself...
                        """, 
                        "Nazka Leosala"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
                dbc.Col(
                    review(
                        "/assets/pictures/aboutus/review3.jpg", 
                        "Perfect for people on a budget", 
                        """
                            We came here on September 23-24, 2023, and it's a nice low-cost place for people who want
                            to start learning how to dive. It's perfect for people on a budget because they have 
                            packages combining accommodation and freediving intro classes. Their intro classes go as deep as 10 meters only...
                        """, 
                        "Dennise Recuerdo"
                    ),
                    xs=10, sm=10, md=3, lg=3,
                ),
            ],
            className="mb-4 d-flex justify-content-center",  # Center content horizontally
        ),
    ]
)


 

 


banner = dbc.Card(
    [
        dbc.CardImg(
            src="/assets/backgrounds/resortbgwide.jpg",
            top=True,
            style={"opacity": 0.7,"height": "350px", "object-fit": "cover"},
        ),
        dbc.CardImgOverlay(
            dbc.CardBody(
                [
                    html.Div(
                        [
                            html.H4(
                                html.B("すぐにお会いしましょう！"), 
                                className="card-title text-center"
                            ),
                            dbc.Row(
                                dbc.Col(
                                    [
                                        dbc.Button(html.B("料金"), color="primary", href="/ja/packages", className="me-2"),  # Add spacing between buttons
                                        dbc.Button(html.B("ご予約お問い合わせ"), color="primary", href="https://www.facebook.com/summercruiseresort"),
                                    ],
                                    style={'display': 'flex', 'justify-content': 'center'}  # Center the buttons
                                )
                            ),
                        ],
                        className="d-flex flex-column justify-content-center align-items-center h-100",  # Center content
                        style={"height": "100%"}  # Make div take full height of card
                    )

                ],
                className="h-100 d-flex flex-column justify-content-center align-items-center",  # Ensure card body takes full height of card and centers content
            ),
        ),
    ],
    style={ "max-height": "350px"},
)



 







 






introinfo2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4(html.B("10サービスの年"), className="text-center"), 
                            html.Br(),
                            html.P(
                            """
                                シュノーケリング、フリーダイビング、​​スキューバダイビング、​​釣りなど。
                                """, className="text-center",
                                style={
                                    "font-size": "16px",   
                                }
                            ), 
                            html.Br(),
                            html.P(
                            """ 
                                カップル、家族、友人グループ、企業チーム、ペット連れの旅行など、
                                サマー クルーズはリラックスや冒険に最適な場所です。
                                """, className="text-center",
                                style={
                                    "font-size": "16px",  
                                }
                            ), 
                        ],
                        className="d-flex flex-column text-center"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center text-center"
                ),
                dbc.Col(
                    html.Img(   
                        src="/assets/pictures/homepage/intro.png",  
                        style={"width": "80%", "height": "auto", "border-radius": "10px"},  
                        alt="Underwater Adventure"   
                    ),
                    width={"size": 12}, 
                    xs=12, sm=12, md=4, lg=4,  
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  
            align='center',
            className="p-3"   

        ),
    ]
)

introinfo1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        
                        html.Br(),
                        html.H2("Summer Cruise Diving Resort", className="text-center"), 
                        html.Br(),
                        html.P("アクティビティー " , className="text-center", style={"font-size": "16px"}),
                        html.P("◆ダイビング講習PADIオープンウォーターからダイブマスターコース◆ファンダイブ（ビーチ＆ボート）◆体験ダイブ" , className="text-center", style={"font-size": "16px"}),
                        html.P("◆スノーケリング◆海水浴◆プール◆BBQ（BBQテーブルレンタル可能）◆食材、飲むものの持込は自由です。" , className="text-center", style={"font-size": "16px"}),
                        html.P("◆ダイビング器材、スノーケリングセット、ライフジャケットレンタル可能。" , className="text-center", style={"font-size": "16px"}),
                        html.P("◆クレジットカード、デビットカード、Gcashご利用可能。" , className="text-center", style={"font-size": "16px"}),
                        
                        html.Br(),
                        html.Br(),
  
                    ], 
                    xs=12, sm=12, md=6, lg=5,
                    className="px-4",
                ), 
            ],
            justify='center',    
            align='center',   
        )
    ]
)




layout = html.Div(
    [
        homepagebackground, 
        html.Br(), 
 
        html.Br(),
        introinfo1,
        introinfo2,

        html.Br(),
        html.Br(),
        ammenities_cards, 
        html.Br(),  

         
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("PADIオープンウォーターコース案内"),
                            html.P("""
                                ２日間（１泊２日、もしくは日帰りｘ２回）、 １時間程度の座学授業を5レッスン
                                限定水域練習（浅場）ｘ５ダイブ（30分～40分/ダイブ）
                                海洋実習ｘ４ダイブ。（30分～40分/ダイブ）
                                日本人インストラクターがレッスンを行います。
                                各個人の体力に応じ楽しみながらスキルと知識を吸収します。
                                水中スキルレッスンは、安全確実なマンツーマン体制で行います。
                                スケジュールの流れ"""),
                            dbc.Button("講習風景動画", color="light", href="https://www.youtube.com/watch?v=033G2aiHIrU", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0" 
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/pictures/homepage/B1.png"},
                            {"key": "2", "src": "/assets/pictures/homepage/B2.png"},
                            {"key": "3", "src": "/assets/pictures/homepage/B3.png"},
                            {"key": "4", "src": "/assets/pictures/homepage/C1.png"},
                            {"key": "5", "src": "/assets/pictures/homepage/C2.png"},
                            {"key": "6", "src": "/assets/pictures/homepage/C3.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ), 
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("講習アドバンスコース"),
                            html.P("""２日間（１泊２日、もしくは日帰りｘ２回）
                                １時間程度の座学授業を5レッスン
                                海洋実習ｘ５ダイブ（30分～40分/1ダイブ）
                                １）中世浮力
                                ２）水中ナビゲーション
                                ３）ナイトダイビング
                                ４）ディープダイビング
                                ５）ドリフトダイビングor水中カメラ
                                試験は無く楽しみながら幅広く「知識と経験」を増すコースです。料金 
                                """),
                            dbc.Button("もっと学ぶ", color="light", href="/ja/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/pictures/homepage/D1.png"},
                            {"key": "2", "src": "/assets/pictures/homepage/D2.png"},
                            {"key": "3", "src": "/assets/pictures/homepage/D3.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("講習レスキューコース（２泊３日、もしくは３日間）"),
                            html.P("""
                                ３日間（２泊３日or飛び飛びも可能）
                                より安全なダイビングを目指すダイバー必須のコース
                                トラブルを予測する能力と解決、その知識とスキルを習得。
                                予測する能力により準備が可能となり、万が一の場合の対応に繋がります。
                                これが、トラブルを未然に防ぐ思考となり、セルフレスキューの重要なキーです。
                                ＥＦＲでは、万一に備えての心肺蘇生法、出血や骨折への対応を学習します。"""),
                            dbc.Button("もっと学ぶ", color="light", href="/ja/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/pictures/homepage/E1.png"}, 
                            {"key": "2", "src": "/assets/pictures/homepage/E2.png"},  
                            {"key": "3", "src": "/assets/pictures/homepage/E3.png"}, 
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("講習ダイブマスターコース"),
                            html.P("""（開始時に４０本、申請時に６０本ログ必要）
                                   短期７日間とインターンシップの２種類から選べます。
                                    ダイビングをトータルで、オーガナイズする知識、スキルを学習します。
                                    クラブやチームのリーダーとして、又将来インストラクターを目指す為のコースです。
                                    インターンシップご希望の場合は、スタートするレベル（ゼロからのスタートも可能）
                                    ご不明点は担当（高柿）までご連絡ください。"""),
                            dbc.Button("もっと学ぶ", color="light", href="/ja/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/pictures/homepage/F1.png"}, 
                            {"key": "2", "src": "/assets/pictures/homepage/F2.png"},
                            {"key": "3", "src": "/assets/pictures/homepage/F3.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(), 
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        [
                            html.H4("ファンダイビング "),
                            html.P("""
                                認定ダイバー対象としたダイビングポイントをご案内いたします。
                                ◆サンルイスエリア（スポット１０ヶ所）
                                お客様のご要望により、ダイビングポイントを調整することが可能です。
                                メール頂けましたら、ポイントＭＡＰお送りいたします。
                                """), 
                            dbc.Button("もっと学ぶ", color="light", href="/ja/activities", 
                                style={
                                    "border": "1px solid black", 
                                    "border-radius": "10px",      
                                    "color": "black", 
                                    "font-size": "14px",      
                                    "width": "120px",
                                    "margin": "20px 0"  
                                }
                            ), 
                        ],
                        className="d-flex flex-column align-items-left"   
                    ),
                    width={"size": 12},
                    xs=12, sm=12, md=8, lg=4,
                    className="d-flex justify-content-center align-items-center"
                ),
                dbc.Col(
                    dbc.Carousel(
                        items=[
                            {"key": "1", "src": "/assets/pictures/homepage/G1.png"},
                            {"key": "2", "src": "/assets/pictures/homepage/G2.png"},
                            {"key": "3", "src": "/assets/pictures/homepage/G3.png"},
                        ],
                        className="carousel-fade custom-carousel",
                        style={"Height": "350px", "overflow": "hidden"}  
                    ),
                    width={"size": 12, "offset": 0}, # Default size for xs
                    xs=12, sm=12, md=8, lg=4,  # Responsive sizes
                    className="d-flex justify-content-center align-items-center"
                ),
            ],
            justify='center',  # Center align the columns in the row
            align='center',
            className="p-3"  # Small padding around the row
        ),
        html.Br(),  
         

        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Br(), 
                                html.H2("ゲストのレビュー", className="text-center"),  
                            ]
                        ),
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                review_cards,  
                            ],  
                        )
                    ], className="justify-content-center align-items-center",
                ),
                dbc.Row(
                    [
                        dbc.Button("証言を参照してください。🠮", color="primary", href="https://www.google.com/search?client=firefox-b-d&q=summer+cruise#lrd=0x33bd0824daf79bfb:0x308106deae431340,1,,,,", style={"width": "auto"}),
                    ], className="d-flex justify-content-center"
                )
            ]
        ),
        html.Br(),
        html.Br(),  
        banner
    ]
)