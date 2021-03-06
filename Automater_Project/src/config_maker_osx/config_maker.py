# reads a cfg file for base and variations and outputs all necessary
# grasshopper config files and a legend

from configparser import ConfigParser
import os
import math

# takes a line and val and returns the line with the val as the new val
def insert_val(line,val):
  pre = line.split(':')[0]
  out = pre + " " + val + ","
  return out

# takes a line, list of variables, and config and returns the line with
# updated val
def rewrite(line, var_list, config):
  s = line
  l_line = line.lstrip()
  for v in var_list:
    v_quote = "\""+v[1]+"\""
    l_line_s = l_line.lower()
    if l_line_s.startswith(v_quote):
      val = config[v[0]][v[1]]
      s = insert_val(line, val)
  return s

# working dir
working = dir_path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1]) + r'/'

# find which iteration of the results we are on
output_dir = working + 'configs'
s = math.ceil((sum(len(files) for _, _, files in os.walk(output_dir)))/2)
output_dir = 'configs'
# paths
file = working + r'user_inputs/base_case.cfg'
output_cons = working + output_dir + r'/cons_' + str(s) + '.txt'
output_win = working + output_dir + r'/window_' + str(s) + '.txt'
default_cons = working + r'default_cons.txt'
default_win = working + r'default_win.txt'

# create config
config = ConfigParser()
config.read(file)

# create var_list (list of variables and their sections)
var_list = []
for sec in config.sections():
  for v in list(config[sec]):
    var_list.append((sec,v))

# output cons
out_C = open(output_cons, "w")
with open(default_cons, "r") as def_C:
  lines = def_C.readlines()
  for line in lines:
    s = rewrite(line, var_list, config)
    out_C.writelines(s)
out_C.close()

# output win
out_W = open(output_win, "w")
with open(default_win, "r") as def_W:
  lines = def_W.readlines()
  for line in lines:
    s = rewrite(line, var_list, config)
    out_W.writelines(s)
out_W.close()
