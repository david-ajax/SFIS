from audioop import add
from lib import *
import pm

version = "v0.3.1 Dev"
edition = "Server"

static_path = os.getcwd()
config = Data.config_data

class Deploy:
    def overview():
        overviewhtml = File.read("./default/overview.html")
        writepath = "overview.html"
        size = str(round(round(Path.getdirsize("./files/") / 1024, 3) / 1024, 3)) + " MB" #GB
        File.rewrite(writepath, overviewhtml)
        File.replace(writepath, "$title", config["title"])
        File.replace(writepath, "$used_space", size)
        File.replace(writepath, "$os_edition", System.os_edition)
        File.replace(writepath, "$cpu_version", System.processor_numbers)
        File.replace(writepath, "$local_time", System.local_time)
        File.replace(writepath, "$python_version", System.python_version) 
        File.replace(writepath, "$sfis_version", version) 
        File.replace(writepath, "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
        if config["about"] == True:
            File.replace(writepath, "$about", "<li><a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")
    def create(one):
        createhtml = File.read("./default/create.html")
        os.chdir(one)
        abspath = Path.abs(".")
        writepath = abspath
        filelist = Path.ls(".", "file")
        folderlist = Path.ls(".", "folder")
        alllist = ""
        print("ok")
        for one in folderlist:
            alllist = alllist + "<br><a href='" + abspath + one + "'>" + one + "/</a>"
        for one in filelist: #TODO(hide some files)
            print("ok")
            alllist = alllist + "<br><a href='../files/" + one + "'>" + one + "</a>"
        File.rewrite(writepath, createhtml)
        File.replace(writepath, "$title", config["title"])
        File.replace(writepath, "$path", Path.contrast(os.getcwd(), static_path))
        File.replace(writepath, "$list", alllist)
        if os.path.exists("README.md") and os.path.isfile("README.md") and config["preview_readme_md"] == True:
            readmemd = File.md2html("README.md")
            File.replace(writepath, "$readme", readmemd)
        else:
            File.replace(writepath, "$readme", "Nothing Here")
        File.replace(writepath, "$ad", config["ad_code"])
        File.replace(writepath, "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
        if config["about"] == True:
            File.replace(writepath, "$about", "<li>Based on <a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")
        if config["compress_html"] == True:
            File.rewrite(writepath,File.htmlmin(File.read(writepath)))
        os.chdir(static_path)
    def welcome():
        welcomehtml = File.read("./default/welcome.html")
        writepath = "index.html"
        File.rewrite(writepath, welcomehtml)
        File.replace(writepath, "$title", config["title"])
        File.replace(writepath, "$owner", config["owner"])
        File.replace(writepath, "$email", config["email"])
        File.replace(writepath, "$ad", config["ad_code"])
        File.replace(writepath, "$copyright", "<li>&copy " + System.year + " " + config["owner"] + "</li>")
        if config["about"] == True:
            File.replace("index.html", "$about", "<li><a href = 'https://github.com/david-ajax/sfis'>SFIS Project</a></li>")
class Function:
    class pkg:
        "Manage Addon Packages of your SFIS container"
        def install(self, package_name, package_version="latest", package_source="https://store.sfis.imwangzhiyu.ga/"):
            "Install ONE package for your SFIS container"
            pm.install(package_name, package_version, package_source)
        def remove(self, package_name):
            "Remove ONE package from your SFIS container"
            pm.remove(package_name)
        def _disenable(self, addon_name):
            "Diaenable addons"
            pm.disenable(addon_name)
        def _enable(self, addon_name):
            "Enable addons"
            pm.enable(addon_name)
        def list(self, mode="offline", source="https://store.sfis.imwangzhiyu.ga"):
            "List addons"
            pm.list(mode, source)
    def run(self, cmd):
        '''Run advanced built-in python commands'''
        print("Start")
        exec(cmd)
    def _reset(self):
        '''Reset and initialize your SFIS container'''
        defaultconfig = b'IyBFZGl0IHRoaXMgZmlsZSB0byBjb25maWd1cmUgU0ZJUwojIERPIE5PVCBERUxFVEUgVEhJUyBGSUxFCgojIFlvdXIgSW5mbWF0aW9uCnRpdGxlOiAiTXkgU0ZJUyBDb250YWluZXIiICMgWW91ciBTaXRlJ3MgVGl0bGUoc3VjaCBhcyAiTXkgQm94IiBvciAiVG9tJ3MgU0ZJUyBDb250YWluZXIiKQpvd25lcjogIkRhdmlkIEFqYXgiICMgeW91ciBuYW1lCmVtYWlsOiAiZGF2aWQtYWpheEBvdXRsb29rLmNvbSIgIyB5b3VyIGVtYWlsKGp1c3Qgd3JpdGUgb25lKQphZF9jb2RlOiAiIiAjIHdyaXRlIHlvdXIgYWQgY29kZSBpbiB0aGUgaW5kZXggcGFnZQoKIyBDb25maWd1cmUgU0ZJUwphYm91dDogVHJ1ZSAjIHNob3cgIkJhc2VkIG9uIFNGSVMiCmNvbXByZXNzX2h0bWw6IFRydWUgIyBDb21wcmVzcyBIVE1MIGZvciBhIGJldHRlciBsb2FkaW5nIGV4cGVyaWVuY2UsIGJ1dCBpdCBzbG93cyBkb3duIGRlcGxveW1lbnQKcHJldmlld19yZWFkbWVfbWQ6IFRydWUgIyBwcmV2aWV3IFJFQURNRS5tZCBpbiBpbmRleC5odG1s'
        os.mkdir("files")
        os.mkdir("tree")
        print("Initializment successful")
    def deploy(self):
        '''Deploy SFIS container under deployment path'''
        Deploy.welcome()
        src_path = ["files"]
        deploy_path = []
        for one in Path.tree("files", "folder"):
            src_path.append(one)
            os.makedirs("tree" + one[5:],exist_ok=True)
            deploy_path.append("tree" + one[5:])
        for one in deploy_path:
            Deploy.create(one)
            print("ok2")
        Deploy.overview()
        print("Deployment successful")
    def purge(self):
        '''Delete files generated by the deployer'''
        try:
            os.remove("index.html")
            os.remove("overview.html")
            path = ["tree"]
            for one in Path.tree("tree", "folder"):
                path.append(one)
            for one in path:
                os.chdir(one)
                os.remove("index.html")
                os.chdir(static_path)
        except:
            pass
        else:
            print("Removment successful")
    def version(self):
        '''Print version information'''
        print("SFIS " + edition + " " + version)
if __name__ == "__main__":
    fire.Fire(Function)
