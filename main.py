import sys
import os

from file_tool import *

ft_name = ""
ft_operation = ""
ft_path = ""
ft_destination = ""
ft_output = ""
ft_start_line = 0
ft_end_line = 0

ft_config_file_path = sys.argv[1]

with open(ft_config_file_path, "r") as ft_file:
    for line in ft_file.readlines():
        try:
            command, value = line.strip().split("=")
            if command == FT_NAME:
                ft_name = value
            elif command == FT_OP:
                ft_operation = value
            elif command == FT_PATH:
                ft_path = value
            elif command == FT_DEST:
                ft_destination = value
            elif command == FT_OUTPUT:
                ft_output = value
            elif command == FT_START_LINE:
                ft_start_line = int(value)
            elif command == FT_END_LINE:
                ft_end_line = int(value)
            else:
                print(
                    f"INVALID KEY : '{command}' | VALUE : '{value}' PAIRS IN THE CONFIG '{ft_config_file_path}'")
                sys.exit(0)
        except ValueError:
            print(
                f"MULTIPLE SPACE CHARACTERS IN THE CONFIG '{ft_config_file_path}'")
            sys.exit(0)

if ft_path == "":
    ft_path = os.getcwd()
if ft_output == "":
    ft_output = "ft_output.txt"

ft = FILE_TOOL(ft_name, ft_operation, ft_path,
               ft_destination, ft_output, ft_start_line, ft_end_line)

ft.handle_operation()
