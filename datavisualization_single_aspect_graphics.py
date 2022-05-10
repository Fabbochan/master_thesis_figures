import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os

# only type the interview name here
interview = "interview0"

# filepath gets generated here
interview_current = interview + "_current.csv"
interview_trend = interview + "_trend.csv"

# dataframe gets loaded in and transformed from l, m, h to 1, 2, 3
df_current = pd.read_csv(f"{interview}/{interview_current}")
df_trend = pd.read_csv(f"{interview}/{interview_trend}")

df_current_num = df_current.replace(["l", "m", "h"],
                                    ["1", "2", "3"])

df_trend_num = df_trend.replace(["l", "m", "h"],
                                ["1", "2", "3"])

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
        fill="toself",
        name=name
    ))


if __name__ == "__main__":

    current_data = []
    trend_data = []

    for col in df_current_num:
        if col == "Unnamed: 0":
            continue
        current_aspect = df_current_num[col].tolist()
        current_aspect_num = list(map(int, current_aspect))
        current_data.append(current_aspect_num)

    for col in df_trend_num:
        if col == "Unnamed: 0":
            continue
        trend_aspect = df_trend_num[col].tolist()
        trend_aspect_num = list(map(int, trend_aspect))
        trend_data.append(trend_aspect_num)

    for i in range(11):
        # new figure class gets created
        fig = go.Figure()

        add_figure_to_plot(current_data[i], categories, "Current")
        add_figure_to_plot(trend_data[i], categories, "Trend")

        # Plot styling happens here
        fig.update_layout(font_family="Arial",
                          legend=dict(
                              title=f"Aspect: {aspects[i]}",
                              orientation="h",
                              y=1.1,
                              yanchor="bottom",
                              x=0.5, xanchor="center"),
                          template='plotly', showlegend=True)
        fig.update_traces(opacity=0.9)

        fig.add_annotation(
            text='<b>Criterion rating information</b>:<br>high = value 3 <br>medium = value 2<br>low = value 1',
            x=1.1,
            y=-0.2,
            bordercolor='black',
            borderwidth=1,
            showarrow=False,
            font=dict(size=12,
                      family="Arial"))

        # if you want to add a title within the axis for the radius
        # fig.update_polars(radialaxis_title_text="low=1, medium=2, high=3", radialaxis_title_font_size=13)

        # savings pngs in specific folders
        interview_interpretation = interview + "_interpretation"
        path = os.path.join(os.getcwd(), interview_interpretation)
        if not os.path.isdir(path):
            os.mkdir(path)
        filename = f"{interview + '_' + str(i) + '_' + aspects[i]}"
        fig.write_image(f"{path}/{filename}.png")

