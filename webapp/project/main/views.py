from django.shortcuts import render
import glob
from . import task

def home(request):
    task.download_a_cat.delay()

    cats = []
    for file in glob.glob('celery_cats/cats/*.gif'):
        print(file)
        cats.append(file)

    return render(request, 'index.html', {'cats': cats})