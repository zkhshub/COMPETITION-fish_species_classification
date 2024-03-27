import json
import shutil

from pycocotools.coco import COCO

def RemakeData(before_json_path, after_json_path, before_data_path, after_data_path, download=False):
    new_train = {
        "images": [],
        "annotations": [],
        "categories": [
            {
                "id": 0,
                "name": "농어",
                "supercategory": ""
            },
            {
                "id": 1,
                "name": "베스",
                "supercategory": ""
            },
            {
                "id": 2,
                "name": "숭어",
                "supercategory": ""
            },
            {
                "id": 3,
                "name": "강준치",
                "supercategory": ""
            },
            {
                "id": 4,
                "name": "블루길",
                "supercategory": ""
            },
            {
                "id": 5,
                "name": "잉어",
                "supercategory": ""
            },
            {
                "id": 6,
                "name": "붕어",
                "supercategory": ""
            },
            {
                "id": 7,
                "name": "누치",
                "supercategory": ""
            }
        ]
    }
    
    # load coco format data
    coco = COCO(before_json_path)
    
    # append image info, if download == true : image download
    all_image_id = coco.getImgIds()
    no_annotation_list = []
    for image_id in all_image_id:
        annotation_id = coco.getAnnIds(imgIds=image_id, iscrowd=False)
        if len(annotation_id) == 0: 
            no_annotation_list.append(image_id)
        else:
            image_info = coco.loadImgs(image_id)[0]
            image_file_name = image_info['file_name']
            image_path = before_data_path + image_file_name
            output_path = after_data_path + image_file_name
            
            # image file download
            if download:
                shutil.copy(image_path, output_path)
                
            new_train['images'].append(image_info)
                
    # append annotation info
    all_annotation_id = coco.getAnnIds()
    for annotation_id in all_annotation_id:
        annotation_info = coco.loadAnns(annotation_id)[0]
        new_train['annotations'].append(annotation_info)
    
    # make coco format json file
    with open(after_json_path, 'w', encoding='UTF-8') as f:
        json.dump(new_train, f, ensure_ascii=False)


if __name__ == '__main__':
    '''
        json파일이 생성되면 command 창에 아래 명령어를 참고해서 입력해주세요. 보기 깔끔하게 바뀐 json파일이 새로 생성됩니다.
        예시)
            jq . /Users/a01/어종분류/데이터/new_train.json > output.json 
        
        의미)
            jq . 바꾸고싶은_파일_경로 > 경로/원하는_파일명.json
    '''
    '''
        path 입력 예시입니다. 해당 path 입력 예시를 참고해서 path를 설정해주세요. json경로는 파일명까지 들어가야 합니다.
        
        before_json_path = '/Users/a01/어종분류/dataset/labels/train.json'
        after_json_path = '/Users/a01/어종분류/데이터/new_train.json'
        before_data_path = '/Users/a01/어종분류/dataset/train/'
        after_data_path = '/Users/a01/어종분류/데이터/'
    '''
    before_json_path = "/USER/mnc/fish/data/labels/train.json"
    after_json_path  = "/USER/mnc/fish/data/labels_re/train.json"
    before_data_path = "/USER/mnc/fish/data/train/"
    after_data_path  = "/USER/mnc/fish/data/train_re_all/"
    
    # download를 True로 설정하면 원하시는 폴더에 annotation이 있는 이미지들이 copy됩니다.
    RemakeData(before_json_path, after_json_path, before_data_path, after_data_path, download=True)
