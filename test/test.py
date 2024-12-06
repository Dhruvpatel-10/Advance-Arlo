from test.add import NeededFunc;NeededFunc()

path = '/home/sun/Laptop/Project/Lexi-Ai/data/images'
if os.path.isdir(path):
    print(f"Error: {path} is a directory.")
else:
    print(f"{path} is a file.")