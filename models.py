import uuid
from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    name: str
    amount: str
    units: str


class Recipe(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    timeToCook: str = Field(...)
    image: str = Field(...)
    ingredients = List[Dict[str, str]] = Field(...)
    instructions = List[str] = Field(...)
