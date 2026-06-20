import plotly.express as px

def bar_chart(df, x, y, title=""):
    fig = px.bar(df, x=x, y=y, text=y, title=title)
    fig.update_layout(height=420, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=20,r=20,t=50,b=20))
    return fig
