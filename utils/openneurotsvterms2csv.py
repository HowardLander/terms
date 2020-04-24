import os, sys, json
import pandas as pd
import prov.model as pm
from argparse import ArgumentParser
from more_itertools import sliced
from datetime import datetime



def ValueType(pathtotsv,term):
    '''
    :param pathtotsv: path to the tsv file
    :param term: BIDS term
    :return: Type of input of the given term
    '''

    #open the tsv file as a data frame
    df = pd.read_csv(pathtotsv, error_bad_lines=False, sep = '\t')

    # iter through the rows based on the term and returns a value type
    for (i,row) in df.iterrows():
        if not pd.isnull(row[term]):
            if isinstance(row[term],int):
                return(pm.XSD["integer"])
            elif isinstance(row[term],str):
                return(pm.XSD["string"])
            elif isinstance(row[term],float):
                return(pm.XSD["float"])


def json_des(file, root_dir, term):
    '''
    :return: json_des looks for a json file that matches the given tsv file, locates the json file, and extract and returns a description of the phenotype term
    '''


    #extracts the name of the tsv file without the extension
    tsvfile = os.path.splitext(file)[0]


    #parse through the phenotype directory looking for a matching json file
    for root, dirs, files in os.walk(root_dir, topdown=True):
        json_path = os.path.join(root_dir, root)
        #if phenotype has other directories look for json in those directories
        for dir in dirs:
            #set a path
            dir_root = os.path.join(json_path, dir)
            for rt, dr, fl in os.walk(dir_root, topdown=True):
                for j in fl:
                    if j.endswith('json'):
                        # extract name of json file and check if it matches the given tsv file name
                        Json = os.path.splitext(j)[0]
                        if Json == tsvfile:
                            json_path2 = os.path.join(dir_root, j)

                            #open json and extract the term description
                            with open(json_path2) as f:
                                jread = json.load(f)
                                for k in jread:
                                    if k == term:
                                        for emp in jread[term]:
                                            #check if the dictionary has a description element
                                            if emp == 'Description':
                                                jsterm = jread[term]['Description']
                                                json_term =  jsterm
                                                return json_term
                                            else:
                                                continue

        #look for matching json file in the phenotype directory
        for j_file in files:
            if j_file.endswith('json'):
                # extract name of json file and check if it matches the given tsv file name
                jfile = os.path.splitext(j_file)[0]
                if jfile == tsvfile:
                    json_path1 = os.path.join(json_path, j_file)

                    #open json and extract the term description
                    with open(json_path1) as d:
                        j_read = json.load(d)
                        for key in j_read:
                            if key == term:
                                for empty in j_read[term]:
                                    #check if the dictionary has a description element
                                    if empty == 'Description':
                                        js_term = j_read[term]['Description']
                                        json_term = js_term
                                        return json_term
                                    else:
                                        continue


def json_longname(file, root_dir, term):
    '''
    :return: json_des looks for a json file that matches the given tsv file, locates the json file, and extract and returns long name of the phenotype term
    '''


    #extracts the name of the tsv file without the extension
    tsvfile = os.path.splitext(file)[0]


    #parse through the phenotype directory looking for a matching json file
    for root, dirs, files in os.walk(root_dir, topdown=True):
        json_path = os.path.join(root_dir, root)
        #if phenotype has other directories look for json in those directories
        for dir in dirs:
            #set a path
            dir_root = os.path.join(json_path, dir)
            for rt, dr, fl in os.walk(dir_root, topdown=True):
                for j in fl:
                    if j.endswith('json'):
                        # extract name of json file and check if it matches the given tsv file name
                        Json = os.path.splitext(j)[0]
                        if Json == tsvfile:
                            json_path2 = os.path.join(dir_root, j)

                            #open json and extract the term long name
                            with open(json_path2) as f:
                                jread = json.load(f)
                                for k in jread:
                                    if k == term:
                                        for emp in jread[term]:
                                            #check if the dictionary has a long name element
                                            if emp == 'LongName':
                                                jsterm = jread[term]['LongName']
                                                jsonln =  jsterm
                                                return jsonln
                                            else:
                                                continue

        #look for matching json file in the phenotype directory
        for j_file in files:
            if j_file.endswith('json'):
                # extract name of json file and check if it matches the given tsv file name
                jfile = os.path.splitext(j_file)[0]
                if jfile == tsvfile:
                    json_path1 = os.path.join(json_path, j_file)

                    #open json and extract the term long name
                    with open(json_path1) as d:
                        j_read = json.load(d)
                        for key in j_read:
                            if key == term:
                                for empty in j_read[term]:
                                    #check if the dictionary has a long name element
                                    if empty == 'LongName':
                                        js_term = j_read[term]['LongName']
                                        json_ln = js_term
                                        return json_ln
                                    else:
                                        continue


