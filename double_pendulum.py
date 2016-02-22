# solve the ODEs for double-pendulum problem
import numpy as np
from scipy import sin, cos
from scipy.integrate import odeint
import matplotlib.pyplot as pl


class DoublePendulum(object):
	"""Define the double pendulum class"""

	def __init__(self, m1, m2, l1, l2):
		self.m1, self.m2, self.l1, self.l2 = m1, m2, l1, l2
		self.status = np.array([0.0,0.0,0.0,0.0])      #[th1, th2, v1, v2]

	def equations(self, w, t):
		""" return the derivatives for each variable"""
		# the input argument w is the state of all target varialbes
		g = 9.8
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

	def ode_solve(self, t):
		""" Solve the system of equations describing the motion of the double pendulum"""
		track = odeint(self.equations, self.status, t)
		th1, th2 = track[-1, 0], track[-1, 1]
		x1 = self.l1*np.sin(th1)
		y1 = -self.l1*np.cos(th1)
		x2 = x1 + self.l2*np.sin(th2)
		y2 = y1 - self.l2*np.cos(th2)
		self.status = track[-1,:].copy() 
		return [x1, y1, x2, y2, th1, th2]

	def euler_ode(self, t, dt):
		""" Euler method to solve the ODEs"""
		# obtain the derivatives of the angle variables (dth1, dth2, d2th1, d2th2)
		deri = self.equations(self.status, t)
		dth1 = deri[0]
		dth2 = deri[1]
		d2th1 = deri[2]
		d2th2 = deri[3]

		# get values for the new timestep by adding the increment
		#[th1, th2, v1, v2]
		self.status[0] += dth1*dt
		self.status[1] += dth2*dt
		self.status[2] += d2th1*dt
		self.status[3] += d2th2*dt

		# 
		while abs(self.status[0]) > np.pi:
			if self.status[0] > 0.0:
				self.status[0] -= 2*np.pi
			else:
				self.status[0] += 2*np.pi

		while abs(self.status[1]) > np.pi:
			if self.status[1] > 0.0:
				self.status[1] -= 2*np.pi
			else:
				self.status[1] += 2*np.pi

		# convert the angle to the cartesian coordinates
		x1 = self.l1*np.sin(self.status[0])
		y1 = -self.l1*np.cos(self.status[0])
		x2 = x1 + self.l2*np.sin(self.status[1])
		y2 = y1 - self.l2*np.cos(self.status[1])

		return [x1, y1, x2, y2, self.status[0], self.status[1]]


if __name__ == "__main__":
	"""to test the double_pendulum module"""

	pendulum = DoublePendulum(1.0, 2.0, 1.0, 2.0)
	th1, th2 = 1.0, 2.0
	pendulum.status[:2] = th1, th2

	ts = 0.0
	te = 30.0
	tstep = 0.01
	t = np.arange(ts, te, tstep)

	x1 = []
	y1 = []
	x2 = []
	y2 = []
	for tim in t:
		time = np.array([tim, tim+tstep])
		result = pendulum.ode_solve(time)
		#result = pendulum.euler_ode(tim, tstep)
		x1.append(result[0])
		y1.append(result[1])
		x2.append(result[2])
		y2.append(result[3])

	pl.plot(x1,y1, label = "upper")
	pl.plot(x2,y2, label = "lower")
	pl.legend()
	pl.axis("equal")
	pl.show()