'''
将json文件重新转换为xml文档
'''
import os 
import xmltodict
import json 

def json2xml(jsonfile,save_dir):
    with open(jsonfile,"r") as f:
        dict_obj = json.load(f)
        print(type(dict_obj))
        for key in dict_obj:
            print(key)
            with open(os.path.join(save_dir,key),"w") as xmlfile:
                data = xmltodict.unparse(dict_obj[key],pretty=True)
                xmlfile.write(data)
    print("write success!")




if __name__ == '__main__':
    #Args:
    jsonfile = 'val2017.json'
    xml_save_dir = jsonfile.split(".")[0]
    print(xml_save_dir)
    if not os.path.exists(xml_save_dir):
        os.makedirs(xml_save_dir)
    json2xml(jsonfile,xml_save_dir)