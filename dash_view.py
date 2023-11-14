# -*- coding: utf-8 -*-
"""
Created on Tue oct 24 22:19:19 2023

@author: Inbatamilan Balasubramanian
"""
import dash
import dash_html_components as html
from dash import dcc as dcc
import dash_bootstrap_components as dbc
import webbrowser
import pandas as pd
import pickle
from dash.dependencies import Input, Output, State

#declaring global variables
project_name=None
app=dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


#defining my fuction

def load_scrappedReviews():
    global scrappedReviews
    scrappedReviews = pd.read_csv('scrappedReviews.csv')
    scrappedReviews=scrappedReviews.iloc[:,1].tolist()


def check_review(reviewText):
    file=open("F:/Forsk/model_dumping.pkl","rb") 
    model_from_pickel=pickle.load(file)
    feature=pickle.load(open("F:/Forsk/model_features.pkl","rb"))
    
    from sklearn.feature_extraction.text import TfidfVectorizer

    vect = TfidfVectorizer(decode_error ='replace',vocabulary=feature).fit([reviewText])
    
    return model_from_pickel.predict(vect.transform([reviewText]))


def UI_main():
    
    main_ui=dbc.Container(html.Div(
        [
        
        dbc.Alert(children="Sentimental Analysis Checker",id="Main_head",color="success",style={'fontSize': '24px'}),
        
        dbc.Textarea(
            id='textarea',
            placeholder='Enter text here...',
            value='',  # You can set an initial value if needed
            style={'width': '100%','background-color':'white', 'height': 200,'fontSize': '24px'},
            ),
        
        dbc.Button("Check Review", id="button", color = 'secondary', className="mt-3",
                   style={'width':'100%','fontSize': '24px'}),
        
        dbc.Button(children="Negative", id='result', color = 'light', className="mt-3",disabled=True,
                   style={'width':'100%','fontSize': '20px'}),
        
        ],
        className="p-5",style={'marginTop': '20px'}
    ))
    return main_ui

def auto_openbrowser():
    webbrowser.open_new("http://127.0.0.1:8050/")
    
    
@app.callback(
    Output( 'result', 'children' ),
    Output('result','color'),
    Output('result','disabled'),
    [
    Input( 'button','n_clicks'),
    State('textarea','value')
    ]
    )
def review_update(n_clicks,values):
    
    print("Data Type = ", type(n_clicks))
    print("Value = ", str(n_clicks))
    
    print("Data Type = ", str(type(values)))
    print("Value = ", str(values))
    
    if n_clicks is not None and n_clicks > 0:
        print(values)
        response = check_review(values)
        print(response)
        if (response[0] == 0):
            return 'Negative','danger',False
        elif (response[0] == 1 ):
            return'Positive','success',False
        else:
            return 'Unknown','dark',False   
    else:
        return ""

 
#main fuction to control flow

def main():
    print("Start of project")
    load_scrappedReviews()
    
    
    global project_name,review,app
    
    project_name="Sentimental Analysis"
    app.title=project_name
    app.layout=UI_main()
    app.run_server()
    auto_openbrowser()
    print("End of project")
    
    project_name=None
    review=None
    app=None
    scrappedReviews=None
    
#calling the main function
if __name__=='__main__':
    main()

#I ordered a pair of earrings and was pleasantly surprised. The delivery was quick, and the earrings are even more gorgeous in person. I'm in love with them!

#This necklace is a total letdown. The chain feels cheap, and the pendant tarnished within a week. Not worth the price.

#I was pretty amazed by the store when I walked in. The variety of top designers was an additional plus. I found a nice diamond necklace for my wife that she wears all the time. I suggest that you check this place out before making a purchase.

#The packaging was damaged when I received my order, and the earrings inside were scratched. Very disappointed with the condition they arrived in.

#The necklace I got as a gift is just okay. It's not as impressive as I'd hoped, but it's the thought that counts, I guess.

#The customer service was fantastic! They helped me find the perfect engagement ring, and it's absolutely stunning. My fiancee is over the moon!


















