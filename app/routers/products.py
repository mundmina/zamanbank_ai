from fastapi import APIRouter, Query
from app.services.recommender import recommend_products

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def get_product_recommendations(goal: str = Query(..., description="Financial goal, e.g. 'купить квартиру'")):
    """
    Returns suitable banking products for a given goal.
    """
    products = recommend_products(goal)
    return {"goal": goal, "recommendations": products}
