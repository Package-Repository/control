
#scion controller @author Matthew Smith - Matthew on Discord
#rewite of 2023 scion_controller in python

from pid_controller import PID_Controller

class Scion_Position_PID_Controller:



    #default constructor create 6 PID_Controller objects that will information for (yaw,pitch,roll, x, y, z)

    def __init__(self):

        # Angle wrapping set to true for roll-pitch-yaw PID controllers
        self.yaw_pid = PID_Controller(0,0,0,True)
        self.pitch_pid = PID_Controller(0,0,0,True)
        self.roll_pid = PID_Controller(0,0,0,True)

        self.x_pos_pid = PID_Controller(0,0,0)
        self.y_pos_pid = PID_Controller(0,0,0)
        self.z_pos_pid = PID_Controller(0,0,0)

        #map string containing PID_controller for each elements by name
        self.controllers =  [
                            {'axis' : "yaw",   "PID" :  self.yaw_pid},
                            {'axis' : "pitch", "PID" :  self.pitch_pid},
                            {'axis' : "roll",  "PID" :  self.roll_pid},

                            {'axis' : "x_pos",  "PID" : self.x_pos_pid},
                            {'axis' : "y_pos",  "PID" : self.y_pos_pid},
                            {'axis' : "z_pos",  "PID" : self.z_pos_pid}
                            ]

        pass




        #MAKE SURE BASE CLASS HAS getStatus FUNTION UNCOMMENTED IF NEEDING TO TEST
    def getStatus(self):
        
        for controller in self.controllers:
            pid = controller['PID']
            pid.getStatus();


        pass




#Test Main 
    
scion_controller = Scion_Position_PID_Controller()

scion_controller.getStatus()








    
