from typing import Dict


def calculate(recipe_info: Dict, portions: int):
    print(
        f"\n\nCalculating details for your recipe based on {', '.join(recipe_info.keys())}...\n\n"
    )

    for ingredient_name, ingredient_info in recipe_info.items():
        print(
            f"The following accounts for nutrition info from {ingredient_name} per portion:"
        )
        ratio = ingredient_info["servings"] / portions
        for attr, val in ingredient_info["nutrition"].items():
            print(f"\t{attr}: {val * ratio}")
        print("\n\n")


def start():
    print("Welcome to the calculator!")
    print("Let's start with entering each ingredient.")
    entering_ingredients = True
    recipe_info = dict()
    while entering_ingredients:
        ingredient_name = input("\nWhat's the name of this ingredient?\n")
        ingredient_info = {
            "nutrition": {},
            "servings": int(
                input(f"How many servings of {ingredient_name} are you using?\n")
            ),
        }
        for attr in {"calories"}:
            ingredient_info["nutrition"][attr] = int(
                input(f"How many {attr} per serving of {ingredient_name}?\n")
            )

        recipe_info[ingredient_name] = ingredient_info

        entering_ingredients = (
            input("Are there any more ingredients to enter? [Y/n]\n") or "Y"
        ).lower() == "y"

    portions = int(input("\nGreat! Now how many portions does this recipe make?\n"))
    calculate(recipe_info, portions)


if __name__ == "__main__":
    start()
