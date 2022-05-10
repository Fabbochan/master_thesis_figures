import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from plotly.subplots import make_subplots
import os
import plotly.io as pio

pio.renderers.default = "browser"

num_of_interviews = [0, 1, 2, 3]

current = True
trend = True

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

    current_data = []
    trend_data = []

    if current == False and trend == False:
        print("Nothing set to draw.")
        exit()

    for i in num_of_interviews:
        df_current_data = []
        df_trend_data = []

        interview = "interview" + str(i)

        # filepath to data gets generated here
        interview_current = interview + "_current.csv"
        interview_trend = interview + "_trend.csv"

        # dataframe gets loaded in and transformed from l, m, h to 1, 2, 3
        df_current = pd.read_csv(f"{interview}/{interview_current}")
        df_trend = pd.read_csv(f"{interview}/{interview_trend}")

        df_current_num = df_current.replace(["l", "m", "h"],
                                            ["1", "2", "3"])

        df_trend_num = df_trend.replace(["l", "m", "h"],
                                        ["1", "2", "3"])

        for col in df_current_num:
            if col == "Unnamed: 0":
                continue
            current_aspect = df_current_num[col].tolist()
            current_aspect_num = list(map(int, current_aspect))
            df_current_data.append(current_aspect_num)

        for col in df_trend_num:
            if col == "Unnamed: 0":
                continue
            trend_aspect = df_trend_num[col].tolist()
            trend_aspect_num = list(map(int, trend_aspect))
            df_trend_data.append(trend_aspect_num)

        current_data.append(df_current_data)
        trend_data.append(df_trend_data)

        # end of for loop

    # rows = 2, cols = 2
    # new figure class gets created
    fig = make_subplots()
    # layout2x2 = [[1, 1], [2, 1], [1, 2], [2, 2]]

    interview_count = 0

    if current:
        for i in current_data:
            add_figure_to_plot(i[specific_aspect], categories, f"Interview{interview_count}: Current")
            interview_count = interview_count + 1

    interview_count = 0
    if trend:
        for i in trend_data:
            add_figure_to_plot(i[specific_aspect], categories, f"Interview{interview_count}: Trend")
            interview_count = interview_count + 1

    fig.update_traces(opacity=0.9)

    # Plot styling happens here
    fig.update_layout(font_family="Arial", legend=dict(
        title=f"Aspect: {aspects[specific_aspect]}",
        font=dict(size=20),
        orientation="h",
        y=1.1,
        yanchor="bottom",
        x=0.5,
        xanchor="center"
        ),
        template='plotly',
        showlegend=True)

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3]
            )),
    )

    fig.add_annotation(text='<b>Criterion rating information</b>:<br>high = value 3 <br>medium = value 2<br>low = value 1',
                       x=0.9,
                       y=0.8,
                       bordercolor='black',
                       borderwidth=1,
                       showarrow=False,
                       font=dict(size=15,
                                 family="Arial"))

    # savings html in specific folders
    if current:
        naming = "current.html"
    if trend:
        naming = "trend.html"
    if trend and current:
        naming = "both.html"
    interview_interpretation = "multigraph_interpretation"
    path = os.path.join(os.getcwd(), interview_interpretation)
    if not os.path.isdir(path):
        os.mkdir(path)
    try:
        filename = f"{aspects[specific_aspect] + '_' + str(num_of_interviews) + '_' + naming}"
        # fig.write_image(f"{path}/{filename}.png")
        fig.write_html(f"{path}/{filename}")
    except:
        print(f"{naming} not defined")



