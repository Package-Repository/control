#import max for fmod/min/etc. recommend import only necessay functions
import math



class PID_Controller:

    __k_p = 0
    __k_i = 0
    __k_d = 0
    __angle_wrap = 0   
    __i_min = -1.0
    __i_max = 1.0
    __ctrl_val_min = -1.0
    __ctrl_val_max  = 1.0
    __ctrl_val_offset = 0.0


    def __init__(self):        

        pass

    #constructor with all variables
    def __init__(self,k_p, k_i,k_d,angle_wrap,
                i_min, i_max, ctrl_val_min,
                ctrl_val_max, 
                ctrl_val_offset):
        #initialize values
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.i_min = i_min                     # Helps clamp integral overshoot
        self.i_max = i_max
        self.ctrl_val_min = ctrl_val_min          # Helps clamp output from -1 to 1
        self.ctrl_val_max = ctrl_val_max
        self.ctrl_val_offset = ctrl_val_offset
        self.angle_wrap = angle_wrap
        self.integral = 0.0                       # Keeps track of integral over time
        self.previous_error = 0.0                 # Helps in derivative calculation
        pass


    #initialize k_p,k_i,k_d
    def __init__ (self,k_p, k_i, k_d):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        self.angle_wrap = 0   
        self.i_min = -1.0
        self.i_max = 1.0
        self.ctrl_val_min = -1.0
        self.ctrl_val_max  = 1.0
        self.ctrl_val_offset = 0.0
        self.angle_wrap = 0
        self.integral = 0.0                       # Keeps track of integral over time
        self.previous_error = 0.0                 # Helps in derivative calculation
        pass




    def set_gains(self,k_p, k_i, k_d):
        """     Reset the gain parameters. These are constants that have to be tuned to fit the system.
        Parameters:
                    
        *  kp - kd - ki Explanation:

        *  kp (proportional gain) determines the proportion of the control signal that is proportional to the error
        *  between the set point and the process variable. The larger the value of kp, the stronger the controller 
        *  will respond to the error.
        * 
        *  ki (integral gain) determines the proportion of the control signal that is proportional to the integral
        *  of the error over time. This term helps to eliminate any residual error that may be present after 
        *  the proportional term has done its job 
        * 
        *  kd (derivative gain) determines the proportion of the control signal that is proportional to the rate 
        *  of change of the error. This term helps to reduce overshoot and oscillations in the control signal, 
        *  by predicting the future error based on the current rate of change.
        */ """

        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d
        return
    

    def update(self,error, dt):
        """
        Perfrom a control step to correct for error in control system.

        Parameters:
        current_point: The current state of the system
        desired_point: The desired state of the system
        dt: The interval between update steps.
        Returns:
        ctrl_val: A PID output control value to correct for error in system
        */


        /* compute error which is important in determining our proportional, integral, derivative */

        /* if error is for angular inputs (roll, pitch, yaw), perform angle wrapping. */
        """

        if(self.angle_wrap):

            error = math.fmod(error,360)
            
            if (error > 180):
                error -= (2*180)

            elif (error < -180):
                error += (2 * 180)
            
        
        #Create our P-I-D based on error
        
        self.integral = self.integral + (error * dt)    #Integral builds over time
        self.integral = max(self.integral, self.i_min)
        self.integral = min(self.integral, self.i_max)
    
        proportional = (self.k_p * error)  # Directly proportional to error based on k_p constant
        integral = self.k_i * self.integral
        derivative = self.k_d * (error - self.previous_error) # Derivative takes into account previous error

        self.previous_error = error            # reset error for next cycle

        #Get our control value and clamp it if necessary
        ctrl_val = proportional + integral + derivative
        self.curr_ctrl_val = ctrl_val

        ctrl_val_first = max(ctrl_val, self.ctrl_val_min)
        ctrl_val_second = min(ctrl_val, self.ctrl_val_max)

        return ctrl_val_first,ctrl_val_second
    

    def getStatus(self):

        """ curretnly in C++
        // cout << "k_p: " << this->k_p << endl
        // cout << "k_i: " << this->k_i << endl
        // cout << "k_d: " << this->k_d << endl
        // cout << "integral: " << this->integral << endl
        // cout << "previous_error: " << this->previous_error << endl
        // cout << "control_value: " << this->curr_ctrl_val << endl
        """

        pass

#END OF CLASS DEFINITION
#TESTING BELOW


controller = PID_Controller(0.0, 0.0, 0.0)

ctrl_val_error_first, ctrl_val_error_second = controller.update(190.0, 3.0)

print(ctrl_val_error_first)   
print(ctrl_val_error_second)