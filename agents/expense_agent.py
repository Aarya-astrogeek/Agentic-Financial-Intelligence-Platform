import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyAePIOKVLUyZHHi-IHRVpE0l7KfTLhJLxM")
)

model = genai.GenerativeModel("gemini-2.0-flash")

def expense_agent_response(df):

    total_spending = df['Amount'].sum()

    top_category = (
        df.groupby('Category')['Amount']
        .sum()
        .idxmax()
    )

    prompt = f"""
    Analyze the following expense profile.

    Total spending: {total_spending}

    Highest spending category: {top_category}

    Give:
1. Spending behavior insights
2. Savings recommendations
3. Financial warnings
4. Budgeting suggestions
5. Potential fraud indicators
6. Suspicious transaction observations
    """

    response = model.generate_content(prompt)

    return response.text