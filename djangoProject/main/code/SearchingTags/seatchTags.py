
tagPY = 0
tagSQL = 0
tagDataS = 0

def search_tags(text):
    fullstring = text
    arrayStr = ["python","Python","питон"]
    arraySQL = ["sql", "SQL", "PostgreSQL", "постгрес","postgres","СУБД", "субд", "эскуэль", "базы данных"]
    arrayDataS = ["Математик", "дата","саенс","data","Data", "математик"]

    global tagPY, tagSQL, tagDataS
    tagPY, tagSQL, tagDataS = 0, 0, 0
    for i in range(len(arrayStr)):
        if arrayStr[i] in fullstring:
            print("PY found!")
            tagPY = 1
        else:
            print("not")

    for i in range(len(arraySQL )):
        if arraySQL [i] in fullstring:
            print("SQL found!")
            tagSQL = 1
        else:
            print("not")

    for i in range(len(arrayDataS )):
        if arrayDataS [i] in fullstring:
            print("DataS found!")
            tagDataS = 1
        else:
            print("not")




def getTag(tag):
    if tag=="PY":
        return tagPY
    if tag=="SQL":
        return tagSQL
    if tag=="DataS":
        return tagDataS

