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


@router.get(
    "/{id}", response_description="Get a single recipe by id", response_model=Recipe
)
def find_recipe(id: str, request: Request):
    if (recipe := request.app.database["recipes"].find_one({"_id": id})) is not None:
        return recipe
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Recipe with ID {id} not found"
    )
