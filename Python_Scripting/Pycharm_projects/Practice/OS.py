import os

print(dir(os))

#os.mkdir('Hello')
print(os.getcwd())
os.chdir("E:\Promethean\Python_Scripting\Pycharm_projects")
print(os.getcwd())
print(os.listdir())
# os.mkdir()
# os.makedirs('Demo/SubDir')  #Creates sub dir as well

#os.rmdir()
#os.removedirs()

#os.rename('test.txt', 'demo.txt')
#os.stat('demo.txt') #Prints info
#os.stat('demo.txt').st_mtime

os.environ.get('HOME')
print(os.path.join("E:\Promethean\Python_Scripting", "New folder", "new"))
print(os.path.basename('E:\Promethean\Python_Scripting\Demo.txt'))
print(os.path.dirname('E:\Promethean\Python_Scripting\Demo.txt'))
print(os.path.split('E:\Promethean\Python_Scripting\Demo.txt'))
print(os.path.exists('E:\Promethean\Python_Scripting\Demo.txt'))
print(os.path.isfile('E:\Promethean\Python_Scripting\Demo.txt'))
print(os.path.splitext('E:\Promethean\Python_Scripting\Demo.txt'))

# for root, dir, file in os.walk("E:\Promethean\Python_Scripting\Pycharm_projects"):
#     print("Root Dir: ", root)
#     print("Dir: ", dir)
#     print("File: ", file)





