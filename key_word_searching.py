# -*- coding: utf-8 -*-

import os

#import markdown
def search_file(path,text,key_word):
    files = os.listdir(path)
    search_results = []
    for f in files:
        f1 = os.path.join(path,f)

        if os.path.isdir(f1):
            results = search_file(f1,text,key_word)
            if len(results)>0:
                search_results.append(results)
        elif os.path.isfile(f1) and os.path.splitext(f1)[1] == text:
            results = search_in_file(f1,key_word)
            if len(results)>0:
                search_results.append(results)
    return search_results



def search_in_file(path,key_word):
    with open(path, 'r',encoding =' utf-8') as f:
        context = f.read()
        cards = context.split('---')
        #print(context)
        search_results=[][]
        for i in cards:
            if key_word in i:
                search_results.append([path][i])
    return search_results



if __name__ == '__main__':
    #search_in_file('E:\Reading\README.md','R')
    #key_word = input()
    lista = search_file('E:\Reading','.md','r')
    for i in lista:
        print(i)
