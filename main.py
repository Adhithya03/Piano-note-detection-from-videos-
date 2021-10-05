#Previously used for Harry potter 7.2
row				= 0  #
cv_thresh_image = 50 #value
key_error_bias	= 10 #px
path 			= 'D:\\My-works\\dev\\Python\\Hobby projects\\Pixels to Midi\\headwig.png'


import cv2
import os
import pickle

# Parameters
# images=os.listdir(path)

with open(r"coords\val_list.txt", "rb") as fp:
	val_list = pickle.load(fp)

with open(r"coords\coords_list.txt", "rb") as fp:
	coords_list = pickle.load(fp)

def image_mode(name_bef_frame_num,frame_number):
	new_path=path+name_bef_frame_num+" "+frame_number+".jpg"
	key_finder(new_path)	
	print(key_list)

key_list=[]
def key_finder(image_path):
	print(f"Finding {image_path}")
	key_locations_coords=[]
	#Preprocessing
	image=cv2.imread(image_path)
	image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	ret, image = cv2.threshold(image, cv_thresh_image , 255, cv2.THRESH_BINARY)
	empty_space=True #Flag

	#Finding lit pixels
	for pixel_pos , pixel_val in enumerate(image[row]):

		if  pixel_val and empty_space:
			empty_space = not empty_space
			key_locations_coords.append(pixel_pos + key_error_bias)
			continue

		if  not(pixel_val) and not empty_space:
			empty_space = not empty_space
			continue

	#Finding the name for key by their coordinate  
	with open(r"results.txt","a") as ragha:
		for k in key_locations_coords:
			for index,values in enumerate(val_list[0]):
				if k in values:
					ragha.write(coords_list[index][0])
					break
		ragha.write("\n")

key_finder(path)