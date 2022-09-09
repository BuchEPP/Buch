#
from sympy import *
init_printing()
#
#
#print('Reading heppackv0.py')
#print()
g0=Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
g1=Matrix([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]])
g2=Matrix([[0,0,0,-I],[0,0,I,0],[0,I,0,0],[-I,0,0,0]])
g3=Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
#g5=I*g0*g1*g2*g3
g5=Matrix([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
one=Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
projpl=(one+g5)/2
projm=(one-g5)/2
#
#
def u_l(Ef,mf,theta,phi):
	elm1=-exp(-I*phi)*sin(theta/2)
	elm2=cos(theta/2)
	fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	fac2=sqrt(Ef+mf)
	elm3=-fac1*elm1
	elm4=-fac1*elm2
	result=fac2*Matrix([[elm1],[elm2],[elm3],[elm4]])
	return result
#
def u_r(Ef,mf,theta,phi):
	elm2=exp(I*phi)*sin(theta/2)
	elm1=cos(theta/2)
	fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	fac2=sqrt(Ef+mf)
	elm3=fac1*elm1
	elm4=fac1*elm2
	result=fac2*Matrix([[elm1],[elm2],[elm3],[elm4]])
	return result
#
def v_l(Ef,mf,theta,phi):
	elm4=exp(I*phi)*sin(theta/2)
	elm3=cos(theta/2)
	fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	fac2=sqrt(Ef+mf)
	elm1=fac1*elm3
	elm2=fac1*elm4
	result=fac2*Matrix([[elm1],[elm2],[elm3],[elm4]])
	return result
#
def v_r(Ef,mf,theta,phi):
	elm3=-exp(-I*phi)*sin(theta/2)
	elm4=cos(theta/2)
	fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	fac2=sqrt(Ef+mf)
	elm1=-fac1*elm3
	elm2=-fac1*elm4
	result=fac2*Matrix([[elm1],[elm2],[elm3],[elm4]])
	return result
#
def u_lbar(Ef,mf,theta,phi):
	h1=u_l(Ef,mf,theta,phi).T*g0
	elm1=h1[0]*exp(2*I*phi)
	elm2=h1[1]
	#fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	#fac2=sqrt(Ef+mf)
	elm3=h1[2]*exp(2*I*phi)
	elm4=h1[3]
	result=Matrix([[elm1,elm2,elm3,elm4]])
	return result
#
def u_rbar(Ef,mf,theta,phi):
	h1=u_r(Ef,mf,theta,phi).T*g0
	elm2=h1[1]*exp(-2*I*phi)
	elm1=h1[0]
	#fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	#fac2=sqrt(Ef+mf)
	elm4=h1[3]*exp(-2*I*phi)
	elm3=h1[2]
	result=Matrix([[elm1,elm2,elm3,elm4]])
	return result
#
def v_lbar(Ef,mf,theta,phi):
	h1=v_l(Ef,mf,theta,phi).T*g0
	elm2=h1[1]*exp(-2*I*phi)
	elm1=h1[0]
	#fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	#fac2=sqrt(Ef+mf)
	elm4=h1[3]*exp(-2*I*phi)
	elm3=h1[2]
	result=Matrix([[elm1,elm2,elm3,elm4]])
	return result
#
def v_rbar(Ef,mf,theta,phi):
	h1=v_r(Ef,mf,theta,phi).T*g0
	elm1=h1[0]*exp(2*I*phi)
	elm2=h1[1]
	#fac1=sqrt(Ef-mf)/sqrt(Ef+mf)
	#fac2=sqrt(Ef+mf)
	elm3=h1[2]*exp(2*I*phi)
	elm4=h1[3]
	result=Matrix([[elm1,elm2,elm3,elm4]])
	return result
#
def u(pp,ha):
        if ha >= 0:
                result=u_r(pp[0],pp[1],pp[2],pp[3])
        elif ha < 0:
                result=u_l(pp[0],pp[1],pp[2],pp[3])
        return result
#
def v(pp,ha):
        if ha >= 0:
                result=v_r(pp[0],pp[1],pp[2],pp[3])
        elif ha < 0:
                result=v_l(pp[0],pp[1],pp[2],pp[3])
        return result
#
def ubar(pp,ha):
        if ha >= 0:
                result=u_rbar(pp[0],pp[1],pp[2],pp[3])
        elif ha < 0:
                result=u_lbar(pp[0],pp[1],pp[2],pp[3])
        return result
#
def vbar(pp,ha):
        if ha >= 0:
                result=v_rbar(pp[0],pp[1],pp[2],pp[3])
        elif ha < 0:
                result=v_lbar(pp[0],pp[1],pp[2],pp[3])
        return result
#
# Ströme gamma_mu Kopplung
#
def ubv(p1,h1,p2,h2):
        j0=ubar(p1,h1)*g0*v(p2,h2)
        j1=ubar(p1,h1)*g1*v(p2,h2)
        j2=ubar(p1,h1)*g2*v(p2,h2)
        j3=ubar(p1,h1)*g3*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
def ubu(p1,h1,p2,h2):
        j0=ubar(p1,h1)*g0*u(p2,h2)
        j1=ubar(p1,h1)*g1*u(p2,h2)
        j2=ubar(p1,h1)*g2*u(p2,h2)
        j3=ubar(p1,h1)*g3*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
def vbu(p1,h1,p2,h2):
        j0=vbar(p1,h1)*g0*u(p2,h2)
        j1=vbar(p1,h1)*g1*u(p2,h2)
        j2=vbar(p1,h1)*g2*u(p2,h2)
        j3=vbar(p1,h1)*g3*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
def vbv(p1,h1,p2,h2):
        j0=vbar(p1,h1)*g0*v(p2,h2)
        j1=vbar(p1,h1)*g1*v(p2,h2)
        j2=vbar(p1,h1)*g2*v(p2,h2)
        j3=vbar(p1,h1)*g3*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
# charged current weak interaction, (1-g5) coupling
#
#
def ubvw(p1,h1,p2,h2):
        j0=ubar(p1,h1)*g0*projm*v(p2,h2)
        j1=ubar(p1,h1)*g1*projm*v(p2,h2)
        j2=ubar(p1,h1)*g2*projm*v(p2,h2)
        j3=ubar(p1,h1)*g3*projm*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
#
def ubuw(p1,h1,p2,h2):
        j0=ubar(p1,h1)*g0*projm*u(p2,h2)
        j1=ubar(p1,h1)*g1*projm*u(p2,h2)
        j2=ubar(p1,h1)*g2*projm*u(p2,h2)
        j3=ubar(p1,h1)*g3*projm*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
#
def vbuw(p1,h1,p2,h2):
        j0=vbar(p1,h1)*g0*projm*u(p2,h2)
        j1=vbar(p1,h1)*g1*projm*u(p2,h2)
        j2=vbar(p1,h1)*g2*projm*u(p2,h2)
        j3=vbar(p1,h1)*g3*projm*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
def vbvw(p1,h1,p2,h2):
        j0=vbar(p1,h1)*g0*projm*v(p2,h2)
        j1=vbar(p1,h1)*g1*projm*v(p2,h2)
        j2=vbar(p1,h1)*g2*projm*v(p2,h2)
        j3=vbar(p1,h1)*g3*projm*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
# Ströme cv-ca*g5 Kopplung
#
def ubvva(p1,h1,p2,h2,cv,ca):
        gv=cv/2
        ga=ca/2
        j0=ubar(p1,h1)*g0*(gv*one-ga*g5)*v(p2,h2)
        j1=ubar(p1,h1)*g1*(gv*one-ga*g5)*v(p2,h2)
        j2=ubar(p1,h1)*g2*(gv*one-ga*g5)*v(p2,h2)
        j3=ubar(p1,h1)*g3*(gv*one-ga*g5)*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
#
def ubuva(p1,h1,p2,h2,cv,ca):
        gv=cv/2
        ga=ca/2
        j0=ubar(p1,h1)*g0*(gv*one-ga*g5)*u(p2,h2)
        j1=ubar(p1,h1)*g1*(gv*one-ga*g5)*u(p2,h2)
        j2=ubar(p1,h1)*g2*(gv*one-ga*g5)*u(p2,h2)
        j3=ubar(p1,h1)*g3*(gv*one-ga*g5)*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
##
def vbuva(p1,h1,p2,h2,cv,ca):
        gv=cv/2
        ga=ca/2
        j0=vbar(p1,h1)*g0*(gv*one-ga*g5)*u(p2,h2)
        j1=vbar(p1,h1)*g1*(gv*one-ga*g5)*u(p2,h2)
        j2=vbar(p1,h1)*g2*(gv*one-ga*g5)*u(p2,h2)
        j3=vbar(p1,h1)*g3*(gv*one-ga*g5)*u(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
#
def vbvva(p1,h1,p2,h2,cv,ca):
        gv=cv/2
        ga=ca/2
        j0=vbar(p1,h1)*g0*(gv*one-ga*g5)*v(p2,h2)
        j1=vbar(p1,h1)*g1*(gv*one-ga*g5)*v(p2,h2)
        j2=vbar(p1,h1)*g2*(gv*one-ga*g5)*v(p2,h2)
        j3=vbar(p1,h1)*g3*(gv*one-ga*g5)*v(p2,h2)
        result=[simplify(j0[0]),simplify(j1[0]),simplify(j2[0]),simplify(j3[0])]
        return result
#
#
def dotprod4(jj1,jj2):
        h1=jj1[0]*jj2[0]-jj1[1]*jj2[1]-jj1[2]*jj2[2]-jj1[3]*jj2[3]
        result=simplify(h1)
        return result
#
def fourvec(pp):
        elm1=pp[0]
        elm2=pp[1]
        elm3=pp[2]
        elm4=pp[3]
        h0=elm3/2
        h1=2*sin(h0)*cos(h0)
        h2=cos(h0)**2-sin(h0)**2
        p=sqrt(elm1**2-elm2**2)
        result=[elm1,p*h1*cos(elm4),p*h1*sin(elm4),p*h2]
        return result
#
def dag(pp):
        elm1=pp[0]
        elm2=pp[1]
        elm3=pp[2]
        elm4=pp[3]
        result=elm1*g0-elm2*g1-elm3*g2-elm4*g3
        return result
#
# Pauli currents
#
def ubuP(p1,h1,p2,h2):
        M=p1[1]
        p14=fourvec(p1)
        p24=fourvec(p2)
# qmu with lower index
        q0=p14[0]-p24[0]
        q1=-p14[1]+p24[1]
        q2=-p14[2]+p24[2]
        q3=-p14[3]+p24[3]
# sigmamunu with upper index like in Bjorken Drell
# but without factor i/2
        jF0=(g0*g1-g1*g0)*q1+(g0*g2-g2*g0)*q2+(g0*g3-g3*g0)*q3
        jF1=(g1*g0-g0*g1)*q0+(g1*g2-g2*g1)*q2+(g1*g3-g3*g1)*q3
        jF2=(g2*g0-g0*g2)*q0+(g2*g1-g1*g2)*q1+(g2*g3-g3*g2)*q3
        jF3=(g3*g0-g0*g3)*q0+(g3*g1-g1*g3)*q1+(g3*g2-g2*g3)*q2
        j0=ubar(p1,h1)*jF0/4/M*u(p2,h2)
        j1=ubar(p1,h1)*jF1/4/M*u(p2,h2)
        j2=ubar(p1,h1)*jF2/4/M*u(p2,h2)
        j3=ubar(p1,h1)*jF3/4/M*u(p2,h2)
        #include factor i/2
        result=[-j0[0],-j1[0],-j2[0],-j3[0]]
        return result
#
#
#
# Polarization vectors for photons and W bosons
#
def pol_r(theta,phi):

        elm1=0
        h1=cos(theta/2)**2-sin(theta/2)**2
        h2=2*sin(theta/2)*cos(theta/2)
        elm2=sqrt(2)*cos(phi)*h1/2-I*sqrt(2)*sin(phi)/2
        elm3=sqrt(2)*sin(phi)*h1/2+I*sqrt(2)*cos(phi)/2
        elm4=-sqrt(2)*h2/2
        result=[elm1,elm2,elm3,elm4]
        return result
#
#
def pol_l(theta,phi):

        elm1=0
        h1=cos(theta/2)**2-sin(theta/2)**2
        h2=2*sin(theta/2)*cos(theta/2)
        elm2=sqrt(2)*cos(phi)*h1/2+I*sqrt(2)*sin(phi)/2
        elm3=sqrt(2)*sin(phi)*h1/2-I*sqrt(2)*cos(phi)/2
        elm4=-sqrt(2)*h2/2
        result=[elm1,elm2,elm3,elm4]
        return result
#
#
def pol_0(e0,m0,theta,phi):
        elm1=sqrt(e0**2-m0**2)/m0
        elm2=e0*sin(theta)*cos(phi)/m0
        elm3=e0*sin(theta)*sin(phi)/m0
        elm4=e0*cos(theta)/m0
        result=[elm1,elm2,elm3,elm4]
        return result
#
def pol(pp,ha):
        e0=pp[0]
        m0=pp[1]
        theta=pp[2]
        phi=pp[3]
        if ha>0:
               result=pol_r(theta,phi)
        elif ha<0:
               result=pol_l(theta,phi)
        else:
               result=pol_0(e0,m0,theta,phi)

        return result
#
def polbar(pp,ha):

        e0=pp[0]
        m0=pp[1]
        theta=pp[2]
        phi=pp[3]
        if ha>0:
               result=pol_l(theta,phi)
        elif ha<0:
                result=pol_r(theta,phi)
        else:
                result=pol_0(e0,m0,theta,phi)
        return result
#
# s channel and u channel amplitudes for compton scattering
#
def compts(k1,hk1,p1,hp1,k2,hk2,p2,hp2):

        ke=fourvec(k1)
        pe=fourvec(p1)
        mm=p1[1]
        mk=k1[1]
        nenner=2*dotprod4(ke,pe)+mk**2
#        nenner=s0+mk^2
        epsbar=polbar(k2,hk2)
        eps=pol(k1,hk1)
        kern=dag(epsbar)*(dag(ke)+dag(pe)+mm*one)*dag(eps)
        h1=simplify(ubar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0]/nenner)
        return result

#
def comptu(k1,hk1,p1,hp1,k2,hk2,p2,hp2):
        ka=fourvec(k2)
        pe=fourvec(p1)
        mm=p1[1]
        mk=k2[1]
        nenner=-2*dotprod4(ka,pe)+mk**2
        #nenner:=u0+mk^2:
        epsbar=polbar(k2,hk2)
        eps=pol(k1,hk1)
        kern=dag(eps)*(dag(pe)-dag(ka)+mm*one)*dag(epsbar)
        h1=simplify(ubar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0]/nenner)
        return result
#
def compt(k1,hk1,p1,hp1,k2,hk2,p2,hp2):

        t1=compts(k1,hk1,p1,hp1,k2,hk2,p2,hp2)
        t2=comptu(k1,hk1,p1,hp1,k2,hk2,p2,hp2)
        result=simplify(t1+t2)
        return result
#
#
# Sometimes one wants the amplitudes without the propagator term
#

def Ncompts(k1,hk1,p1,hp1,k2,hk2,p2,hp2):

        ke=fourvec(k1)
        pe=fourvec(p1)
        mm=p1[1]
        mk=k1[1]
        epsbar=polbar(k2,hk2)
        eps=pol(k1,hk1)
        kern=dag(epsbar)*(dag(ke)+dag(pe)+mm*one)*dag(eps)
        h1=simplify(ubar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0])
        return result
