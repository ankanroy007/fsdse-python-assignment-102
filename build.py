def is_rotation(src,dest):
    if(src == None or dest == None):
        return False
    elif(src == "" and dest == ""):
        return True
    elif(src == "" and dest != ""):
        return False
    elif(src != "" and dest == ""):
        return False
    else:
        if(len(src) != len(dest)):
            return False

        for i in range(len(src)):
             if dest.startswith(src[i:]) and dest.endswith(src[:i]):
                 return True
        return False
