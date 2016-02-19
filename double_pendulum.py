# solve the ODEs for double-pendulum problem
import numpy as np
from scipy import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt


class DoublePendulum(object):
	"""Define the double pendulum class"""

	def __init__(self, m1, m2, l1, l2):
		self.m1, self.m2, self.l1, self.l2 = m1, m2, l1, l2
		self.init_status = np.array([0.0,0.0,0.0,0.0])      #[dth1, dth2, dv1, dv2]

	def equations(self, w, t):
		m1, m2, l1, l2 = self.m1, self.m2, self.l1, self.l2
		th1, th2, v1, v2 = w
		dth1 = v1
		dth2 = v2

		#eq of th1
		a = l1*l1*(m1+m2) # dv1 parameter
		b = l1*m2*l2*cos(th1-th2) # dv2 paramter
		c = l1*(m2*l2*sin(th1-th2)*dth2*dth2 + (m1+m2)*g*sin(th1))

		#eq of th2
		d = m2*l2*l1*cos(th1-th2) # dv1 parameter
		e = m2*l2*l2 # dv2 parameter
		f = m2*l2*(-l1*sin(th1-th2)*dth1*dth1 + g*sin(th2))

		dv1, dv2 = np.linalg.solve([[a,b],[d,e]], [-c,-f])

		return np.array([dth1, dth2, dv1, dv2])

	def double_pendulum(pendulum, ts, te, tstep):
		t = np.arange(ts, te, tstep)
		track = odeint(self.equations, pendulum.init_status, t)
		th1_array, th2_array = track[:,0], track[:, 1]
		l1, l2 = pendulum.l1, pendulum.l2
		x1 = l1*np.sin(th1_array)
		y1 = -l1*np.cos(th1_array)
		x2 = x1 + l2*np.sin(th2_array)
		y2 = y1 - l2*np.cos(th2_array)
		pendulum.init_status = track[-1,:].copy() 
		return [x1, y1, x2, y2]
