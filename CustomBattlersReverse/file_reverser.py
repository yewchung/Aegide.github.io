from os import listdir
from os.path import isfile, join
from shutil import copyfile

path_custom = "CustomBattlers"
path_reverse = "CustomBattlersReverse"
path_json = "json"
fusions = []

for element in listdir(path_custom):
    if isfile(join(path_custom, element)) and element.endswith(".png"):
        fusion_name = element[:-4].split(".")
        if len(fusion_name)==2:
            reverse_fusion_name = fusion_name[1] + "." + fusion_name[0]
            fusions.append(reverse_fusion_name)
            print(reverse_fusion_name)
            copyfile(join(path_custom, element), join(path_reverse, "r"+reverse_fusion_name+".png"))
        else:
            print(fusion_name)


print("DONE : ", len(fusions))

# ^(?!("[0-9]+\.[0-9]+"))
# "[0-9]+\.[0-9]+"