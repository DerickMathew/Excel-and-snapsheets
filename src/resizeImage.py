import os, sys
from PIL import Image


class resize_image():

    def get_thumbnail_name(self, img_path):
        # TODO cycle through until we generate a truly unique thumbnail name
        return os.path.splitext(img_path)[0] + ".thumbnail"

    def get_size_maintaining_ratio(self, w, l):
        # Assuming that width > length
        ratio = w / 128.0
        return (w * ratio, l * ratio)

    def get_size_if_larger_width(self, w, l):
        return self.get_size_maintaining_ratio(w, l)

    def get_size_if_larger_length(self, w, l):
        size = self.get_size_maintaining_ratio(l, w)
        return size[::-1]

    def get_size(self, w, l):
        if w > l:
            return self.get_size_if_larger_width(w, l)
        else:
            return self.get_size_if_larger_length(w, l)
        return 128, 128

    def create_thumbnail(self, original_img_path):
        thumbnail_path = self.get_thumbnail_name(original_img_path)
        try:
            im = Image.open(original_img_path)
            # TODO get w & l from the image
            w = 123
            l = 123
            size = self.get_size(w, l)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(thumbnail_path, "JPEG")
            return thumbnail_path
        except IOError:
            print "cannot create thumbnail for '%s'" % original_img_path
            raise IOError("cannot create thumbnail for '%s'" % original_img_path)
