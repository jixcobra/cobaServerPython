import time
from androguard.misc import AnalyzeAPK
import sys
import os

def frequency(dx, api_freq):
    for c in dx.get_classes():
    #for c in dx.get_external_classes():
        for key, items in c.xrefto.items():
            for item in items:
                kind, method, offset = item
                if method in api_freq:
                    api_freq[method] += 1
                else:
                    api_freq[method] = 1

def main():
    input_dir = './recv'
    file_num = 1
    tic = time.time()
    # user_input = raw_input("Masukkan Lokasi File: ")
    user_input = os.path.join(input_dir, '%06d.apk' % file_num)
    assert os.path.exists(user_input), "file tidak ditemukan pada, "+str(user_input)
    print("File Ditemukan !!")
    a, d, dx = AnalyzeAPK(user_input)
    dx.create_xref()
    package_name = a.get_package()
    permissions = a.get_permissions()
    val =["android.permission.READ_PHONE_STATE", "android.permission.RECEIVE_BOOT_COMPLETED", "android.permission.READ_SMS", "android.permission.WRITE_SMS", "android.permission.SEND_SMS", "android.permission.RECEIVE_SMS", "android.permission.CALL_PHONE","android.permission.CHANGE_WIFI_STATE","android.permission.RESTART_PACKAGES","android.permission.GET_TASKS"]
    # valApi = ['Landroid/content/Intent;->getAction()','Ldalvik/system/DexClassLoader;->loadClass','Landroid/telephony/TelephonyManager;->getDeviceId()','Landroid/telephony/TelephonyManager;->getLine1Number()','Landroid/telephony/TelephonyManager;->getNetworkOperator()','Landroid/telephony/TelephonyManager;->getSimSerialNumber()','Landroid/telephony/TelephonyManager;->getSimOperator()','Landroid/telephony/TelephonyManager;->getSubscriberId()','Landroid/telephony/SmsManager;->sendTextMessage','Landroid/location/LocationManager;->getLastKnownLocation']
    ps = []


    API_freq = dict()
    frequency(dx, API_freq)

    fs = open(os.path.join('./Documents/API-Kurang/coba',package_name+'.txt'), "w")
    #datas = str(sorted(API_freq.items(), key=lambda b:b[1], reverse=True))
    datas = str(sorted(API_freq.items(), key=lambda b:b[1], reverse=True))
    #print(sorted(API_freq.items(), key=lambda b:b[1], reverse=True))
    print(permissions)
    for i in range(0,len(val)):
        if (check(permissions,val[i])):
            ps.append(1)
        else :
            ps.append(0)

    if 'Landroid/content/Intent;->getAction()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Ldalvik/system/DexClassLoader;->loadClass' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getDeviceId()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getLine1Number()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getNetworkOperator()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getSimSerialNumber()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getSimOperator()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/TelephonyManager;->getSubscriberId()' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/telephony/SmsManager;->sendTextMessage' in datas:
        ps.append(1)
    else :
        ps.append(0)

    if 'Landroid/location/LocationManager;->getLastKnownLocation' in datas:
        ps.append(1)
    else :
        ps.append(0)

    ps.append(package_name)

    print(ps)

    # fs.write(datas)
    # #print(time.time()-tic)
    # fs.close()

    #print(sorted(API_freq.items(), key=lambda b:b[1], reverse=True))
    print(time.time()-tic)
    print("Done !!!")

    return ps
    file_num += 1

def check(permissions, val):
    for x in permissions :
        if x == val :
            return True



if __name__ == '__main__':
    main()