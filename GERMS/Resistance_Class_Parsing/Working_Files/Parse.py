import sys
import os
Input = sys.argv[1]
working_files_path = sys.argv[2]
Output = sys.argv[3]

# Input = "/Users/schuyler/SS/test/test.out"
# working_files_path = "/Users/schuyler/Dropbox/Scripts/Resistance_Class_Parsing"
# Output = "/Users/schuyler/SS/test/out.out"

for line in open(Input):
    line = line.rstrip().strip('\"')
    try:
        dat = line.split()[1]
    except:
        dat = line.split()[0]
    dat2 = dat.split('|')[-1]
    dat3 = dat2.split('_')[-1]

    if dat3.lower() == "int":
        gene = dat2.split('_int')[0]
        gene = gene.replace("/","_")
        out = open('%s/Int/%s.blast'  %(Output, gene), 'a+')

    elif dat3.lower() == "card":
        gene = dat2.split('_')[0][:3]
        out = open('%s/Card/%s.blast'  %(Output, gene), 'a+')

    elif dat3.lower() == "megares":
        classes = dat.split('|')[-3].lower()
        if len(dat2.split('_')) == 5:
            gene = dat2.split('_')[2]
        else:
            gene = dat2.split('_')[0]
        for AB_class in open('%s/Working_Files/Classes.list' %working_files_path):
            if classes.lower() in AB_class.lower():
                AB_C = AB_class.split('\n')[0]
        out = open('%s/Megares/%s/%s.blast'  %(Output, AB_C, gene), 'a+')
        megout = open('%s/%s.blast' %(Output, AB_C), 'a+')
        megout.write(line + '\n')

    out.write(line + '\n')

cardlist = os.listdir('%s/Card' % Output)
for file in cardlist:
	code = file.split('.')[0]
	if code.lower() in open('%s/Working_Files/AR_DB_Classes' % (working_files_path)).read().lower():
		for AB_class in open('%s/Working_Files/Classes.list' %working_files_path):
			AB_C = AB_class.split('\n')[0]
			if code.lower() in open('%s/Working_Files/Keys/%s.list' %(working_files_path, AB_C)).read().lower():
				out = open('%s/%s.blast'  %(Output, AB_C), 'a+')
				break
	else:
    		out = open('%s/Uncategorized.blast'  % Output, 'a+')

	for line in open('%s/Card/%s' % (Output,file)):
		out.write(line)
	# os.remove('%s/Card/%s' % (Output,file))



