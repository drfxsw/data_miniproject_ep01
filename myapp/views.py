from django.shortcuts import render

# Create your views here.

# 3-2-1
def dashboard(request):

    # 3-2-2
    return render(request, "index.html") # 일반적으로 가장 root에 있는 html명은 index를 사용

def sol(request):
    return render(request, "sol.html") # sol에 해당하는 html 파일을 사용

def tack(request):
    return render(request, "tack.html") # tack에 해당하는 html 파일을 사용

def jong(request):
    return render(request, "jong.html") # jong에 해당하는 html 파일을 사용

def final(request):
    return render(request, "final.html") # final에 해당하는 html 파일을 사용