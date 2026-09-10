import config
import modules.database as dabes
import modules.api as apii
import modules.utils as utility

# Baca data dari file  
utility.read_data() 


# validasi, ambil yang lolos aja
data_valid = utility.validate_data(utility.list_data) 


#  3. Simpan yang valid ke csv 
dabes.store_data_csv(data_valid,config.OUTPUT_PATH,dabes.action) 

# 4. Hitung rata-rata suhu 
rata_rata = apii.hitung_rata_rata(utility.list_data) 

# Extreme Value 
maxValue = apii.sensor_extreme(utility.list_data)

print(rata_rata)
print(maxValue)








