IMG_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm']
def is_image_file(filename):
    """Checks if a file is an image.
      Args:
          filename (string): path to a file
      Returns:
          bool: True if the filename ends with a known image extension
    """
    filename_lower = filename.lower()
    return any(filename_lower.endswith(ext) for ext in IMG_EXTENSIONS)

def get_imagelist_from_dir(dirpath):
    images = []
    for f in os.listdir(dirpath):
        if is_image_file(f):
            images.append(os.path.join(dirpath, f))
    return images

#扩展
# assert args.image_dir or args.images
# assert bool(args.image_dir) ^ bool(args.images)


imglist=get_imagelist_from_dir(image)
num_images = len(imglist)

assert args.image_dir or args.images
assert bool(args.image_dir) ^ bool(args.images)

for i in xrange(num_images):
	print('img', i)
	im = cv2.imread(imglist[i])
	#+预测



def parse_args():
#     """Parse in command line arguments"""
#     parser = argparse.ArgumentParser(description='Demonstrate mask-rcnn results')
#     parser.add_argument(
#         '--dataset', required=True,
#         help='training dataset')

#     parser.add_argument(
#         '--cfg', dest='cfg_file', required=True,
#         help='optional config file')
#     parser.add_argument(
#         '--set', dest='set_cfgs',
#         help='set config keys, will overwrite config in the cfg_file',
#         default=[], nargs='+')

#     parser.add_argument(
#         '--no_cuda', dest='cuda', help='whether use CUDA', action='store_false')

#     parser.add_argument('--load_ckpt', help='path of checkpoint to load')
#     parser.add_argument(
#         '--load_detectron', help='path to the detectron weight pickle file')

#     parser.add_argument(
#         '--image_dir',
#         help='directory to load images for demo')
#     parser.add_argument(
#         '--images', nargs='+',
#         help='images to infer. Must not use with --image_dir')
#     parser.add_argument(
#         '--output_dir',
#         help='directory to save demo results',
#         default="infer_outputs")
#     parser.add_argument(
#         '--merge_pdfs', type=distutils.util.strtobool, default=True)

#     args = parser.parse_args()

#     return args