def json_lev(file, root_dir, term):
    '''
    :return: json_des looks for a json file that matches the given tsv file, locates the json file, and extract and returns a levels of the phenotype term
    '''


    #extracts the name of the tsv file without the extension
    tsvfile = os.path.splitext(file)[0]


    #parse through the phenotype directory looking for a matching json file
    for root, dirs, files in os.walk(root_dir, topdown=True):
        json_path = os.path.join(root_dir, root)
        #if phenotype has other directories look for json in those directories
        for dir in dirs:
            #set a path
            dir_root = os.path.join(json_path, dir)
            for rt, dr, fl in os.walk(dir_root, topdown=True):
                for j in fl:
                    if j.endswith('json'):
                        # extract name of json file and check if it matches the given tsv file name
                        Json = os.path.splitext(j)[0]
                        if Json == tsvfile:
                            json_path2 = os.path.join(dir_root, j)

                            #open json and extract the term levels
                            with open(json_path2) as f:
                                jread = json.load(f)
                                for k in jread:
                                    if k == term:
                                        for emp in jread[term]:
                                            tlev = []
                                            #check if the dictionary has a levels element
                                            if emp == 'Levels':
                                                for l in jread[term]['Levels']:
                                                    klev = l + ':' + jread[term]['Levels'][l]
                                                    tlev.append(klev)
                                                jsonlevels = ';'.join(tlev)
                                                return jsonlevels
                                            else:
                                                continue

        #look for matching json file in the phenotype directory
        for j_file in files:
            if j_file.endswith('json'):
                # extract name of json file and check if it matches the given tsv file name
                jfile = os.path.splitext(j_file)[0]
                if jfile == tsvfile:
                    json_path1 = os.path.join(json_path, j_file)

                    #open json and extract the term levels
                    with open(json_path1) as d:
                        j_read = json.load(d)
                        for key in j_read:
                            if key == term:
                                for empty in j_read[term]:
                                    #check if the dictionary has a levels element
                                    if empty == 'Levels':
                                        for emp in j_read[term]:
                                            t_lev = []
                                            #check if the dictionary has a levels element
                                            if emp == 'Levels':
                                                for l in j_read[term]['Levels']:
                                                    k_lev = l + ':' + j_read[term]['Levels'][l]
                                                    t_lev.append(k_lev)
                                                json_lev = ';'.join(t_lev)
                                                return json_lev
                                            else:
                                                continue

