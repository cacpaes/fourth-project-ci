from django.shortcuts import render
from django.views import generic
from .models import CoffeePost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib import messages
from django.urls import reverse_lazy



class CoffeeIndex(generic.ListView):
    model = CoffeePost
    queryset = CoffeePost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class CreateCoffee(LoginRequiredMixin, generic.CreateView):
    model = CoffeePost
    fields = ['coffee_name', 'coffee_origin', 'coffee_brand', 'coffee_content', 'coffee_image']
    template_name ='add_coffee.html'
    success_url =reverse_lazy('home')

    def form_valid(self,form):
        form.instance.username = self.request.user
        form.instance.status = 1
        return super(CreateCoffee, self).form_valid(form)



