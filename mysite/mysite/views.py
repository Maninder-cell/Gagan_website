from django.http import HttpResponse
from django.shortcuts import render
from .settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def index(request):
    return render(request,"main_web.html")

def send_message(request):
    user_message=request.POST.get('my_message','default')
    user_name=request.POST.get('username')
    number=request.POST.get('number_')
    email=request.POST.get('email_')
    full_message=f"""
                    Someone Responed On Your Website\n
                    Name={user_name}
                    Number={number}
                    Email={email}
                    Message={user_message}
                    """
    if len(str(number))==10:
        send_mail("",full_message,EMAIL_HOST_USER,["manindermatharu65@gmail.com"],fail_silently=False)
        return render(request,"send_msg.html")
    else:
        return render(request,"no_send_msg.html")