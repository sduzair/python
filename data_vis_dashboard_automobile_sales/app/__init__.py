import pandas as pd
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
import plotly.express as px

from config import Config


def create_app(data: pd.DataFrame):
    # Initialize the Dash app
    app = dash.Dash(name=__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

    # Set the title of the dashboard
    app.title = "Automobile Statistics Dashboard"

    app.server.config.from_object(Config)

    # Create the dropdown menu options
    dropdown_options = [
        {"label": "Yearly Statistics", "value": "Yearly Statistics"},
        {
            "label": "Recession Period Statistics",
            "value": "Recession Period Statistics",
        },
    ]

    # List of years
    year_list = [i for i in range(1980, 2024, 1)]

    # Create the layout of the app
    app.layout = dbc.Container(
        [
            # TASK 2.1 Add title to the dashboard
            dbc.Row(
                [
                    html.H1(
                        app.title, className="text-center"
                    ),  # May include style for title
                ]
            ),
            # TASK 2.2: Add two dropdown menus
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Label("Select Statistics:"),
                            dcc.Dropdown(
                                id="dropdown-statistics",
                                options=dropdown_options,
                                value="Select Statistics",
                                placeholder="Select a report type",
                                searchable=False,
                            ),
                        ],
                        width=9,
                    )
                ],
                justify="center",
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Label("Select Year:"),
                            html.Div(
                                dcc.Dropdown(
                                    id="select-year",
                                    options=[
                                        {"label": i, "value": i} for i in year_list
                                    ],
                                    placeholder="Select an year",
                                    searchable=False,
                                )
                            ),
                        ],
                        width=9,
                    )
                ],
                justify="center",
            ),
            # TASK 2.3: Add a division for output display
            dbc.Container(id="output-container", className="chart-grid mt-4"),
        ]
    )

    # TASK 2.4: Creating Callbacks
    # Define the callback function to update the input container based on the selected statistics

    @app.callback(
        Output(component_id="select-year", component_property="disabled"),
        Input(component_id="dropdown-statistics", component_property="value"),
    )
    def update_input_container(selected_statistics: str):
        if selected_statistics == dropdown_options[0]["value"]:  # 'Yearly Statistics'
            return False
        return True

    # Callback for plotting
    # Define the callback function to update the input container based on the selected statistics
    @app.callback(
        Output(component_id="output-container", component_property="children"),
        Input(component_id="dropdown-statistics", component_property="value"),
        Input(component_id="select-year", component_property="value"),
    )
    def update_output_container(selected_statistics: str, input_year: str):
        if (
            selected_statistics == dropdown_options[1]["value"]
        ):  # 'Recession Period Statistics'
            # Filter the data for recession periods
            recession_data = data[data["Recession"] == 1]

            # TASK 2.5: Create and display graphs for Recession Report Statistics

            # Plot 1 Automobile sales fluctuate over Recession Period (year wise)
            # use groupby to create relevant data for plotting
            sales_rec_by_year = (
                recession_data.groupby("Year")["Automobile_Sales"].mean().reset_index()
            )

            R_chart1_title = (
                "Average automobile sales fluctuation over recession period"
            )
            R_chart1 = dcc.Graph(
                figure=px.line(
                    sales_rec_by_year,
                    x="Year",
                    y="Automobile_Sales",
                )
            )

            # Plot 2 Calculate the average number of vehicles sold by vehicle type
            # use groupby to create relevant data for plotting
            sales_rec_by_veh = (
                recession_data.groupby("Vehicle_Type")["Automobile_Sales"]
                .mean()
                .reset_index()
            )

            R_chart2_title = "Average number of vehicles sold by vehicle type"
            R_chart2 = dcc.Graph(
                figure=px.bar(
                    data_frame=sales_rec_by_veh,
                    x="Vehicle_Type",
                    y="Automobile_Sales",
                )
            )

            # Plot 3 Pie chart for total expenditure share by vehicle type during recession
            # use groupby to create relevant data for plotting
            exp_rec_by_veh = (
                recession_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
                .sum()
                .reset_index()
            )

            R_chart3_title = "Total expenditure share by vehicle type during recession"
            R_chart3 = dcc.Graph(
                figure=px.pie(
                    data_frame=exp_rec_by_veh,
                    names="Vehicle_Type",
                    values="Advertising_Expenditure",
                )
            )

            # Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
            sales_rec_by_uemp_veh = (
                recession_data.groupby(["unemployment_rate", "Vehicle_Type"])[
                    "Automobile_Sales"
                ]
                .sum()
                .reset_index()
            )

            R_chart4_title = "Vehicle wise sales by unemployment rate during recession"
            R_chart4 = dcc.Graph(
                figure=px.bar(
                    sales_rec_by_uemp_veh,
                    x="unemployment_rate",
                    y="Automobile_Sales",
                    color="Vehicle_Type",
                )
            )

            return [
                dbc.Row(
                    className="chart-item",
                    children=[
                        create_chart_container(R_chart1_title, R_chart1),
                        create_chart_container(R_chart2_title, R_chart2),
                    ],
                ),
                dbc.Row(
                    className="chart-item",
                    children=[
                        create_chart_container(R_chart3_title, R_chart3),
                        create_chart_container(R_chart4_title, R_chart4),
                    ],
                ),
            ]

        # TASK 2.6: Create and display graphs for Yearly Report Statistics
        # Yearly Statistic Report Plots
        elif (
            input_year and selected_statistics == dropdown_options[0]["value"]
        ):  # 'Yearly Statistics'
            yearly_data = data[data["Year"] == input_year]

            # #TASK 2.5: Creating Graphs Yearly data

            # plot 1 Yearly Automobile sales using line chart for the whole period.
            yas = data.groupby("Year")["Automobile_Sales"].mean().reset_index()

            Y_chart1_title = (
                "Yearly automobile sales using line chart for the whole period"
            )
            Y_chart1 = dcc.Graph(
                figure=px.line(
                    data_frame=yas,
                    x="Year",
                    y="Automobile_Sales",
                )
            )

            # Plot 2 Total Monthly Automobile sales using line chart.
            mas = yearly_data.groupby("Month")["Automobile_Sales"].sum().reset_index()

            Y_chart2_title = "Total monthly automobile sales in the year {}".format(
                input_year
            )
            Y_chart2 = dcc.Graph(
                figure=px.line(
                    data_frame=mas,
                    x="Month",
                    y="Automobile_Sales",
                )
            )

            # Plot bar chart for average number of vehicles sold during the given year
            avr_vdata = (
                yearly_data.groupby("Vehicle_Type")["Automobile_Sales"]
                .sum()
                .reset_index()
            )

            Y_chart3_title = (
                "Average vehicles sold by vehicle type in the year {}".format(
                    input_year
                )
            )
            Y_chart3 = dcc.Graph(
                figure=px.bar(
                    data_frame=avr_vdata,
                    x="Vehicle_Type",
                    y="Automobile_Sales",
                )
            )

            # Total Advertisement Expenditure for each vehicle using pie chart
            exp_data = (
                yearly_data.groupby("Vehicle_Type")["Advertising_Expenditure"]
                .sum()
                .reset_index()
            )

            Y_chart4_title = "Advertisement expenditure for each vehicle in the year {}".format(
                input_year
            )
            Y_chart4 = dcc.Graph(
                figure=px.pie(
                    data_frame=exp_data,
                    names="Vehicle_Type",
                    values="Advertising_Expenditure",
                )
            )

            # TASK 2.6: Returning the graphs for displaying Yearly data
            # return [
            #   html.Div(className='.........', children=[html.Div(....,html.Div(....)],style={...}),
            #   html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...})]

            return [
                dbc.Row(
                    className="chart-item",
                    children=[
                        create_chart_container(Y_chart1_title, Y_chart1),
                        create_chart_container(Y_chart2_title, Y_chart2),
                    ],
                ),
                dbc.Row(
                    className="chart-item",
                    children=[
                        create_chart_container(Y_chart3_title, Y_chart3),
                        create_chart_container(Y_chart4_title, Y_chart4),
                    ],
                ),
            ]

        else:
            return None

    return app


def create_chart_container(title, chart):
    return dbc.Col(
        [
            dbc.Row(html.H4(title, className="text-center")),
            dbc.Row(chart),
        ],
        xs=12,
        lg=6,
        className="mb-4",
    )
