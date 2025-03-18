# --------------------------------------------
# Imports - PyShiny EXPRESS VERSION
# --------------------------------------------

from shiny import reactive, render
from shiny.express import input, ui
from pathlib import Path
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from faicons import icon_svg

# --------------------------------------------
# Load Data
# --------------------------------------------

# Path to the dataset
data_path = Path(__file__).parent / "../docs/symbols_valid_meta.csv"
df = pd.read_csv(data_path)

# --------------------------------------------
# Define User Interface
# --------------------------------------------

ui.page_opts(
    title="Stock Market Insights Dashboard",
    fillable=True,
)

ui.h2("📈 Stock Market Dashboard", class_="text-primary text-center")
ui.h5(
    "An interactive and dynamic dashboard for exploring the stock market landscape",
    class_="text-center text-muted",
)

# Sidebar with filtering options
with ui.sidebar(title="Filters", open="open"):
    ui.h3("Filter Options", class_="text-primary")
    ui.input_selectize(
        "market_category",
        "Market Category:",
        choices=sorted(df["Market Category"].dropna().unique()),
        selected=[],
        multiple=True,
    )
    ui.input_selectize(
        "listing_exchange",
        "Listing Exchange:",
        choices=sorted(df["Listing Exchange"].dropna().unique()),
        selected=[],
        multiple=True,
    )
    ui.input_checkbox_group(
        "financial_status",
        "Financial Status:",
        choices=sorted(df["Financial Status"].dropna().unique()),
        selected=[],
    )
    ui.hr()
    ui.p("Use the filters to customize your insights.", class_="text-muted")

# Layout with Value Boxes
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("chart-line"), theme="bg-gradient-green-blue"):
        "Number of Stocks"

        @render.text
        def stock_count():
            return f"{filtered_df().shape[0]} stocks"

    with ui.value_box(showcase=icon_svg("building-columns"), theme="bg-gradient-blue-purple"):
        "Unique Exchanges"

        @render.text
        def exchange_count():
            return f"{filtered_df()['Listing Exchange'].nunique()} exchanges"

    with ui.value_box(showcase=icon_svg("tags"), theme="bg-gradient-yellow-orange"):
        "Market Categories"

        @render.text
        def market_category_count():
            return f"{filtered_df()['Market Category'].nunique()} categories"

# Chart and Table Layout
with ui.layout_columns():
    # Market Category Chart
    with ui.card(full_screen=True, theme="shadow"):
        ui.card_header("Market Category Distribution", class_="text-primary")
        
        @render_plotly
        def market_category_chart():
            df_filtered = filtered_df()
            if df_filtered.empty:
                return px.scatter(title="No data available")
            fig = px.bar(
                df_filtered,
                x="Market Category",
                title="Market Category Distribution",
                labels={"Market Category": "Category"},
                color_discrete_sequence=["#2ca02c"],  # Green bars
            )
            fig.update_layout(
                title_font=dict(size=18, color="darkblue"),
                xaxis_title="Market Category",
                yaxis_title="Count",
                template="plotly_white",
            )
            return fig

    # Stock Data Table
    with ui.card(full_screen=True, theme="shadow"):
        ui.card_header("Filtered Stock Data", class_="text-primary")

        @render.data_frame
        def stock_data_table():
            cols = [
                "Symbol",
                "Security Name",
                "Market Category",
                "Listing Exchange",
                "Financial Status",
            ]
            return filtered_df()[cols]

# --------------------------------------------
# Define Reactive Content
# --------------------------------------------

@reactive.calc
def filtered_df():
    # Start with the full dataset
    filt_df = df

    # Filter by Market Category
    selected_categories = input.market_category()
    if selected_categories:
        filt_df = filt_df[filt_df["Market Category"].isin(selected_categories)]

    # Filter by Listing Exchange
    selected_exchanges = input.listing_exchange()
    if selected_exchanges:
        filt_df = filt_df[filt_df["Listing Exchange"].isin(selected_exchanges)]

    # Filter by Financial Status
    selected_statuses = input.financial_status()
    if selected_statuses:
        filt_df = filt_df[filt_df["Financial Status"].isin(selected_statuses)]

    return filt_df
