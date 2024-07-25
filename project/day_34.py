import numpy as np
import pandas as pd
import plotly.express as px
import plotly.offline as py
import plotly.graph_objs as go
from plotly.figure_factory import create_table

# Load the gapminder dataset
gapminder = px.data.gapminder()

# Create a table from the first 15 rows of the dataset
table = create_table(gapminder.head(15))

# Plot the table using plotly.offline.plot
# py.plot(table, filename='gapminder_table.html')

india_data = px.data.gapminder().query("country == 'India'")
# print(india_data)

# Task-4
fig = px.bar(india_data, x='year', y='pop', height=400)
# fig.show()

fig1 = px.bar(india_data, x='year', y='pop', color='lifeExp', labels={'pop': 'Population of India'}, height=400)
# fig1.show()

gap2007 = gapminder.query('year == 2007')
fig2 = px.scatter(gap2007, x='gdpPercap', y='lifeExp', height=400, color='continent',
                  size='pop', hover_data=['country'], size_max=30)
# fig2.show()

fig3 = px.scatter(gap2007, x='gdpPercap', y='lifeExp', height=400, color='continent',
                  size='pop', hover_name='country', facet_col='continent', size_max=60)
# fig3.show()

fig4 = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent',
                  size='pop', hover_name='country', log_x=True, animation_frame='year',
                  animation_group='country', range_x=[25, 10000], range_y=[25, 90], size_max=40)
# fig4.show()

fig5 = px.scatter(gapminder, x='gdpPercap', y='lifeExp', color='continent',
                  size='pop', hover_name='country', log_x=True, animation_frame='year',
                  animation_group='country', range_x=[25, 10000], range_y=[25, 90],
                  labels=dict(pop="Population", gdpPercap="GDP Per Capita", lifeExp="Life Expectancy"), size_max=40)
# fig5.show()

fig6 = px.line_geo(gapminder.query('year == 2007'), locations='iso_alpha', color='continent',
                   projection='orthographic', hover_name='country')
# fig6.show()

# Creating a map using scatter_geo()
fig7 = px.scatter_geo(gapminder.query('year == 2007'), height=500, locations='iso_alpha', color='continent',
                      size='pop', size_max=30, projection='orthographic', hover_name='country')
# fig7.show()

fig8 = px.choropleth(gapminder, locations='iso_alpha', height=500, hover_name='country', color='lifeExp',
                     animation_frame='year', color_continuous_scale=px.colors.sequential.Viridis, projection='orthographic')
fig8.show()