from pathlib import Path

# i put both my files in home directory
data_folder = Path.home()
i_f = data_folder / 'jap.log'
o_f = data_folder / 'audit.log'

def read_log():
    with open(i_f, 'r') as input_file:
        for line in input_file:
            split_line = line.split()
            yield split_line

# since the log file must be huge let's use a generator
def read_in_chunks(file_object, chunk_size=1024):
    while True:
        data = file_object.readline(chunk_size)
        if not data:
            break
        yield data

with open(i_f, 'r') as inputfile, open(o_f, 'w') as output_file:
    for line in read_in_chunks(inputfile):

        split_line = line.split()

        try:
            name_space,context = split_line[7], split_line[12]
            if name_space == 'm.api.common.server.ApiServerCore' and context == '/api/v3/order':
                output_line = '{0} {1} {2} {3} from {4} {5}'.format(split_line[0], split_line[1], split_line[14],
                                                                        split_line[15], split_line[10], split_line[13])
                output_file.write(output_line + '\n')
        except IndexError:
            pass


## Generator-less version
# with open(i_f, 'r') as input_file, open(o_f, 'w') as output_file:
#     for line in input_file:
#         split_line = line.split()
#
#         try:
#             name_space = split_line[7]
#             if name_space == 'm.api.common.server.ApiServerCore':
#                 output_line = split_line[0] + ' ' + split_line[1] + '  ' + split_line[14] + ' ' + split_line[15] + \
#                               ' from ' + split_line[10] + ' ' + split_line[13]
#                 output_file.write(output_line + '\n')
#         except IndexError:
#             print(line)

## named tuple lazy loading version
# from collections import namedtuple
# logs_list = []
#
# with open(i_f, 'r') as inputfile, open(o_f, 'w') as output_file:
#     for line in read_in_chunks(inputfile):
#
#         split_line = line.split()
#
#         try:
#             name_space,context = split_line[7], split_line[12]
#             if name_space == 'm.api.common.server.ApiServerCore' and context == '/api/v3/order':
#                 ParsedLogLine = namedtuple('ParsedLogLine', 'date time operation quantity ip currency')
#                 log = ParsedLogLine(split_line[0], split_line[1], split_line[14],split_line[15],split_line[10], split_line[13])
#
#                 output_line = '{0} {1} {2} {3} from {4} {5}'.format(log.date, log.time, log.operation, log.quantity,
#                                                                     log.ip, log.currency)
#
#                 output_file.write(output_line + '\n')
#                 logs_list.append(output_line)
#         except IndexError:
#             pass
