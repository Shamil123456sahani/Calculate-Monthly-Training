# Program to calculate training fees for North Sussex Judo athletes

# Constants for prices
BEGINNER_FEE = 2000
INTERMEDIATE_FEE = 5000
ELITE_FEE = 7000
PRIVATE_COACHING_FEE = 500
COMPETITION_FEE = 2500

# List of weight categories and their upper limits
weight_categories = [
    ("Heavyweight", float('inf')),
    ("Light-Heavyweight", 100),
    ("Middleweight", 90),
    ("Light-Middleweight", 81),
    ("Lightweight", 73),
    ("Flyweight", 66)
]

def get_training_fee(plan):
    """
    Returns the training fee based on the athlete's plan.
    """
    if plan == "Beginner":
        return BEGINNER_FEE
    elif plan == "Intermediate":
        return INTERMEDIATE_FEE
    elif plan == "Elite":
        return ELITE_FEE
    else:
        raise ValueError("Invalid training plan")

def get_weight_category(weight):
    """
    Returns the weight category based on the athlete's weight.
    """
    for category, limit in weight_categories:
        if weight <= limit:
            return category
    return "Unknown"

def calculate_total_cost(training_fee, competition_count, private_hours):
    """
    Calculates the total cost based on training fee, number of competitions,
    and hours of private coaching.
    """
    competition_cost = competition_count * COMPETITION_FEE
    private_coaching_cost = private_hours * PRIVATE_COACHING_FEE
    total_cost = training_fee + competition_cost + private_coaching_cost
    return total_cost

def main():
    """
    Main function to interact with the user and compute costs.
    """
    print("Welcome to the North Sussex Judo Fee Calculator!")
    
    # Getting user input
    name = input("Enter athlete's name: ")
    plan = input("Enter training plan (Beginner, Intermediate, Elite): ")
    weight = float(input("Enter current weight in kilograms (kg): "))
    competition_count = int(input("Enter number of competitions entered this month: "))
    private_hours = int(input("Enter number of private coaching hours (0 to 5): "))

    # Input validation
    if private_hours < 0 or private_hours > 5:
        print("Private coaching hours must be between 0 and 5.")
        return

    # Calculating fees
    try:
        training_fee = get_training_fee(plan)
    except ValueError as e:
        print(e)
        return
    
    total_cost = calculate_total_cost(training_fee, competition_count, private_hours)
    weight_category = get_weight_category(weight)

    # Displaying the results
    print("\nAthlete's Name: ", name)
    print(f"Training Plan: {plan}")
    print(f"Current Weight: {weight} kg")
    print(f"Competition Weight Category: {weight_category}")
    print(f"Breakdown of Costs:\nTraining Fee: Rs. {training_fee:.2f}")
    print(f"Competition Fees: Rs. {competition_count * COMPETITION_FEE:.2f}")
    print(f"Private Coaching Fees: Rs. {private_hours * PRIVATE_COACHING_FEE:.2f}")
    print(f"Total Cost for the Month: Rs. {total_cost:.2f}")

if __name__ == "__main__":
    main()
