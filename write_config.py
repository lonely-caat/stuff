class ConfigDict(dict):
    """
    The idea is to have a class for operating on config files in a same manner you work with a dict, so that you don't need
    to learn how to work with it - you already know how to work with dicts

    """
    def __init__(self, ffile):
          super().__init__()
          self._file=ffile                  #file should be instance shared, and is for internal use only
          try:
              with open(self._file, 'r+') as config:
                  for line in config:           # you don't really need to use file.read() or readlines in this case
                    line = line.strip()
                    key, value = line.split('=', 1) # 1 here is for the case that there's a '=' in body of parameter, e.g. password
                                                    # we split string into to tuples and assign them to key,value

                    dict.__setitem__(key,value) # We call dict. not self, because we want to call parent class set_item not
                                                # the one below because it would be a loop otherwise, e.g. init calls set item
                                                # which calls init again
          except OSError as e:
              print(e)

    def __setitem__(self, key, val):
            dict.__setitem__(self, key, val)
            with open(self._file, 'w+') as config:
                for key,value in self.items():
                    config.write("{0}={1}".format(key, value))
            # code that writes to the file -- see above

class ConfigKeyError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args
        else:
            self.message = 'No message at all'

    def __str__(self):
        if self.message:
            return self.message





c = ConfigDict('cash.txt')

