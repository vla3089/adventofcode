#!/usr/bin/env python

registers = dict()


def get_reg(reg):
     if reg in registers:
          return registers[reg]
     else:
          return 0

highest = 0
     
def process_op(reg, op, value):
  global highest
  reg_value = get_reg(reg)
  if op == 'inc':
       new_value = reg_value + int(value)
       registers[reg] = new_value
       highest = max(highest, new_value)
  elif op == 'dec':
       registers[reg] = reg_value - int(value)
       
with open('input_8.txt', 'r') as f:
     for line in f:
     	 line = line.strip()
	 if len(line) > 0:
              reg, op, value, _if, cond_reg, cmp_op, cmp_value = line.split(' ')
              expression = str(get_reg(cond_reg)) + cmp_op + cmp_value
              if eval(expression):
                  process_op(reg, op, value)



import operator 
print max(registers.iteritems(), key=operator.itemgetter(1))
print highest
