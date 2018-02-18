def spreadsheet_decode_column(col_num):
    col_str = ""
    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        col_str += chr(ord('A') + remainder)
    return col_str


print(spreadsheet_decode_column(702))