from django.shortcuts import render

# main
def index(request):
    return render(request,'main/index.html')