def json_Units(file, root_dir, term):
    '''
    :return: json_des looks for a json file that matches the given tsv file, locates the json file, and extract and returns a Unit of the phenotype term
    '''


    #extracts the name of the tsv file without the extension
    tsvfile = os.path.splitext(file)[0]


    #parse through the phenotype directory looking for a matching json file
    for root, dirs, files in os.walk(root_dir, topdown=True):
        json_path = os.path.join(root_dir, root)
        #if phenotype has other directories look for json in those directories
        for dir in dirs:
            #set a path
            dir_root = os.path.join(json_path, dir)
            for rt, dr, fl in os.walk(dir_root, topdown=True):
                for j in fl:
                    if j.endswith('json'):
                        # extract name of json file and check if it matches the given tsv file name
                        Json = os.path.splitext(j)[0]
                        if Json == tsvfile:
                            json_path2 = os.path.join(dir_root, j)

                            #open json and extract the term Unit
                            with open(json_path2) as f:
                                jread = json.load(f)
                                for k in jread:
                                    if k == term:
                                        for emp in jread[term]:
                                            #check if the dictionary has a Unit element
                                            if emp == 'Units':
                                                jsterm = jread[term]['Units']
                                                jsonln =  jsterm
                                                return jsonln
                                            else:
                                                continue

        #look for matching json file in the phenotype directory
        for j_file in files:
            if j_file.endswith('json'):
                # extract name of json file and check if it matches the given tsv file name
                jfile = os.path.splitext(j_file)[0]
                if jfile == tsvfile:
                    json_path1 = os.path.join(json_path, j_file)

                    #open json and extract the term Unit
                    with open(json_path1) as d:
                        j_read = json.load(d)
                        for key in j_read:
                            if key == term:
                                for empty in j_read[term]:
                                    #check if the dictionary has a Unit element
                                    if empty == 'Units':
                                        js_term = j_read[term]['Units']
                                        json_ln = js_term
                                        return json_ln
                                    else:
                                        continue


def ValueType(pathtotsv,term):
    '''
    :param pathtotsv: path to the tsv file
    :param term: the term of interest
    :return: the value type for each term
    '''

    # open tsv file as a data frame
    df = pd.read_csv(pathtotsv, error_bad_lines=False, sep = '\t')

    # iter through the data frame and check and return the value type
    for (i,row) in df.iterrows():
        if not pd.isnull(row[term]):
            if isinstance(row[term],int):
                return(pm.XSD["integer"])
            elif isinstance(row[term],str):
                return(pm.XSD["string"])
            elif isinstance(row[term],float):
                return(pm.XSD["float"])
            elif isinstance(row[term],datetime.date):
                return(pm.XSD["date"])




def phenotype_parser(i,path):
    '''
    This function parses the phenotype directory and extract terms from assessment tsv files and add them to the csv sheet along with the
    terms extracted from participants.tsv file for each dataset.
    :param i: index which represents the dataset number
    :param path: path to OpenNeuro dataset directory
    :return:
    Tuple of terms and their properties like description, longname, units, valueType, etc...
    '''



    df_tuple = []


    if os.path.isdir(path):
        pt_extract = os.listdir(path)

        #loops through dir and check whether a data set has a phenotype directory
        for dir_name in pt_extract:
            if dir_name == 'phenotype':
                root_dir = os.path.join(path, dir_name)
                #parse through the phenotype directory looking for assessment terms
                for root, dirs, files in os.walk(root_dir, topdown=True):
                    #access sub-directories to extract assessment terms
                    for dir in dirs:
                        sub_dir = os.path.join(root_dir, dir)
                        #access tsv files in sub-directories
                        for subroot, subdirs, tsv_files in os.walk(sub_dir):
                            for FL in tsv_files:
                                if FL.endswith('.tsv'):
                                    p_tsv = os.path.join(subroot, FL)
                                    r_tsv = pd.read_csv(p_tsv, error_bad_lines=False)

                                    #exract terms from tsv files
                                    for c in r_tsv.columns :
                                        #create a term list
                                        term_list = c.split("\t")
                                        while '' in term_list:
                                            term_list.remove('')
                                        for t in term_list:
                                            if t == 'participant_id':
                                                term_list.remove('participant_id')

                                        jsonterm = []
                                        jsonlongname = []
                                        jsonlevels = []
                                        jsonunits = []
                                        termtype = []

                                        #loop through the terms extract description, long name, levels, units, type respectively
                                        for term in term_list:
                                            jsonterm.append(json_des(FL, root_dir, term))
                                            jsonlongname.append(json_longname(FL,root_dir,term))
                                            jsonlevels.append(json_lev(FL,root_dir,term))
                                            jsonunits.append(json_Units(FL,root_dir,term))
                                            termtype.append(ValueType(p_tsv,term))

                                        #create a data set ID list
                                        ds_list = i*len(term_list)
                                        d_s = ds_list.split('ds')
                                        while '' in d_s:
                                            d_s.remove('')

                                        tuple1 = list(zip(term_list,d_s,jsonterm,jsonlongname,jsonlevels,jsonunits,termtype))
                                        df_tuple.extend(tuple1)


                    #look for tsv files in phenotype directory
                    for file in files:
                        if file.endswith('.tsv'):
                            pathtotsv = os.path.join(root, file)
                            rtsv = pd.read_csv(pathtotsv, error_bad_lines=False)
                            #extract terms from tsv files
                            for col in rtsv.columns :
                                #create a term list
                                termlist = col.split("\t")
                                while '' in termlist:
                                    termlist.remove('')
                                for T in termlist:
                                    if T == 'participant_id':
                                        termlist.remove('participant_id')

                                json_d = []
                                json_ln = []
                                json_l = []
                                json_u = []
                                term_t = []

                                #loop through the terms extract description, long name, levels, units, type respectively
                                for term in termlist:
                                    json_d.append(json_des(file,root_dir,term))
                                    json_ln.append(json_longname(file,root_dir,term))
                                    json_l.append(json_lev(file,root_dir,term))
                                    json_u.append(json_Units(file,root_dir,term))
                                    term_t.append(ValueType(pathtotsv,term))

                                #create a data set ID list
                                dslist = i*len(termlist)
                                ds = dslist.split('ds')
                                while '' in ds:
                                    ds.remove('')

                                #create a tuple of term and its properties
                                tuple2 = list(zip(termlist,ds,json_d,json_ln,json_l,json_u,term_t))
                                df_tuple.extend(tuple2)

    return df_tuple




