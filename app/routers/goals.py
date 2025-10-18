from fastapi import APIRouter
from app.models.schemas import Goal, GoalResponse

router = APIRouter(prefix="/goals", tags=["Goals"])

# temporary in-memory store
user_goals = {}

@router.post("/", response_model=GoalResponse)
def create_goal(goal: Goal):
    """
    Creates a financial goal for a user (mock).
    """
    if goal.user_id not in user_goals:
        user_goals[goal.user_id] = []
    user_goals[goal.user_id].append(goal)
    return GoalResponse(message=f"Goal '{goal.title}' created successfully.")
