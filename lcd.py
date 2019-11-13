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

import lcddriver
from time import *
from optparse import OptionParser

#parse arguments
parser = OptionParser()
#parse values
parser.add_option("-a", "--address", action="store", dest="address",
                  help="I2C Adress")
                  
parser.add_option("-p", "--persistent",
                  action="store_true", dest="persistent", default=False,
                  help="-p = do not clear display before new write")
                  
parser.add_option("--line1",
                  action="store", dest="line1",
                  help="text to line 1")

parser.add_option("--line2",
                  action="store", dest="line2",
                  help="text to line 2")
                  
parser.add_option("--line3",
                  action="store", dest="line3",
                  help="text to line 3")
                  
parser.add_option("--line4",
                  action="store", dest="line4",
                  help="text to line 4")              
                  
parser.add_option("--backlight-off",
                  action="store_true", dest="backlightoff", default=False,
                  help="Turn off backlight")    

#parse arguments to values
(options, args) = parser.parse_args()

#process argument - address
#lcd = lcddriver.lcd(options.address)
lcd = lcddriver.lcd(int(options.address,0))

#process argument - persistent
if not options.persistent:
    lcd.lcd_clear()
    
#process argument - backlight
if options.backlightoff:
    lcd.backlightOff()
else:
    lcd.backlightOn()
    
#process argument line 1-4
for num in range(1,4):  #to iterate between lines 1 to 4
    try:
        getattr(options, "line%d" % num)
    except NameError:
        print "Line %d not set" (num)
    except NoneType:
        print "Line %d noneType" (num)
    else:
        if getattr(options, "line%d" % num) is not None and len(getattr(options, "line%d" % num)) > 0:
            lcd.lcd_display_string(getattr(options, "line%d" % num),num);
