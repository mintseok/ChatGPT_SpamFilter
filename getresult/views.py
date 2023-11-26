from django.shortcuts import render
from .tryout_gpt import call_gpt
import os
import json
import glob

# Create your views here.
def getresult(request):
    # ChatGPT 호출 및 csv 쿼리 보내기
    print("\nCalled getresult from views.py\n")
    call_gpt()
    
    # 보내고 결과 읽기
    SAVE_FILE_DIR_PATH = "./getresult/results"
    assert os.path.exists(SAVE_FILE_DIR_PATH), f"{SAVE_FILE_DIR_PATH} 디렉토리가 존재하지 않습니다."
    
        # read KISA-provided spam data file path 
    spam_result_file_path_list = glob.glob(os.path.join(SAVE_FILE_DIR_PATH, "*.json"))
    # 뒤의 파일이 가장 최근 파일임
    SPAM_RESULT_PATH = spam_result_file_path_list[-1]
    with open(SPAM_RESULT_PATH, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        # print(json.dumps(data, ensure_ascii=False, indent=3))
    
    year = SPAM_RESULT_PATH[20:24]
    month = SPAM_RESULT_PATH[24:26]
    date = SPAM_RESULT_PATH[26:28]
    spam_data_name = year+"년 "+month+"월 "+date+"일 CSV file"

    spam_data = []
    for i in range(len(data)):
        sd_dict = {}
        sd_dict['content'] = data[i]['content'].split(',')[0]
        sd_dict['query_response'] = data[i]['query_response']
        time1 = data[i]['time1']
        date = time1[0:4]+"년 "+time1[4:6]+"월 "+time1[6:8]+"일"
        time = time1[8:10]+"시 "+time1[10:12]+"분"
        sd_dict['date'] = date
        sd_dict['time'] = time
        sd_dict['label'] = data[i]['label']
        spam_data.append(sd_dict)
    
    context = {
        "spam_data_name": spam_data_name,
        "spam_data": spam_data
    }
    
    return render(request, 'getresult.html', context)