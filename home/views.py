from django.shortcuts import render, redirect
from django.contrib.auth import logout

from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View


# TODO: test to do here
def home(request):
    # import pdb
    # pdb.set_trace()    # pára a execução nesta linha,
                       # permitindo vc debugar o script 
    return render(request, 'home.html')


def my_logout(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    """ template views """
    template_name='home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_test'] = 'This is a test of get_context_data'
        return context


class Myview(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello World')



# FBV - Function-based views
# CBV - Class-based views