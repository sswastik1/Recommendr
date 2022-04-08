import webbrowser
from PIL import Image, ImageEnhance
from PIL.ExifTags import TAGS

def Luminosity(image):
	image_data = image.getdata()
	Luminosity = []
	for tup in image_data:
		r, g, b = tup[:3]
		pixel_Luminosity =  (r+r+b+g+g+g)/6
		Luminosity.append(pixel_Luminosity)
	value = sum(Luminosity)/len(Luminosity)
	value = round((value/255)*100, 2)
	return value

def Saturation(image):
	Saturation = []
	image_data = image.getdata()
	for tup in image_data:
		try:
			val = (max(tup) - min(tup))/max(tup)
			Saturation.append(val)
		except ZeroDivisionError:
			Saturation.append(0)

	value = round(((sum(Saturation)/len(Saturation))*100),2)

	return value
