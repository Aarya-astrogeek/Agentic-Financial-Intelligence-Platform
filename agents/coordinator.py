def coordinator_agent(user_query):

    if "stock" in user_query.lower():
        return "Routing to Stock Analysis Agent"

    elif "expense" in user_query.lower():
        return "Routing to Expense Analysis Agent"

    else:
        return "Routing to General Financial Agent"