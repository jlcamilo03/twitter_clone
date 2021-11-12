from django.shortcuts import redirect, render
from .models import Post, Profile, relationship
from .forms import user_register_form , post_form ,user_edit,profile_edit
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    posts= Post.objects.all()
    if request.method == 'POST':
        form= post_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= request.user
            post.save()
            return redirect('home')
    else:
        form=post_form()

    context= {'posts':posts, 'form':form}
    return render(request, 'twitter/newsfeed.html',context)


def register(request):
    if request.method == 'POST':
        form= user_register_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=user_register_form()

    context ={'form':form}
    return render(request, 'twitter/register.html', context)

@login_required
def profile(request, username):
    user=User.objects.get(username=username )
    posts=user.posts.all
    context={'user':user,'posts':posts}
    return render(request, 'twitter/profile.html', context)

@login_required
def editar(request):
    if request.method == 'POST':
        u_form=user_edit(request.POST , instance=request.user)
        P_form=profile_edit(request.POST ,request.FILES , instance=request.user.profile)
        if u_form.is_valid() and P_form.is_valid() :
            u_form.save()
            P_form.save()
            return redirect('home')
    else :
        u_form=user_edit( instance=request.user)
        P_form=profile_edit()
        
    context={'u_form':u_form,'p_form':P_form}

    return render(request, 'twitter/editar.html', context)

@login_required
def delete (request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return redirect('home')
@login_required
def follow(request ,username):
    current_user= request.user
    to_user= User.objects.get(username=username)
    rel= relationship(from_user=current_user , to_user=to_user)
    rel.save()
    return redirect('profile',username)
@login_required
def unfollow(request,username):
    current_user= request.user
    to_user= User.objects.get(username=username)
    rel= relationship.objects.get(from_user=current_user.id , to_user=to_user.id)
    rel.delete()
    return redirect('profile',username)