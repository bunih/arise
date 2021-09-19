from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.views import View


class LoginView(View):
    template_name = 'accounts/login.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(f"user is {user}")
        if user is None:
            messages.error(self.request, 'invalid credentials')
            return render(self.request, self.template_name)
        else:
            auth.login(self.request, user)
            messages.success(
                self.request, f'Login as {self.request.user} successfully!')
            return redirect('home:welcome')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        gender = request.POST['gender']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already exist ')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email Already exist ')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                    auth.login(request, user)
                    messages.success(request, 'login successfully!')
                    if gender == '1':
                        my_status = 'Mr'
                        Profile.objects.create(
                            user_id=request.user.id, profile='images/users/default/he.png', status=my_status)
                        return redirect('administrator:start')

                    elif gender == '2':
                        my_status = 'Miss'
                        Profile.objects.create(
                            user_id=request.user.id, profile='images/users/default/she.png', status=my_status)
                        return redirect('administrator:start')

        else:
            messages.error(request, "Password doesn't match")
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'Logout successfully!')
    return redirect('login')


def profile(request):
    if request.method == 'POST':

        upload = request.FILES['upload']
        status = request.POST['status']
        if 'upload' in request.FILES:

            Profile.objects.filter(user_id=request.user.id).delete()
            Profile.objects.create(
                user_id=request.user.id, profile=upload, status=status)
            messages.success(request, 'Profile Updated successfully!')
            return redirect('profile')

    else:

        return render(request, 'accounts/profile.html')


def reset(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            username_only = User.objects.get(username=username)
            username_only.set_password('abgoogle')
            username_only.save()
            messages.success(request, 'Password Reset Successfully!')
            return redirect('login')

        else:
            messages.error(request, "Username doesn't exist !")
            return redirect('reset')

    else:
        return render(request, 'accounts/reset.html')
