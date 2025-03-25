# from django.shortcuts import render
# from django.http import JsonResponse
# from .utils.chat import chatbot_response  

# def chatbot_view(request):
#     if request.method == "POST":
#         import json
#         data = json.loads(request.body)
#         text = data.get("message", "")

#         response = chatbot_response(text)
#         return JsonResponse({"answer": response})
    
#     return JsonResponse({"message": "This is the chatbot endpoint."})

# from django.shortcuts import render
# from django.http import JsonResponse
# from .utils.chat import chatbot_response  

# def chatbot_view(request):
#     if request.method == "POST":
#         import json
#         data = json.loads(request.body)
#         text = data.get("message", "")

#         response = chatbot_response(text)
#         return JsonResponse({"answer": response})
    
#     return render(request, "chatbot.html")

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# import json
# from .utils.chat import chatbot_response  

# @csrf_exempt  # Disable CSRF for testing
# def chatbot_view(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             text = data.get("message", "")

#             print("Received message:", text)  # Debugging log

#             response = chatbot_response(text)
#             print("Chatbot response:", response)  # Debugging log

#             return JsonResponse({"answer": response}, safe=False)
#         except Exception as e:
#             print("Error:", str(e))  # Debugging log
#             return JsonResponse({"error": "Something went wrong!"}, status=500)

#     return render(request, "chatbot.html")

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils.chat import chatbot_response  

@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            text = data.get("message", "")

            if not text:
                return JsonResponse({"error": "Empty message"}, status=400)

            response = chatbot_response(text)
            return JsonResponse({"answer": response})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, "chatbot.html")  # Load the frontend HTML

