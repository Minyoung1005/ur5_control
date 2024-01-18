import mujoco_py
from environment import lab_env
import numpy as np
import time
import math
import ikpy

"""model_path = 'UR5gripper.xml'
save_model_path = 'UR5gripper_custom.xml'
tree, _ = changer(model_path)
tree.write(open(save_model_path, 'wb'))"""

def gripper_consistent(angle):
    x = -0.006496 + 0.0315 * math.sin(angle[0]) + 0.04787744772 * math.cos(angle[0] + angle[1] - 0.1256503306) - 0.02114828598 * math.sin(angle[0] + angle[1] + angle[2] - 0.1184899592)
    y = -0.0186011 - 0.0315 * math.cos(angle[0]) + 0.04787744772 * math.sin(angle[0] + angle[1] - 0.1256503306) + 0.02114828598 * math.cos(angle[0] + angle[1] + angle[2] - 0.1184899592)
    return math.atan2(y, x) + 0.6789024115

env = lab_env(None)
num_action = len(env.sim.data.ctrl[:])
grasp = 0

render = True

"""for j in range(50):
	for i in range(1000):
		env.sim.data.qpos[9] = 0.7
		env.sim.data.qpos[13] = 0.7
		env.sim.forward()
		if render:
			env.viewer.render()

	for i in range(1000):
		env.sim.data.qpos[9] = 0.0
		env.sim.data.qpos[13] = 0.0
		env.sim.forward()
		env.sim.step()
		if render:
			env.viewer.render()"""
for j in range(300):
	random_action = np.random.rand(num_action) * 2.0 - 1.0
	env.sim.data.ctrl[:num_action] = np.zeros((num_action))
	env.sim.data.ctrl[1] = -1.0
	env.sim.data.ctrl[8] = -1.0
	env.sim.step()
	if render:
		env.viewer.render()
		time.sleep(0.01)



"""for j in range(50):
	for i in range(1000):
		random_action = np.random.rand(num_action) * 2.0 - 1.0
		env.sim.data.ctrl[:num_action] = np.zeros((num_action))
		env.sim.data.ctrl[6:8] = 1.0
		env.sim.data.ctrl[8] = -1.0
		env.sim.step()

		env.sim.data.qpos[9] = gripper_consistent(env.sim.data.qpos[6: 9])
		env.sim.data.qpos[13] = gripper_consistent(env.sim.data.qpos[10: 13])
		env.sim.forward()
		if render:
			env.viewer.render()

	for i in range(1000):
		random_action = np.random.rand(num_action) * 2.0 - 1.0
		env.sim.data.ctrl[:num_action] = np.zeros((num_action))
		env.sim.data.ctrl[6:8] = -1.0
		env.sim.data.ctrl[8] = -1.0
		env.sim.step()

		env.sim.data.qpos[9] = gripper_consistent(env.sim.data.qpos[6: 9])
		env.sim.data.qpos[13] = gripper_consistent(env.sim.data.qpos[10: 13])
		env.sim.forward()
		if render:
			env.viewer.render()"""	


"""for j in range(50):
	for i in range(1000):
		random_action = np.random.rand(num_action) * 2.0 - 1.0
		env.sim.data.ctrl[:num_action] = np.zeros((num_action))
		env.sim.data.ctrl[6:8] = 5.0
		env.sim.data.ctrl[8] = -1.0
		env.sim.step()
		if render:
			env.viewer.render()

	for i in range(1000):
		random_action = np.random.rand(num_action) * 2.0 - 1.0
		env.sim.data.ctrl[:num_action] = np.zeros((num_action))
		env.sim.data.ctrl[6:8] = -5.0
		env.sim.data.ctrl[8] = -1.0
		env.sim.step()
		if render:
			env.viewer.render()"""