import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render



def myform_view(request):
    if request.method == 'POST':
        data = request.POST.get("data")
        file = request.FILES.get("file")

        if not file:
            return JsonResponse({"message": "No se ha seleccionado un archivo."})

        try:
            files = {"file": (file.name, file.read())}
            response = requests.post('http://127.0.0.1:5000/upload_file', data={"data": data}, files=files)
            response.raise_for_status()
            response_data = response.json()
            return JsonResponse(response_data)
        except requests.exceptions.RequestException as e:
            return HttpResponse(str(e), status=500)

    return render(request, 'myform.html')

def get_response_from_flask(request):
    try:
        response = requests.get('http://127.0.0.1:5000/flask_response')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)
    
def get_response_from_flask2(request):
    try:
        response = requests.get('http://127.0.0.1:5000/flask_response2')
        response.raise_for_status()
        response_data = response.json()
        return JsonResponse(response_data)
    except requests.exceptions.RequestException as e:
        return HttpResponse(str(e), status=500)

def pulpito_view(request):

    return render(request, 'pulpito.html')