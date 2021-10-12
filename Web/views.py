import imageio
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import warnings

from skimage import img_as_ubyte

from Web.models import Result

from Web.model.main_model import start
warnings.filterwarnings("ignore")

from moviepy.editor import *

def muvi():
    # print(os.getcwd())
    videoclip = VideoFileClip("static/result/generated_result_1.mp4")
    audioclip = AudioFileClip("static/bgm.mp3")
    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile("static/result/generated_result.mp4")


@csrf_exempt
def predict(request):

    return render(request, 'index.html')


@csrf_exempt
def make_ani_1(request):
    if request.method == 'POST':
        if request.is_ajax():
            image = request.FILES.get('img')
            prediction = start(image, 'Web/inputdata/고생했어.mp4')
            imageio.mimsave('static/result/generated_result_1.mp4', [img_as_ubyte(frame) for frame in prediction])
            muvi()

    return render(request, 'index.html')

@csrf_exempt
def make_ani_2(request):
    if request.method == 'POST':
        if request.is_ajax():
            image = request.FILES.get('img')
            prediction = start(image, 'Web/inputdata/웃음_최종.mp4')
            imageio.mimsave('static/result/generated_result_1.mp4', [img_as_ubyte(frame) for frame in prediction])
            muvi()

    return render(request, 'index.html')



