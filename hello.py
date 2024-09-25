from typing import List
import ell

ell.init(store="./logs", autocommit=True, verbose=True)


@ell.simple(model="gpt-4o-mini", temperature=1.0)
def generate_city_ideas():
    """You are an expert travel advisor. Only answer with a single city name."""
    return "Generate a random city name for travel."


@ell.simple(model="gpt-4o-mini", temperature=1.0)
def generate_activity_ideas(city: str):
    """You are an expert local guide. Suggest activities in a single sentence."""
    return f"Suggest an interesting activity in {city}."


@ell.simple(model="gpt-4o-mini", temperature=1.0)
def create_daily_itinerary(city: str, activity: str):
    """You are an adept travel planner. The itinerary should cover 3 days."""
    return f"Create a 3-day itinerary for {city}, including {activity}."


@ell.simple(model="gpt-4o", temperature=0.1)
def choose_best_itinerary(itineraries: List[str]):
    """You are an expert travel editor."""
    return (
        f"Choose the best itinerary from the following list: {'\n'.join(itineraries)}."
    )


@ell.simple(model="gpt-4-turbo", temperature=0.2)
def create_final_travel_itinerary():
    """You are an expert travel writer that writes in a concise, informative style."""
    # Note: You can pass in api_params to control the language model call
    # in the case n = 4 tells OpenAI to generate a batch of 4 outputs.
    cities = generate_city_ideas(api_params=dict(n=4))

    activities = [generate_activity_ideas(city) for city in cities]
    itineraries = [
        create_daily_itinerary(city, activity)
        for city, activity in zip(cities, activities)
    ]

    best_itinerary = choose_best_itinerary(itineraries)

    return f"Refine and format this travel itinerary: {best_itinerary}"


final_itinerary = create_final_travel_itinerary()
