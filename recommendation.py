import random
from wardrobe import get_wardrobe

# Predefined outfit suggestions for different occasions and weather
outfit_suggestions = {
    "School": {
        "Cold": ["Thick coat", "Sweater", "Jeans", "Boots"],
        "Hot": ["T-shirt", "Shorts", "Sneakers"],
        "Cloudy": ["Sweatshirt", "Jeans", "Sneakers"],
        "Rainy": ["Waterproof jacket", "Jeans", "Rain boots"]
    },
    "Date": {
        "Cold": ["Overcoat", "Sweater", "Casual pants", "Leather shoes"],
        "Hot": ["Shirt", "Casual shorts", "Canvas shoes"],
        "Cloudy": ["Jacket", "Shirt", "Casual pants", "Leather shoes"],
        "Rainy": ["Trench coat", "Shirt", "Casual pants", "Waterproof shoes"]
    },
    "Party": {
        "Cold": ["Knitwear", "Casual jacket", "Jeans", "Casual shoes"],
        "Hot": ["Polo shirt", "Casual shorts", "Canvas shoes"],
        "Cloudy": ["Shirt", "Jeans", "Casual shoes"],
        "Rainy": ["Sweatshirt", "Jeans", "Casual shoes"]
    },
    "Work": {
        "Cold": ["Suit", "Shirt", "Suit pants", "Leather shoes"],
        "Hot": ["Thin shirt", "Suit pants", "Leather shoes"],
        "Cloudy": ["Suit", "Shirt", "Suit pants", "Leather shoes"],
        "Rainy": ["Trench coat", "Shirt", "Suit pants", "Waterproof shoes"]
    }
}

def recommend_outfit():
    """Recommend an outfit based on occasion and weather."""
    print("\n===== Outfit Recommendation (Style Companion) =====")
    print("Select an occasion:")
    print("1. School")
    print("2. Date")
    print("3. Party")
    print("4. Work")

    occasions = ["School", "Date", "Party", "Work"]
    try:
        occasion_choice = int(input("Choose (1-4): ")) - 1
        if not (0 <= occasion_choice < len(occasions)):
            print("Invalid choice.")
            return
        occasion = occasions[occasion_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    print("\nSelect weather:")
    print("1. Cold")
    print("2. Hot")
    print("3. Cloudy")
    print("4. Rainy")

    weathers = ["Cold", "Hot", "Cloudy", "Rainy"]
    try:
        weather_choice = int(input("Choose (1-4): ")) - 1
        if not (0 <= weather_choice < len(weathers)):
            print("Invalid choice.")
            return
        weather = weathers[weather_choice]
    except ValueError:
        print("Please enter a valid number.")
        return

    color_pref = None
    if input("\nDo you have a color preference? (y/n): ").lower() == 'y':
        color_pref = input("Please enter your preferred color: ")

    generate_recommendation(occasion, weather, color_pref)

def generate_recommendation(occasion, weather, color_pref=None):
    """Generate and display the outfit recommendation."""
    print(f"\nRecommended outfit for {occasion} occasion, {weather} weather:")

    wardrobe_items = get_wardrobe()

    # Try to find user wardrobe item that matches color, occasion, and weather
    if color_pref and wardrobe_items:
        colored_items = [item for item in wardrobe_items
                        if item["color"].lower() == color_pref.lower()
                        and occasion in [o.strip() for o in item["occasion"]]
                        and weather in [w.strip() for w in item["weather"]]]

        if colored_items:
            random_item = random.choice(colored_items)
            print(f"- From your wardrobe: {random_item['color']} {random_item['name']} ({random_item['type']})")
            # Avoid duplicate type suggestion
            if random_item["type"].lower() in ("top", "shirt", "t-shirt", "sweater", "coat", "jacket"):
                display_items = [item for item in outfit_suggestions[occasion][weather] if "shirt" not in item.lower() and "sweater" not in item.lower() and "coat" not in item.lower() and "jacket" not in item.lower()]
            else:
                display_items = outfit_suggestions[occasion][weather]
            for item in display_items:
                print(f"- {item}")
            return

    # Default suggestion
    if occasion in outfit_suggestions and weather in outfit_suggestions[occasion]:
        for item in outfit_suggestions[occasion][weather]:
            print(f"- {item}")
    else:
        print("Sorry, no suitable recommendation found.")

def random_outfit():
    """Generate a random outfit suggestion."""
    print("\n===== Random Outfit (Style Companion) =====")
    print("Generating a random outfit for you...")

    occasions = list(outfit_suggestions.keys())
    weathers = ["Cold", "Hot", "Cloudy", "Rainy"]

    random_occasion = random.choice(occasions)
    random_weather = random.choice(weathers)

    print(f"\nRandom outfit for {random_occasion} occasion, {random_weather} weather:")

    wardrobe_items = get_wardrobe()
    user_items_used = False

    if wardrobe_items:
        suitable_items = [item for item in wardrobe_items
                        if random_occasion in [o.strip() for o in item["occasion"]]
                        and random_weather in [w.strip() for w in item["weather"]]]

        if suitable_items:
            tops = [item for item in suitable_items if item["type"].lower() == "top"]
            bottoms = [item for item in suitable_items if item["type"].lower() == "bottom"]
            shoes = [item for item in suitable_items if item["type"].lower() == "shoes"]

            if tops and bottoms and shoes:
                user_items_used = True
                print(f"- Top: {random.choice(tops)['color']} {random.choice(tops)['name']}")
                print(f"- Bottom: {random.choice(bottoms)['color']} {random.choice(bottoms)['name']}")
                print(f"- Shoes: {random.choice(shoes)['color']} {random.choice(shoes)['name']}")

    if not user_items_used:
        if random_occasion in outfit_suggestions and random_weather in outfit_suggestions[random_occasion]:
            for item in outfit_suggestions[random_occasion][random_weather]:
                print(f"- {item}")
        else:
            tops = ["T-shirt", "Shirt", "Sweater", "Sweatshirt"]
            bottoms = ["Jeans", "Casual pants", "Shorts"]
            shoes = ["Sneakers", "Leather shoes", "Sandals", "Boots"]
            print(f"- Top: {random.choice(tops)}")
            print(f"- Bottom: {random.choice(bottoms)}")
            print(f"- Shoes: {random.choice(shoes)}")