# index.html generator for PC Engines releases
import sys
import datetime

def get_index(text):
    with open(filename,'r') as f:
        for (i, line) in enumerate(f):
            if text in line:
                return i
    return -1

def get_mr_number():
    index = get_index("href=\"#mr-")
    with open(filename) as f:
        for i, line in enumerate(f):
            if i == index:
                temp = line.split("\"")[1]
                return temp.split("-")[1]
    return -1

def get_old_version(phrase):
    index = get_index(phrase)
    with open(filename) as f:
        for i, line in enumerate(f):
            if i == index:
                temp = line.split("...")[1]
                return temp.split("\"")[0]
    return -1

def copy_release_notes(start, stop):
    with open(filename, "r") as f:
        for i, line in enumerate(f):
            if i >= start:
                latest_release_notes.append(line)
            if i > stop:
                break

def remove_line(number):
    ignored_line = [number]
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w") as f:
        for linenum, line in enumerate(lines, 1):
            if linenum not in ignored_line:
                f.write(line)

def insert_line(index, value):
    with open(filename, "r") as f:
        contents = f.readlines()
    contents.insert(index, value)
    with open(filename, "w") as f:
        contents = "".join(contents)
        f.write(contents)

def replace_line(keyword, replacement):
    num = get_index(keyword)
    if num == -1:
        sys.exit("'get_index' function returned status -1")
    remove_line(num+1)
    insert_line(num, replacement)

# set variables
latest_release_notes = []
filename = "index.html"
version = input("Coreboot version (e.g. 'v4.9.0.4'): ")
seabios_ver = raw_input("SeaBIOS version (e.g. 'rel-1.12.1.1') or leave empty if doesn't change: ")
sortbootorder_ver = raw_input("sortbootorder version (e.g. 'v4.6.13') or leave empty if doesn't change: ")
date = raw_input("release date (format `YYYY-MM-DD`) or leave empty (today): ")
if not date:
    date = datetime.date.today()

# get old versions
old_version = get_old_version("https://github.com/pcengines/coreboot/compare")
if old_version == -1:
    sys.exit("'get_old_version' of coreboot returned status -1")
old_seabios_ver = get_old_version("https://github.com/pcengines/seabios/compare")
if old_seabios_ver == -1:
    sys.exit("'get_old_version' of seabios returned status -1")
old_sortbootorder_ver = get_old_version("https://github.com/pcengines/sortbootorder/compare")
if old_sortbootorder_ver == -1:
    sys.exit("'get_old_version' of sortbootorder returned status -1")

# increment MR number
mr_number = get_mr_number()
if mr_number == -1:
    sys.exit("'get_mr_number' returned status -1")
mr_number = int(mr_number) + 1

# copy last release notes block
start_index = get_index("<!-- mainline releases ")
stop_index = get_index(" <div class=\"break\"></div>")
copy_release_notes(start_index, stop_index)
latest_release_notes = "".join(latest_release_notes)

# insert new release point
num = get_index("<li><a href=\"#mr-")
input = "                        <li><a href=\"#mr-" + str(mr_number) + "\">" + version + "</a></li>\n"
insert_line(num, input)

# remove unnecessary lines
num = get_index("<!--<div class=\"break\"></div>insert this code")
remove_line(num+1) # new line
remove_line(num) # div class comment line
num = get_index("h2 tag needs to be moved to the newest version")
remove_line(num) # h2 class tag line
remove_line(num) # h2 comment line

# insert copied release notes
num = get_index("<!-- mainline releases ")
insert_line(num,"\n")
insert_line(num, latest_release_notes)

# update latest release notes
input = "        <!-- mainline releases " + version + " -->\n"
replace_line("<!-- mainline releases ", input)
input = "        <div class=\"smaller-margin\" id=\"mr-" + str(mr_number) + "\">\n"
replace_line("<div class=\"smaller-margin\" id=\"mr-", input)
input = "            <h4><a target=\"_blank\" href=\"https://github.com/pcengines/coreboot/compare/" +old_version + "..." + version + "\">" + version + "</a></h4>\n"
replace_line("<h4><a target=\"_blank\" href=\"https://github.com/pcengines/coreboot/compare", input)
input = "            <p>Release date: " + str(date) +"</p>\n"
replace_line("<p>Release date:", input)

# update binaries links
input = "                    <li><a class=\"sha-button\" href=\"https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_"+version+".rom\">apu1 "+version+"</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_"+version+".SHA256\" class=\"sha-button\">SHA256</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu1/apu1_"+version+".SHA256.sig\" class=\"sha-button\">SHA256.sig</a></li>\n"
replace_line("https://3mdeb.com/open-source-firmware/pcengines/apu1", input)
input = "                    <li><a class=\"sha-button\" href=\"https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_"+version+".rom\">apu2 "+version+"</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_"+version+".SHA256\" class=\"sha-button\">SHA256</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu2/apu2_"+version+".SHA256.sig\" class=\"sha-button\">SHA256.sig</a></li>\n"
replace_line("https://3mdeb.com/open-source-firmware/pcengines/apu2", input)
input = "                    <li><a class=\"sha-button\" href=\"https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_"+version+".rom\">apu3 "+version+"</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_"+version+".SHA256\" class=\"sha-button\">SHA256</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu3/apu3_"+version+".SHA256.sig\" class=\"sha-button\">SHA256.sig</a></li>\n"
replace_line("https://3mdeb.com/open-source-firmware/pcengines/apu3", input)
input = "                    <li><a class=\"sha-button\" href=\"https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_"+version+".rom\">apu4 "+version+"</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_"+version+".SHA256\" class=\"sha-button\">SHA256</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu4/apu4_"+version+".SHA256.sig\" class=\"sha-button\">SHA256.sig</a></li>\n"
replace_line("https://3mdeb.com/open-source-firmware/pcengines/apu4", input)
input = "                    <li><a class=\"sha-button\" href=\"https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_"+version+".rom\">apu5 "+version+"</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_"+version+".SHA256\" class=\"sha-button\">SHA256</a><a href=\"https://3mdeb.com/open-source-firmware/pcengines/apu5/apu5_"+version+".SHA256.sig\" class=\"sha-button\">SHA256.sig</a></li>\n"
replace_line("https://3mdeb.com/open-source-firmware/pcengines/apu5", input)

# update source code links
input = "                    <li><a target=\"_blank\" href=\"https://github.com/pcengines/coreboot/compare/"+old_version+"..."+version+"\">coreboot "+version+"</a></li>\n"
replace_line("<li><a target=\"_blank\" href=\"https://github.com/pcengines/coreboot/compare", input)

if seabios_ver:
    input = "                    <li><a target=\"_blank\" href=\"https://github.com/pcengines/seabios/compare/"+old_seabios_ver+"..."+seabios_ver+"\">SeaBIOS "+seabios_ver+"</a></li>\n"
    replace_line("https://github.com/pcengines/seabios/compare", input)

if sortbootorder_ver:
    input = "                    <li><a target=\"_blank\" href=\"https://github.com/pcengines/sortbootorder/compare/"+old_sortbootorder_ver+"..."+sortbootorder_ver+"\">sortbootorder "+sortbootorder_ver+"</a></li>\n"
    replace_line("https://github.com/pcengines/sortbootorder/compare", input)

print "\nSTATUS: `index.html` file generated successfully"
