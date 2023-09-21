import shutil

class FT:
  def __init__(self, name, operation, path, destination, start_line = 0, end_line = 0):
    self.name = name
    self.operation = operation
    self.path = path
    self.destination = destination
    self.start_line = int(start_line)
    self.end_line = int(end_line)
    self.source_file_data = ""

  def handle_operation(self):
    if self.operation == "CP":
      shutil.copyfile(f"{self.path}/{self.name}", f"{self.destination}/log.txt")
    elif self.operation == "MV" or self.operation == "RENAME":
      shutil.move(f"{self.path}/{self.name}", self.destination)
    elif self.operation == "COPY_AND_PASTE":
      with open(f"{self.path}/{self.name}", "r") as source_file:
        file_index = 0
        file_open = False
        for line in source_file.readlines():

          if file_index == self.start_line:
            file_open = True
            self.source_file_data += line
          elif file_index == self.end_line:
            file_open = False
            self.source_file_data += line
            break
          elif(file_open):
            self.source_file_data += line

          file_index += 1

      with open(f"{self.path}/log.txt", "w") as destination_file:
        destination_file.write(self.source_file_data)