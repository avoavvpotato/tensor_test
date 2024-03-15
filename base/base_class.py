import datetime
import os

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result

    """Method assert url"""
    def assert_title(self, substring_title):
        assert substring_title in self.driver.title

    """Method assert title"""
    def assert_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url

    """Method assert size file"""
    def assert_file_size(self, file, size, unit):
        if unit == 'MB':
            assert str(round(os.path.getsize(file) / (1024 * 1024), 2)) == size

    """Method Image Width"""
    def assert_img_width(self, image, width):
        assert image['width'] == width

    """Method Image Height"""
    def assert_img_height(self, image, height):
        assert image['height'] == height

    """Method Image Size"""
    def check_size_image(self, image, height, width):
        self.assert_img_width(image.size, width)
        self.assert_img_height(image.size, height)

    """Method Images Size"""
    def check_size_images(self, images, height, width):
        for image in images:
            self.check_size_image(image, height, width)

    """Method Clear Directory"""
    def clear_directory(self, directory):
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    """Method assert file download"""
    def assert_file_download(self, directory, file):
        file_path = os.path.join(directory, file)
        assert os.access(file_path, os.F_OK) == True