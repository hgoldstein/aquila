USER = "huntergoldstein"
IMAGE = "aquila"
TAG = "latest"

def image_name():
    return "{}/{}:{}".format(USER, IMAGE, TAG)
