def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num


def spreadsheet_decode_column(col_num):
    col_str = ""
    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        col_str += chr(ord('A') + remainder)
    return col_str


print(spreadsheet_encode_column("ZZ"))
print(spreadsheet_decode_column(702))
