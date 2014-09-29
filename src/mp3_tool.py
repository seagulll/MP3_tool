'''
Created on Apr 10, 2013

@author: elingyu
'''

import os
import eyed3
import optparse
import fnmatch

def parse_args():
    usage = """usage: %prog [options] 
This is the small mp3 file tools, used for deleting same song mp3 files under the directory.
Run it like this:

    python Main.py -d "C:\simon\Personal\Music\English_Songs"
    
it means it  will delete same song mp3 files under the directory "C:\simon\Personal\Music\English_Songs".
"""
    parser = optparse.OptionParser(usage)
    parser.add_option("-d", "--directory", dest="directory", help="please input directory", default="c:")

    options, _ = parser.parse_args()
        
    return options.directory


def mp3_file_handler():
    file_path = parse_args()
    file_list = os.listdir(file_path)
    file_number = len(file_list)
    song_info = {}
    org_song_list = []
    operate_song_list = []
    removed_song_info = []
    removed_song_list = []

    for i in range(0, file_number):
        if fnmatch.fnmatch(file_list[i], '*.mp3'): 
            song = eyed3.load(file_path + "\\" + file_list[i])
            org_song_list.append(file_list[i])
            if song.tag != None and song.tag.title != '':
                song_info = {'name': file_list[i], 'title': song.tag.title}
                operate_song_list.append(song_info)
    
    org_song_number = len(org_song_list)
    operate_song_number = len(operate_song_list)

    for j in range(0, operate_song_number-1):
        song1_title = operate_song_list[j]['title']
        j = j + 1
        for v in range(j, operate_song_number):
            song2_title = operate_song_list[v]['title']
            if song1_title == song2_title:
                removed_song_list.append(operate_song_list[v]['name'])
                removed_song_info.append(operate_song_list[v])

    for q in range(0, len(removed_song_info)):
        os.remove(file_path + "\\" + removed_song_info[q]['name'])
        
        
    removed_song_number = len(removed_song_list)
    final_song_number = org_song_number - removed_song_number
        
    print "The removed song list is %s" %(removed_song_list)
    print "The original song number is %d" %(org_song_number)
    print "The removed song number is %d" %(removed_song_number)
    print "The final song number is %d" % (final_song_number)


if __name__ == '__main__':
    mp3_file_handler()

