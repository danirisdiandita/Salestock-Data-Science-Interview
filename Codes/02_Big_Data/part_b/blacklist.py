def initialize(blacklist):
    """
    This function would convert a textfile consists of 
    (name) and (phone_number) and give an output of python
    dictionary with phone number as the key and the 
    name as the value. This is because the phone number is
    more likely to be unique
    
    input: a string of textfile name (example: "blacklist.txt")
    output: {1341441: "Andi", 8565467:"Melisa", ...}
    """
    
    
    with open(blacklist) as f:
        blacklist = f.read()
    blacklist = blacklist.split()
    blacklist_dict = {}
    for i in range(0, len(blacklist), 2):
        blacklist_dict[int(blacklist[i+1])] = blacklist[i]
    return blacklist_dict

API_call = initialize("blacklist.txt")

def check_blacklist(name, phone_number):
    """
    This function would check whether the input (name, phone_number)
    is within the blacklist or not
    
    input: name (a string), phone_number (an integer)
    output: True (if the name and phone_number combination is
            within the blacklist), False (the other way around)
    """
    return API_call.get(phone_number) == name


print("CHECKING THE RESULT")
print(check_blacklist("Andi", 1341441))
print(check_blacklist("Robert", 1311441))
print(check_blacklist("Takeshi", 8321441))
print(check_blacklist("Aslam", 2908345))
