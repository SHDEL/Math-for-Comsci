t_w = [
    ["Honda", "Mini", "Toyota"],
    ["Mini", "Toyota", "Honda"],
    ["Mini", "Honda", "Toyota"],
]
sale_w = [
    ["อ.วิชญะ", "อ.ธีระ", "อ.สันธนะ"],
    ["อ.สันธนะ", "อ.ธีระ", "อ.วิชญะ"],
    ["อ.วิชญะ", "อ.ธีระ", "อ.สันธนะ"],
]
tc = ["อ.วิชญะ", "อ.ธีระ", "อ.สันธนะ"]
tc_w = [False, False, False] 
sale = ["Mini", "Honda", "Toyota"]
sale_get = [-1, -1, -1] 

tc_at = 0 
while tc_w.count(False) > 0: 
    if tc_w[tc_at] == False: 
        sale_at = t_w[tc_at][0] 
        t_w[tc_at].pop(0) 
        if sale_get[sale.index(sale_at)] != -1:
            if (
                sale_w[sale.index(sale_at)].index(tc[tc_at]) 
                < sale_w[sale.index(sale_at)].index(
                    tc[sale_get[sale.index(sale_at)]]
                ) 
                and sale_w[sale.index(sale_at)].index(tc[tc_at]) >= 0):
                
                tc_w[sale_get[sale.index(sale_at)]] = False
                sale_get[sale.index(sale_at)] = tc_at
                tc_w[tc_at] = True
        else:
            sale_get[sale.index(sale_at)] = tc_at
            tc_w[tc_at] = True
        
    if tc_at + 1 >= len(tc):
        tc_at = 0
    else:
        tc_at += 1

for i in range(0, len(tc)):
    print("คนขาย " + sale[i], tc[sale_get[i]], sep=" เลือก ")