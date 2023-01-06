from picamera2 import *

tuning = Picamera2.load_tuning_file("imx477.json")

exposures = [100, 150, 250, 400, 650, 1050, 1700, 2750]

with picamera2.Picamera2(tuning=tuning) as cam:
	config = cam.configuration(main={"size": (1014, 760), "format": "RGB"},
                                   raw={"format": "SRGGB12", "size": (2032, 1520)})
	
        for exp in exposures:
            camera.set_controls({"ExposureTime": exp, "AnalogueGain": 1, "ColourGains": (1.0, 1.0)})
            camera.start()
