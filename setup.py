import subprocess
import platform
import os
 
# not sure the direction i want to take these tools,
# I just need an easy install script for vms 

def main():
    system = platform.system()
    if system == "Linux":
        linux_install()
    # else, run windows install

tools = ["https://github.com/d3v1nG/recon-ng.git", "https://github.com/d3v1nG/EyeSpy.git", "https://github.com/d3v1nG/GatherContacts.git"]

def linux_install():
    for tool in tools:
        subprocess.run(["git", "clone", tool])
    # recon-sk setup
    subprocess.run(["recon-cli", "-C", "marketplace install all"])
    # tool reqs
    tool_dirs = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]
    for tool in tool_dirs:
        subprocess.run(["pip3", "install", "-r", "{0}/requirements.txt".format(str(tool))])
    # todo: add script dirs to path
    

if __name__ == "__main__":
    main()