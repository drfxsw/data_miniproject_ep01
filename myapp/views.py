from django.shortcuts import render

# Create your views here.

# 3-2-1
def dashboard(request):

    # 5-1-1
    # 대시보드 팀별 카드 내용
    team_data = [
        {
            'title': '인구학적 정보',
            'items': ['연령', '성별', '국적'],
            'url_name': 'sol',
            'team_number': '1조',
            'members': '권다솔, 이충원'
        },
        {
            'title': '생활습관 및 건강지표', 
            'items': ['bmi', '흡연상태', '콜레스테롤 수치', '고혈압', '천식', '간경화', '기타 암'],
            'url_name': 'jong',
            'team_number': '2조',
            'members': '김종성, 신중건, 전범하'
        },
        {
            'title': '진단 및 치료정보',
            'items': ['진단일', '암 병기', '치료 시작일', '가족력', '치료 유형', '치료 종료일'],
            'url_name': 'tack',
            'team_number': '3조',
            'members': '김규택, 장태영, 하태우'
        }
    ]

    context = {
        'team_data': team_data
    }
    # 3-2-2
    return render(request, "index.html", context) # 일반적으로 가장 root에 있는 html명은 index를 사용

def sol(request):
    return render(request, "sol.html") # sol에 해당하는 html 파일을 사용

def tack(request):
    return render(request, "tack.html") # tack에 해당하는 html 파일을 사용

def jong(request):
    return render(request, "jong.html") # jong에 해당하는 html 파일을 사용

def final(request):
    return render(request, "final.html") # final에 해당하는 html 파일을 사용
