from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64

@login_required(login_url='/auth/')
def Home(request): 
    username = request.user
    context={
        'username':username,
    }
    return render(request, 'home/index.html', context)

def Teste(request):
    x = [1, 2, 3, 7]
    y = [[1, 2, 3], [3, 4, 7], [5, 6, 2], [5, 6, -2]]
    plt.plot(x, y, label='linear')
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)    
    return render(request, 'home/teste.html', {'data': uri})
