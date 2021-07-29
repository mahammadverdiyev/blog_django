from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    data = [
        'Learn java',
        'Learn unity',
        'Learn Spring',
        'Learn Swing',
        'Learn Python',
        'Learn C#',
        'Learn Django',
    ]
    
    return render(request,'about.html',{'items':data})

    