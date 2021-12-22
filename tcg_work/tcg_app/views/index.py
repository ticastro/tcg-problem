from django.shortcuts import render
from django.http import HttpResponse

# cambiar la salida por un texto que sirva
def index(request):
    context = {'inp_value': ''}
    if request.method == "POST":
        inp_value = request.POST['results']
        context = {'inp_value': inp_value}
        out_value = '1234'
        context['out_value'] = out_value
    elif request.method == 'GET':
        inp_value = 'Ingrese aqui su texto'
        out_value = 'aqui se mostraran las respuestas'
        context['inp_value'] = inp_value
    return render(request, 'index.html', {'response': context})
