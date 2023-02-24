import sys, os
import re
from PIL import Image

# function to convert image
def convert_to_png(first_folder, second_folder, name_file):
	img = Image.open(first_folder + name_file)
	name_file = os.path.splitext(name_file)[0]
	img.save(second_folder + name_file + ".png", "png")

# function to check is folder's name is valid
def check_valid_input(name_folder):
	valid_pattern = re.compile(r"[a-zA-Z]?[:]?[\/]?[a-zA-Z0-9\,\.\-\/_]{1,}\/?")
	return valid_pattern.fullmatch(name_folder)

# fuction to format input name folder
def valid_name_folder(name_folder):
	if "/" not in name_folder:
		name_folder = "./" + name_folder
	if name_folder[-1]!='/':
		name_folder += '/'
	return name_folder

def main_function(first_folder, second_folder):
	try:
		if not check_valid_input(first_folder) or not check_valid_input(second_folder):
  			raise Exception("Wrong name of folder")

		first_folder = valid_name_folder(first_folder)
		second_folder = valid_name_folder(second_folder)

		if not os.path.exists(first_folder):
			raise Exception("First folder does not exist")

		# if second folder not exists - to create
		if not os.access(second_folder, os.F_OK):
			os.mkdir(second_folder)

		# get list of pics from first folder	
		name_pics_list = os.listdir(first_folder)

		if not name_pics_list:
			raise Exception("First folder must contain files")	

		flag = 0
		for name in name_pics_list:
			if ".jpg" in name:
				flag += 1
			if not flag:
				raise Exception("First folder must contain jpg files")

		# loop through first folder and convert
		for name_pic in name_pics_list:
			convert_to_png(first_folder, second_folder, name_pic)
		return 0
	except Exception as err:
		print(err)
		return str(err)

if __name__ == '__main__':
	# grab the first and second argument
	# first - folder's name with jpg image
	# second - folder's name with png image
	first_folder = sys.argv[1]
	second_folder = sys.argv[2]

	main_function("C:/Users/UCAR/Desktop/ckdataset/anger", "C:/Users/UCAR/Desktop/deneme")