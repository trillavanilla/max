from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from home.forms import HomeForm
from home.models import Post, Friend

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        form = HomeForm()
        posts = Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friends = Friend.objects.filter(current_user=request.user)

        args = {
            'form': form, 'posts': posts, 'users': users, 'friends': friends,
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            text = form.cleaned_data['post']
        return redirect('home:home')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, {'form': form})

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')

def counter(request, pk):
    Counter.objects.filter(pk=pk).update(views=F('views')+1)
    return render(request, "home/counter.html")
