import wardrobe
import recommendation

def main():
    while True:
        print("\n===== Style Companion =====")
        print("1. Wardrobe Management")
        print("2. Outfit Recommendation")
        print("3. Random Outfit")
        print("0. Exit")

        choice = input("Please select an option (0-3): ")

        if choice == "1":
            wardrobe.manage_wardrobe()
        elif choice == "2":
            recommendation.recommend_outfit()
        elif choice == "3":
            recommendation.random_outfit()
        elif choice == "0":
            print("Thank you for using Style Companion! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()