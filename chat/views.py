from django.shortcuts import render
from .models import Message
# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def room_name(request, name):
    return render(request, 'chat/chatroom.html', {'room_name': name})