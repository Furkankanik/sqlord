import os 

def sqlordmap():
    os.system("figlet sqlordmap")
    
    print("""
    sqlordmap Programına hoş geldiniz...

    1 - Mevcut veritabanlarının listesini ekrana getir
    2 - Mevcut veritabanlarındaki tabloları ekrana getir
    3 - Mevcut veritabanlarının tablolarının kolonlarını ve kayıtlarını ekrana getir
    """)
    
    seçim = input("Lütfen yapmak istediğiniz işlemi belirtin (1/2/3): ")

    if seçim == "1":
        site_Adı = input("Hedef site adını giriniz: ")
        os.system("sqlmap -u " + site_Adı + " --dbs")

    elif seçim == "2":
        site_Adı = input("Lütfen hedef sitenin adını giriniz: ")
        os.system("sqlmap -u " + site_Adı + " -D --tables")

    elif seçim == "3":
        site_Adı = input("Lütfen hedef sitenin adını giriniz: ")
        os.system("sqlmap -u " + site_Adı + " -D -T -C --dump")

    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3 giriniz.")

sqlordmap()
