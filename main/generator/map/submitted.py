""" Plot the interactive map with time slider for the web"""
import plotly.express as px

fig_pfizer = px.choropleth(
    pfizer_data,
    locationmode = "USA-states",
    locations = "States",
    animation_frame = "Week of Allocations",
    hover_name = "Jurisdiction",
    hover_data = {
        "Week of Allocations": True,
        "States": False,
        "Cumulative Allocations": True,
    },
    color = "Cumulative Allocations",
    width = 1200,
    height = 600,
    color_continuous_scale = px.colors.sequential.Bluyl,
    range_color = [0, max(pfizer_data["Cumulative Allocations"])],
)
fig_pfizer.update_traces(
    zauto = False, zmin = 0, zmax = max(pfizer_data["Cumulative Allocations"])
)
fig_pfizer["layout"].pop("updatemenus")
fig_pfizer.update_layout(
    title_text = "  ",
    title_font_size = 20,
    title_xref = "paper",
    title_x = 0.5,
    title_xanchor = "center",
    separators = ".,",
    geo_scope = "usa",
    hoverlabel = dict(bgcolor = "white", font_size = 13),
    coloraxis_colorbar = dict(
        title = "Cumulative Allocations",
        thicknessmode = "pixels",
        thickness = 40,
        lenmode = "pixels",
        len = 400,
        yanchor = "top",
        y = 0.9,
        ticks = "outside",
    ),
    margin = dict(l = 10, r = 10, t = 10, b = 10),
)
fig_pfizer.add_scattergeo(
    lon = pfizer_data["lon"],
    lat = pfizer_data["lat"],
    locationmode = "USA-states",
    text = pfizer_data["States"],
    mode = "text",
    hoverinfo = "skip",
)
fig_pfizer.update_layout(font = dict(size = 13, color = "black"), showlegend = False)
#fig_pfizer.write_html("pfizer.html")

fig_moderna = px.choropleth(
    moderna_data,
    locationmode = "USA-states",
    locations = "States",
    animation_frame = "Week of Allocations",
    hover_name = "Jurisdiction",
    hover_data = {
        "Week of Allocations": True,
        "States": False,
        "Cumulative Allocations": True,
    },
    color = "Cumulative Allocations",
    width = 1200,
    height = 600,
    color_continuous_scale = px.colors.sequential.Bluyl,
    range_color = [0, max(pfizer_data["Cumulative Allocations"])],
)
fig_moderna.update_traces(
    zauto = False, zmin = 0, zmax = max(pfizer_data["Cumulative Allocations"])
)
fig_moderna["layout"].pop("updatemenus")

fig_moderna.update_layout(
    title_text = "  ",
    title_font_size = 20,
    title_xref = "paper",
    title_x = 0.5,
    title_xanchor = "center",
    separators = ".,",
    geo_scope = "usa",
    hoverlabel = dict(bgcolor = "white", font_size = 13),
    coloraxis_colorbar = dict(
        title = "Cumulative Allocations",
        thicknessmode = "pixels",
        thickness = 40,
        lenmode = "pixels",
        len = 400,
        yanchor = "top",
        y = 0.9,
        ticks = "outside",
    ),
    margin = dict(l = 10, r=10, t=10, b=10),
)
fig_moderna.add_scattergeo(
    lon = moderna_data["lon"],
    lat = moderna_data["lat"],
    locationmode = "USA-states",
    text = moderna_data["States"],
    mode = "text",
    hoverinfo = "skip",
)
fig_moderna.update_layout(font = dict(size = 13, color = "black"), showlegend = False)
#fig_moderna.write_html("moderna.html")
