from PIL import Image, ImageFilter, ImageEnhance

image = Image.open("681.png")
resized_image = image.resize((100, 100))
resized_image.show()

rotated_image = image.rotate(90)
rotated_image.show()

grayscale_image = image.convert('L')
grayscale_image.show()

custom_image = image.filter(ImageFilter.SMOOTH_MORE)
custom_image.show()


resized_image.save('resized_image.png')
rotated_image.save('rotated_image.png')
grayscale_image.save('grayscale_image.png')
custom_image.save('custom_image.png')

# enhancer = ImageEnhance.Sharpness(image)
# enhancer = ImageEnhance.Color(image)
# enhancer = ImageEnhance.Brightness(image)
# enhancer = ImageEnhance.Contrast(image)
# enhancer.enhance(10).show()
