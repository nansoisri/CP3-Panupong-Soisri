#Master
water = 10
instantNoodle = 7
sodaWater = 6
energyDrink = 10
bread = 15
#---------------


usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "customer"  and passwordInput == "1234":
    print("              Welcome to Easy Shop               ")
    print("                                                 ")
    print("----------------รายการสินค้าที่ต้องการ----------------")
    print("1. น้ำดื่ม (ขนาด 600 มล.)              ราคา ", water," บาท")
    print("2. บะหมี่กึ่งสำเร็จรูป                    ราคา  ", instantNoodle, " บาท")
    print("3. เครื่องดื่มน้ำอัดลม (กระป๋อง 325 มล.)   ราคา  ",sodaWater," บาท")
    print("4. เครื่องดื่มชูกำลัง                     ราคา ",energyDrink," บาท")
    print("5. ขนมปัง                            ราคา ", bread," บาท")
    print("-------------------------------------------------")
    userSelected = int(input("ระบุเลขสินค้าที่ต้องการ:  "))
    if userSelected == 1:
        unit = int(input("จำนวนที่ต้องการ: "))
        total = water * unit
        print("ราคารวม: ", total, " บาท")
    elif userSelected == 2:
        unit = int(input("จำนวนที่ต้องการ: "))
        total = instantNoodle * unit
        print("ราคารวม: ", total, " บาท")
    elif userSelected == 3:
        unit = int(input("จำนวนที่ต้องการ: "))
        total = sodaWater * unit
        print("ราคารวม: ", total, " บาท")
    elif userSelected == 4:
        unit = int(input("จำนวนที่ต้องการ: "))
        total = bread * unit
        print("ราคารวม: ", total, " บาท")