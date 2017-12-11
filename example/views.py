from django.shortcuts import render

def home(request):
    query=request.GET.get('name')
    template='home.html'
    context={'title':'home','message':'Hello, {} from context'.format(query)}
    return render(request,template,context)