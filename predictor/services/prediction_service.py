def predict_price(
    area,
    bedrooms,
    location=None,
    property_type=None,
    bathrooms=1,
    floors=1,
    year_built=None,
    condition=None,
    garage=False,
):
    location_factors = {
        "downtown": 1.35,
        "suburbs": 1.1,
        "urban": 1.2,
        "rural": 0.85,
        "outskirts": 0.9,
    }

    property_factors = {
        "standard": 1.0,
        "villa": 1.3,
        "luxury": 1.5,
        "residential": 1.0,
        "commercial": 1.2,
    }

    condition_factors = {
        "excellent": 1.2,
        "good": 1.0,
        "fair": 0.9,
        "poor": 0.8,
    }

    location_multiplier = location_factors.get((location or "").strip().lower(), 1.0)
    property_multiplier = property_factors.get((property_type or "").strip().lower(), 1.0)
    condition_multiplier = condition_factors.get((condition or "").strip().lower(), 1.0)
    garage_multiplier = 1.1 if garage else 1.0

    current_year = 2026
    age = current_year - int(year_built) if year_built is not None else 20
    age_multiplier = max(0.75, 1 - (age * 0.008))

    base_price = (
        area * 3800
        + bedrooms * 90000
        + bathrooms * 40000
        + floors * 15000
    )

    predicted_price = (
        base_price
        * location_multiplier
        * property_multiplier
        * condition_multiplier
        * garage_multiplier
        * age_multiplier
    )

    return round(predicted_price, 2)