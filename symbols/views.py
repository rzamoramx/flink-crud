
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Create your views here.

def messages_example(request):
    if request.method == 'GET':
        messages.add_message(request, messages.INFO, "Hello world from messages of django.contrb")

    return render(request, 'messages.html', status=202)


@csrf_exempt
def function_view(request):
    if request.method == 'GET':
        print(f'a GET request from function view: {request}')

    if request.method == 'POST':
        print(f'a POST request from function view: {request}')

    """context = {
        "foo": "bar"
    }
    return render(request, 'view.html', context)"""
    now = datetime.datetime.now()
    html = "<html><body>It is now %s. from function view</body></html>" % now
    return HttpResponse(html, status=201)


class ClassView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        print(f'a GET request from CLASS view (using template view): {context}')
        return context

    """def get(self, request):
        print(f'a GET request from CLASS view: {request}')
        now = datetime.datetime.now()
        html = "<html><body>It is now %s. from CLASS view</body></html>" % now
        return HttpResponse(html, status=201)"""

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = datetime.datetime.now()
        print(f'a POST request from CLASS view: {context}')
        return super().get(request, *args, **context)
