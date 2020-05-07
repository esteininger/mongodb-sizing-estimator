#!/usr/bin/env python3
import os

file_path = 'output.txt'

def build_obj(keys_list, row):
    obj = {}
    for index, key in enumerate(keys_list):
        obj[key] = row[index]

    return obj

def clean_msg(obj, total):
    msg = ''
    for key, val in obj.items():
        st = f'{val/total} {key}s / sec \n'
        msg += st
    return msg

def formulate(lis):
    iops = {
        'insert': 0,
        'query': 0,
        'update': 0,
        'delete': 0
    }
    for obj in lis:
        for row_key, row_val in obj.items():
            # loop thru iops dict
            for iop_key, iop_val in iops.items():
                if iop_key == row_key:
                    # strip asterik
                    if '*' in row_val:
                        row_val = row_val.replace("*","")

                    iops[iop_key] += int(row_val)

    return iops


def build_list_of_objs():
    keys_list = []
    master_arr = []

    with open(file_path) as f:
        lis = [line.split() for line in f]
        for index, row in enumerate(lis):
            if row[0] == 'insert':
                keys_list = row
            else:
                obj = build_obj(keys_list=keys_list, row=row)
                # obj['counter'] = index
                master_arr.append(obj)

    return master_arr

master_stats = build_list_of_objs()
result_set = formulate(master_stats)
total = len(result_set)


msg = clean_msg(obj=result_set, total=total)

print(msg)
