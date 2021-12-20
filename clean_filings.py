import os
import errno
import re
rootdir = './scraped_data'

total = 198835

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        with open(os.path.join(subdir, file)) as f:
            data_path = './cleaned_data/' + file
            if not os.path.exists(os.path.dirname(data_path)):
                try:
                    os.makedirs(os.path.dirname(data_path))
                except OSError as exc:
                    if exc.errno != errno.EEXIST:
                        raise
            with open(data_path, 'w', encoding='utf-8') as tc:
                    try:
                        text = f.read()
                        type_start = text.find("CONFORMED SUBMISSION TYPE:	") + len("CONFORMED SUBMISSION TYPE:	")
                        type_end = text.find("PUBLIC DOCUMENT COUNT:")
                        ftype = text[type_start:type_end]
                        blpos =  ftype.find('\n')
                        ftype = ftype[:blpos]

                        if ftype == '10-K':
                            p11_pos = text.find('PART IV')
                            p12_pos = text[p11_pos+len('PART IV'):].find('PART I')
                            result = text[p11_pos+p12_pos+len('PART I'):]
                            end_pos = result.find('PART III')
                            print(result[:end_pos],file=tc)

                        if ftype == '10-Q':
                            p1_pos = re.search('item 1', text, re.IGNORECASE).start()
                            xbrl_pos = -1
                            try:
                                xbrl_pos = re.search('XBRL TAXONOMY EXTENSION SCHEMA DOCUMENT', text, re.IGNORECASE).start()
                            except Exception as e:
                                print(e)
                            print(text[p1_pos:xbrl_pos], file=tc)

                    except Exception as e:
                        print(e)
                                 
            tc.close()
        f.close()
        total-=1
        print(str(total) + 'files remaining')
    
                    
