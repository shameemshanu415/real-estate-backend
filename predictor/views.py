from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .services.prediction_service import predict_price
from .chatbot.gemini import generate_response
from .models import Prediction, ChatHistory


# 🔮 PREDICTION + SAVE
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def predict(request):
    area = request.data.get('area')
    bedrooms = request.data.get('bedrooms')
    bathrooms = request.data.get('bathrooms')
    floors = request.data.get('floors')
    year_built = request.data.get('year_built')
    condition = request.data.get('condition')
    garage = request.data.get('garage')
    location = request.data.get('location')
    property_type = request.data.get('property_type')

    if not all([area, bedrooms, bathrooms, floors, year_built, condition, garage, location, property_type]):
        return Response({"error": "Missing data"}, status=400)

    try:
        area = float(area)
        bedrooms = int(bedrooms)
        bathrooms = int(bathrooms)
        floors = int(floors)
        year_built = int(year_built)
    except ValueError:
        return Response({"error": "Invalid input type"}, status=400)

    garage_flag = str(garage).strip().lower() in ["yes", "true", "1", "y"]

    price = predict_price(
        area,
        bedrooms,
        location=location,
        property_type=property_type,
        bathrooms=bathrooms,
        floors=floors,
        year_built=year_built,
        condition=condition,
        garage=garage_flag,
    )

    # SAVE to DB
    Prediction.objects.create(
        user=request.user,
        area=area,
        bedrooms=bedrooms,
        bathrooms=bathrooms,
        floors=floors,
        year_built=year_built,
        condition=condition,
        garage=garage_flag,
        location=location,
        property_type=property_type,
        predicted_price=price
    )

    return Response({
        "predicted_price": price
    })


# 🤖 CHATBOT
@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message", "")

            if message == "":
                return JsonResponse({"error": "Message is empty"}, status=400)

            # Get Gemini response
            reply = generate_response(message)

            # Save chat history if user is authenticated
            if request.user.is_authenticated:
                ChatHistory.objects.create(
                    user=request.user,
                    message=message,
                    response=reply
                )
            else:
                ChatHistory.objects.create(
                    user=None,
                    message=message,
                    response=reply
                )

            return JsonResponse({
                "user_message": message,
                "bot_response": reply
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)

