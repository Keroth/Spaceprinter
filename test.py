#!/usr/bin/env python
from datetime import datetime
import locale
import textwrap


def textwrapper(text):
	wraped_text = textwrap.fill(text, initial_indent='   ', subsequent_indent='   ', width=29)

	textblock = wraped_text.split('\n')
	return textblock


def get_word(value):

	int_value = int(value)
	str_value = str(int_value)
	lenge = len(str_value)

	if lenge > 0:
		e = translate(int(str_value[lenge-1]))

	if lenge > 1:
		z  = translate(int(str_value[lenge-2]))

	if lenge > 2:
		h  = translate(int(str_value[lenge-3]))

	if lenge > 3:
		t  = translate(int(str_value[lenge-4]))

	return t,h,z,e

def translate(unit):

	if unit == 0:
		v = "Null"
	elif unit == 1:
		v = "Eins"
	elif unit == 2:
		v = "Zwei"
	elif unit == 3:
		v = "Drei"
	elif unit == 4:
		v = "Vier"
	elif unit == 5:
		v = "F\x81nf"
	elif unit == 6:
		v = "Sechs"
	elif unit == 7:
		v = "Sieben"
	elif unit == 8:
		v = "Acht"
	elif unit == 9:
		v = "Neun"

	return v

dt = datetime.now()

betrag = 1337.42

tausender, hunderter, zehner, einer = get_word(betrag)

verwendungszweck = textwrapper("Spendeneinnahmen 02.19 Zweckbindung 3D-Drucker")

#exit()

with open('/dev/usb/lp0', 'w') as printer:
	printer.write("\x1b\x43\x00\x04")
	printer.write("\n")
	printer.write("\n")
	printer.write("\n")
	printer.write("\t DE34 2806 0228 0037 0185 00\t")
	printer.write(locale.format("%.2f",betrag,grouping=True) + "\n")
	printer.write("\n")
	printer.write("\t Kreativit\x84t trifft Technik eV\n")
	printer.write("\n")
	printer.write("   \x1b\x53\x01Verwendungszweck:\x1b\x54")
	printer.write("\x1b\x24\xca\x00" + tausender + "\x1b\x24\x0e\x01" + hunderter + "\n")
	printer.write(verwendungszweck[0] + "\n")
	printer.write(verwendungszweck[1])
	printer.write("\x1b\x24\xca\x00" + zehner + "\x1b\x24\x0e\x01" + einer + "\n")
	printer.write("\n")
	printer.write("\n")
	printer.write("\x1b\x24\xca\x00" + dt.strftime('%d.%m.%Y') + ",\n")
	printer.write("\f\x07")