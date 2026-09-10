
import config


list_data = []
data_valid =[]

def read_data():
    with open(config.INPUT_PATH, 'r') as file: 

        for i in file : 
            if i == '\n':
                continue
            list_sensor = i.split(',')
            sensor = list_sensor[0]
            temp = list_sensor[1]
            humid = list_sensor[2].strip('\n')


            data = {
                "sensor": sensor,
                "suhu": temp,
                "kelembapan":humid
            } 

            list_data.append(data)

# read_data()


def validate_data(data):
    for i in range(len(data)):
        if float(data[i]["suhu"]) > config.SUHU_MIN and float(data[i]["suhu"]) <= config.SUHU_MAX :
            data_new = {
                "sensor" : data[i]["sensor"],
                "suhu" : data[i]["suhu"],
                "kelembapan" : data[i]["kelembapan"]
            }

             # Store data yang valid aja buat Return 
            data_valid.append(data_new)
    return data_valid
                


# validate_data(list_data)
