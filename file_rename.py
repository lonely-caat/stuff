import os
counter = 0
path = "/Users/mbilichenko/Downloads"
for file in os.listdir(path):
    file_name, file_extension = os.path.splitext(file)
    counter += 1
    file_name.split('_')
    new_name= '{}{}{}'.format(counter,file_name,file_extension)
    print path+file, path+'/'+new_name
    os.rename(path+'/'+file, path+'/'+new_name)