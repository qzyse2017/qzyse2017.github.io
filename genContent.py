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
    
    with open('conf.json','r') as cfg:
        tmpData = json.load(cfg)
        
    lastUpdateTime = tmpData['last_update']
    
    with open('conf.json','w') as cfg:
        tmpData['last_update'] = time.strftime('%Y-%m-%d', time.localtime())      
        json.dump(tmpData,cfg)

    for file in fileList:
        strPieces = file.split('-')
        
        postTime = strPieces[0] + '-' + strPieces[1] + '-' + strPieces[2]
        timeLater = isTimeLater('-'.join(strPieces[0:4]),lastUpdateTime)
        if timeLater == False:
            continue

        titleEnd = file.rfind('.')
        newList = (file[:titleEnd + 1] + 'html').split('-')
        title = ' '.join((file[:titleEnd + 1]).split('-')[3:])
        #e.g. http://qzyse2017.github.io/daily-posts/2018/07/03/Use-Tennyson's-verses-to-greet-my-new-blog.html
        titleLink = '[' +title + ']' + '(' + 'https://qzyse2017.github.io/daily-posts/' + strPieces[0] + '/' \
                    + strPieces[1]  +'/' + strPieces[2] + '/' +  '-'.join(newList[3:]) + ')'
        newLine = postTime + '  ' + titleLink + '\r\n'
        f = open('content.md','a')
        f.write(newLine)


if __name__ == "__main__":
    genPostsContent()