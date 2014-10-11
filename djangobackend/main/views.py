from django.shortcuts import render, render_to_response
# Create your views here.

def test_page(request):
    return render_to_response('test.html', {})

def index_page(request):
    return render_to_response('index.html', {})
