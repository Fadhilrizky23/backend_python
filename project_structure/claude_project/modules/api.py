import config

# print(utils.data_valid)

def hitung_rata_rata(data): 
    store_jumlah = 0 
    rata_rata = store_jumlah / len(data)

    for i in data : 
        rata_rata += float(i["suhu"])

    return rata_rata

# print(utils.list_data)

# hitung_rata_rata(utils.list_data) 



def sensor_extreme(data):
    new_data = []
    for i in data : 
        # Validasi All Sensor 
        # print(i["sensor"], "suhu : ", i["suhu"], "-> Lolos ? ", float(i["suhu"]) >= config.SUHU_EXTREM )
        if float(i["suhu"])>= 70 : 
            data_extreme = {
                "sensor" : i["sensor"],
                "suhu" : i["suhu"],
                "kelembapan" : i["kelembapan"]
                }    
            new_data.append(data_extreme) #masuk di dalm loop if 
    return new_data



# print(sensor_extreme(utils.list_data))