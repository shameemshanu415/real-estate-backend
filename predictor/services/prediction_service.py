def predict_price(area, bedrooms, location=None, property_type=None):
    # Apply simple weighting factors for location and property type
    location_factors = {
        "downtown": 1.35,
        "suburbs": 1.0,
        "outskirts": 0.85,
    }

    property_factors = {
        "residential": 1.0,
        "commercial": 1.2,
        "luxury": 1.5,
    }

    base_price = area * 4500 + bedrooms * 110000
    location_multiplier = location_factors.get((location or "").lower(), 1.0)
    property_multiplier = property_factors.get((property_type or "").lower(), 1.0)

    return round(base_price * location_multiplier * property_multiplier, 2)