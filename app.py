import streamlit as st
import pandas as pd

from utils.stock_utils import get_stock_data
from utils.charts import create_stock_chart
from utils.anomaly_detection import detect_anomalies

from agents.stock_agent import stock_agent_response
from agents.expense_agent import expense_agent_response
from agents.report_agent import generate_report
from agents.coordinator import coordinator_agent

st.set_page_config(
    page_title="Agentic Financial Intelligence",
    page_icon="📈",
    layout="wide"
)

st.title("Agentic AI Financial Intelligence Platform")

user_query = st.text_input(
    "Ask Financial AI",
    "Analyze stock trends"
)

selected_agent = coordinator_agent(user_query)

st.info(f"Active Agent: {selected_agent}")

menu = st.sidebar.selectbox(
    "Choose Module",
    [
        "Stock Analysis",
        "Expense Analysis"
    ]
)

# =========================
# STOCK ANALYSIS
# =========================

if menu == "Stock Analysis":

    st.header("AI Stock Analysis")

    st.divider()

    ticker = st.text_input(
        "Enter Stock Ticker",
        "AAPL"
    )

    if st.button("Analyze Stock"):

        stock_data = get_stock_data(ticker)

        risk_score = round(
            stock_data['Returns'].std() * 100,
            2
        )

        st.metric(
            "AI Risk Score",
            risk_score
        )

        st.subheader("Stock Dataset")

        st.dataframe(
            stock_data.tail()
        )

        chart = create_stock_chart(
            stock_data,
            ticker
        )

        st.plotly_chart(chart)

        st.subheader(
            "AI Financial Insights"
        )

        st.info(
            "This analysis helps evaluate "
            "market volatility, investment "
            "risk, and financial trends."
        )

        insight = stock_agent_response(
            ticker,
            stock_data
        )

        st.write(insight)

# =========================
# EXPENSE ANALYSIS
# =========================

elif menu == "Expense Analysis":

    st.header(
        "Expense Analytics & Fraud Monitoring"
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Expense CSV"
    )

    if uploaded_file:

        df = pd.read_csv(uploaded_file)

        total_spending = df['Amount'].sum()

        top_category = (
            df.groupby('Category')['Amount']
            .sum()
            .idxmax()
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "Total Spending",
            f"${total_spending}"
        )

        col2.metric(
            "Top Category",
            top_category
        )

        st.subheader("Expense Data")

        st.dataframe(df.head())

        st.subheader("Category Summary")

        category_summary = (
            df.groupby('Category')['Amount']
            .sum()
        )

        st.bar_chart(category_summary)

        st.subheader(
            "Anomaly Detection"
        )

        anomalies = detect_anomalies(df)

        health_score = 85 - (
            len(anomalies) * 5
        )

        fraud_risk = min(
            len(anomalies) * 15,
            100
        )

        col3, col4 = st.columns(2)

        col3.metric(
            "Financial Health Score",
            health_score
        )

        col4.metric(
            "Fraud Risk Score",
            f"{fraud_risk}%"
        )

        st.dataframe(anomalies)

        if len(anomalies) > 0:

            st.error(
                "Potential suspicious "
                "financial transactions detected."
            )

        st.subheader(
            "AI Expense Insights"
        )

        st.info(
            "Expense anomalies may indicate "
            "unusual financial behavior or "
            "overspending patterns."
        )

        insights = expense_agent_response(df)

        st.write(insights)

        if st.button(
            "Generate Executive Report"
        ):

            path = generate_report(
                insights
            )

            st.success(
                f"Report Generated: {path}"
            )