import os
import re
from mutagen.easyid3 import EasyID3

def is_movie(file):
    # check if file is a movie based on metadata information
    try:
        audio = EasyID3(file)
        if 'genre' in audio and audio['genre'][0] == 'Movie':
            return True
        return False
    except:
        return False

def categorize_file(file):
    # categorize file as movie or TV show based on file name
    if is_movie(file):
        return 'movies'
    else:
        if re.search(r'(.*) - S\d+E\d+ - (.*)\..*', file):
            return 'tvshows'
        else:
            return 'other'

def main(src_folder, dest_folder):
    # scan src_folder for media files
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            category = categorize_file(src_file)
            dest_dir = os.path.join(dest_folder, category)
            dest_file = os.path.join(dest_dir, file)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            if not os.path.exists(dest_file):
                os.rename(src_file, dest_file)

if __name__ == '__main__':
    main('./downloads', './media')
