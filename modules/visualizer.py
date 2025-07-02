import plotly.graph_objects as go 

def plot_price(df,ticker):
    fig = go.Figure() #create a figure object
    
    fig.add_trace(go.Candlestick(
        x=df['Datetime'],  # use the datetime column for the x axis
        open=df['Open'],  # use the open price for the open of the candlestick
        high=df['High'],  # use the high price for the high of the candlestick
        low=df['Low'],  # use the low price for the low of the candlestick
        close=df['Close'],  # use the close price for the close of the candlestick
        name='Price Data'  # this will set the name of the trace to Price Data 
    ))

    fig.update_layout(
        title=f'{ticker} Price Chart',  # this will set the title of the chart to the ticker symbol 
        xaxis_title='Datetime',  # this will set the x axis title to Datetime
        yaxis_title='Price (USD)',  # this will set the y axis title to Price (USD)
        xaxis_rangeslider_visible=False,  # this will hide the range slider at the bottom of the chart
        xaxis=dict(tickangle=45), # this will rotate the x axis labels by 45 degrees for better readability 
        template='plotly_dark',  # this will set the chart to use the dark theme
        height=450, # this will set the height of the chart to 450 pixels
        margin=dict(l=40, r=20, t=40, b=40)  # this will set the margins of the chart to left=40, right=20, top=40, bottom=40
    )

    return fig  # return the figure object to be displayed in the Streamlit app 


def plot_volume(df,ticker):
    fig = go.Figure()  # create a figure object
    fig.add_trace(go.Bar(
        x=df['Datetime'],  # use the datetime column for the x axis
        y=df['Volume'],  # use the volume column for the y axis
        name='Volume',  # this will set the name of the trace to Volume
        marker=dict(color='orange')
    ))

    fig.update_layout(
        title=f"{ticker} Volume Chart",  # this will set the title of the chart to the ticker symbol
        xaxis_title='Time',  # this will set the x axis title to Datetime\
        yaxis_title='Volume',  # this will set the y axis title to Volume
        xaxis=dict(tickangle=45),  # this will rotate the x axis labels by 45 degrees for better readability
        template='plotly_dark',  # this will set the chart to use the dark theme
        height=300,  # this will set the height of the chart to 450 pixels
        margin=dict(l=40, r=20, t=40, b=40)  # this will set the margins of the chart to left=40, right=20, top=40, bottom=40 
    )

    return fig  # return the figure object to be displayed in the Streamlit app