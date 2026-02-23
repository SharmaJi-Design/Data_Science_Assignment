# tip_prediction_app.py

import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

# --------------------------------------------------
# 1. Load dataset and train Linear Regression model
# --------------------------------------------------

# Load tips dataset
tips = sns.load_dataset("tips")

# Features and target
X = tips[["total_bill", "size"]]
y = tips["tip"]

# Train model
model = LinearRegression()
model.fit(X, y)

# --------------------------------------------------
# 2. Create Dash App
# --------------------------------------------------

app = Dash(__name__)

app.layout = html.Div(
    style={"width": "50%", "margin": "auto", "padding": "20px"},
    children=[
        html.H1("Tip Prediction App"),

        html.Label("Total Bill Amount"),
        dcc.Input(
            id="total-bill",
            type="number",
            placeholder="Enter total bill",
            style={"width": "100%"}
        ),

        html.Br(), html.Br(),

        html.Label("Number of People"),
        dcc.Input(
            id="size",
            type="number",
            placeholder="Enter number of people",
            style={"width": "100%"}
        ),

        html.Br(), html.Br(),

        html.Button("Predict Tip", id="predict-btn", n_clicks=0),

        html.Br(), html.Br(),

        html.H3(id="output")
    ]
)

# --------------------------------------------------
# 3. Callback for Prediction
# --------------------------------------------------

@app.callback(
    Output("output", "children"),
    Input("predict-btn", "n_clicks"),
    State("total-bill", "value"),
    State("size", "value")
)
def predict_tip(n_clicks, total_bill, size):
    if n_clicks > 0:
        if total_bill is None or size is None:
            return "Please enter both total bill and number of people."

        prediction = model.predict(np.array([[total_bill, size]]))
        return f"Predicted Tip Amount: ${prediction[0]:.2f}"

    return ""

# --------------------------------------------------
# 4. Run App
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)