class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def get_real(self):
        return self.real

    def get_img(self):
        return self.img

    def set_real(self, value):
        self.real = value

    def set_img(self, value):
        self.img = value

    def __str__(self):
        return str(self.get_real()) + "+" + str(self.get_img()) + "i"



