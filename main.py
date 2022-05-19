from utils.get_comments import get_comments

import sys

def main():
    video_id = sys.argv[1]
    list_of_comments = get_comments(video_id)
    return list_of_comments

if __name__ == '__main__':
    main()
