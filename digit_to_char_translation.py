phone=input(" ").replace(" ","")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "10":"Ten",
    "0":"Zero"

}
outpus=" "
for ch in phone:
    outpus+=digits_mapping.get(ch, "!")+ " "
print(outpus)