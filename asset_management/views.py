from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Asset
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.db import IntegrityError


def landing_page(request):
    return render(request, 'landing_page.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.save()
            return redirect('assigned_assets')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

@login_required()
@csrf_exempt 
def assigned_assets(request):
    user = request.user
    assets = Asset.objects.filter(assigned_to=user)
    return render(request, 'assigned_assets.html', {'assets': assets})

def choose_page(request):
    return render(request, 'choose_page.html')

class LogoutView(LogoutView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)

@login_required()
@csrf_exempt 
def asset_details(request, barcode):
    asset = get_object_or_404(Asset, barcode=barcode)
    context = {
        'asset': asset,
    }
    return render(request, 'asset_details.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user.username = username
            user.set_password(password)
            user.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('user_login')
        else:
            messages.error(request, "Passwords don't match.")
    
    return render(request, 'edit_profile.html')

