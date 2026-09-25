"""A beginner-friendly console program for planning travel costs."""


def get_positive_integer(prompt):
    """Ask for a whole number greater than zero."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def get_non_negative_float(prompt):
    """Ask for a number that is zero or greater."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Cost cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_transportation_cost(number_of_travelers, cost_per_traveler):
    """Return the total transportation cost for all travelers."""
    return number_of_travelers * cost_per_traveler


def calculate_hotel_cost(number_of_days, hotel_cost_per_day):
    """Return the total hotel cost for the trip."""
    return number_of_days * hotel_cost_per_day


def calculate_hotel_food_cost(number_of_travelers, number_of_days):
    """Return the estimated hotel food cost.

    The estimate uses a simple built-in assumption of $25 per traveler per day.
    """
    food_cost_per_traveler_per_day = 25.00
    return number_of_travelers * number_of_days * food_cost_per_traveler_per_day


def calculate_activity_cost(number_of_travelers, activity_cost_per_traveler):
    """Return the total activity cost for all travelers."""
    return number_of_travelers * activity_cost_per_traveler


def calculate_overall_trip_cost(
    transportation_cost, hotel_cost, hotel_food_cost, activity_cost
):
    """Return the complete cost of the trip."""
    return transportation_cost + hotel_cost + hotel_food_cost + activity_cost


def calculate_cost_per_traveler(overall_trip_cost, number_of_travelers):
    """Return the average trip cost for one traveler."""
    return overall_trip_cost / number_of_travelers


def calculate_average_daily_cost(overall_trip_cost, number_of_days):
    """Return the average trip cost for one day."""
    return overall_trip_cost / number_of_days


def display_travel_summary(travel_information, costs):
    """Display the collected travel information and calculated costs."""
    print("\n" + "=" * 48)
    print("SMART TRAVEL PLANNER - TRAVEL SUMMARY")
    print("=" * 48)
    print(f"Traveler name       : {travel_information['traveler_name']}")
    print(f"Destination         : {travel_information['destination']}")
    print(f"Number of travelers : {travel_information['number_of_travelers']}")
    print(f"Number of days      : {travel_information['number_of_days']}")
    print("-" * 48)
    print(f"Transportation cost : ${costs['transportation']:,.2f}")
    print(f"Hotel cost          : ${costs['hotel']:,.2f}")
    print(f"Hotel food cost     : ${costs['hotel_food']:,.2f}")
    print(f"Activity cost       : ${costs['activity']:,.2f}")
    print("-" * 48)
    print(f"Overall trip cost   : ${costs['overall']:,.2f}")
    print(f"Cost per traveler   : ${costs['per_traveler']:,.2f}")
    print(f"Average daily cost  : ${costs['daily_average']:,.2f}")
    print("=" * 48)


def main():
    """Collect trip details, calculate costs, and show the summary."""
    print("Welcome to Smart Travel Planner!")
    print("Enter your trip details below.\n")

    traveler_name = input("Traveler name: ").strip()
    while not traveler_name:
        print("Traveler name cannot be empty.")
        traveler_name = input("Traveler name: ").strip()

    destination = input("Destination: ").strip()
    while not destination:
        print("Destination cannot be empty.")
        destination = input("Destination: ").strip()

    number_of_travelers = get_positive_integer("Number of travelers: ")
    number_of_days = get_positive_integer("Number of travel days: ")
    transportation_cost_per_traveler = get_non_negative_float(
        "Transportation cost per traveler: $"
    )
    hotel_cost_per_day = get_non_negative_float("Hotel cost per day: $")
    activity_cost_per_traveler = get_non_negative_float(
        "Activity cost per traveler: $"
    )

    travel_information = {
        "traveler_name": traveler_name,
        "destination": destination,
        "number_of_travelers": number_of_travelers,
        "number_of_days": number_of_days,
    }

    transportation_cost = calculate_transportation_cost(
        number_of_travelers, transportation_cost_per_traveler
    )
    hotel_cost = calculate_hotel_cost(number_of_days, hotel_cost_per_day)
    hotel_food_cost = calculate_hotel_food_cost(number_of_travelers, number_of_days)
    activity_cost = calculate_activity_cost(
        number_of_travelers, activity_cost_per_traveler
    )
    overall_trip_cost = calculate_overall_trip_cost(
        transportation_cost, hotel_cost, hotel_food_cost, activity_cost
    )

    costs = {
        "transportation": transportation_cost,
        "hotel": hotel_cost,
        "hotel_food": hotel_food_cost,
        "activity": activity_cost,
        "overall": overall_trip_cost,
        "per_traveler": calculate_cost_per_traveler(
            overall_trip_cost, number_of_travelers
        ),
        "daily_average": calculate_average_daily_cost(
            overall_trip_cost, number_of_days
        ),
    }

    display_travel_summary(travel_information, costs)


if __name__ == "__main__":
    main()