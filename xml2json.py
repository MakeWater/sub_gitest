'''
将用于目标检测图像的xml标注信息转为json对象，减少存储空间；
输入一个含有xml文件的目录，将其中所有的xml文件中的信息保存到一个json文件中；
使用时再将json文件中的信息还原为一个个xml文件。
'''

import os 
import json
import xmltodict


def save_to_json(xml_dir,jsonfile):
    '''将信息保存到json中
    Args:
        xml_dir(a list object): a list object contains xml file name
        jsonfile: a json file name 
    Returns: save a json file in current dir.
        
    '''
    with open(jsonfile,"w") as jsf:
        dic = {}
        file_list = [x for x in os.listdir(xml_dir) if x.endswith(".xml")]
        for f in file_list:
            print(str(f))

            #解析每个xml的信息
            full_path = os.path.join(xml_dir,f)
            with open(full_path,"r") as fi:
                data_dict = xmltodict.parse(fi.read())
                dic.setdefault(str(f),data_dict)
        json.dump(dic,jsf)
    print("json save success!")


if __name__ == '__main__':
    #Args:
    xml_dir = '/media/mlc/新加卷/华为展厅/上报项目/coco/images/train2017'
    jsonfile = 'train2017.json'

    #process:
    # fl = get_all_xml_file(xml_dir)
    save_to_json(xml_dir,jsonfile)