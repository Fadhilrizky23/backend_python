
import modules.utils as utiliti
import config


list_data_util = utiliti.data_valid
path = config.OUTPUT_PATH
action = "a"


def store_data_csv(list_data,path,action) : 
    with open(path,action) as file: 
        for row in list_data : 
            baris = f"{row["sensor"]},{row["suhu"]},{row["kelembapan"]}\n"
            file.writelines(baris)


# store_data_csv(list_data_util,path,action)
