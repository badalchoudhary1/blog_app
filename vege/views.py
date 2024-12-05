from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as loginAuth, logout as logoutAuth
from .forms import  UserProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Post
from .forms import PostForm, UserCreationForm

# Create your views here.
def login(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        db_user =  User.objects.filter(username=user_name)

        if not db_user.exists():
            messages.info(request, "Username is valid")
            return redirect("/login/")

        user = authenticate(username= user_name, password = password)

        if user is None: 
            messages.info(request, 'Invalid Cred')
            return redirect("/login/")
        else: 
            loginAuth(request, db_user[0])
            return redirect("/add-profile/")

    return render(request, "vege_login.html")

def register(request):
    if request.method ==  "POST":
        user_name = request.POST.get("user_name")

        if User.objects.filter(username = user_name).exists():
            messages.info(request, "User name already exist" )
            return redirect("/register/")

        user = User.objects.create(
            first_name = request.POST.get("first_name"),
            last_name = request.POST.get("last_name"),
            email = request.POST.get("email"),
            username = user_name,
        )

        user.set_password(request.POST.get("password"))
        user.save()
        print("user created succssfuly")
        messages.info(request, "User Created Successfuly")
        return redirect("/register/")
    else:
        return render(request, 'vege_register.html')
    
def welcome(request):
    print(request.user, 'This is requiest user')
    return render(request, "home.html")

def logout(request):
    logoutAuth(request)
    return render(request, "home.html")

def add_profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to add a profile.")
        return redirect("/login/")
    
    try:
        # Check if the user already has a profile
        UserProfile.objects.get(user=request.user)
        messages.info(request, "You already have a profile.")

        if request.method == 'POST':
            profile_form = UserProfileForm(request.POST, request.FILES)
            if profile_form.is_valid(): 
                profile = profile_form.save(commit=False) 
                profile.user = request.user  # Associate the logged-in user
                profile.save()
                messages.success(request, "Profile created successfully!")
                return redirect('user_profiles')
            else:
               messages.error(request, "Something went wrong!")
               return render(request, 'add_profile.html', {'profile_form': profile_form})
        else:
            profile_form = UserProfileForm()

        return render(request, 'add_profile.html', {'profile_form': profile_form,})
    
    except UserProfile.DoesNotExist:
        messages.info(request, "You do not have a profile")
        return redirect("user_profiles")

# View to display all profiles
def user_profiles(request):
    profiles = UserProfile.objects.select_related('user').all()
    return render(request, 'user_profiles.html', {'profiles': profiles})

# View to display all profiles
def all_user_blogs(request):
    posts = Post.objects.all()
    return render(request, 'all_user_blogs.html', {'posts': posts})

# Display user profile and their posts
@login_required
def user_profile_detail(request):
    user_profile = request.user.userprofile  # Get the logged-in user's profile
    posts = user_profile.posts.all()  # Access related posts via related_name
    return render(request, 'user_profile_detail.html', {'user_profile': user_profile, 'posts': posts})

# Create a new post
@login_required
def create_post(request):
    try:
        UserProfile.objects.get(user = request.user)
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user_profile = request.user.userprofile  # Link the post to the logged-in user's profile
                post.save()
                return redirect('user_profile_detail')
        else:
            print(vars(request.user.userprofile), 'user prfok req')
            form = PostForm()

        return render(request, 'create_post.html', {'form': form})

    except UserProfile.DoesNotExist:
        messages.error(request, "user prfile not exist")
        return render(request, 'create_post.html', {'form': PostForm(request.POST)})


   












