from django.shortcuts import render

def home(request):
    template='home.html'
    context={'title':'home','message':'Hello from context'}
    return render(request,template,context)