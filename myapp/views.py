from django.shortcuts import render
from django.http import HttpResponse
import json


def index(request):

    def parser(input_string):
        with open("myapp/data/grammaire.json", "r") as file:
            parsed_data = {}
            json_file = json.load(file)
            grammar = json_file["Fichier-Perso-PIN-Change"]
            for field in grammar:
                field_name = field["FIELD"]
                field_type = field["TYPE"]
                size = int(field["SIZE"])
                offset1 = int(field["OFFSET1"]) - 1
                offset2 = int(field["OFFSET2"])
                s = slice(offset1, offset2)
                input_slice = input_string[s]
                slice_length = offset2-offset1
                if field_type == "AN":
                    if len(input_slice) == size and slice_length == size and input_slice.isalnum():
                        key = field_name
                        value = input_slice
                        parsed_data
                        parsed_data[key] = value
                elif field_type == "N":
                    if len(input_slice) == size and slice_length == size and input_slice.isnumeric():
                        key = field_name
                        value = input_slice
                        parsed_data[key] = value
                else:
                    continue
        return parsed_data
    

    final_result = {}
    dict_key = 0
    with open("myapp/data/CV00011P2.56159", "r") as file:
        lines = file.readlines()
        for line in lines[1:-1]:
            result = parser(line)
            final_result[str(dict_key)] = result
            dict_key += 1
    
    #dict2D = {"dict1" : { "key1" : "vale1"}, "dict2" : { "key2" : "vale2"}}
    return render(request,'index.html', {"data" : final_result})
