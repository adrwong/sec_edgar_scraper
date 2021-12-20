import mmap

'''

This programme returns a list of Russell 3000 stocks with all stocks name formatted to
match the name in Edgar CIK index to retrieve the CIK of each of the Russell 3000 stocks

'''

# https://content.ftserussell.com/sites/default/files/ru3000_membershiplist_20210628.pdf
nfound_stock_list_raw = open("ru3000_membershiplist_20210628.txt", "r")
# split stock list by line
nfound_stock_list = nfound_stock_list_raw.read().splitlines()
# filter out all blank line
nfound_stock_list = list(filter(lambda a: a !='', nfound_stock_list))
# remove ticker symbol
for i in range(1, len(nfound_stock_list)):
    if i == len(nfound_stock_list) + 1:
        break
    del nfound_stock_list[i]

# print(nfound_stock_list)

out_nfound = open("nfound.txt", "w")
out_found = open("found.txt", "w")
out_cik = open("R3000_CIK_list.txt", "w")
found_stock_list = []

# first formatting stocks name to match name in cik lookup table 
for i in range(len(nfound_stock_list)):
    if nfound_stock_list[i].find("CL A") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" CL A", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CL B") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" CL B", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CL C") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" CL C", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("(A)") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" (A)", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("(B)") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" (B)", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("(C)") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace(" (C)", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CLASS A") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace("CLASS A", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CLASS B") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace("CLASS B", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CLASS C") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace("CLASS C", "")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("CORP.") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace("CORP.", "CORP")
        # print(nfound_stock_list[i])
    if nfound_stock_list[i].find("INC.") != -1:
        nfound_stock_list[i] = nfound_stock_list[i].replace("INC.", "INC")
        # print(nfound_stock_list[i])

# https://www.sec.gov/Archives/edgar/cik-lookup-data.txt
with open('edgar_cik_lookup.txt') as cik_lookup:
    s = mmap.mmap(cik_lookup.fileno(), 0, access=mmap.ACCESS_READ)
    
    temp_nfound =[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        if s.find(bytes(e, 'utf-8')) != -1:
            print(e, file=out_found)
            found_stock_list.append(e)
        else: 
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
        
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # second formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find("CORPORATION") != -1:
            n = e.replace("CORPORATION", "CORP")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # third formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find("INC") != -1:
            n = e.replace(" INC", ", INC")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # forth formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find("INTL") != -1:
            n = e.replace("INTL", "INTERNATIONAL")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # fifth formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find("THE") != -1:
            n = e.replace("THE ", "")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # sixth formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find(".") != -1:
            n = e.replace(".", " ")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    # seventh formatting
    nfound_stock_list = temp_nfound
    temp_nfound=[]
    while nfound_stock_list:
        e = nfound_stock_list[0]
        n = e
        if e.find("AND") != -1:
            n = e.replace("AND", "&")
        if s.find(bytes(n, 'utf-8')) != -1:
            print(n, file=out_found)
            found_stock_list.append(n)
        else:
            temp_nfound.append(e)
        nfound_stock_list.pop(0)
            
    print("found: " + str(len(found_stock_list)))
    print("nfound: " + str(len(temp_nfound)))
    
    nfound_stock_list = temp_nfound
    temp_nfound = []
    
    # print(found_stock_list)
    if len(nfound_stock_list) == 0:
        cik_list = []
        # print(s.read().splitlines())
        for line in s.read().splitlines():
            for stock in found_stock_list:
                if line.decode("utf-8").find(stock) != -1:
                    
                    cik_list.append(line.decode("utf-8")[-11:][:10])
                    # print("found: " + stock +  ", line: " + line.decode("utf-8"))
                    # cik_list.append(line)
                    # print(line)
                    
        cik_list = list(dict.fromkeys(cik_list))
        for cik in cik_list:
            print(cik, file=out_cik)
    print(len(cik_list))
        

    
for e in nfound_stock_list:
    print(e, file=out_nfound)
    
# If still have not found stock in russell 3000 list, manual name-matching is required
# Ard 300 names required manual name-matching after filtering for 7 times

print(len(found_stock_list))