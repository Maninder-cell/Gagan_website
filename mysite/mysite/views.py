from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"main_web.html")

def send_message(request):
    message=request.POST.get('my_message','default')
    user_name=request.POST.get('username')
    number=request.POST.get('number_')
    email=request.POST.get('email_')
    data=[message,user_name,number,email]
    if all([len(i) for i in data])>0:
        print(message)
        return render(request,"send_msg.html")
    else:
        return render(request,"no_send_msg.html")