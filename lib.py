import pyfiglet
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[1;33;40m'
    class background:
        RED='\033[0;37;41m'
        GREEN='\033[0;37;42m'
        YELLOW='\033[0;37;43m'
        BLUE='\033[0;37;44m'
        MAGENTA='\033[0;37;45m'
        CYAN='\033[0;37;46m'
        WHITE='\033[0;37;47m'
        BLACK='\033[0;37;48m'

banners={
    "fonts":[
        'slant',
        '3-d',
        '3x5',
        '5lineoblique',
        'alphabet',
        'banner3-D',
        'doh',
        'isometric1',
        'letters',
        'alligator'
    ],
    "startup":[
        #['text', 'font'] # standard structure
        ['DDoS', '5lineoblique'],
        ['o f f s e c', 'banner3-D'],
        ['hack', 'isometric1']
    ],
    "errors":[
        ['[!!] Error', '0']
    ],
    "warns":[
        ['[!] Warning', '0']
    ]
}

