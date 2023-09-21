# This is filetool utility

import sys
from filetool import FT

ft_path = sys.argv[1]

with open(ft_path, "r") as ft_file:
  command_value = {}
  for line in ft_file.readlines():
    command, value = line.split("=")
    command_value[command.strip()] = value.strip()

  ft = FT(command_value["NAME"], command_value["OP"], command_value["PATH"], command_value["DEST"], command_value["START_LINE"], command_value["END_LINE"])

  ft.handle_operation()