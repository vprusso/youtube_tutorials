# YouTube Link:
"""
Implement a function that converts an integer to the spreadsheet
column ID.

Example:
    Input: 1 -> A
    Input: 27 -> AA
    Input: 702 -> ZZ
"""


def spreadsheet_decode_column(col_num):
    """Decodes a column number into a column id."""
    col_str = ""
    while col_num > 0:
        col_num, remainder = divmod(col_num - 1, 26)
        col_str += chr(ord('A') + remainder)
    return col_str


# A
print(spreadsheet_decode_column(1))

# AA
print(spreadsheet_decode_column(27))

# ZZ
print(spreadsheet_decode_column(702))
