#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# ############################################################################
#
# genmaps.py
# 20/04/2023 (c) Juan M. Casillas <juanm.casillas@gmail.com>
# https://github.com/juanmcasillas/quakeIII_2023
#
# Generate a random maps.txt file suitable to use in Quake3 server via exec.
# useful to randomize and select maps on start.
#
# Usage:
# .\genmaps.py -e -r -a # All Quake3 maps
# .\genmaps.py -r -a # All Quake3 maps, plus extra [https://lvlworld.com/download/id:664#]
# .\genmaps.py # All maps, remove the removed_maps, save to default location
#
# ############################################################################


import random
import copy
import os
import argparse
import sys

map_file    = "I:\\Games/quake3server/baseq3/maps.txt"

removed_maps = [
  #"q3ctf1",
  #"q3ctf2",
  #"q3ctf3",
  #"q3ctf4",
  #"q3ctf5",
  "q3dm0"
] 

extra_maps = [
"tig_den",
"natedm2",
"ik3dm1",
"ztn3dm2",
"bal3dm2",
"japandm",
"lun3dm2",
"auh3dm1",
"mrcq3t3",
"ztn3dm1",
"auh3dm2",
"cpm8",
"shortcircuit",
"fff",
"devdm3",
"d3xf1"    
]

quake3_map_list = [
# optional maps
"q3ctf1",
"q3ctf2",
"q3ctf3",
"q3ctf4",
"q3ctf5",
"q3dm0",

# useful maps
"q3dm1",
"q3dm2",
"q3dm3",
"q3dm4",
"q3dm5",
"q3dm6",
"q3dm7",
"q3dm8",
"q3dm9",
"q3dm10",
"q3dm11",

# more optional maps
"q3dm12",
"q3dm13",
"q3dm14",
"q3dm15",
"q3dm16",
"q3dm17",
"q3dm18",
"q3dm19",
"q3jurney1",
"q3jurney2",
"q3jurney3",
"q3jurney4",
"q3jurney5",
"q3jurney6"
]

if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    
    # by default, Generate only the map with the default selection (with extra maps)
    
    parser.add_argument("-v", "--verbose", help="Show data about file and processing (Debug)", action="count", default=0)
    parser.add_argument("-r", "--norandomize", help="Don't Randomize the list (default randomize them)", action="store_true", default=False)
    parser.add_argument("-e", "--noextra", help="Don't Enable extra maps (default true) [https://lvlworld.com/download/id:664#]", action="store_true", default=False)
    parser.add_argument("-a", "--all", help="Use all available maps",  action="store_true")
    parser.add_argument("-o", "--output", help="Outputs to the defined file. Default = '%s'" % map_file, default=map_file)
    parser.add_argument("-l", "--list", help="List the selected map, exists",  action="store_true")

    args = parser.parse_args()

    # configure the working map list.

    working_list = copy.copy(quake3_map_list)

    if args.noextra == False:
        if args.verbose > 0:
            print("adding extra maps")

        working_list = working_list + extra_maps
    
    if not args.all:
        # remove the removed_maps:
        
        #
        # fast but onsort the list
        # working_list = list(set(working_list).difference(removed_maps))
        items = []
        for i in working_list:
            if not i in removed_maps:
                items.append(i)
            else:
                if args.verbose > 0:
                    print("removing map %s" % i)

        working_list = items


    if args.norandomize == False:
        random.shuffle(working_list)

    if args.list:
        
        for i in working_list:
            print("map: %s" % i)
        print("loaded %d maps" % len(working_list))            
        sys.exit(0)

    if args.output:
        map_file = args.output
        if args.verbose > 0:
            print("Remaping output to: %s " % map_file)

    i = 1
    idx = "lvl%d"
    tpl = "set %s \"map %s; set nextmap vstr %s\""
    cmds = []
    for item in working_list:
        cur_idx  = idx % i
        next_idx = idx % (i+1)
        # if last one
        if item == working_list[-1]:
            next_idx = idx % 1
        cmd = tpl % (cur_idx, item, next_idx)
        i +=1
        cmds.append(cmd)
    cmds.append("vstr lvl1")

    try:
        fd = open(map_file,"w")
        fd.write("\n".join(cmds))
        fd.close()
    except:
        print("can't open %s for writting" % map_file)
        sys.exit(1)

    print("written %d maps into %s successfully" % (len(working_list),map_file))
    
    if args.verbose > 1:
        print("\n".join(cmds))

