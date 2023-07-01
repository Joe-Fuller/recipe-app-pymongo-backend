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

    class Config:
        schema_extra = {
            "example": {
                "_id": "1",
                "name": "Trifle",
                "timeToCook": "1 Hour",
                "image": "http:image.com/recipeimage",
                "ingredients": [{"name": "milk", "amount": "2", "units": "cups"}],
                "instructions": ["Make trifle", "Serve trifle"],
            }
        }


class RecipeUpdate(BaseModel):
    name: Optional[str]
    timeToCook: Optional[str]
    image: Optional[str]
    ingredients: Optional[List[Dict[str, str]]]
    instructions: Optional[List[str]]

    class Config:
        schema_extra = {
            "example": {
                "name": "Trifle",
                "timeToCook": "1 Hour",
                "image": "http:image.com/recipeimage",
                "ingredients": [{"name": "milk", "amount": "2", "units": "cups"}],
                "instructions": ["Make trifle", "Serve trifle"],
            }
        }
