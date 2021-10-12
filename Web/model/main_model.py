import imageio
import torch
from skimage.transform import resize
import warnings
from Web.model.demo import make_animation
from skimage import img_as_ubyte
from Web.model.demo_vox import load_checkpoints
warnings.filterwarnings("ignore")

# load generator, kp_detector


def start(image_dir, video_dir):
    generator, kp_detector = load_checkpoints(checkpoint_path='Web/model/checkpoint/vox-cpk.pth.tar', cpu=False)
    # load image and video
    source_image = imageio.imread(image_dir)
    driving_video = imageio.mimread( video_dir, memtest=False)

    #Resize image and video to 256x256
    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    # make animation
    predictions = make_animation(source_image, driving_video, generator, kp_detector, relative=True,
                                 adapt_movement_scale=True)

    return predictions

