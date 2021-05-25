my_file=open("file.txt",'r+')
content=my_file.read()
my_file_to_list=content.split()
my_file_to_list.remove('6')
str=""
for i in my_file_to_list:
   str += i
   str += " "
my_file.truncate(1)
my_file.write(str)
