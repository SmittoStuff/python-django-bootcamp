from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_content': "Welcome to lvl 2sies"}
    return render(request,'level_2_app/index.html',context=my_dict)
