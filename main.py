import re

f=open("sample-example.html","r")
writeDataToFile=open("data.txt","w")

fileData=""

for character in f.read():
    fileData+=character

#regexPattern="<tr>(\s*<td.{1,}\s*.{1,}\s*.{1,}){1,}"

regexPattern="<tr>(\s*<td.{1,}\s*.{1,}\s*.{1,}\s*<td.{1,}\s*<td.{1,}\s*.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*<td.{1,}\s*)\s*<\/tr>"
nameRegex="\">[A-Za-z]{3,}\s[\s]?[A-Za-z]{3,}"
appointmentReferenceRegex="[A-Z]{2}\d{8}-\d{5}"
patientPhoneRegex="\(\d{3}\)\s\d{3}-\d{4}"
statusRegex="[A-Z]{9}"
appointmentDateRegex="\d{2}\s\w{3}\s\d{4}\s\d{2}:\d{2}\s[A-Z]{2}"
trackingRegex=">\s\d{5,}"
addressRegex="(\w{1,}\s*\w{1,}\s\w{1,},\s)?(\w{1,}\s)?(\w{1,},\s)?(\w(1,)\s)?(\w{1,}\s)?(\w{1,}\s)?(\w{1,}\s\w{1,},\s)?\w{1,},\s*(\s*|\w{1,})\s\w{1,},\s\w{1,},.\d{5}"
row=""
for i in re.findall(regexPattern,fileData):
    data=i
    name=re.findall(nameRegex,data)
    tracking=re.findall(trackingRegex,data)

    row=re.findall(appointmentReferenceRegex,data)[0]+" "+re.findall(nameRegex,data)[0][2:]+" "+re.findall(patientPhoneRegex,data)[0]+" "

    if len(name)==1:
        row+=" N/A "
    else:
        row+=re.findall(nameRegex,data)[1][2:]+" "+re.findall(statusRegex,data)[0]+" "

    if len(tracking)==0:
        row+=" n/a "
    else:
        row+=re.findall(trackingRegex,data)[0][2:]+" "
    row+=re.findall(appointmentDateRegex,data)[0]+"\n"

    writeDataToFile.writelines(row)