#
def Ncomptu(k1,hk1,p1,hp1,k2,hk2,p2,hp2):
        ka=fourvec(k2)
        pe=fourvec(p1)
        mm=p1[1]
        mk=k1[1]
        epsbar=polbar(k2,hk2)
        eps=pol(k1,hk1)
        kern=dag(eps)*(dag(pe)-dag(ka)+mm*one)*dag(epsbar)
        h1=simplify(ubar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0])
        return result
#
#
# Now f+fbar-->gamma gamma
# p1+p2=k1+k2
#
#
def gamgamt(p1,hp1,p2,hp2,k1,hk1,k2,hk2):
        ka=fourvec(k1)
        pe=fourvec(p1)
        mm=p1[1]
        M=k1[1]
        nenner=-2*dotprod4(ka,pe)+M**2
        epsbar2=polbar(k2,hk2)
        epsbar1=polbar(k1,hk1)
        kern=dag(epsbar2)*(dag(ka)-dag(pe)+mm*one)*dag(epsbar1)
        h1=simplify(vbar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0]/nenner)
        return result
#
#
def gamgamu(p1,hp1,p2,hp2,k1,hk1,k2,hk2):
        ka=fourvec(k2)
        pe=fourvec(p1)
        mm=p1[1]
        M=k2[1]
        nenner=-2*dotprod4(ka,pe)+M**2
        epsbar2=polbar(k2,hk2)
        epsbar1=polbar(k1,hk1)
        kern=dag(epsbar1)*(dag(ka)-dag(pe)+mm*one)*dag(epsbar2)
        h1=simplify(vbar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0]/nenner)
        return result
