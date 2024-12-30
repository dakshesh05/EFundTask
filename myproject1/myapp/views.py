from django.shortcuts import render
from django.template import engines
from django.conf import settings

def my_view(request):
    print(engines['django'].engine.dirs)  # This will print the template directories
    # your view logic here
    return render(request, 'your_template.html')

print("Template directories:", settings.TEMPLATES[0]['DIRS'])
def chat_room(request, room_name):
    return render(request, 'chat_room.html', {'room_name': room_name})
def login_view(request):
    return render(request, 'login.html')