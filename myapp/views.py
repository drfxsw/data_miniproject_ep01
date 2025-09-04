from django.shortcuts import render
from utils.image_loader import load_images_from_static

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

    # 가설데이터 불러오기
    hypothesis_data = get_hypothesis_data('sol')

    context = {
        'hypothesis_data': hypothesis_data
    }
    return render(request, "sol.html", context) # sol에 해당하는 html 파일을 사용

def tack(request):

    # 가설데이터 불러오기
    hypothesis_data = get_hypothesis_data('tack')

    context = {
        'hypothesis_data': hypothesis_data
    }
    return render(request, "tack.html", context) # tack에 해당하는 html 파일을 사용

def jong(request):

    # 가설데이터 불러오기
    hypothesis_data = get_hypothesis_data('jong')

    context = {
        'hypothesis_data': hypothesis_data
    }
    return render(request, "jong.html", context) # jong에 해당하는 html 파일을 사용

def final(request):

    # 가설데이터 불러오기
    hypothesis_data = get_hypothesis_data('final')
    
    context = {
        'hypothesis_data': hypothesis_data
    }
    return render(request, "final.html", context) # final에 해당하는 html 파일을 사용

# 가설 데이터 분류
def get_hypothesis_data(page):
    if page == 'final':
        return hypothesis_data['final']
    elif page == 'sol':
        return hypothesis_data['sol']
    elif page == 'tack':
        return hypothesis_data['tack']
    elif page == 'jong':
        return hypothesis_data['jong']
    else:
        return []

# 가설 데이터
hypothesis_data = {
    'final': [
                {
                    'title': '가설 1', # 가설
                    'hypothesis': {
                        'h0': '귀무가설 내용',
                        'h1': '대립가설 내용'
                    },
                    'folder_path': 'images/final_page/hypothesis_01', # 이미지파일 경로
                    'images': load_images_from_static('images/final_page/hypothesis_01', 'chart'), #이미지파일경로, 파일명공통접두어
                    'results': { # 표시되는 결과
                        'p_value': '0.05',
                        '적합도': '0.95',
                        '샘플수': '100',
                    },
                    'conclusion': '가설 1의 결과는 유의미합니다.',
                    'result': '~~~~~~해서 여러모로 해봤으나 뭐 그러함'
                },
                {
                    'title': '가설 2',
                    'hypothesis': {
                        'h0': '귀무가설 내용',
                        'h1': '대립가설 내용'
                    },
                    'folder_path': 'images/final_page/hypothesis_02',
                    'images': load_images_from_static('images/final_page/hypothesis_02', 'chart'),
                    'results': {
                        'p_value': '0.02',
                        '적합도': '0.45',
                        '샘플수': '100',
                    },
                    'conclusion': '가설 2의 결과는 무의미합니다.',
                    'result': '~~~~~~해서 여러모로 해봤으나 뭐 그러함'
                },
                {
                    'title': '가설 3',
                    'hypothesis': {
                        'h0': '귀무가설 내용',
                        'h1': '대립가설 내용'
                    },
                    'folder_path': 'images/final_page/hypothesis_03',
                    'images': load_images_from_static('images/final_page/hypothesis_03', 'chart'),
                    'results': {
                        'p_value': '0.03',
                        '적합도': '0.78',
                        '샘플수': '100',
                    },
                    'conclusion': '가설 3의 결과는 유의미합니다.',
                    'result': '~~~~~~해서 여러모로 해봤으나 뭐 그러함'
                }
            ],
    'sol': [
                {
                    'title': '가설 1',
                    'hypothesis': {
                        'h0': '귀무가설 내용',
                        'h1': '대립가설 내용'
                    },
                    'folder_path': 'images/sol_page/hypothesis_01',
                    'images': load_images_from_static('images/sol_page/hypothesis_01', 'chart'),
                    'results': {
                        'p_value': '0.05',
                        '적합도': '0.95',
                        '샘플수': '100',
                    },
                    'conclusion': '가설 1의 결과는 유의미합니다.',
                    'result': '~~~~~~해서 여러모로 해봤으나 뭐 그러함'
                },
            ],
    'jong': [
        {
            'title': '고혈압은 폐암 생존율에 영향을 미친다',
            'folder_path': 'images/jong_page/hypothesis_01',
            'images': load_images_from_static('images/jong_page/hypothesis_01', 'chart'),
            'results': {
                'p_value': '0.0477',
                '적합도': '0.7803',
                '샘플수': '3,250,000',
            },
            'conclusion': '고혈압은 폐암 생존율과 연관성이 있다.'
        },
        {
            'title': '다른 암은 폐암 생존율에 영향을 미친다',
            'folder_path': 'images/jong_page/hypothesis_02',
            'images': load_images_from_static('images/jong_page/hypothesis_02', 'chart'),
            'results': {
                'p_value': '0.026',
                '적합도': '0.7803',
                '샘플수': '3,250,000',
            },
            'conclusion': '다른 암 보유 여부는 폐암 생존율과 연관성이 있다.'
        },
    ],
    'tack': [
                {
                    'title': '가설 1',
                    'hypothesis': {
                                'h0': '귀무가설 내용',
                                'h1': '대립가설 내용'
                            },
                    'folder_path': 'images/tack_page/hypothesis_01',
                    'images': load_images_from_static('images/tack_page/hypothesis_01', 'chart'),
                    'results': {
                        'p_value': '0.05',
                        '적합도': '0.95',
                        '샘플수': '100',
                    },
                    'conclusion': '가설 1의 결과는 유의미합니다.',
                    'result': '~~~~~~해서 여러모로 해봤으나 뭐 그러함'
                },
    ]
}