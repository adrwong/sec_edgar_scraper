import mmap

'''

This programme returns a list of Russell 3000 stocks with all stocks name formatted to
match the name in Edgar CIK index to retrieve the CIK of each of the Russell 3000 stocks

'''

# https://content.ftserussell.com/sites/default/files/ru3000_membershiplist_20210628.pdf
stock_list_raw = open("ru3000_membershiplist_20210628_original.txt", "r")
# split stock list by line
stock_list = stock_list_raw.read().splitlines()
# filter out all blank line
stock_list = list(filter(lambda a: a !='', stock_list))
bk_list = list(filter(lambda a: a !='', stock_list))
# remove ticker name
for i in range(0, len(stock_list)):
    if i == len(stock_list) + 1 or i == len(stock_list):
        break
    del stock_list[i]

print(len(stock_list))

out_nfound = open("nfound.txt", "w")
out_found = open("found.txt", "w")
out_cik = open("R3000_CIK_list.txt", "w")
found_stock_list = []

# https://www.sec.gov/include/ticker.txt
with open("edgar_cik_lookup_bysymbol.txt", "r") as f:
    stock_lookup = []
    for s in f.read().splitlines():
        content = s.split("\t")
        content[0] = content[0].upper()
        stock_lookup.append(content)
    
    count = 0
    for s in stock_list:
        for ck in stock_lookup:
            if s == ck[0]:
                count += 1
                print(s +", " + ck[1], file=out_found)
                print(ck[1], file=out_cik)
                stock_list[stock_list.index(s)] = s + "true"
    
    for s in stock_list:
        if s[-4:] != "true":
            print(bk_list[bk_list.index(s)-1], file=out_nfound)
    
    print(count)
    