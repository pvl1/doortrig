import serial
import io
import time
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("/home/pavel/cops_theme.wav")
#play_obj = wave_obj
#, timeout=1000
ser = serial.serial_for_url('/dev/ttyACM0',timeout=5)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
testnum=1
result=0
someflag=0
while testnum==1:
	#time.sleep(1)
	returned=sio.readline().rstrip(' ').rstrip('\n').rstrip(' ')
	try:
		result=float(returned)
		#print (result)
	except ValueError:
		result = 950

    #    returned=0

	if result>1000.0:
		someflag=0
		#print ("Atf")
		try:
			if play_obj.is_playing():
				#print ("stop")

				play_obj.stop()

		except NameError:
			#print("stoperr")
			continue
	#if returned:
	#	someflag=1
	#	print('open')
	elif result<900.0:
			print(result)
			#try:
			#	if play_obj.is_playing():
			#		print("playing")
			#		someflag=1
			#	#play_obj.wait_done()
			#except NameError:
			#	print("doesntex")
			if someflag==0:
				someflag=1
				try:
					if play_obj.is_playing():
						print ("skip")
					else:
						print("play")
						play_obj = wave_obj.play()
						time.sleep(15)
				except NameError:
					print("playcatch")
					play_obj = wave_obj.play()
					time.sleep(15)
					#continue

				#play_obj = wave_obj.play()
				#time.sleep(5)
	#				play_obj.stop()

				#except Error:
				#	print("someerror")#play_obj.wait_done()
			#if someflag==0:

		#time.sleep(30)
# sio.write(unicode("hello\n"))
# sio.flush() # it is buffering. required to get the data out *now*
# hello = sio.readline()
# print(hello == unicode("hello\n"))
