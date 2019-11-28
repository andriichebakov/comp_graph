import plotly as pl
import plotly.graph_objects as go
import math as m

def y(x):
    return m.cos(x)

def graph():
    x= -5
    for i in range(1000):
        yield (x+0.01*i, y(x + 0.01 * i))

with open("data.txt", mode="w") as f:
    f.write('\n'.join(';'.join(str(j) for j in i) for i in graph()))

trace = go.Scatter(x = list(i[0] for i in graph()),
                   y = list(i[1] for i in graph())
                   )

fig = go.Figure(data=[trace])

fig.update_xaxes(title_text='X')
fig.update_yaxes(title_text='Y')

pl.offline.plot(fig,filename='graphic.html',)