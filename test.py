
class Contact(object):

    def __init__(self, name, email,phone):
        self.name = name
        self.email = email
        self.phone = phone


    def __str__(self):
        return f"{self.name} <{self.email}> {self.phone}"



class Leads(object):
    def __init__(self, name, email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"{self.name} <{self.email}> {self.phone}"
    

class registrants(object):

    def __init__(self, name, email,phone):
        self.name = name
        self.email = email
        self.phone = phone


    def __str__(self):
        return f"{self.name} <{self.email}> {self.phone}"



if __name__ == "__main__":

    obj_con=[] 
    obj_le=[] 
    obj_reg =[]
    obj_con.append(Contact('Alice Brown' ,None,'1231112223'))
    obj_con.append(Contact('Bob Crown' ,'bob@crowns.com',None))
    obj_con.append(Contact('Carlos Drew' ,'carl@drewess.com','3453334445'))
    obj_con.append(Contact('Doug Emerty' ,None,'4564445556'))
    obj_con.append(Contact('Egan Fair' ,'eg@fairness.com','5675556667'))
    obj_le.append(Leads(None,'kevin@keith.com',None))
    obj_le.append(Leads('Lucy' ,'lucy@liu.com','3210001112'))
    obj_le.append(Leads('Mary Middle' ,'mary@middle.com','3331112223'))
    obj_le.append(Leads(None ,None,'4442223334'))
    obj_le.append(Leads(None ,'ole@olson.com',None))

    obj_reg.append(registrants('Lucy Liu','lucy@liu.com',None))
    obj_reg.append(registrants('Doug' ,'doug@emmy.com','4564445556'))
    obj_reg.append(registrants('Uma Thurman' ,'uma@thurs.com',None)) 
    reg1={
        "registrant": 
        { 
            "name": "Tom Jones", 
            "email": "tom@jones.com",
            "phone": "3211234567",
            }
            }
    if  reg1['registrant']['email'] in [c.email for c in obj_con] :
        print('email matched')
          
    elif reg1['registrant']['phone'] in [c.phone for c in obj_con] :
        print("phone matched")
                
    else:
        for l in obj_le:
            if reg1['registrant']['email'] == l.email:
                temp=l
                obj_le.remove(l)
                obj_con.append(temp)
            elif not reg1['registrant']['phone'] == l.phone :
                obj_con.append(Contact(l.name,l.email,l.phone))
    print("**********CONTACTS*************")
    for c in obj_con:
        print(c.__str__())
        # print('name %s email %s phone %s '%(c.name,c.email,c.phone ))
    print("**********LEADS****************")
    for le in obj_le:
        print(le.__str__())
        # print('name %s email %s phone %s '%(le.name,le.email, le.phone ))
    print("**********REGISTRANTS**********")
    for r in obj_reg:
        print(r.__str__())
        # print('name %s email %s phone %s '%(r.name,c.email,c.phone))
