from struct import pack
from lib import *
"The Package Manager of SFIS"
def install(package_name, package_version="latest", package_source="https://store.sfis.imwangzhiyu.ga/"):
    Path.mkdir("tmp")
    os.chdir("tmp")
    print("Install " + package_name)
    if package_version == "latest":
        print("Using latest version")
        print("Get: latest.json")
        latest = File.json2dict(Net.get(package_source + "latest.json"))
        package_version = latest[package_name]
        print("Auto Currect: the latest version is " + package_version)
    name = str(package_name) + "_" + str(package_version) + ".sap"
    link = package_source + name
    print("Download: " + link + " (" + "size:" + Net.size(link) + ")")
    time.sleep(0.5)
    File.rewrite(name, Net.get(link))
    os.chdir("..")
    os.chdir("addons")
    print("Unpacking: " + name)
    Path.rm(package_name)
    os.mkdir(package_name)
    os.chdir(package_name)
    File.untar("../../tmp/" + name, ".") # .sap file is .tar file
    os.chdir("..")
    print("Setting up: " + package_name + " " + package_version)
    print("Add to package database")
    db_data = File.json2dict(File.read("addons.json"))
    db_data[package_name] = package_version
    File.rewrite("addons.json", File.dict2json(db_data))
    os.chdir("..")
    print("Addon [" + package_name + "] has completely installed!")
def remove(package_name):
    os.chdir("addons")
    if os.path.exists(package_name):
        print("Remove: " + package_name)
        print("Deleting files")
        Path.rm(package_name)
        print("Setting up: " + package_name)
        print("Remove from database")
        db_data = File.json2dict(File.read("addons.json"))
        db_data.pop(package_name)
        File.rewrite("addons.json", File.dict2json(db_data))
        print("Addon [" + package_name + "] has completely removed!")
    else:
        print("Can not find the target")
def list(mode="offline", source="https://store.sfis.imwangzhiyu.ga"):
    print("List: " + mode)
    if mode == "online":
        try:
            global source_status
            if source == "https://store.sfis.imwangzhiyu.ga":
                source_status = "Official"
            else:
                source_status = "Three-party"
            print("Get: latest.list" + " from " + source + " (" + source_status + ")")
            source_list = File.json2dict(Net.get(source + "/latest.json"))
            for one in source_list:
                print(one + " v" + source_list[one])
        except:
            print("E: Network Error")
    else:
        print("Reading local database")
        source_list = File.json2dict(File.read("./addons/addons.json"))
        for one in source_list:
            print(one + " v" + source_list[one])
def _info(addon_name): #TODO
    pass
    print("Developing")