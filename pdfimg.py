import os

from PIL import Image

files={
    'image_post': [[]]
}
image_set=[]
temp=""
i=0
rootdir = './history_of_modern_india/'
for file in os.listdir(rootdir):
    print(file)
    if '.jpg' in file:
        
        # print(len(file))
        trim_name=file[0:23]
        # print(trim_name)
        if temp==trim_name or i==0:
            image_set.append(file)
        else:
            files['image_post'].append(image_set)
            image_set=[]
            image_set.append(file)
        
        temp=trim_name
        i=+1

print("\n\n")

for i in files['image_post']:

    print(i)






#         files.append(trim_name)

# print(files)






# image1 = Image.open(r'./history_of_modern_india/2021-08-20_06-35-47_UTC_1.jpg')
# im1 = image1.convert('RGB')
# im1.save(r'./pdf_file/1.pdf')
