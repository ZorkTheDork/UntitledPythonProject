import pandas


def read_excel(filename, sort_by):
    info_dict = pandas.read_excel(filename)
    info_list = info_dict.to_dict(sort_by)
    return info_list