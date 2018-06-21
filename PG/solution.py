class FileReader:

    def __init__(self,filename):
        self.filename = filename

    def read(self):
        try:
            file = open(self.filename, "r")
            result = file.read()
        except IOError as e:
            result = ""
        else:
            file.close()
        return result