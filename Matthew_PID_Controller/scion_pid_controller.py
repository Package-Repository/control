
#scion controller @author Matthew Smith - Matthew on Discord
#rewite of 2023 scion_controller in python

from pid_controller import PID_Controller
import numpy as np

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



        self.current_ctrl_vals = []
        self.current_thrust_values = []
        self.pid_thrust_mapper = [[]]


        #map string containing PID_controller for each elements by name
        self.controllers = {
                                'yaw':   self.yaw_pid,
                                'pitch': self.pitch_pid,
                                'roll':  self.roll_pid,
                                'x_pos': self.x_pos_pid,
                                'y_pos': self.y_pos_pid,
                                'z_pos': self.z_pos_pid
                            }

        pass


    """
    matrix mapping the 6 pid controller outputs to the 8 thrusters
    -----yaw---pitch---roll---x---y---z
    | T0
    | T1
    | T2
    | T3
    | T4
    | T5
    | T6
    | T7
    """


    ## 6X1 matrix ctrls . 8x1 matrix thrust . Need 8x6 matrix * 6x1 matrix
    ## 6X1 matrix . 2X1 matrix, Need 2X6 matrix * 6x1 matrix


    ##PID params constructor will tune PID using pid_params.py values

    # def __init__(self,pid_params):

    #     for controller in pid_params:
    #         print(1)



    #     pass


    #  /* 
    #   * Every time we have new data on our current and desired position, we can tell each PID_Controller
    #   * to update their current state 
    #   */

    def update(self, errors, dt):

        yaw_ctrl =    self.yaw_pid.update(errors[0], dt)
        pitch_ctrl =  self.pitch_pid.update(errors[1], dt)
        roll_ctrl =   self.roll_pid.update(errors[2], dt)
        x_pos_ctrl =  self.x_pos_pid.update(errors[3], dt)
        y_pos_ctrl =  self.y_pos_pid.update(errors[4], dt)
        z_pos_ctrl =  self.z_pos_pid.update(errors[5], dt)
        
        self.ctrl_vals = [yaw_ctrl, pitch_ctrl, roll_ctrl, x_pos_ctrl, y_pos_ctrl, z_pos_ctrl]

        self.current_ctrl_vals = self.ctrl_vals

        return self.ctrl_vals



    #MAKE SURE PID_CONTROOLER CLASS HAS getStatus FUNTION UNCOMMENTED IF NEEDING TO TEST
    def getStatus(self):
        

        print("REPORT FOR SCION PID")
        print("------------------------------------------------ \n")
            
        print("SCION PID Last Generated Control Values")
        print(self.current_ctrl_vals)


        for axis, pid in self.controllers.items():
            pid.getStatus()
        pass




#Test Main 
    
scion_controller = Scion_Position_PID_Controller()
scion_controller.getStatus()








    
