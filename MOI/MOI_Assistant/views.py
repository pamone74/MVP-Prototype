from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Consumers
import requests
import time
from datetime import datetime
from django.shortcuts import render
from django.http import StreamingHttpResponse





# This is the chat view function that is used to handle the chat messages from the user and return the response from the MOI Assistant.


@csrf_exempt
def chat_view(request):
    if request.method == 'POST':
        message = request.POST.get('msg', '')
        try:
            rasa_response = requests.post('http://localhost:50055/webhooks/rest/webhook', json={"sender": "user", "message": message})
            rasa_response.raise_for_status()
            if not rasa_response.json():
                return JsonResponse({"response": "I am sorry, I could not understand that."})
            moi_assistant_response = ""
            object_user = Consumers.objects.get(id=2)

            for response in rasa_response.json():
                moi_assistant_response += handle_response(response, object_user) + "\n"

            return JsonResponse({"response": moi_assistant_response})

        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": str(e)})

    return HttpResponseBadRequest("Invalid request method or data")

# This function is used to handle the response from the MOI Assistant and return the appropriate response to the user.

def handle_response(response, object_user):
    text = response["text"]
    if text == "Check_fines":
        return check_fines(object_user)
    elif text == "Check_criminal_record_certificate":
        return check_criminal_record(object_user)
    elif text == "driving_license":
        return check_driving_license(object_user)
    elif text == "renew_vehicle_registration":
        return renew_vehicle_registration(object_user)
    elif text == "pay_vehicle_registration":
        return pay_vehicle_registration(object_user)
    elif text == "renew_driving_license":
        return renew_driving_license(object_user)
    elif text in ["pay_now", "pay_fines"]:
        return pay_fines(object_user)
    elif text == "pay_criminal_record_certificate":
        return pay_criminal_record_certificate(object_user)
    else:
        return text

# These functions are used to check the user's fines, criminal record, driving license, vehicle registration, and provide the appropriate response.

def check_fines(user):
    if user.traffic_fine == "No fines":
        return "You have no fines"
    else:
        return f"You have {user.traffic_fine} AED. Do you want to proceed to Pay? Please Note: you will be redirected for payment. Just say [yes pay]"

def check_criminal_record(user):
    if user.criminal_record_certificate == "No criminal record":
        return "You have no criminal record"
    else:
        return f"You have {user.criminal_record_certificate}" 

def check_driving_license(user):
    if user.driver_license < time.strftime('%Y-%m-%d'):
        return f"Your driving License {user.driver_license} has expired on {user.drivers_expiry_date}. Do you want to renew? Please Note: you will be redirected for renewal"
    elif not user.driver_license:
        return "You do not have a driver's license. Do you want to apply for one? Please Note: you will be redirected for application"
    else:
        return "Your driver's license is still valid"

def renew_vehicle_registration(user):
    if user.vehicle_registration_expiry_date < datetime.now().date():
        return f"Your vehicle registration {user.vehicle_registration} has expired on {user.vehicle_registration_expiry_date}. Do you want to renew? Please Note: you will be redirected for renewal"
    elif not user.vehicle_registration:
        return "You do not have a vehicle registration. Do you want to apply for one? Please Note: you will be redirected for application"
    else:
        return "Your vehicle registration is still valid"

def pay_vehicle_registration(user):
    if user.vehicle_registration_expiry_date < datetime.now().date() or not user.vehicle_registration:
        return "Redirecting to payment page"
    else:
        return "Your vehicle registration is still valid"

def renew_driving_license(user):
    if user.driver_license < time.strftime('%Y-%m-%d') or not user.driver_license:
        return "Redirecting to renewal page"
    else:
        return "Your driver's license is still valid"

def pay_fines(user):
    if user.traffic_fine == "No fines":
        return "You have no fines to pay"
    else:
        return "Redirecting to payment page"

def pay_criminal_record_certificate(user):
    if user.criminal_record_certificate == "No criminal record":
        return "You have no criminal record to pay"
    else:
        return "Redirecting to payment page"


# These functions are used to render the different pages of the MOI Assistant.

def MOI_Assistant(request):
    return render(request, 'MOI_Assistant/MOI_Assistant.html')

def index(request):
    return render(request, 'MOI_Assistant/index.html')

def base(request):
    return render(request, 'MOI_Assistant/base.html')

def statistics(request):
    return render(request, 'MOI_Assistant/statistics.html')

def payment(request):
    return render(request, 'MOI_Assistant/payment.html')

def gamified(request):
    return render(request, 'MOI_Assistant/Gamified.html')