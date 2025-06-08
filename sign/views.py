# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import SignupForm, LoginForm
# from .models import User
#
#
# def signup_view(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         student_id = request.POST['student_id']
#         password = request.POST['password']
#
#         if User.objects.filter(student_id=student_id).exists():
#             return render(request, 'sign/signup.html', {'error': '이미 존재하는 학번입니다.'})
#
#         User.objects.create(name=name, email=email, student_id=student_id, password=password)
#
#         # ✅ 회원가입 성공 → 로그인 페이지로 redirect 하면서 쿼리스트링에 메시지 전달
#         from urllib.parse import urlencode
#         query_string = urlencode({'message': '회원가입이 완료되었습니다. 로그인 해주세요.'})
#         return redirect(f"/sign/login/?{query_string}")
#
#     return render(request, 'sign/signup.html')
#
# def login_view(request):
#     next_url = request.GET.get('next', 'club:main')
#
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=student_id, password=password)
#
#         try:
#             user = User.objects.get(student_id=student_id)
#             if user.password == password:
#                 request.session['user_name'] = user.name
#                 request.session['user_id'] = user.id
#
#                 # ✅ POST 요청에도 next 파라미터 반영
#                 next_url = request.POST.get('next') or next_url
#                 return redirect(next_url)
#             else:
#                 return render(request, 'sign/login.html', {'error': '비밀번호가 일치하지 않습니다.'})
#         except User.DoesNotExist:
#             return render(request, 'sign/login.html', {'error': '존재하지 않는 학번입니다.'})
#
#     return render(request, 'sign/login.html', {'next': next_url})
#
#
#
# def logout_view(request):
#     request.session.flush()
#     return redirect('club:main')


# sign/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages # Django messages framework를 사용하지 않으므로 주석 처리 또는 삭제
from .forms import SignupForm, LoginForm # 현재 코드에서는 forms.py를 사용하지 않으므로 필요 없다면 삭제
from .models import User
from urllib.parse import urlencode # 추가

def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        student_id = request.POST['student_id']
        password = request.POST['password']

        if User.objects.filter(student_id=student_id).exists():
            return render(request, 'sign/signup.html', {'error': '이미 존재하는 학번입니다.'})

        # ✅ User.objects.create 대신 User.objects.create_user 사용
        user = User.objects.create_user(student_id=student_id, name=name, email=email, password=password)
        # user 객체가 성공적으로 생성되었는지 확인 (선택적)
        if user:
            # 회원가입 성공 → 로그인 페이지로 redirect 하면서 쿼리스트링에 메시지 전달
            query_string = urlencode({'message': '회원가입이 완료되었습니다. 로그인 해주세요.'})
            return redirect(f"/sign/login/?{query_string}")
        else:
            # 사용자 생성 실패 시 (일반적으로 create_user에서 예외 발생 전에 처리되지만, 방어적으로)
            return render(request, 'sign/signup.html', {'error': '회원가입 중 오류가 발생했습니다.'})


    return render(request, 'sign/signup.html')

# login_view, logout_view는 제공해주신 코드가 비교적 잘 작성되어 있어 큰 수정 없이 사용할 수 있습니다.
# 다만, login_view에서 error_message를 설정하는 부분에 약간의 개선 여지가 있을 수 있습니다.

def login_view(request):
    next_url_from_get = request.GET.get('next')
    error_message = None # error_message 초기화
    if request.method == 'POST':
        student_id_input = request.POST.get('student_id')
        password_input = request.POST.get('password')
        user = authenticate(request=request, username=student_id_input, password=password_input) # request 전달 권장
        print(f"Authenticated user object: {user}") # 디버깅용
        if user is not None:
            if user.is_active:
                login(request, user) # Django 세션에 사용자 등록
                next_url_from_post = request.POST.get('next')
                default_next_url = 'club:main' # 이 URL name이 urls.py에 정의되어 있는지 확인 필요
                try:
                    from django.urls import reverse
                    # club:main이 유효한지 확인하기 위해 reverse 시도 (선택적이지만 좋은 습관)
                    reverse(default_next_url)
                except:
                    default_next_url = '/' # club:main이 없다면 루트로
                final_next_url = next_url_from_post or next_url_from_get or default_next_url
                return redirect(final_next_url)
            else:
                error_message = '비활성화된 계정입니다. 관리자에게 문의하세요.'
        else:
            # authenticate가 None을 반환한 경우 (학번 없음 또는 비밀번호 틀림)
            try:
                User.objects.get(student_id=student_id_input)
                # 학번은 존재하나 authenticate가 실패했으므로 비밀번호가 틀린 경우
                error_message = '비밀번호가 일치하지 않습니다.'
            except User.DoesNotExist:
                error_message = '존재하지 않는 학번입니다.'
            except Exception as e:
                print(f"An unexpected error occurred during login attempt: {e}")
                error_message = '로그인 중 오류가 발생했습니다. 다시 시도해주세요.'
        # 로그인 실패 시 또는 GET 요청 시 로그인 페이지 렌더링
        return render(request, 'sign/login.html', {
            'error': error_message,
            'next': next_url_from_get or 'club:main' # 'club:main'은 예시, 실제 URL로 대체
        })
    return render(request, 'sign/login.html', {
        'next': next_url_from_get or 'club:main', # 'club:main'은 예시, 실제 URL로 대체
    })


def logout_view(request):
    logout(request) # Django의 logout 함수 사용 권장
    # request.session.flush() 는 세션 전체를 비우지만, logout()은 인증 관련 세션 데이터만 제거합니다.
    # 일반적으로 logout()이 더 적절합니다.
    # 'club:main' 이 유효한 URL name인지 확인 필요
    default_redirect_url = 'club:main'
    try:
        from django.urls import reverse
        reverse(default_redirect_url)
    except:
        default_redirect_url = '/' # club:main이 없다면 루트로
    return redirect(default_redirect_url)