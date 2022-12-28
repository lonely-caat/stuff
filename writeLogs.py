import datetime
import abc

class WriteFile(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, file):
        self.file = file

    @abc.abstractmethod
    def handle_file(self,filename,input_data):
        with open(filename, "a+") as l_f:
            for element in input_data:
                l_f.write(element)

class LogFile(WriteFile):

    def write(self,input_data):
        input_data = datetime.datetime.now().strftime('%Y-%m-%d %H:%M') + ' ' + input_data + '\n'
        self.handle_file(self.file, input_data)


class DelimFile(WriteFile):
        super().__init__(self, file, delim)
        self.file = file
        self.delim = delim

    def write(self,input_data):
        input_data = ",".join(input_data)

        self.handle_file(self.file, input_data)


log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same
