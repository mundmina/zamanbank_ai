from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_products(goal: str):
    # В реальном проекте можно парсить продукты с сайта Zaman Bank
    if "квартира" in goal.lower():
        return [{"name": "Zaman Smart", "type": "Депозит", "profit": "4.5%"}]
    else:
        return [{"name": "Zaman Halal", "type": "Инвестиции", "profit": "5.0%"}]
