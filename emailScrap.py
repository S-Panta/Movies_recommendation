import re
import json
with open("websiteData.txt",encoding='UTF-8') as f:
    lines = f.read()
    # print(lines)
    lst = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",lines)
    print(lst)

number = len(lst)
email_dic = {}
for email in lst:
    if email_dic.get(email)==None:
        email_dic[email] = {
            "Occurrence": 1,
            "EmailType": "Non-Human" if (
                        len(email.split('@')[0].split('.')) == 1 or len(email.split('@')[0]) < 8) else "Human"
        }
    else:
        email_dic[email]['Occurrence'] = email_dic[email]['Occurrence'] + 1

print(email_dic)
json_object = json.dumps(email_dic,indent=1)
with open("result.json", "w") as outfile:
    outfile.write(json_object)
    print(json_object)

