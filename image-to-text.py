import cv2
import pytesseract
from os import walk, getcwd
import re

# image_path = r"images/abc.jpeg"
# img = cv2.imread(image_path)
# text = pytesseract.image_to_string(img)

imageDir = getcwd()+'/images'
filenames = next(walk(imageDir), (None, None, []))[2]  # [] if no file

output = ''
i = 1
for filename in filenames:
    print('extracting from image: ',filename)
    img = cv2.imread(imageDir+'/'+filename)
    output += pytesseract.image_to_string(img)
    output = re.sub(r'Question \d of 50','',output)
    output = output.replace('','')
    output = output.replace('| wescnool','')
    output = output.replace('RAJAS PANDHARKAR','')
    output = output.replace('Subject: Managerial','')
    output = output.replace('Welinakar Education','')
    output = output.replace('weschool Welingkar E;','')
    output = output.replace('es oo','')
    output = output.replace('oes','')
    output += '=================================================='
    
    i += 1
f = open("output/1.txt", "a")
f.write(output)
f.close()

# print(text[:-1])
