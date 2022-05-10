import plotly.express as px
import plotly.io as pio
import pandas as pd
pio.renderers.default = "browser"

df = pd.read_csv("interview0/interview0_current.csv")
lst0 = list(df.iloc[0])
lst0.pop(0)
print(lst0)

lst1 = list(df.iloc[1])
lst1.pop(0)
print(lst1)


# initial lists for heatmap
ll = []
lm = []
lh = []
ml = []
mm = []
mh = []
hl = []
hm = []
hh = []
# end of initial lists

input = "input"
for i in range(len(lst0)):
    if lst0[i] == "l" and lst1[i] == "l":
        ll.append(input)
    elif lst0[i] == "l" and lst1[i] == "m":
        lm.append(input)
    elif lst0[i] == "l" and lst1[i] == "h":
        lh.append(input)
    elif lst0[i] == "m" and lst1[i] == "l":
        ml.append(input)
    elif lst0[i] == "m" and lst1[i] == "m":
        mm.append(input)
    elif lst0[i] == "m" and lst1[i] == "h":
        mh.append(input)
    elif lst0[i] == "h" and lst1[i] == "l":
        hl.append(input)
    elif lst0[i] == "h" and lst1[i] == "m":
        hm.append(input)
    elif lst0[i] == "h" and lst1[i] == "h":
        hh.append(input)
    else:
        print("wrong input")

data=[[len(hl), len(hm), len(hh)],
      [len(ml), len(mm), len(mh)],
      [len(ll), len(lm), len(lh)]]

fig = px.imshow(data,
                labels=dict(x="Value for the producer", y="Value for the customer", color="Occurrence"),
                x=['low', 'medium', 'high'],
                y=['low', 'medium', 'high']
               )
fig.update_xaxes(side="bottom")
# fig.show()
fig.write_html(f"test_heatmap.html")
