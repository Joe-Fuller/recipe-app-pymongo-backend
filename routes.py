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


@router.put("/{id}", response_description="Update a recipe", response_model=Recipe)
def update_recipe(id: str, request: Request, recipe: RecipeUpdate = Body(...)):
    recipe = {k: v for k, v in recipe.dict().items() if v is not None}
    if len(recipe) >= 1:
        update_result = request.app.database["recipes"].update_one(
            {"_id": id}, {"$set": recipe}
        )

        if update_result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Recipe with ID {id} not found",
            )

    if (
        existing_book := request.app.database["recipes"].find_one({"_id": id})
    ) is not None:
        return existing_book

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, detail=f"Recipe with ID {id} not found"
    )


@router.delete("/{id}", response_description="Delete a recipe")
def delete_recipe(id: str, request: Request, response: Response):
    delete_result = request.app.database["recipes"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Recipe with ID {id} not found"
    )
