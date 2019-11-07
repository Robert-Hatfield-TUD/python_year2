# All files in the same location please

import string

def clean(text):
    for i in string.punctuation:
        text = text.replace(i, "").lower()
    return text.split()

def diction(words):
    dict = {}

    #with open("stopwords.txt") as stopwordsfile:
        #stopwords = stopwordsfile.read().split()
    for word in words:
        #if word in stopwords:
            #continue
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1

    return dict

def htmlmake(words):
    with open("cloud.html", "w") as file:
        file.write("<!DOCTYPE html><html><head lang=\"en\"><meta charset=\"UTF-8\">\n\
            <title>Tag Cloud Generator</title></head><body>\n\
            <div style=\"text-align: center; vertical-align: middle;font-family: arial; \n\
            color: white; background-color:black;border:1px solid black\">\n")

        for word,size in words.items():
            file.write("<span style=\"font-size: "+str(size*10)+"px\"> "+word+"</span>\n")

        file.write("</div></body></html>")

with open("gettysburg.txt") as file:
    htmlmake(diction(clean(file.read())))
