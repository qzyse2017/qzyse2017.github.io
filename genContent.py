'''
Generate contents.md from new post files in'.\_posts'
'''

import os
import time
import datetime
import json


def isTimeLater(date1,date2):
    return date1 > date2
    

def genPostsContent():
    #e.g. 2018-07-03-Use-Tennyson's-verses-to-greet-my-new-blog
    fileList = os.listdir('_posts')
    newLines = "---\n" + \
    "layout: page\n" + \
    "title: cotents\n" + \
    "permalink: /contents/\n" + \
    "---\n\n"
    fileList.sort()
    for file in fileList:
        if os.path.isfile(file):
            strPieces = file.split('-')
            
            postTime = strPieces[0] + '-' + strPieces[1] + '-' + strPieces[2]

            titleEnd = file.rfind('.')
            newList = (file[:titleEnd + 1] + 'html').split('-')
            title = ' '.join((file[:titleEnd + 1]).split('-')[3:])
            #e.g. http://qzyse2017.github.io/daily-posts/2018/07/03/Use-Tennyson's-verses-to-greet-my-new-blog.html
            titleLink = '[' + title + ']' + '(' + 'https://qzyse2017.github.io/daily-posts/' + strPieces[0] + '/' \
                        + strPieces[1]  +'/' + strPieces[2] + '/' +  '-'.join(newList[3:]) + ')'
            newLine = postTime + '  ' + titleLink + '\r\n'
            newLines += newLine
    f = open('content.md','w')
    f.write(newLines)


if __name__ == "__main__":
    genPostsContent()