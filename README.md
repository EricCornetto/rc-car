# rc-car
Remote Controller Car Project build by raspberry pi

#Configuration :
LEFT MOTOR PIN GPIO : 19,26
RIGTH MOTOR PIN GPIO : 20,21


#Pre-Prerequisites :

Xbox Controller version :
If you want to used xbox controller to controlling the rc-car you have to install fews of packages like xpadneo (if you used xbox one controller) and xbox360controller

a. Install xpadneo
xpadneo is a advanced linux driver for xbox one wireless gamepad controller, you can check out how to install it on this link https://atar-axis.github.io/xpadneo/

b. Install xbox360controller
 xbox360controller is a python packages aims to provide pythonic and complete API for your xbox360 and similiar game controllers.
 
 you will need Python 3.4 or above.
 
 Any linux distribution.
 
 pip3 install -U xbox360controller
 
 #Run Program :
 python3 rccar_xbox.py
