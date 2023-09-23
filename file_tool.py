import shutil
from os import path

FT_NAME = "NAME"
FT_OP = "OP"
FT_PATH = "PATH"
FT_DEST = "DEST"
FT_OUTPUT = "OUTPUT"
FT_START_LINE = "START_LINE"
FT_END_LINE = "END_LINE"

FT_OP_CP = "CP"
FT_OP_MV = "MV"
FT_OP_RENAME = "RENAME"
FT_OP_CAP = "COPY_AND_PASTE"


class FILE_TOOL:
    def __init__(self, name, operation, path, destination, output, start_line, end_line):
        self.name = name
        self.operation = operation
        self.path = path
        self.destination = destination
        self.output = output
        self.start_line = start_line
        self.end_line = end_line

    def handle_operation(self):
        old_path = path.join(self.path, self.name)
        new_path = path.join(self.destination, self.output)
        ft_file_index = 0
        ft_source_file_data = ""

        if self.operation == FT_OP_CP:
            shutil.copyfile(old_path, new_path)

        elif self.operation == FT_OP_MV or self.operation == FT_OP_RENAME:
            shutil.move(old_path, self.destination)

        elif self.operation == FT_OP_CAP:
            with open(old_path, "r") as source_file:
                for line in source_file.readlines():

                    if ft_file_index >= self.end_line - 1:
                        print("1", ft_file_index, line)
                        ft_source_file_data += line
                        break

                    elif ft_file_index >= self.start_line - 1:
                        print("2", ft_file_index, line)
                        ft_source_file_data += line

                    ft_file_index += 1

            with open(new_path, "w") as destination_file:
                destination_file.write(ft_source_file_data)
