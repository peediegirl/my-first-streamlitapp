# Streamlit live coding script
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# First some Data Exploration
st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

volcano_df_raw = load_data(path="./data/volcano_ds_pop.csv")
volcano_df = deepcopy(volcano_df_raw)

volcano_df['Country'] = volcano_df['Country'].replace({'United States':'United States of America',
                                                                      'Tanzania':'United Republic of Tanzania',
                                                                      'Martinique':'Martinique',
                                                                      'Sao Tome & Principe':'Sao Tome and Principe',
                                                                      'Guadeloupe':'Guadeloupe',
                                                                      'Wallis & Futuna':'Wallis and Futuna'})


# Add title and header
st.title("Introduction to Streamlit")
st.header("Volcanoes Data Exploration")

# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
if st.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data=volcano_df)

# Setting up columns
left_column, middle_column, right_column = st.columns([3, 1, 1])

# Widgets countries: selectbox
countries = ["All"]+sorted(pd.unique(volcano_df['Country']))
country = left_column.selectbox("Choose a Country", countries)

# Flow control and plotting
if country == "All":
    reduced_df = volcano_df
else:
    reduced_df = volcano_df[volcano_df["Country"] == country]


# Widgets types: selectbox
types = ["All"]+sorted(pd.unique(reduced_df['Type']))
type = left_column.selectbox("Choose a Type", types)

#if country != "All":
 #   types = sorted(pd.unique(volcano_df[['Country']== country]["Type"]))


# Flow control and plotting
#if country == "All" and type =='All':
  #  reduced_df = volcano_df
#elif country == "All" and type !='All':
  #  reduced_df = volcano_df[volcano_df["Type"] == type]
#elif country != "All" and type =='All':
  #  reduced_df = volcano_df[volcano_df["Country"] == country]
#else:
 #   reduced_df = volcano_df[([volcano_df["Country"] == country])&([volcano_df["Type"] == type])]




# Flow control and plotting
#if type == "All":
#   reduced_df = volcano_df
#else:
#    reduced_df = volcano_df[volcano_df["Type"] == type]


# Another header
st.header("Maps")

fig = px.scatter_mapbox(reduced_df,
                        lat='Latitude',
                        lon='Longitude',
                        color='Type',
                        hover_name='Volcano Name',
                        hover_data=['Type', 'Country', 'Region', 'Status'],
                        zoom=1.5,
                        title="<b>'Volcanoes of the World'</b>",
                        color_discrete_sequence=px.colors.qualitative.Plotly)

fig.update_layout(
                    title={"font_size":20,
                        "xanchor":"center", "x":0.38,
                        "yanchor":"bottom", "y":0.95},
                    title_font=dict(size=24, color='Black', family='Arial, sans-serif'),
                    height=1100,
                    width=1300,
                    autosize=True,
                    hovermode='closest',
                    mapbox=dict(
                        style='open-street-map'
                    ),
                    legend_title_text='Volcano Type'
)

st.plotly_chart(fig)


# Another header
st.header("Elevation")


# Flow control and plotting
#if country == "All":
   # reduced_country_df = volcano_df
#else:
   # reduced_country_df = volcano_df[volcano_df["Country"] == country]

#fig2 = px.scatter(reduced_country_df, x="Volcano Name", y="Elev", color="Country")
fig2 = px.scatter(reduced_df, x="Volcano Name", y="Elev", color="Country")
fig2.update_layout( height=800,
                    width=800,
                    autosize=True)
st.plotly_chart(fig2)
