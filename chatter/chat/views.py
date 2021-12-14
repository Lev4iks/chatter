from django.shortcuts import render

from .models import Message


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    username = request.GET.get('username', 'AMOGUS')
    messages = Message.objects.filter(room=room_name)[:30]
    context = {
        'room_name': room_name,
        'username': username,
        'messages': messages
    }

    return render(request, 'chat/room.html', context)
