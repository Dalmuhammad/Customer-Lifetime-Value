import streamlit as st
import matplotlib.pyplot as plt

def show_metrics(metrics):
    st.subheader('Model Evaluation Metrics:')

    # Membuat tabel dengan Markdown
    table = f"""
    | Metric                                       | Value                         |
    |----------------------------------------------|-------------------------------|
    | **Model**                                    | XGB Regressor                 |
    | **Mean Squared Error (MSE)**                 | {metrics["MSE"].iloc[0]}       |
    | **Root Mean Squared Error (RMSE)**           | {metrics["RMSE"].iloc[0]}     |
    | **Mean Absolute Error (MAE)**                | {metrics["MAE"].iloc[0]}      |
    | **Mean Absolute Percentage Error (MAPE)**    | {metrics["MAPE"].iloc[0]}     |
    | **R-squared (R²)**                           | {metrics["R2"].iloc[0]}       |
    """

    st.markdown(table)


def show_plot(prediction):
    y_test = prediction['y_test']
    y_pred = prediction['y_pred']
    st.subheader('True vs Predicted:')
    fig, ax = plt.subplots()
    ax.scatter(y_test, y_pred, color='blue')
    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2)
    ax.set_xlabel('True Values')
    ax.set_ylabel('Predicted Values')
    ax.set_title('True vs Predicted Values')
    st.pyplot(fig)