#
#
def gamgam(p1,hp1,p2,hp2,k1,hk1,k2,hk2):
        t1=gamgamt(p1,hp1,p2,hp2,k1,hk1,k2,hk2)
        t2=gamgamu(p1,hp1,p2,hp2,k1,hk1,k2,hk2)
        result=simplify(t1+t2)
        return result
#
# Amplitudes without denominator
#
#
def Ngamgamt(p1,hp1,p2,hp2,k1,hk1,k2,hk2):
        ka=fourvec(k1)
        pe=fourvec(p1)
        mm=p1[1]
        epsbar2=polbar(k2,hk2)
        epsbar1=polbar(k1,hk1)
        kern=dag(epsbar2)*(dag(ka)-dag(pe)+mm*one)*dag(epsbar1)
        h1=simplify(vbar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0])
        return result
#
#
def Ngamgamu(p1,hp1,p2,hp2,k1,hk1,k2,hk2):
        ka=fourvec(k2)
        pe=fourvec(p1)
        mm=p1[1]
        epsbar2=polbar(k2,hk2)
        epsbar1=polbar(k1,hk1)
        kern=dag(epsbar1)*(dag(ka)-dag(pe)+mm*one)*dag(epsbar2)
        h1=simplify(vbar(p2,hp2)*kern*u(p1,hp1))
        result=simplify(h1[0,0])
        return result




#print('Done')
