import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("AIzaSyAePIOKVLUyZHHi-IHRVpE0l7KfTLhJLxM")
)


model = genai.GenerativeModel("gemini-2.0-flash")

def stock_agent_response(ticker, stock_data):

    latest_price = stock_data['Close'].iloc[-1]

    volatility = stock_data['Returns'].std()

    prompt = f"""
    Analyze stock {ticker}.

    Latest price: {latest_price}

    Volatility: {volatility}

    Give:
    1. Trend summary
    2. Risk analysis
    3. Investment recommendation
    4. Volatility interpretation
    5. Overall conclusion
    """

    response = model.generate_content(prompt)

    return response.text