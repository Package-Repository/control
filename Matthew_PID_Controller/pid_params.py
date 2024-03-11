# /*
#  @author Matthew Smith 
#  Took json file written by Tristan and translated to C++ plus
#  changed some things.
#  These are PID parameters to tune the PID on initialization
#  Read about k_p, k_i, and k_d in the pid_controller.cpp file
#  Use MAX and MIN values to clamp our values to a reasonable range





#     To make sure motor isn't running at maximum value, we want to cap our ctrl_val min/max. You can do this changing the macros up above to 
#     your desired cap value.

#     k_p value should be set to a very low value for orientation to keep from always blasting the motors

class PID_Params:

    #MAX = .5
    #MIN = .5

    def __init__(self):

        MAX = .5
        MIN = -.5

        self.yaw = {

                    'kp': 0.0015,
                    'ki': 0.0003,
                    'kd': 0.0006,
                    #'ctrl_val_offset' :10.0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }
        
        self.pitch = {

                    'kp': 0.0015,
                    'ki': 0.0003,
                    'kd': 0.0006,
                    'ctrl_val_offset' :0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }
        
        self.roll = {

                    'kp': 0.0015,
                    'ki': 0.0003,
                    'kd': 0.0006,
                    #'ctrl_val_offset' :0.0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }
        
        self.x_pos = {

                    'kp': 0.16,
                    'ki': 0.005,
                    'kd': 0.008,
                    'ctrl_val_offset' : 0.0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }
        

        self.y_pos = {

                    'kp': 0.16,
                    'ki': 0.005,
                    'kd': 0.008,
                    'ctrl_val_offset' : 0.0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }

        self.z_pos = {

                    'kp': 0.800,
                    'ki': 0.003,
                    'kd': 0.002,
                    'ctrl_val_offset' : 0.0,
                    'ctrl_val_max': MAX,
                    'ctrl_val_min': MIN,
                    'i_max': MAX,
                    'i_min': MIN

                    }

    #comments are unused as of now, if uncommenting ensure proper python syntax
        
    # // self.yaw = 
    # // {
    # //     {'kp', 0.012},  // .015
    # //     {'ki', 0.003},   // .003
    # //     {'kd', 0.006},  // .006
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };

    # // self.pitch = 
    # // {
    # //     {'kp', 0.00015},
    # //     {'ki', 0.00003},
    # //     {'kd', 0.00006},
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };
    
    # // self.roll = 
    # // {
    # //     {'kp', 0.00015},
    # //     {'ki', 0.00003},
    # //     {'kd', 0.00006},
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };
    
    # // self.x_pos =
    # // {
    # //     {'kp', 0.4},
    # //     {'ki', 0.03},
    # //     {'kd', 0.01},
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };

    # // self.y_pos = 
    # // {
    # //     {'kp', 0.4},
    # //     {'ki', 0.03},
    # //     {'kd', 0.01},
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };

    # // self.z_pos =
    # // {
    # //     {'kp', 0.00001},
    # //     {'ki', 0.00001},
    # //     {'kd', 0.00001},
    # //     {'ctrl_val_offset', 0.0},
    # //     {'ctrl_val_max', MAX},
    # //     {'ctrl_val_min', MIN},
    # //     {'i_max', MAX},
    # //     {'i_min', MIN}
    # // };


        self.pid_params = {

                            'roll',  self.roll,
                            'pitch', self.pitch,
                            'yaw',   self.yaw,
                            'x_pos', self.x_pos,
                            'y_pos', self.y_pos,
                            'z_pos', self.z_pos,
                            'x_vel', self.x_vel,
                            'y_vel', self.y_vel,
                            'z_vel', self.z_vel

                            }


        pass
    

    def get_pid_params(self):

        return self.pid_params

        pass
