import os

import yaml

from common import constant


def data_analyze(filename, data_key):
    with open(constant.data_dir + os.sep + filename, "r", encoding='utf8') as f:
        data = yaml.full_load(f)
        print(data)
        data_dict = data[data_key]
        return [datas for datas in data_dict.values()]


if __name__ == '__main__':
    args = data_analyze("login.yaml", "test_login")
    print(args)

