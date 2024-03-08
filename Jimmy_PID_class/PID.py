from threading import Thread
from time import sleep, perf_counter
from collections import deque

class PID:
####################################################################################################
#################################### Public API Functions Below ####################################
####################################################################################################
	def kill(self):
		self.__del__()

	def set_refrence(self, refence_signal: float) -> None:
		self.__current_refrence_signal = float(refence_signal)
	
	# TODO:	Implement
	def set_input(self, signal_times: [float], refence_signals: [float]) -> None:
		# TODO: Validate times are floats in sequential order and start at zero
		# TODO: Validate signals are floats have have the same cardinality as [times]
		# TODO: Create sleep schedule
		# TODO: Interate through sleep schedule seting the refrences
		# TODO: Make sure sleep times account for already used time
		pass

	def get_refrence(self) -> float:
		return float(self.__current_refrence_signal)

	# TODO: Implement an internal variable for current signal inside the class
	def get_obverved(self) -> float: 
		# Refrence_Signal - Error_Signal
		# Refrence_Signal - (Refrence_Signal - Observed_Signal)
		return float(self.__current_refrence_signal) - float(self.__error_signal_history[0])

	def __init__(self, 
		# Both are mandatory function assignments
		signal, output,
		# pid coeffients should be in order and be convertable in to floats
		Kpid: [float] = [0.0, 0.0, 0.0],
		# TODO: think of ideal default time
		min_loop_time_sec: float = 0.05,
		# This is a file that time, refrence, and observed can be written to. It must be in a file 
		# format. Setting to None type will print to console
		default_log_file = False # TODO: Implement
	):

		self.__read_signal = signal
		self.__output_to_plant = output

		# Validate as needed
		[self.__Kp, self.__Ki, self.__Kd] = [float(K_value) for K_value in Kpid]

		min_loop_time_sec = float(min_loop_time_sec)
		if min_loop_time_sec < 0:
			raise ValueError('The closed loop time is less than zero.')

		self.__min_closed_loop_time_sec: float = min_loop_time_sec

		# validate read function and bootstrap the math functionality
		current_observed_signal:  float = float(self.__read_signal())
		current_observation_time: float = perf_counter()
		
		self.__start_time:        float = current_observation_time

		self.__current_refrence_signal: float = current_observed_signal

		self.__keep_contoller_alive: bool = True

		# Running history of errors and thier respective times
		self.__integral_time_range_sec: float = 0.50 # TODO: think of good default value
		self.__error_signal_history: [int] = deque()
		self.__signal_times_history: [int] = deque()

		current_error_signal: float = self.__current_refrence_signal - current_observed_signal

		self.__error_signal_history.append(current_error_signal)
		self.__signal_times_history.append(current_observation_time)

		
		

		self.__current_error_integral: float = 0.0
		self.__current_error_integral += current_error_signal

		self.__current_error_derivitive: float = 0.0



		self.__background_work_t = Thread(target=self.__closed_loop_daemon, args=[], daemon=True)
		self.__background_work_t.start()
####################################################################################################
################################ Protected Access Level Code Below #################################
####################################################################################################
	

	# Both read signal and output signal functions are assigned at runtime
	# Both functions should be multithread-safe if they are to be called with PID is alive
	def __read_signal(self) -> float:
		pass
	def __output_to_plant(self, final_output: float) -> None:
		pass

	def __del__(self) -> None:
		# Once the object is out of scope, the PID controller can not be used
		self.__keep_contoller_alive = False


	def __closed_loop_daemon(self) -> None:
		while self.__keep_contoller_alive:
			time_delta_sec: float = perf_counter()

			# Do the observation
			current_observed_signal  = float(self.__read_signal())
			current_observation_time = perf_counter()

			# Do the math
			current_error_signal: float 
			current_error_signal = self.__current_refrence_signal - current_observed_signal
			
			previous_observation_time: float = self.__signal_times_history[-1]
			closed_loop_time_delta: float = current_observation_time - previous_observation_time

			self.__current_error_integral += current_error_signal

			error_signal_delta: float = current_error_signal - self.__error_signal_history[-1]
			self.__current_error_derivitive = error_signal_delta	/ closed_loop_time_delta

			
			calculated_output_signal: float = self.__Kp * current_error_signal
			calculated_output_signal       += self.__Ki * self.__current_error_integral
			calculated_output_signal       += self.__Kd * self.__current_error_derivitive

			# output the calculated signal
			self.__output_to_plant(calculated_output_signal)

			# Update the history
			self.__error_signal_history.append(current_error_signal)
			self.__signal_times_history.append(current_observation_time)
			
			# remove entries if nessary
			max_allow_time = self.__signal_times_history[0] + self.__integral_time_range_sec
			history_in_range: bool = max_allow_time > current_observation_time

			while not history_in_range:
				self.__error_signal_history.popleft()
				self.__signal_times_history.popleft()

				max_allow_time = self.__signal_times_history[0] + self.__integral_time_range_sec
				history_in_range = max_allow_time > current_observation_time

			# Output to Log if nessary
			# TODO
			
			time_delta_sec = perf_counter() - time_delta_sec
			sleep_time_sec: float = self.__min_closed_loop_time_sec - time_delta_sec
			if sleep_time_sec > 0.0:
				sleep(sleep_time_sec)


def example_test_read_signal() -> float:
	return float(perf_counter() // 1 % 100)
def example_text_output(input):
	print(f"outputing {input}")
	pass
if __name__ == '__main__':
	my_obj = PID(output=example_text_output, signal=example_test_read_signal, Kpid = [0.0, 0.0, 0.0])
	sleep(2.0)