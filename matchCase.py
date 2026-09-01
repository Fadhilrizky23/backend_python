hari = input("Hari ini adalah hari : ").lower()

match hari :
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat" :
        print("Hari Kerja") 
    case "sabtu" | "minggu" :
        print("Hari Libur")
    case _: #ini kayak else di if else 
        print("Nama hari tidak Valid") 









