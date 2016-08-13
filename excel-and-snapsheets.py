import argparse
import os
from src.resizeImage import resize_image
from src.snap2snapsheet import img_to_excel


def is_prexisting_path(given_path):
    return os.path.exists(given_path)

parser = argparse.ArgumentParser(
    description=(
        'A hobby project that converts '
        'your picture into a spreadsheet.'),
    epilog=(
        'now you know how it works. '
        'Try it out for yourself'))

parser.add_argument(
    '--snap',
    nargs=1,
    required=True,
    type=file,
    help=(
        'Path to the picture '
        'that you want a snapsheet off'))

parser.add_argument(
    '--autoresize',
    action='store_true',
    help=(
        'If set this will resize you image '
        'such that the larger of either width or length '
        'is <=128 pixels, this option maintains '
        'the ratio of the image if possible'))

parser.add_argument(
    '--snapsheet',
    nargs=1,
    required=True,
    # type=file,
    type=argparse.FileType('w'),
    help=(
        'Path to where you want your '
        'brand new snapsheet. If the path is invalid '
        'or the path already exists then this script '
        'will raise an exception'))

args = parser.parse_args()

img_path = args.snap[0].name
if args.autoresize:
    img_path = resize_image().create_thumbnail(img_path)
snapsheet_path = args.snapsheet[0].name
img_to_excel().create_excel_from_image(img_path, snapsheet_path)
