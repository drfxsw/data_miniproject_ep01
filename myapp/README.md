## 명명규칙
 - 폴더명 : 스네이크(snake_case)
 - python 파일 : 스네이크(snake_case)
 - html 파일 : 스네이크(snake_case)
 - python 내부 method : 스네이크(snake_case)
 - javascript method : 카멜(camelCase)

---

## 1. 프로젝트 생성
### 1-1 기본 프로젝트 어플리케이션 생성
- **1-1-1** mkdir [폴더명] - 폴더생성
- **1-1-2** 가상환경 활성화 (예시명령어 - C:/Users/acorn/anaconda3/Scripts/activate)
- **1-1-3** django-admin startproject mainapp [폴더명] - django 프로젝트 생성
- **1-1-4** cd [폴더명] - 폴더로 이동
- **1-1-5** python manage.py startapp [어플리케이션명] - 어플리케이션 추가

### 1-2 어플리케이션 실행
- **1-2-1** python manage.py migrate - (어플리케이션 초기실행 또는 데이터 변경이 있을시)
- **1-2-2** python manage.py runserver - 서버실행

## 2. 기본 설정
### 2-1 mainapp/settings.py
- **2-1-1** INSTALLED_APPS에 어플리케이션 명 추가(`1-1-4`에 사용한 어플리케이션명) 
- **2-1-2** TEMPLATES.DIRS에 [BASE_DIR / "templates"] 추가
- **2-1-3** STATIC_URL = "static/" 추가
- **2-1-4** STATICFILES_DIRS = [BASE_DIR / "static"] 추가
- **2-1-5** DATABASES변경 (필요할경우)

### 2-2 폴더추가
 - **2-2-1** templates 폴더 추가 (`2-1-2`와 폴더명 통일)
 - **2-2-2** static 폴더 추가(`2-1-4`와 폴더명 통일)

## 3. 화면연결
### 3-1 mainapp/urls.py
 - **3-1-1** 사용할 views import
 - **3-1-2** 경로에 따른 사용함수 이름 및 경로 설정

### 3-2 myapp/views.py
 - **3-2-1** `3-1-2`에서 설정한 함수 추가
 - **3-2-2** 랜더링할 html을 return

### 3-3 html파일 생성
 - **3-3-1** templates 이하에 html 파일생성 (`3-2-2`에서 사용한 파일명으로 생성)

### 3-4 html내에서 화면이동 경로 설정
 - **3-4-1** a태그 의 href

## 4. style 적용
### 4-1 전역 css파일 추가
 - **4-1-1** static/styles폴더 추가
 - **4-1-2** static/styles/[파일명].css 추가
 - **4-1-3** 추가 css파일을 main.css에 import

### 4-2 html에 외부시트 적용
 - **4-2-1** 해당 html에 경로 추가 (main.css만 추가하면 import된 다른 css파일도 읽음)
 - **4-2-2** 필요에따라 라이브러리 링크 추가

## 5. 모델링 추가