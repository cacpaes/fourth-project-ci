from django.views import generic
from .models import CoffeePost, Comment
from .forms import CoffeePostForm, CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.urls import reverse_lazy


class CoffeeIndex(generic.ListView):
    model = CoffeePost
    queryset = CoffeePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8

class CoffeeMyarea(generic.ListView):
    model = CoffeePost
    template_name = 'my-area.html'
    paginate_by = 8
    def get_queryset(self):
        return CoffeePost.objects.filter(username=self.request.user).order_by('-created_on')


class CreateCoffee(generic.CreateView, LoginRequiredMixin):
    """
    User can create a coffee post.
    """
    model = CoffeePost
    form_class= CoffeePostForm
    template_name ='add_coffee.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Sets logged in user 
        Sets form default status 
        """
        form.instance.username = self.request.user
        form.instance.status = 1
        return super(CreateCoffee, self).form_valid(form)

def DetailCoffee(request, slug):
    template_name='detail_coffee.html'
    post = get_object_or_404(CoffeePost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST' and request.user:
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class EditCoffee(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    """
    User can edit their coffee post.
    """
    model = CoffeePost
    form_class= CoffeePostForm
    template_name = 'add_coffee.html'
    success_url = reverse_lazy('home')
    success_message = "Your post is up to date."

    def test_func(self):
        """
        Function that only allows the user to update their post.
        """
        coffee_post = self.get_object()
        return coffee_post.username == self.request.user


class DeleteCoffee(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """
    User can delete their coffee post.
    """
    model = CoffeePost
    success_url = reverse_lazy('myarea')
    success_message = "Deleted."
    template_name = 'delete_coffee.html'

    def test_func(self):
        """
        Function that only allows the user to delete their post.
        """
        coffee_post = self.get_object()
        return coffee_post.username == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteCoffee, self).delete(request, *args, **kwargs)
