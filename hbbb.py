file_path="C:\\Users\\Toshiba\\source\\repos\\hamza\\homework\\football.txt"
with open(file_path ,"x") as e:
    e.write("story")


with open(file_path ,"a") as e:
    e.write("\niogiogos")


with open(file_path ,"r") as e:
    t=e.read()
    print(t)