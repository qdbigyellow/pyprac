
# https://mp.weixin.qq.com/s/QPWKLM2R49NPetHUQYyuig
import json
import string
import pathlib

curdir = pathlib.Path(__file__).parent.absolute()
with open(curdir.joinpath("data.json")) as f:
    data = json.loads(f.read())
    content = ""
    for i, (author, title) in enumerate(data.items()):
        content += "<tr>"
        content += f"<td>{i + 1}</td>"
        content += f"<td>{author}</td>"
        content += f"<td>{title}</td>"
        content += "</tr>"
    
with open(curdir.joinpath("template.html")) as t:
    template = string.Template(t.read())

# 在template模板里，有${elements}， 通过 string.Template.substitute(), 把 elements 替代成我们需要的内容
    
final_output = template.substitute(elements=content)
#  安全， 但谨慎使用
# final_output = template.safe_substitute(elements=content)
with open(curdir.joinpath("report.html"), "w") as output:
    output.write(final_output)