from django.shortcuts import redirect

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # التأكد من أن اسم الرابط هنا هو 'login'
        return view_func(request, *args, **kwargs)
    return _wrapped_view