from django.shortcuts import render
from django.views import generic
from .models import CoffeePost
from .forms import CoffeePostForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.urls import reverse_lazy


class CoffeeIndex(generic.ListView):
    model = CoffeePost
    queryset = CoffeePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

class CoffeeMyarea(generic.ListView):
    model = CoffeePost
    template_name = 'my-area.html'
    paginate_by = 6
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

class DetailCoffee(generic.DetailView):
    model = CoffeePost
    template_name="detail_coffee.html"
    slug_url_kwarg = 'slug'



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



