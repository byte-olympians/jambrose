from django.shortcuts import render, redirect
from joe_chain.helpers.api_calls import call
import pudb

selector = ['jeff', 'read', 'write']

# Create your views here.
def index(request):
    resp = request.session.pop('resp', False)
    if resp:
        context = {
            'resp': resp
        }
    else:
        context = {}
    return render(request, 'index.html', context)

def write(request):

    user_1 = request.POST.get('user_1')
    user_2 = request.POST.get('user_2')
    func = int(request.POST.get('selector'))

    resp = call(selector[func], user_1, user_2).text
    request.session['resp'] = resp

    return redirect('index')