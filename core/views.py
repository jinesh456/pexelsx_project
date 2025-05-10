from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm, SignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import PhotoForm
from django.db.models import Q

def like_photo(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    Like.objects.create(user=request.user, photo=photo)
    return redirect('home')

def search(request):
    query = request.GET.get('q', '')
    photos = Photo.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_results.html', {'photos': photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'core/home.html', {'photos': photos})

@login_required
def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('home')
    else:
        form = PhotoForm()
    return render(request, 'core/upload.html', {'form': form})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'core/photo_detail.html', {'photo': photo})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def profile_view(request):
    user_photos = Photo.objects.filter(user=request.user)
    return render(request, 'core/profile.html', {'photos': user_photos})

def search_view(request):
    query = request.GET.get('q')
    results = Photo.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(tags__icontains=query)
    )
    return render(request, 'core/search.html', {'photos': results, 'query': query})
