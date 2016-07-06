import os, json
from clarifai.client import ClarifaiApi


class ImageRecognition(object):

    '''

    Class to recognize images using the ClarifaiAPI

    tag_image_url: tags a images that is given in a url (http://*.* or https://*.*) returns: json
    tag_image: tags a image from wich the path is given (/*/*.jpg, /*/*.jpeg, /*/*.png, etc...) returns: json
    tag_images_dir: tags all the images in a directory given (/*/) returns: json
    get_most_likely: returns the most likely result from the json object returned by on of the functions above returns: list

    Example: img_recon.get_most_likely(img_recon.tag_image('/root/Documents/dog1.jpeg'), r=4)
             returns: [u'dog', u'pet', u'canine', u'mammal', u'puppy']

    '''

    def __init__(self, app_id='NXSqUv3U17C0iglZLv0OQIb81h6-LBdWa5OLHDQG', app_secret='gDxYm_QgzUEu0_Dp20S0RzYWSF8EkFfP0ierQoPu'):
        """
        Setsup the ClarifaiAPI
            :param app_id: ID of the clarifai app
            :param app_secret: SECRET of the clarifai app
        """
        self.api = ClarifaiApi(app_id=app_id, app_secret=app_secret)

    def tag_image_url(self, url):
        """
        Tags a image on the web
            :param url: A url (http://*.* or https://*.*)
            :return: returns a json string with the api output from the clarifaiAPI
        """
        return self.api.tag_image_urls(url)

    def tag_image(self, image):
        """
        Tags a image stored on the local machine
            :param image: Path to the image (/*/*/*.jpg, /*/*/*.jpeg, /*/*/*.png)
            :return: returns a json string with the api output from the clarifaiAPI
        """
        with open(image, 'rb') as image_file:
            return self.api.tag_images(image_file)

    def tag_images_dir(self, path):
        """
        Tags all images in a directory
            :param path: Path to the directory (/*/*/)
            :return: returns a json string with the api output from the clarifaiAPI
        """
        images = []
        path = path.rstrip(os.sep)
        for fname in os.listdir(path):
            images.append((open(os.path.join(path, fname), 'rb'), fname))
        return self.api.tag_images(images)

    def get_most_likely(self, response):
        """
        Filter a json response of the ClarifaiAPI for the most likeliest match
            :param response: A string with json
            :return: The most likeliest match
        """
        data = json.loads(json.dumps(response))
        most_likeliest = data["results"][0]['result']['tag']['classes']
        return most_likeliest[0]


