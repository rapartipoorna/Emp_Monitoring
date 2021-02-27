import browserhistory as bh
dict_obj = bh.get_browserhistory()
print(dict_obj.keys())
# dict_keys(['safari', 'chrome', 'firefox'])
# dict_obj['chrome'][0]
bh.write_browserhistory_csv()
