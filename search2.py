import json
import sys
import glob
import webbrowser

with open('index2.json', 'r') as index_file:
    index = json.load(index_file)

if len(sys.argv) > 1:
    try:
        dates = sorted(index[''.join(sys.argv[1:])])
        if len(dates) > 0:
            f = open('result.html','w')
            f.write("<html>\n<head>\n<title>\nResult: "+''.join(sys.argv[1:]) + "\n</title>\n</head>\n<body>\n")
            for i in dates:
                f.write(i+'<br>\n<img src="'+glob.glob('*/*'+i+'*')[0]+'"><br>\n')
            f.close()
            webbrowser.open('result.html', new=2)
        else:
            print(sys.argv[1:] + ' not found')
    except:
        exit(-1)
