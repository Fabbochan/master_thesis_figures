import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import os
import plotly.io as pio
pio.renderers.default = "browser"

num_of_interviews = [0, 1, 2, 3]

y_list = 3
x_list = 6

current = False
trend = False

# example: communication = 0
specific_aspect = 1

# categories set for the radar plots
categories = ["Value for the customer",
              "Value for the producer",
              "Risks for the customer",
              "Risks for the producer",
              "Cost of development",
              "Cost of implementation",
              "Return of investment",
              "Market establishment"
              ]

# aspect names
aspects = ["Communication",
           "Data handling",
           "Data driven problem solving",
           "Situational context awareness",
           "Adaption to different contexts",
           "Remote Operation",
           "Recommendation and decision support",
           "Self-organization and control",
           "Predictive acting",
           "Continuous improvement",
           "Task automation"]


def add_figure_to_plot(values, _categories, name):
    """
    This function adds another trace to a plotly figure.
    You need to provide values, categories and a plot name.
    """
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=_categories,
        fill=None,
        name=name
    ))


if __name__ == "__main__":
    # df gets loaded from csv
    df = pd.read_csv("interview0/interview0_current.csv")

    # 0 = "Value for the customer"
    # 1 = "Value for the producer"
    # 2 = "Risks for the customer"
    # 3 = "Risks for the producer"
    # 4 = "Cost of development"
    # 5 = "Cost of implementation"
    # 6 = "Return of investment"
    # 7 = "Market establishment"
    # first criterion row gets selected.
    lst0 = list(df.iloc[y_list])
    lst0.pop(0)
    # print(lst0)

    # second criterion row gets selected.
    lst1 = list(df.iloc[x_list])
    lst1.pop(0)
    # print(lst1)

    # initial lists for the heatmap
    # hl / hm / hh
    # ml / mm / mh
    # ll / lm / lh
    ll = []
    lm = []
    lh = []
    ml = []
    mm = []
    mh = []
    hl = []
    hm = []
    hh = []

    # first and second list get sorted into the initial lists for the heatmap
    for i in range(len(lst0)):
        value = "input"
        if lst0[i] == "l" and lst1[i] == "l":
            ll.append(value)
        elif lst0[i] == "l" and lst1[i] == "m":
            lm.append(value)
        elif lst0[i] == "l" and lst1[i] == "h":
            lh.append(value)
        elif lst0[i] == "m" and lst1[i] == "l":
            ml.append(value)
        elif lst0[i] == "m" and lst1[i] == "m":
            mm.append(value)
        elif lst0[i] == "m" and lst1[i] == "h":
            mh.append(value)
        elif lst0[i] == "h" and lst1[i] == "l":
            hl.append(value)
        elif lst0[i] == "h" and lst1[i] == "m":
            hm.append(value)
        elif lst0[i] == "h" and lst1[i] == "h":
            hh.append(value)
        else:
            print(f"Cannot sort value {lst0[i], lst1[i]}, wrong input")

    # data list gets created
    data = [[len(hl), len(hm), len(hh)],
            [len(ml), len(mm), len(mh)],
            [len(ll), len(lm), len(lh)]]

    # figure gets created
    fig = px.imshow(data,
                    labels=dict(x=categories[x_list], y=categories[y_list], color="Occurrence"),
                    x=['low', 'medium', 'high'],
                    y=['high', 'medium', 'low']
                    )
    fig.update_xaxes(side="bottom")
    # fig.show()
    fig.write_html(f"test_heatmap.html")

    # # new figure class gets created
    # fig = make_subplots()
    #
    # interview_count = 0
    #
    # if current:
    #     for i in current_data:
    #         add_figure_to_plot(i[specific_aspect], categories, f"Interview{interview_count}: Current")
    #         interview_count = interview_count + 1
    #
    # interview_count = 0
    # if trend:
    #     for i in trend_data:
    #         add_figure_to_plot(i[specific_aspect], categories, f"Interview{interview_count}: Trend")
    #         interview_count = interview_count + 1
    #
    # fig.update_traces(opacity=0.9)
    #
    # # Plot styling happens here
    # fig.update_layout(font_family="Arial", legend=dict(
    #     title=f"Aspect: {aspects[specific_aspect]}",
    #     font=dict(size=20),
    #     orientation="h",
    #     y=1.1,
    #     yanchor="bottom",
    #     x=0.5,
    #     xanchor="center"
    #     ),
    #     template='plotly',
    #     showlegend=True)
    #
    # fig.update_layout(
    #     polar=dict(
    #         radialaxis=dict(
    #             visible=True,
    #             range=[0, 3]
    #         )),
    # )
    #
    # fig.add_annotation(text='<b>Criterion rating information</b>:<br>high = value 3 <br>medium = value 2<br>low = value 1',
    #                    x=0.9,
    #                    y=0.8,
    #                    bordercolor='black',
    #                    borderwidth=1,
    #                    showarrow=False,
    #                    font=dict(size=15,
    #                              family="Arial"))
    #
    # # savings html in specific folders
    # if current:
    #     naming = "current.html"
    # if trend:
    #     naming = "trend.html"
    # if trend and current:
    #     naming = "both.html"
    # interview_interpretation = "multigraph_interpretation"
    # path = os.path.join(os.getcwd(), interview_interpretation)
    # if not os.path.isdir(path):
    #     os.mkdir(path)
    # try:
    #     filename = f"{aspects[specific_aspect] + '_' + str(num_of_interviews) + '_' + naming}"
    #     # fig.write_image(f"{path}/{filename}.png")
    #     fig.write_html(f"{path}/{filename}")
    # except:
    #     print(f"{naming} not defined")



