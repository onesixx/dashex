from dash.dependencies import Input, Output, State
from dashPages.iris.model import iris

from sklearn.cluster import KMeans
import plotly.graph_objs as go


def get_callbacks(app):
    # Update figure on slider change
    @app.callback(
        Output("cluster-graph", "figure"),
        [
            Input("x-variable", "value"),
            Input("y-variable", "value"),
            Input("cluster-count", "value"),
        ],
    )
    def make_graph(x, y, n_clusters):
        # minimal input validation, make sure there's at least one cluster
        km = KMeans(n_clusters=max(n_clusters, 1))
        df = iris.loc[:, [x, y]]
        km.fit(df.values)
        df["cluster"] = km.labels_

        centers = km.cluster_centers_

        data = [
            go.Scatter(
                x=df.loc[df.cluster == c, x],
                y=df.loc[df.cluster == c, y],
                mode="markers",
                marker={"size": 8},
                name="Cluster {}".format(c),
            )
            for c in range(n_clusters)
        ]
        data.append(
            go.Scatter(
                x=centers[:, 0],
                y=centers[:, 1],
                mode="markers",
                marker={"color": "#000", "size": 12, "symbol": "diamond"},
                name="Cluster centers",
            )
        )
        layout = {
            "xaxis": {"title": x}, 
            "yaxis": {"title": y}
        }
        return go.Figure(data=data, layout=layout)

    # make sure that x and y values can't be the same variable
    def filter_options(v):
        """Disable option v"""
        return [
            {"label": col, "value": col, "disabled": col == v}
            for col in iris.columns
        ]

    # functionality is the same for both dropdowns, so we reuse filter_options
    app.callback(
        Output("x-variable", "options"),
        [Input("y-variable", "value")])(
        filter_options
    )
    app.callback(
        Output("y-variable", "options"),
        [Input("x-variable", "value")])(
        filter_options
    )
