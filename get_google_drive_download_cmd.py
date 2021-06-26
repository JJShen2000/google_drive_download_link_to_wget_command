import requests
import sys

def get_file_name(t):
    i=t.find('content=')
    t=t[i+1:]
    i=t.find('content=')
    t=t[i+1:]
    i=t.find('content=')
    t=t[i+1:]
    i=t.find('content=')
    t=t[i+9:]
    i=t.find("\"")
    return t[:i]

def generate_download_decompression_cmd(filename, id):
    return 'wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate '+"'https://docs.google.com/uc?export=download&id="+id+"' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\\1\\n/p\')&id="+id+'" -O '+filename+" && rm -rf /tmp/cookies.txt"

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 get_google_drive_download_cmd.py [Your google drive file share link]')
    
    # share_link = 'https://drive.google.com/file/d/1a2yp0nlxLyhXkkm_2rUzP_5RagZme3pA/view?usp=sharing'
    share_link = sys.argv[1]
    r = requests.get(share_link)
    t = r.text
    filename = get_file_name(t)
    i1 = share_link.find('file/d/')+7
    i2 = share_link.find('/view')
    id = share_link[i1:i2]
    print(generate_download_decompression_cmd(filename, id))

if __name__ == '__main__':
    main()
