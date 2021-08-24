import json
from collections import OrderedDict
from download_ffhq import recreate_aligned_images

json_file = '/Users/jchetboun/Downloads/ffhq-dataset-v2.json'
with open(json_file, 'rb') as f:
    json_data = json.load(f, object_pairs_hook=OrderedDict)
json_data_small = OrderedDict()
json_data_small["749"] = json_data["749"]
recreate_aligned_images(json_data_small, dst_dir='realign1024x1024', output_size=1024, transform_size=4096, enable_padding=True)
