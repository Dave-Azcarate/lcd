#The MIT License (MIT)
#
#Copyright (c) [2016] [David "Fires" Stein] [http://davidstein.cz]
#
#Based on RPI I2C backpack from Michael Horne at http://www.recantha.co.uk/blog/?p=4849
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from time import *
from OmegaExpansion import onionI2C

class i2c_device:
   def __init__(self, addr, port=0):
      self.addr = addr
      self.i2c = onionI2C.OnionI2C(port)

# Write a single command
   def write_cmd(self, cmd):
      self.i2c.write(self.addr, [cmd])
      sleep(0.0001)

# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.i2c.writeByte(self.addr, cmd, data)
      sleep(0.0001)

# Write a block of data
   def write_block_data(self, cmd, data):
      self.i2c.writeBytes(self.addr, cmd, [data])
      sleep(0.0001)

# Read a single byte
#   def read(self):
#      return self.bus.read_byte(self.addr)
#
## Read
#   def read_data(self, cmd):
#      return self.i2c.readBytes(self.addr, cmd,1)
#
## Read a block of data
#   def read_block_data(self, cmd):
#      return self.i2c.readBytes(self.addr, cmd)