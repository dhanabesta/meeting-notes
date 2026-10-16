from pydantic import BaseModel
from typing import List, Optional
import json

class ActionItem(BaseModel):
    task: str
    owner: Optional[str] = None
    deadline: Optional[str] = None
    priority: Optional[str] = "Medium"


class ActionItemsResponse(BaseModel):
    action_items: List[ActionItem]


def parse_output(output: str):
    data = json.loads(output)
    return ActionItemsResponse(**data)