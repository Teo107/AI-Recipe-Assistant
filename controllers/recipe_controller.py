import json
from models.ai_model import ask_ai_for_recipe

def generate_recipes(ingredients, flavor, diet, allergies, budget):
    prompt = f"""
    You are one of the best chefs in the world!
    The user has these ingredients: {ingredients}.
    Flavor preference: {flavor}.
    Diet: {diet}.
    Allergies: {allergies}.
    Price: {budget} RON per serving.

    TASK:
    Generate EXACTLY 3 recipes as a valid JSON array (no text or explanations before or after it).
    Each recipe must have this format:
    [
      {{
        "name": "Recipe name",
        "calories": "### kcal",
        "prep_time": "## minutes",
        "price": "## RON per serving",
        "ingredients": ["ingredient1", "ingredient2", ...],
        "to_buy": ["ingredient1", "ingredient2", ...],
        "steps": ["Step 1...", "Step 2...", ...]
      }},
      ...
    ]
    
    RULES: 
    1. Recipe 1 must use only the available ingredients!
    2. Recipe 2 and 3 can include extra ingredients that are in the given budget!
    3. keep it realistic for someone who might not want to go shopping
        Those extra ones must be listed under "to_buy".
    4. keep the price within the given budget
    5. Do not display price: at the recipes that do not includes shopping
    6. be careful about diet and allergies because maybe there are in the list but you have to AVOID them in the recipes!
    7. Reply only with JSON
    """

    response = ask_ai_for_recipe(prompt)

    # Cleanup: remove code block markers or text before JSON
    cleaned = (
        response.replace("```json", " ")
        .replace("```", " ")
        .replace("`", " ")
        .replace("\\n", " ")
        .strip()
    )

    # Parse the JSON safely
    try:
        recipes = json.loads(cleaned)
    except Exception as e:
        recipes = [
            {
                "name": "Error",
                "calories": "-",
                "prep_time": "-",
                "price": "-",
                "ingredients": [],
                "steps": [response],
            }
        ]

    return recipes