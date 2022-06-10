
import argparse
from os.path import expanduser


home = expanduser("~")

parser = argparse.ArgumentParser()
parser.add_argument("-file", type=argparse.FileType('r'),
                    required=True, help="Directs the file list torrent tracker")
parser.add_argument("-out", type=argparse.FileType('w'), metavar='PATH',
                    default="rtorrent.txt", help="Directs the file otput checked trackers")
parser.add_argument("-rt", action='store_true',
                    help="add file to path ~/.rtorrent.rc")
parser.add_argument("-tracker", type=int, default=3,
                    help="switch start number tracker")
args = parser.parse_args()


num = 0
tracker = args.tracker

list_rtorrent = []


def command(n, tr, track):
        if len(str(n)) == 1:
            nu = '00'+str(n)
        elif len(str(n)) == 2:
            nu = '0'+str(n)
        else:
            nu = str(n)
        tracker_list = 'method.set_key=event.download.inserted_new,add_all_trackers' + \
        str(nu)+',"d.tracker.insert=\\"'+str(tr)+'\\",\\"'+track+'\\""'
        list_rtorrent.append(tracker_list)
        # write(tracker_list)


for line in args.file:
    command(num, tracker, line.strip()) 
    num = num+1
    tracker = tracker+1



if not args.rt:
    args.out.write('\n'.join(list_rtorrent))
else:
    try:
        with open(home+"/.rtorrent.rc",'a') as a_write:
            a_write.write('\n'.join(list_rtorrent))
    except FileNotFoundError:
         with open(home+"/.rtorrent.rc",'w') as a_write:
            a_write.write('\n'.join(list_rtorrent))