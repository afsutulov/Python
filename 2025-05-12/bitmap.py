#!/usr/bin/python3

import sys

bitmap = """
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
"""

print(bitmap)

print('Введите сообщение для всего мира')
message = input()
if message == "": sys.exit()
for line in bitmap.splitlines():
    for i, bit in enumerate(line):
       if bit == ' ': print(" ", end='')
       else: print(message[i % len(message)], end='')
    print()
