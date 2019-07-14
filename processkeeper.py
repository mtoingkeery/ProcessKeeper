import json
import os
import time

main_path = "/opt/processkeeper/"
batch_path = main_path+"batch"

rnk = 0
time.sleep(1)

try:
    while(1):
        print(time.strftime('%Y/%m/%d %T')+" ----------------------------------------- %d" % rnk)

        obj = open(main_path+"config.json","r")
        process = json.load(obj)
        obj.close()

        for para in process.keys():
            content = process[para]
            print(time.strftime('%Y/%m/%d %T')+' - '+content["title"]+' - '+content["label"])

            log = os.popen(content["check"].replace("${batch_path}",batch_path))
            log_lines = log.readlines()
            log_total = "".join(log_lines)

            if content["label"]=="0":
                if content["key"] not in log_total:
                    print(time.strftime('%Y/%m/%d %T')+' ---------- No Process')
                else:
                    print(time.strftime('%Y/%m/%d %T')+' ---------- Still Running & Will Kill')
                    for log_line in log_lines:
                        if content["key"] in log_line:
                            pid = log_line.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").split(" ")[1]
                            os.system("kill -9 %s" % pid)
            else:
                if content["key"] not in log_total:
                    print(time.strftime('%Y/%m/%d %T')+' ---------- No Process & Will Re-Run')
                    os.system(content["run"].replace("${batch_path}",batch_path))
                else:
                    print(time.strftime('%Y/%m/%d %T')+' ---------- Still Running')

        time.sleep(60)
        rnk += 1
        #if rnk>6: break

except Exception as e:
    print(time.strftime('%Y/%m/%d %T')+"- Exception")
    print(str(e))
