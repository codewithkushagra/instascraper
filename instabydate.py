
import os

from PIL import Image

import instaloader

from datetime import datetime

from instaloader import Profile

from fpdf import FPDF

L = instaloader.Instaloader()



profile = Profile.from_username(L.context, 'history_of_modern_india')
def getTodaysPost():
    i=0
    for post in profile.get_posts():
        print(post.date)
            
        if(post.date>datetime(2021, 8, 20)) and post.date<datetime(2021,8,21):
            L.download_post(post, target=profile.username)
            print("okay")
            print(post.caption)
            generatePDF(i)
            i+=1
            rootdir = './history_of_modern_india/'
            for file in os.listdir(rootdir):
                os.remove(os.path.join(rootdir, file))

            
        elif post.date<datetime(2021, 8, 20):
            break





def generatePDF(num):
    image_post=[]
    text_post=[]
    rootdir = './history_of_modern_india/'
    for file in os.listdir(rootdir):
        
        if '.jpg' in file:
            image_post.append(os.path.join(rootdir, file))
        elif '.txt' in file:
            text_post.append(os.path.join(rootdir, file))

    print(image_post)
    imgRGB=[]
    for img in image_post:

        img_post=Image.open(img)
        imgRGB.append(img_post.convert('RGB'))



    print(imgRGB)
    img1=imgRGB.pop(0)
    img1.save(f'./pdf_file/{num}.pdf',save_all=True, append_images=imgRGB)
    # num*=2
    
    # pdf = FPDF()
  
    # pdf.add_page()

    # pdf.set_font("Arial", size = 15)
    # for text in text_post:
    #     txt_post=open(text, "r")
    #     for x in txt_post:
    #         pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    #     pdf.output(f"./pdf_file/{num}.pdf")
    
     
# generatePDF()

getTodaysPost()


    # if datetime(2021, 7, 20)>post.date and datetime(2021, 8, 20)<post.date:
    #     L.download_post(post, target=profile.username)
    #     print(post.date)
    #     print(post.caption)

# for post in profile.get_profile_pic_url():
#     print(post)

# print(profile.get_profile_pic_url())




