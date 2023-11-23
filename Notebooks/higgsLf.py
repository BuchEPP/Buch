import sympy as sy
from sympy.physics.matrices import mgamma, msigma

VERSION = '00.01.dev'
class HiggsLf():
    """
    Calculate Lagrangian for fermion gauge boson coupling
    from Higgs mechanism.
    """
    def __init__(self):
        """
        Initialize all sympy variables.
        """
        self.psiL = sy.symbols("psi_L",commutative=False)
        self.psiR = sy.symbols("psi_R",commutative=False)
        self.psibarL = sy.symbols("psibar_L",commutative=False)
        self.psibarR = sy.symbols("psibar_R",commutative=False)
        self.Bmu = sy.symbols("B_mu",commutative=False)
        self.Zmu = sy.symbols("Z_mu",commutative=False)
        self.Amu = sy.symbols("A_mu",commutative=False)
        self.W1mu = sy.symbols("W^1_mu",commutative=False)
        self.W2mu = sy.symbols("W^2_mu",commutative=False)
        self.W3mu = sy.symbols("W^3_mu",commutative=False)
        self.Wpmu = sy.symbols("W^+_mu",commutative=False)
        self.Wmmu = sy.symbols("W^-_mu",commutative=False)
        self.gammaMU = sy.symbols("gamma^\mu",commutative=False)
        self.gamma5 = sy.symbols("gamma^5",commutative=False)
        self.one = sy.symbols("1",commutative=False)
        self.PL = sy.symbols("P_L",commutative=False)
        self.PR = sy.symbols("P_R",commutative=False)
        self.dmu = sy.symbols("{\partial_\mu}",commutative=False)
        self.DmuL = sy.symbols("D_mu^L",commutative=False)
        self.DmuR = sy.symbols("D_mu^R",commutative=False)

        self.Q = sy.symbols("Q",real=True)
        self.I3 = sy.symbols("I_3",real=True)
        self.Y = sy.symbols("Y",real=True)
        self.s = sy.symbols("s",real=True) #sin(theta_W)
        self.c = sy.symbols("c",real=True) #cos(theta_W)
        self.e = sy.symbols("e",real=True, positive=True)
        self.g = sy.symbols("g",real=True, positive=True)
        self.gp = sy.symbols("{g^\prime}",real=True, positive=True)
        self.gz = sy.symbols("g_Z",real=True, positive=True)
        self.v = sy.symbols("v",real=True, positive=True)
        self.H = sy.symbols("H",real=True, positive=True)
        self.u = sy.symbols("u",commutative=False)
        self.ubar = sy.symbols("ubar",commutative=False)
        self.d = sy.symbols("d",commutative=False)
        self.dbar = sy.symbols("dbar",commutative=False)
        self.uL = sy.symbols("u_L",commutative=False)
        self.ubarL = sy.symbols("ubar_L",commutative=False)
        self.dL = sy.symbols("d_L",commutative=False)
        self.dbarL = sy.symbols("dbar_L",commutative=False)

        self.Wmu = sy.Matrix([[self.W1mu],[self.W2mu],[self.W3mu]])
        # add I3 to keep the general.
        # note 2*I3 = 1 for up, -2*I3 = 1 for down
        # therefore introduction of I3 makes no change
        # but it is usefull to have I3 in the result.
        self.sigmaWmu = msigma(1)*self.W1mu + msigma(2)*self.W2mu +\
            2*sy.Matrix([[self.I3,0],[0,-self.I3]])*msigma(3)*self.W3mu

    def LgRight(self, to="g"):
        """
        Return right handed Lagrangian for spinor psiR

        **Parameters**
        - to : (str); e,g,gz,gp: convert couplings to e, g, gz, gp

        **Returns**
        -  right handed Lagrangian for spinor psiR
        """
        DmuR = self.dmu + sy.Rational(1,2) * sy.I * self.gp * self.Y * self.Bmu
        LFR = sy.I * self.psibarR * self.gammaMU * DmuR * self.psiR
        LFR1 = LFR.subs(self.Y,2*(self.Q-self.I3))
        LFR2 = LFR1.subs(self.Bmu,-self.s*self.Zmu+self.c*self.Amu)
        LFR3 = LFR2.subs(self.I3,0)
        LFR4 = self.xsy_to_eg(LFR3, to=to)
        return LFR4.expand()

    def LgLeft(self, to="g"):
        """
        Return left-handed Lagrangian for dublett (u,d)_L

        **Parameters**
        - to : (str); e,g,gz,gp: convert couplings to e, g, gz, gp

        **Returns**
        -  left handed Lagrangian for dublett (u,d)_L
        """
        DmuL = self.dmu*sy.eye(2)+\
        sy.eye(2)*sy.I*self.gp*self.Y*self.Bmu*sy.Rational(1,2) +\
            sy.I*self.g*sy.Rational(1,2)*self.sigmaWmu
        DmuL1 = DmuL.subs(self.W1mu-sy.I*self.W2mu,sy.sqrt(2)*self.Wpmu)
        DmuL2 = DmuL1.subs(self.W1mu+sy.I*self.W2mu,sy.sqrt(2)*self.Wmmu)
        DmuL3 = DmuL2.subs(self.Y,2*(self.Q-self.I3))
        DmuL4 = DmuL3.subs(self.Bmu,-self.s*self.Zmu+self.c*self.Amu)
        DmuL5 = DmuL4.subs(self.W3mu,self.c*self.Zmu+self.s*self.Amu)
        psiu = sy.Matrix([[self.uL],[self.dL]])
        psibaru = sy.Matrix([[self.ubarL,self.dbarL]])
        LFL = sy.I*psibaru*self.gammaMU*DmuL5*psiu
        LFL1 = LFL[0].expand()
        LFL2 = LFL1.subs(self.g*self.c,self.g/self.c-self.g*self.s**2/self.c)
        LFL3 = self.xsy_to_eg(LFL2, to="g")
        LFL4 = sy.simplify(LFL3.expand()).expand()
        return  LFL4

    def LgUD(c, PRINT=True):
        """
        Return total Lagragian (left and right-handded) dublet u-,d-quarks

        **Parameters**
        - PRINT: (bool); True: display/print results

        **Returns**
        - dLg: (dict); dictionary with intermediate and final results with keys:
            - LdR1: L-righthanded for d
            - LdR2: L-righthanded for d with chiral projector P_R
            - LuR1: L-righthanded for u
            - LuR2: L-righthanded for u with PR
            - LudL1: L-lefthanded for ud
            - LudL2: L-lefthanded for ud with PL
            - Lud: L-total for ud

        """
        # calculate right handed Lagrangian for d
        LdR1 = c.LgRight(to="g")
        # L-lefthanded for d
        if PRINT:
            c.display("LdR1: L-righthanded for d:",LdR1)
        rpsiR1 = LdR1.subs(c.Amu*c.psiR,c.psiR*c.Amu)
        rpsiR2 = rpsiR1.subs(c.Zmu*c.psiR,c.psiR*c.Zmu)
        rdR1 = rpsiR2.subs(c.psibarR*c.gammaMU,c.dbar*c.gammaMU*c.PR)
        rdR2 = rdR1.subs(c.psiR,c.PR*c.d)
        rdR3 = rdR2.subs(c.PR*c.dmu,c.dmu*c.PR)
        LdR2 = rdR3.subs(c.PR*c.PR,c.PR)
        # L-lefthanded for d with chiral projector P_R
        if PRINT:
            c.display("LdR2: L-righthanded for d with chiral projector P_R:",LdR2)
        #
        # calculate right handed Lagrangian for u
        LuR1 = c.LgRight(to="g")
        # L-lefthanded for u
        if PRINT:
            c.display("LuR1: L-righthanded for u: ",LuR1)
        rpsiR1 = LuR1.subs(c.Amu*c.psiR,c.psiR*c.Amu)
        rpsiR2 = rpsiR1.subs(c.Zmu*c.psiR,c.psiR*c.Zmu)
        ruR1 = rpsiR2.subs(c.psibarR*c.gammaMU,c.ubar*c.gammaMU*c.PR)
        ruR2 = ruR1.subs(c.psiR,c.PR*c.u)
        ruR3 = ruR2.subs(c.PR*c.dmu,c.dmu*c.PR)
        LuR2 = ruR3.subs(c.PR*c.PR,c.PR)
        if PRINT:
            c.display("LuR2: L-righthanded for u with PR: ",LuR2)
        #
        # calculate lefthanded L for (u,d)
        LudL1 = c.LgLeft(to="g");LudL1
        if PRINT:
            c.display("LudL1: L-lefthanded for ud: ",LudL1)
        rL2 = LudL1.subs(c.Amu*c.uL,c.uL*c.Amu)
        rL3 = rL2.subs(c.Zmu*c.uL,c.uL*c.Zmu)
        rL4 = rL3.subs(c.Wmmu*c.uL,c.uL*c.Wmmu)
        rL5 = rL4.subs(c.Amu*c.dL,c.dL*c.Amu)
        rL6 = rL5.subs(c.Zmu*c.dL,c.dL*c.Zmu)
        rL7 = rL6.subs(c.Wpmu*c.dL,c.dL*c.Wpmu)
        rL8 = rL7.subs(c.ubarL*c.gammaMU, c.ubar*c.gammaMU*c.PL)
        rL9 = rL8.subs(c.ubarL*c.gammaMU, c.ubar*c.gammaMU*c.PL)
        rL10 = rL9.subs(c.dbarL*c.gammaMU, c.dbar*c.gammaMU*c.PL)
        rL11 = rL10.subs(c.uL,c.PL*c.u)
        rL12 = rL11.subs(c.dL,c.PL*c.d)
        rL13 = rL12.subs(c.PL*c.dmu,c.dmu*c.PL)
        LudL2 = rL13.subs(c.PL**2,c.PL)
        if PRINT:
            c.display("LudL2: L-lefthanded for ud with PL:",LudL2)
        #
        # calculate Lagranian in u,d
        Lg1 = LdR2 + LuR2 + LudL2
        Lg2 = Lg1.subs(c.PL,sy.Rational(1,2)*(c.one-c.gamma5))
        Lg3 = Lg2.subs(c.PR,sy.Rational(1,2)*(c.one+c.gamma5))
        Lud = Lg3.simplify().expand()
        if PRINT:
            c.display("Lud: L-total for ud:",Lud)
        #
        dLg = {}
        dLg["LdR1"] = LdR1
        dLg["LdR2"] = LdR2
        dLg["LuR1"] = LuR1
        dLg["LuR2"] = LuR2
        dLg["LudL1"]= LudL1
        dLg["LudL2"]= LudL2
        dLg["Lud"] = Lud
        return dLg

    def display(self, s, x):
        """
        Display in Jupyter, otherwise print text and sympy expression.

        **Parameters**
        - s: (str); string to be printed
        - x: (sympy expr); sympy expression to be displayed or printed

        **Returns**
        - None

        """
        if is_jupyter():
            display(s, x)
        else:
            print(s,x)
        return

    def syparts(self, xsy ,filter=""):
        """
        Display in Jupyter, otherwise print parts (args) of sympy expression.

        Use input sympy expression xsy and get all terms (args).
        Display terms which fullfil filter condition (for repr string).
        Display: sympy expression, latex and repr for each term.

        **Parameters**
        - xsy: (sympy expr); input sympy expression
        - filter: (str)
            - "" : display all terms of expression
            - "repr string" : select terms with fiolter string

        **Returns**
        - None

        """
        n=-1
        for item in xsy.args:
            if filter=="" or filter in repr(item):
                n += 1
                if is_jupyter():
                    display(n,item, "latex: "+sy.latex(item),"repr: "+repr(item))
                else:
                    print("n: ",n)
                    print("latex: "+sy.latex(item))
                    print("repr: "+repr(item))
        return

    def select(self, xsy, filter=""):
        """
        Select terms of sympy expr using filter condition, return sum.

        Use input sympy expr xsy, filter terms with repr expression.
        Return the sum of the selected terms.

        **Parameters**
        - xsy: (sympy epr); input sympy expr
        - filter: (str);
            - repr str : use repr string to select terms
            - keys : use predefined f´keys in dict: dA,uA,dZ,uZ,uW,dW

        Returns
        - sum of selected sympy expr
        """
        d = {"dA":"d*A_mu",
            "uA":"u*A_mu",
            "dZ":"d*Z_mu",
            "uZ":"u*Z_mu",
            "uW":"u*W^-_mu",
            "dW":"d*W^+_mu"}
        if filter in d.keys():
            search = d[filter]
        else:
            search = filter
        rr = 0
        for i in range(len(xsy.args)):
            r = repr(xsy.args[i])
            if search in r:
                rr = rr + xsy.args[i]
        return rr

    def xsy_part_to(self, xsy, dsubs={"A_":"e","Z_":"gz","W^":"g"}):
        """
        Convert coupling constants based on dict

        The input sympy epr xsy is analyzed for each term.
        If a repr string matches the defined key in dsubs,
        the term is converted to the specified coupling constant.

        **Parameters**
        - xsy: (sympy epr); input sympy expr
        - dsubs: (dict);
            - key : repr string to select terms
            - value : e, g, gp, gz , convert to these coupligs

        **Returns**
        - sum of selected sympy expr with modified couplings

        **Usage**
        xsy_part_to(self, xsy, dsubs={"A_":"e","Z_":"gz","W^":"g"}
        - this will convert all a terms to e, Z to gz and W to g.
        """
        txsy = xsy.args
        lxsy = [txsy[i] for i in range(len(txsy))]
        xsum = 0
        for i in range(len(lxsy)):
            for key in dsubs:
                if key in repr(lxsy[i]):
                    lxsy[i] = self.xsy_to_eg(lxsy[i], to=dsubs[key])
                    xsum += lxsy[i]
        xsum = sy.simplify(xsum).expand()
        return xsum

    def xsy_to_eg(self, xsy, to=""):
        """
        Convert all coupling constants to the given one in 'to'.

        **Parameters**
        - xsy: (sympy epr); input sympy expr
        - to: (str);
            - choices: e, g, gp, gz

        **Returns**
        - modified sympy expression
        """
        xx = xsy
        x1 = xsy
        if to.strip() == "e":
            x2 = x1.subs(self.gp, self.e/self.c)
            x3 = x2.subs(self.g, self.e/self.s)
            x4 = x3.subs(self.gz, self.e/self.s/self.c)
            xx = x4.expand()
        elif to.strip() == "g":
            x2 = x1.subs(self.gp, self.g*self.s/self.c)
            x3 = x2.subs(self.e, self.g*self.s)
            x4 = x3.subs(self.gz, self.g/self.c)
            xx = x3.expand()
        elif to.strip() == "gp":
            x2 = x1.subs(self.g, self.gp*self.c/self.s)
            x3 = x2.subs(self.e, self.gp*self.c)
            x4 = x3.subs(self.gz, self.gp/self.s)
            xx = x3.expand()
        elif to.strip() == "gz":
            x2 = x1.subs(self.g, self.gz*self.c)
            x3 = x2.subs(self.e, self.gz*self.c*self.s)
            x4 = x3.subs(self.gp, self.gz*self.s)
            xx = x3.expand()
        else:
            pass

        return xx.expand()

def is_jupyter() -> bool:
    """
    Return True if running in Jupyther notebook
    """
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter
