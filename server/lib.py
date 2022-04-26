import glob, codecs, os, platform, time, urllib, shutil, tarfile, json # Built-in
import markdown, yaml, requests, fire # Add-on

class File:
    def json2dict(src):
        return json.loads(src)
    def dict2json(src):
        return json.dumps(src)
    def untar(inputpath, outputpath):
        data = tarfile.open(inputpath)
        data.extractall(outputpath)
        data.close()
    def md2html(path): 
        input_file = codecs.open(path, mode="r", encoding="utf-8")
        text = input_file.read()
        html = markdown.markdown(text)
        return html
    def replace(path, old_content, new_content):
        content = File.read(path)
        content = content.replace(old_content, new_content)
        File.rewrite(path, content)
    def read(path):
        with open(path, encoding='UTF-8') as f:
            read_all = f.read()
            f.close()
        return read_all
    def rewrite(path, data):
        with open(path, 'w', encoding='UTF-8') as f:
            f.write(data)
            f.close()
    def htmlmin(data): # Compress HTML files by deleting empty lines (seems a little stupid)
        data = data.replace('\n','')
        data = data.replace('\t','')
        data = data.replace('\r','')
        return data
class Path:
    def mkdir(target):
        if os.path.exists(target):
            return "Folder Exists"
        else:
            os.mkdir(target)
    def find(command):
        list = None
        for one in  glob.glob(command):
            list.append(one)
        return list
    def rm(target):
        if os.path.exists(target):
            if os.path.isdir(target):
                shutil.rmtree(target)
            else:
                os.remove(target)
        else:
            pass
    def move(inputpath, target):
        shutil.move(inputpath, target)
    def copy(inputpath, outputpath):
        if os.path.isfile(inputpath):
            shutil.copyfile(inputpath, outputpath)
        elif os.path.isdir(inputpath):
            shutil.copytree(inputpath, outputpath)
    def abs(path="."):
        return os.path.abspath(path)
    def rel(path="."):
        return os.path.relpath(path)
    def getdirsize(path="."):
        size = 0
        for root, dirs, files in os.walk(path):
            size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
        return size # GB: size / 1024 / 1024 / 1024 / 1024
    def ls(path=".", mode="all"):
        all = os.listdir(path)
        filelist = []
        folderlist = []
        for one in all:
            if os.path.isfile(one):
                filelist.append(one)
            if os.path.isdir(one):
                folderlist.append(one)
        if mode == "all":
            return all
        elif mode == "file":
            return filelist
        elif mode == "folder":
            return folderlist
        else:
            return "unknown"
    def getparentfolder(path): # Useless
        of = os.getcwd()
        os.chdir(path)
        os.chdir("..")
        pf = os.getcwd()
        os.chdir(of)
        return pf
    def contrast(path1, path2):
        return os.path.relpath(path1, path2)
    def tree(path=".", mode="all"): # Generate file tree(all)
        a = []
        b = []
        c = []
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                a.append(os.path.join(root, name))
                c.append(os.path.join(root, name))
            for name in dirs:
                a.append(os.path.join(root, name))
                b.append(os.path.join(root, name))
        if mode == "all":
            return a
        if mode == "folder":
            return b
        if mode == "file":
            return c
class Net:
    def get(target):
        data = requests.get(target)
        data.encoding = data.apparent_encoding
        return data.text
    def size(target):
        data = urllib.request.urlopen(target)
        return data.headers['content-length']
class System:
    os_edition = platform.platform()
    local_time = time.ctime()
    processor_numbers = platform.machine()
    python_version = platform.python_version()
    year = time.strftime("%Y", time.localtime()) 
class Data:
    config_data = yaml.load(File.read("config.yml"), Loader=yaml.FullLoader)
