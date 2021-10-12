import imageio
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import warnings

from skimage import img_as_ubyte

from Web.models import Result

from Web.model.main_model import start
warnings.filterwarnings("ignore")


#
@csrf_exempt
def predict(request):

    return render(request, 'index.html')

@csrf_exempt
def make_ani(request):
    photo = Result()
    if request.method == 'POST':
        if request.is_ajax():
            image = request.FILES.get('img')
            prediction = start(image, 'Web/inputdata/1.mp4')
            imageio.mimsave('static/result/generated_result.mp4', [img_as_ubyte(frame) for frame in prediction])

    return render(request, 'index.html')



