import numpy as np

a,b,h,m=[int(i) for i in input().split()]

def get_angle(h,m):
    long_angle=2*np.pi*m/60
    short_angle=2*np.pi*h/12+(2*np.pi/12)*m/60
    big_angle=max(long_angle,short_angle)
    small_angle = min(long_angle, short_angle)
    angle=min(big_angle-small_angle,2*np.pi-big_angle+small_angle)
    return angle

def yogen(a,b,theta):
    ans=a**2+b**2-2*a*b*np.cos(theta)
    return ans**0.5

print(yogen(a,b,get_angle(h,m)))