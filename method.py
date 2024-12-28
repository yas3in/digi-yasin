class Owner:
    
    owner_list = [6719097274]
    
    
    def __init__(self, id):
        self.id = id
        
        
    def ban(self):
        if self.id in Owner.owner_list:
            return True
        return False
    
    
class Members:
    
    def __init__(self):
        pass

        
    def date(self, month):
        match month: 
            case 1:
                return "فروردین"
            case 2:
                return "اردیبهشت"
            case 3:
                return "خرداد"
            case 4:
                return "تیر"
            case 5:
                return "مرداد"
            case 6:
                return "شهریور"
            case 7:
                return "مهر"
            case 8:
                return "آبان"
            case 9:
                return "آذر"
            case 10:
                return "دی"
            case 11:
                return "بهمن"
            case 12:
                return "اسفند"