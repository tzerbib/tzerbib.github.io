

# # Leaflet cluster map of talk locations
#
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
#
# Run this from the _talks/ directory, which contains .md files of all your talks. 
# This scrapes the location YAML field from each .md file, geolocates it with
# geopy/Nominatim, and uses the getorg library to output data, HTML,
# and Javascript for a standalone cluster map.
#
# Requires: glob, getorg, geopy

import glob
import getorg
import geopy
from enum import Enum
import re
from time import sleep
from difflib import SequenceMatcher
import shutil
import sys


ORIGIN = "_config.yml"
STUDY  = "_pages/cv.md"
WORK   = "_pages/cv.md"
TALK   = "_talks/*.md"

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


def findloc_talks(file):
  location = []
  with open(file, 'r') as f:
    lines = f.read()
    if lines.find('location: "') > 1:
      loc_start = lines.find('location: "') + 11
      lines_trim = lines[loc_start:]
      loc_end = lines_trim.find('"')
      location.append(lines_trim[:loc_end])
  return location


def findloc_origin(file):
  location = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if "location" in line:
        tokens = line.split('\"')
        location.append(tokens[1])
  return location

def findloc_study(file):
  token = "studymap"
  location = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if token in line:
        location.append(re.findall(r'\"([^]]*)\"', line)[0])
  return location

def findloc_work(file):
  token = "workmap"
  location = []
  with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
      if token in line:
        location.append(re.findall(r'\"([^]]*)\"', line)[0])
  return location


def add_loc_type(file, type_dict):
  i = 0
  state = 0
  loc_type = 0

  with open(file, 'r') as f:
    contents = f.readlines()

  for line in contents:
    # Case looking for a place
    if state == 1:
      key = re.search('\"(.*)\"', line).group(1)
      loc_type = type_dict[key]
      state = 2
    
    # Case insert location type
    elif state == 4:
      # Add a ',' at the end of the line
      contents[i-1] = contents[i-1][:-1] + ",\n"
      # Insert the type
      contents.insert(i, "    " + str(loc_type) + '\n')
      state = 0
    
    # Case longitude/latitude
    elif state > 1:
      state = state + 1

    # Case start of a new location
    elif line == "  [\n":
      state = 1

    i = i +1

  with open(file, 'w') as f:
    f.writelines(contents)


class Location_type:
  def __init__(self,v,p,f):
    self.val = v
    self.path = p
    self.search_fun = f


location_type_t = [
  Location_type(0,ORIGIN, findloc_origin),
  Location_type(1,STUDY, findloc_study),
  Location_type(2,WORK, findloc_work),
  # Location_type(3,TALK, findloc_talks),
]


def main():
  geopy.geocoders.options.default_user_agent = "geofinder-resume"
  respath = "talkmap/org-locations.js"
  prox_max = 0.75
  geocoder = geopy.Nominatim()
  location_dict = {}
  location = ""
  permalink = ""
  title = ""
  location_dict = dict()
  location_type = dict()

  for t in location_type_t:
    # Get all file following the path of t
    g = glob.glob(t.path)
    print(bcolors.OKCYAN, g, bcolors.ENDC)

    for file in g:
      # Look for a location in the file
      location = t.search_fun(file)
    
      # Case no location found
      if len(location) == 0:
        print(bcolors.WARNING, "No location found for ", file, bcolors.ENDC)
        continue

      # For all location find
      for l in location:
        print(l)
        unique = True
        # Ignore close matches
        for k in location_dict.keys():
          proximity = SequenceMatcher(None, l, k).ratio()
          if proximity >= prox_max:
            print(bcolors.WARNING, "Skipped \"", l, '\", to close to \"', k, "\" (proximity=",proximity," >",prox_max,")", bcolors.ENDC)
            unique = False
            break
          
        if unique:
          # Call location service to get coorinates
          location_dict[l] = geocoder.geocode(l)
          location_type[l] = t.val

          print(l, "\n", location_dict[l], t.val)

          # Wait to not saturate the service
          sleep(2)
            

  # Use getorg to create a map and the location array in /tmp
  m = getorg.orgmap.create_map_obj()
  getorg.orgmap.output_html_cluster_map(location_dict, folder_name="/tmp", hashed_usernames=False)

  # Move the formatted array to /talkmap
  shutil.move("/tmp/org-locations.js", respath)

  # Add a line for the type of location in the file
  add_loc_type(respath, location_type)


if __name__ == "__main__":
    sys.exit(main())