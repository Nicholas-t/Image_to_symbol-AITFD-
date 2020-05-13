import cv2
import numpy as np
import matplotlib.pyplot as plt


#============================= 
# initialize
#=============================

SPECIAL = {
    '*' : 'star',
    '|' : 'vert-line',
    '"' : 'double-quot',
    '<' : 'less',
    '>' : 'greater',
    "'" : 'single-quot',
    '?' : 'question',
    '\\' : 'slash1', 
    '/' : 'slash2'
}

N = 500

dic = {}

with open('CHARS.txt', 'r') as file:
    lines = file.readlines()
    for lin in lines:
        lin = lin.strip('\n')
        cat, val = lin[:lin.index('=')], lin[lin.index('=')+1:]
        dic[cat] = val

#============================= 



def convert_character(char, row, col):
    cat = None
    for key in dic.keys():
        if char in dic[key]:
            cat = key
    if char in SPECIAL.keys():
        char = SPECIAL[char]
    if (cat == None):
        print('character unknown')
        return False
    path = './CHARS/'+cat+'-'+char+'.png'
    img = cv2.imread(path)
    img = cv2.resize(img, (row,col))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img
    #print(img.shape)
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

def get_alphabet_dictionary(row, col):
    out = {}
    for k in dic.keys():
        for _k in dic[k]:
            out[_k] = convert_character(_k, row, col)
    return out

