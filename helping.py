def razdelitel (stroka:str, simvol:str,) -> list:
    spisok_vsex = []
    while stroka != '':
        index = stroka.find(simvol)
        if index != -1:
            spisok_vsex.append(stroka[0:index])
            stroka = stroka[index+1:]
        else:
            spisok_vsex.append(stroka)
            stroka = ''
    return spisok_vsex

