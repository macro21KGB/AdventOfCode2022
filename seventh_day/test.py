from classes import File, Directory

root_dir = Directory("/", [])


root_dir.add([File("file1", 1234)])
root_dir.add([Directory("a", [
    File("b", 123)
    ])])



print(root_dir.view(0))
