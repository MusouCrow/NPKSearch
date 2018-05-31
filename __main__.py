import os
import json
from sys import argv
from model.npk import NPK

suffix = argv[1][-4:].lower()

if suffix != '.img':
    npk_list = []
    img_dict = {}
    data = {
        'npk_list': npk_list,
        'img_dict': img_dict
    }

    for root, dirs, files in os.walk(argv[1]):
        for f in files:
            if f[-4:] == '.NPK':
                try:
                    npk = NPK(open(root + '/' + f, 'br+'))
                    npk_list.append(f)

                    for i in range(len(npk)):
                        info = npk.info(i)
                        img_dict[info['name']] = len(npk_list) - 1
                except:
                    pass

    content = json.dumps(data)
    f = open('config.json', 'w')
    f.write(content)
    f.close()
else:
    path = 'sprite/' + argv[1].lower()  # type: str

    f = open('config.json', 'r')
    data = json.loads(f.read())
    index = data['img_dict'][path]
    print(data['npk_list'][index])
