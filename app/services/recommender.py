def recommend_products(goal: str):
    goal = goal.lower()
    if "квартира" in goal:
        return [
            {"name": "Zaman Smart", "type": "Депозит", "profit": "4.5% годовых"},
            {"name": "Halal Home Plan", "type": "Инвестиции", "profit": "5.0% годовых"}
        ]
    elif "путешествие" in goal:
        return [{"name": "Zaman Travel Saver", "type": "Сберегательный счет", "profit": "3.8%"}]
    else:
        return [{"name": "Zaman Universal", "type": "Базовый депозит", "profit": "4.0%"}]
