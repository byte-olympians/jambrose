from django.shortcuts import render, redirect
import pudb

# Create your views here.
def index(request):
    user_1 = request.session.pop('user_1', False)
    user_2 = request.session.pop('user_2', False)
    func = request.session.pop('func', False)
    if user_2 and user_1 and func:
        context = {
            'user_1': user_1,
            'user_2': user_2,
            'func': func
        }
    else:
        context = {}
    return render(request, 'index.html', context)

def write(request):
    print("HEY!")
    request.session['user_1'] = request.POST.get('user_1')
    request.session['user_2'] = request.POST.get('user_2')
    request.session['func'] = request.POST.get('read_write')

    return redirect('index')