def main(argv):

    parser = ArgumentParser(description='This program will extract BIDS terms from participants.tsv and assessment tsv '
                                        'files in the phenotype directory if found. It will then associate the terms with'
                                        'their dataset ID and save the output in a csv file')

    parser.add_argument('-ds_dir', dest='directory', required=True, help="Path to OpenNeuro datasets directory")
    parser.add_argument('-out', dest='output_dir', required=True, help="Output dir to save csv file")
    args = parser.parse_args()



    #list ds ID's inside the given directory and set path
    dsid = os.listdir(args.directory)
    path = args.directory

    df_tuples = []
    global state
    global st


    #acress every ds individually
    for i in dsid:
        #add ds ID to the end of the path to access the data set
        path = os.path.join(path, i)
        if os.path.isdir(path):
            tsv_extract = os.listdir(path)
            jp_extract = os.listdir(path)


            #extract participant.tsv file from a dataset
            for file_name in jp_extract:
                #search for participants.json file in the data set
                if file_name != 'participants.json':
                    state = ''
                elif file_name == 'participants.json':
                    state = 1
                    break

            for f in jp_extract:
                #search for phenotype directory in the data set
                if f != 'phenotype':
                    st = ''
                elif f == 'phenotype':
                    st = 1
                    break



            for filename in tsv_extract:
                #search for phenotype directory in the data set
                if filename != 'participants.tsv':
                    continue
                if filename == 'participants.tsv':
                    print('Extracting terms from participants.tsv for %s' %i)
                    pathtotsv = os.path.join(path, filename)
                    #read tsv file
                    r_tsv = pd.read_csv(pathtotsv, error_bad_lines=False)


                    # extract terms (column names) from participants.tsv data frame
                    for c in r_tsv.columns:
                        #create a list with all terms in the tsv file
                        term_list = c.split("\t")
                        while '' in term_list:
                            term_list.remove('')
                        #remove the term participant id
                        for T in term_list:
                            if T == 'participant_id':
                                term_list.remove('participant_id')
                                continue
                        #create a list with ds ID to match to each term
                        ds_list = i*len(term_list)
                        ds = ds_list.split('ds')
                        #takeout any empty items in the ds list
                        while '' in ds:
                            ds.remove('')

                        term_des = []
                        term_long = []
                        term_level = []
                        term_levels = []
                        term_units = []
                        term_type = []
                        global s

                        #if the dataset doesn't have a participants.json file add an empty item to the list
                        if state == '':
                            for t in term_list:
                                term_des.extend([''])
                                term_long.extend([''])
                                term_levels.extend([''])
                                term_units.extend([''])
                                term_type.append(ValueType(pathtotsv,t))

                        #if the dataset has a participants.json file extract the appropriate term
                        elif state == 1:
                            json_file = 'participants.json'
                            pathtojson = os.path.join(path,json_file)
                            #load json file as a dictionary
                            with open(pathtojson) as d:
                                json_read = json.load(d)
                            for term in term_list:
                                if term == '"ISI"':
                                    term = 'ISI'
                                #call value type function to get the type of input and add it to the list
                                term_type.append(ValueType(pathtotsv,term))

                                s = ''
                                l = ''
                                lv = ''
                                u = ''

                                #look for a key that matches the term
                                for key in json_read:
                                    global term_ln
                                    global term_d
                                    if key == term:
                                        #look for term description in the json file
                                        for e in json_read[term]:
                                            if e == 'Description':
                                                term_d = json_read[term]['Description']
                                                term_des.append(term_d)
                                                s = 2
                                                break
                                            elif e != 'Description':
                                                s = 3
                                        #look for term long name in the json file
                                        for a in json_read[term]:
                                            if a == 'LongName':
                                                term_ln = json_read[term]['LongName']
                                                term_long.append(term_ln)
                                                l = 2
                                                break
                                            elif a != 'LongName':
                                                l = 3
                                        #look for term levels in the json file
                                        for b in json_read[term]:
                                            if b == 'Levels':
                                                for level in json_read[term]['Levels']:
                                                    key_lev = level + ':' + json_read[term]['Levels'][level]
                                                    term_level.append(key_lev)
                                                levels = [';'.join(term_level)]
                                                term_levels.extend(levels)
                                                term_level = []
                                                lv = 2
                                                break
                                            elif b != 'Levels':
                                                lv = 3
                                        #look for term units in the json file
                                        for c in json_read[term]:
                                            if c == 'Units':
                                                term_u = json_read[term]['Units']
                                                term_units.append(term_u)
                                                u = 2
                                                break
                                            elif c != 'Units':
                                                u = 3

                                    elif key != term:
                                        if s != 2:
                                            s = 1
                                        if l != 2:
                                            l = 1
                                        if lv != 2:
                                            lv =1
                                        if u != 2:
                                            u = 1

                                #if no description, long name, levels, or unit was found add an empty item to the list
                                if s == 1 or s == 3:
                                    term_des.extend([''])
                                    s = ''

                                if l == 1 or l == 3:
                                    term_long.extend([''])
                                    l = ''

                                if lv == 1 or lv == 3:
                                    term_levels.extend([''])
                                    lv = ''

                                if u == 1 or u == 3:
                                    term_units.extend([''])
                                    u = ''



                        #pair each term with the appropriate ds ID
                        tuples = list(zip(term_list,ds,term_des,term_long,term_levels,term_units,term_type))
                        df_tuples.extend(tuples)

                if st == 1:
                    print('Found phenotype directory for %s' %i)
                    df_tuples.extend(phenotype_parser(i,path))
                else:
                    continue


        path = args.directory


    #create and save data frame to csv
    df = pd.DataFrame(df_tuples)
    df.to_csv('OpenNeuro_BIDS_terms.csv', header = ['Term','ds_number','Description', 'LongName','Levels','Units','ValueType'], index=False)



    print('OpenNeuro terms have been extracted and saved into a csv file in your output directory')





if __name__ == '__main__':
    main(sys.argv[1:])




