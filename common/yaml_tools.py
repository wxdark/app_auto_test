import yaml

from common import constant


class YamlTools:
    def write_yaml(self, *args):
        """
        把自定义的类型数据写入yaml文件
        :param args:
        :return:
        """
        with open(args[0], 'w', encoding='utf-8') as file:
            yaml.dump(args[1], stream=file, allow_unicode=True)

    def write_yaml_all(self, *args):
        with open(args[0], 'w', encoding='utf-8') as file:
            yaml.dump_all([args[1], args[2]], stream=file, allow_unicode=True)

    def read_yaml(self, file):
        """
        读取yaml文件
        :param file:
        :return:
        """
        with open(file, 'r', encoding='utf-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            return data

    def read_yaml_all(self, file):
        """
        读取yaml中的多条数据，并返回一个列表
        :param file:
        :return:
        """
        with open(file, "r", encoding="utf-8") as file:
            datas = yaml.load_all(file, Loader=yaml.FullLoader)
            return [data for data in datas]


if __name__ == '__main__':
    print(YamlTools().read_yaml(constant.dev_login_dir))
