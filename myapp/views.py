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
                    'title': '가설 1. 나이가 어릴수록 폐암사망률이 높다',
                    'hypothesis': {
                        'h0': '나이가 어릴수록 사망률이 높다',
                        'h1': '나이가 어릴수록 사망률이 높지않다'
                    },
                    'folder_path': 'images/sol_page/hypothesis_01',
                    'images': load_images_from_static('images/sol_page/hypothesis_01', 'chart'),
                    'results': {
                        '카이제곱': '6.9508',
                        'p_value': '0.05',
                        '샘플수': '3,250,000',
                        '정밀도': '0.0',
                        '재현율': '0.0',
                        'f1-score': '0.0'
                    },
                    'conclusion': '나이 그룹과 사망 여부는 관련이 없다고 볼 수 있음. (유의미하지 않음)',
                    'result': '카이제곱 검정 결과에 따르면, 나이와 폐암 사망률 간에는 유의미한 연관성이 없다고 판단됨. (p = 0.5419 > 0.05)\n'
                              '머신러닝 평가 지표에서도 나이 그룹만으로는 사망 여부를 예측할 수 없는 수준임. (정밀도/재현율 = 0)\n'
                              '따라서, "나이가 어릴수록 폐암 사망률이 높다"는 가설은 통계적 근거가 없으며 기각되어야 함.'
                },
            {
                    'title': '가설 2. 남성이 폐암사망률이 더 높다',
                    'hypothesis': {
                        'h0': '남성이 사망률이 더 높다',
                        'h1': '남성이 사망률이 더 높지않다'
                    },
                    'folder_path': 'images/sol_page/hypothesis_02',
                    'images': load_images_from_static('images/sol_page/hypothesis_02', 'chart'),
                    'results': {
                        '카이제곱': '0.0003',
                        'p_value': '0.9853',
                        '샘플수': '3,250,000',
                        '정밀도': '0.0',
                        '재현율': '0.0',
                        'f1-score': '0.0'
                    },
                    'conclusion': '남성과 여성의 사망률 차이는 의미 없다고 볼 수 있음 (유의미하지 않음)',
                    'result': '통계적 검정 결과와 머신러닝 평가 결과 모두 “남성이 폐암 사망률이 높다”는 가설을 지지하지 못함\n'
                              '성별과 폐암 사망률 간에 유의미한 차이가 없음\n'
                              '성별에 따른 폐암 사망률 차이가 있는지 알아보기 위해서는 더 많은 데이터 혹은 다른 위험 요인(흡연, 직업, 건강 상태 등)을 함께 고려하는 분석이 필요해 보임'
                },
            {
                    'title': '가설 3. 서유럽이 다른 지역에 비해 폐암사망률이 더 높다',
                    'hypothesis': {
                        'h0': '서유럽 환자들이 북유럽, 동유럽, 남유럽 환자들보다 사망률이 더 높다',
                        'h1': '서유럽 환자들이 북유럽, 동유럽, 남유럽 환자들보다 사망률이 더 높지 않다'
                    },
                    'folder_path': 'images/sol_page/hypothesis_03',
                    'images': load_images_from_static('images/sol_page/hypothesis_03', 'chart'),
                    'results': {
                        '카이제곱': '22.1118',
                        'p_value': '0.6826',
                        '샘플수': '3,250,000',
                        '정밀도': '0.0',
                        '재현율': '0.0',
                        'f1-score': '0.0'
                    },
                    'conclusion': '유럽의 지역 그룹(동, 서, 남, 북) 간의 사망률 차이는 통계적으로 유의미하지 않음',
                    'result': '통계적 검정과 분류 평가 결과 모두 “서유럽이 폐암 사망률이 가장 높다”는 가설을 지지하지 않는다는 결론이 나옴\n'
                              '유럽 내 지역 그룹과 폐암 사망률 간에 통계적으로 유의미한 차이가 없으며, 제조업 발달 정도가 폐암 사망률에 미치는 영향이 명확하게 확인되지 않음\n'
                              '폐암 사망률에 영향을 미치는 요인은 제조업 외에도 다양한 환경적, 개인적 요인이 있을 수 있으므로, 추가적인 변수와 심층적인 분석이 필요해 보임'
                },
            ],
    'jong': [
        {
            'title': '가설 1. 고혈압은 폐암 생존율에 영향을 미친다',
            'hypothesis': {
                        'h0': '고혈압은 폐암 생존율에 영향을 미친다',
                        'h1': '고혈압은 폐암 생존율에 영향을 미치지 않는다'
                    },
            'folder_path': 'images/jong_page/hypothesis_01',
            'images': load_images_from_static('images/jong_page/hypothesis_01', 'chart'),
            'results': {
                '카이제곱': '3.92',
                'p_value': '0.0477',
                '샘플수': '3,250,000',
                '정밀도': '0.0',
                '재현율': '0.0',
                'f1-score': '0.0'
            },
            'conclusion': '고혈압은 폐암 생존율과 연관성이 있다.',
            'result': '카이제곱 검정 결과에 따르면, 고혈압과 폐암 사망률 간에는 유의미한 연관성이 있다고 판단됨. (p = 0.0477 < 0.05)\n'
                      '머신러닝 평가 지표에서도 나이 그룹만으로는 사망 여부를 예측할 수 없는 수준임. (정밀도/재현율 = 0)\n'
                      '따라서, "고혈압이 있으면 사망률이 높다"라는 가설은 통계적 근거가 없으며 기각되어야 함'
        },
        {
            'title': '가설 2. 다른 암 보유 여부는 폐암 생존율에 영향을 미친다',
            'hypothesis': {
                    'h0': '다른 암 보유는 폐암 생존율에 영향을 미치지 않는다',
                    'h1': '다른 암 보유는 폐암 생존율에 영향을 미친다'
                    },
            'folder_path': 'images/jong_page/hypothesis_02',
            'images': load_images_from_static('images/jong_page/hypothesis_02', 'chart'),
            'results': {
                '카이제곱': '4.944',
                'p_value': '0.026',
                '샘플수': '3,250,000',
                '정밀도': '0.2194',
                '재현율': '0.2264',
                'f1-score': '0.2228'
            },
            'conclusion': '다른 암 보유 여부는 폐암 생존율과 연관성이 있다.',
            'result': '즉, 다른 암을 보유한 환자가 생존할 가능성이 낮다고 볼 수 있음\n'
                      '머신러닝 관점에서는, other_cancer 단일 변수만으로는 생존 여부를 예측하는 데 한계가 존재하며, 더 많은 임상 변수와 결합해야 모델 성능이 향상될 수 있음\n'
                      '위험도 분석 결과, 실제 사망률 차이는 크지 않지만, 대규모 데이터에서는 미세한 차이도 통계적으로는 유의미할 수 있음'
        },
        {
            'title': '가설 3. BMI 수치는 폐암 생존율에 영향을 미친다',
            'hypothesis': {
                    'h0': 'BMI 수치와 폐암 사망률과 관련없다',
                    'h1': 'BMI 수치와 폐암 사망률과 관련있다'
                    },
            'folder_path': 'images/jong_page/hypothesis_03',
            'images': load_images_from_static('images/jong_page/hypothesis_03', 'chart'),
            'results': {
                '카이제곱': '1.9348',
                'p_value': '0.8581',
                '샘플수': '3,250,000',
                '정밀도': '0.0',
                '재현율': '0.0',
                'f1-score': '0.0'
            },
            'conclusion': 'BMI 수치와 생존여부 사이에는 통계적으로 유의한  연관성이 없다',
            'result': '카이제곱 검정 결과에 따르면 Bmi와 폐암사망률은 서로 연관성이 존재하지 않는다(p = 0.8581 > 0.05)\n'
                      '로지스틱회귀 모델에서도 Bmi만으로는 사망 여부를 예측할수없다는 결론이 도출됨\n'
                      '따라서, "BMI 수치가 높을수록 폐암 사망률이 높다"는 가설은 기각되어야 함\n'
                      '이러한 결과를 보았을 때 다른 변수 즉 환경이나 유전적인 요인이 폐암 사망률을 높인다고 생각됨'

        }
    ],
    'tack': [
                {
                    'title': '가설1: 기존 건강상태(폐암 외의 암, 고혈압)가 폐암 환자의 생존률에 영향을 준다.',
                    'hypothesis': {
                                'h0': '환자들의 기존 건강상태(폐암 외의 암, 고혈압)은 폐암에 의한 생존률에 독립적이다.',
                                'h1': '환자들의 폐암 생존률은 환자의 기존 건강상태에 따라 좌우된다.'
                            },
                    'folder_path': 'images/tack_page/hypothesis_01',
                    'images': load_images_from_static('images/tack_page/hypothesis_01', 'chart'),
                    'results': {
                        'other_cancer': '0.258  >  0.05',
                        'hypertension': ' 0.086  >  0.05',
                        '상호작용': ' 0.491  >  0.05',
                    },
                    'conclusion': '환자의 기저질환은 폐암 생존률에 영향을 끼치지 못한다.',
                    'result': 'ANOVA 검정 결과에 따르면, 고혈압(hypertension)은 유의수준 0.05에 근사한 값으로 여겨 그 종속변수(survived)와의 종속성을 용인할 수 있겠지만, 보수적인 시점에서는 독립적임으로 판단해야 합니다.따라서, 폐암 외의 질병(other_cancer)과 고혈압(hypertension)은 단원제 혹은 다원제의 상황 모두 대립가설을 기각하고 귀무가설을 채택합니다.'
                },

                {
                    'title': '가설2: 암 진단으로부터 최초 치유 착수기간이 짧을수록 환자의 생존율이 높다.',
                    'hypothesis': {
                                'h0': ' 환자들의 최초 암 진단으로부터 치유기간과, 발견한 암 단계는 생존률에 영향을 끼친다.',
                                'h1': '환자들의 폐암 생존율은 최초 암의 단계와 그 정체 발견에 달려있다.'
                            },
                    'folder_path': 'images/tack_page/hypothesis_01',
                    'images': load_images_from_static('images/tack_page/hypothesis_02', 'chart'),
                    'results': {
                        'initiate_treatment_days': '0.208  >  0.05',
                        'cancer_stage': '0.943  >  0.05',
                        '상호작용': '0.515  >  0.05',
                    },
                    'conclusion': '환자의 생존률, 암 진단으로부터 치유 개시 시간은 환자의 폐암 생존율에 영향을 끼치지 못한다.',
                    'result': 'ANOVA 검정 결과에 따라 대립가설을 기각하고, 환자의 생존율(survived)은 치유착수기간(initiate_treatment_days)이나 진단받은 암의 기수(cancer_stage)와는 “상관관계가 없음”을 알 수 있다.'
                },
    ]
}