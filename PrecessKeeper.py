import json
import os
import time

obj = open("config.json")
process = json.load(obj)
obj.close()

main_path = os.getcwd()
batch_path = main_path+"/batch"

rnk = 0
time.sleep(1)

try:
    while(1):
        print(time.strftime('%Y/%m/%d %T')+" ---------- %d" % rnk)

        for para in process.keys():
            content = process[para]
            if content["label"]=="0": continue

            print(time.strftime('%Y/%m/%d %T')+' - '+content["title"])

            log = os.popen(content["check"].replace("${batch_path}",batch_path))
            logs = "".join(log.readlines())

            if content["key"] not in logs:
                print(time.strftime('%Y/%m/%d %T')+' ----- No Process & Will Re-Run')
                os.system(content["run"].replace("${batch_path}",batch_path))
            else:
                print(time.strftime('%Y/%m/%d %T')+' ----- Still Running')

        time.sleep(60)
        rnk += 1
        #if rnk>1: break

except Exception as e:
    print(time.strftime('%Y/%m/%d %T')+"- Exception")
    print(str(e))