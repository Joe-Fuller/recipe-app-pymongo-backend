from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Dict

from models import Recipe, RecipeUpdate

router = APIRouter()


@router.post(
    "/",
    response_description="Create a new recipe",
    status_code=status.HTTP_201_CREATED,
    response_model=Recipe,
)
def create_recipe(request: Request, recipe: Recipe = Body(...)):
    recipe = jsonable_encoder(recipe)
    new_recipe = request.app.database["recipes"].insert_one(recipe)
    created_recipe = request.app.database["recipes"].find_one(
        {"_id", new_recipe.inserted_id}
    )

    return created_recipe


@router.get("/", response_description="List all recipes", response_model=List[Recipe])
def list_recipes(request: Request):
    recipes = list(request.app.database["recipes"]).find(limit=100)
    return recipes
