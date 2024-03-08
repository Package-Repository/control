# from PID import PID
from PID import PID

from multiprocessing import Process, Value
from time import sleep, perf_counter


class AirSimulation:
	def measure_speed(self) -> float:
		value = float()
		with self.__current_velocity.get_lock():
			value = float(self.__current_velocity.value)
		return value

	def set_power(self, signal: float) -> None:
		with self.__current_power.get_lock():
			self.__current_power.value = float(signal)

	def __init__(self, inital_velocity: float = 10.0):
		self.__current_velocity = Value('f', float(inital_velocity))
		self.__current_power = Value('f', 0.0)

		Process(target=self.__background_daemon, args=[], daemon=True).start()
	def __background_daemon(self):

		while True:
			current_velocity = self.__current_velocity.value
			current_speed = abs(current_velocity)

			current_power = self.__current_power.value

			# Calculate Air Resistive Delta
			coe_air: float = -0.002
			air_delta: float = coe_air * current_velocity * current_speed

			# Calulate Motor Delta
			coe_motor: float = 0.2
			motor_delta: float = coe_motor * current_power / (current_speed + 1)

			with self.__current_velocity.get_lock():
				self.__current_velocity.value += air_delta 
				self.__current_velocity.value += motor_delta
			
			# Go to next time step
			time_step_time_sec: float = 0.01
			sleep(time_step_time_sec)

start_time_sec: float = perf_counter()
sleep_time_interal_sec: float = 0.100

def idle_log(total_sleep_time: float, measure):
	num_sleeps: int = int(total_sleep_time // sleep_time_interal_sec)
	rem_sleep_time_sec: float = total_sleep_time % sleep_time_interal_sec

	for i in range(num_sleeps):
		print(f"time: {(perf_counter() - start_time_sec):.3f} --- velocity: {measure():.3f}")
		sleep(sleep_time_interal_sec)
	sleep(rem_sleep_time_sec)


if __name__ == '__main__':
	
	sim = AirSimulation(inital_velocity=0.0)

	idle_log(1.000, sim.measure_speed)


	my_pid_controller = PID(
		output=sim.set_power, signal=sim.measure_speed, Kpid = [10.0, 5.0, -0.5]
	)
	refrence_signal = 20.0
	print(f"setting PID {refrence_signal}")
	my_pid_controller.set_refrence(refrence_signal)

	idle_log(4.000, sim.measure_speed)

	refrence_signal = 10.0
	print(f"setting PID {refrence_signal}")
	my_pid_controller.set_refrence(refrence_signal)

	idle_log(4.000, sim.measure_speed)

	# start_time = perf_counter()
	# for i in range(0,10):
	# 	print(f"time: {perf_counter() - start_time}, vel: {sim.measure_speed()}")
	# 	sleep(0.1)
	# print("######################changing power!######################")
	# sim.set_power(100.0)
	# for i in range(0,50):
	# 	print(f"time: {perf_counter() - start_time}, vel: {sim.measure_speed()}")
	# 	sleep(0.1)
