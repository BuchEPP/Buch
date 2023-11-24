# Notebooks

This folder contains Jupyter notebooks with calculations. 
They are referred to in the book, provide solutions to exercises or 
show details of calculations.
Some notebooks contain links to figures. 
They are stored in the subfolder `img`.
Make sure that you download the figures as well.  

The easiest way to use the notebooks is to clone this repository to your local computer 
and to work locally:
1. Option: use the terminal and the `git` command (for experts)
2. Option: use the Web-Interface 
    - go to [Main page](https://github.com/BuchEPP/Buch)
    - click on the green field `<>Code`
    - select `Download ZIP`

The comments in the notebooks are short.  So read the relevant section of the book carefully and try to understand every line of code.  Play with it: change parameters such as masses or vertex factors and see what happens. You can also use these notebooks as examples for calculating other processes.   

----
- [Argand.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Argand.ipynb)
    - section 2.4, exercise 2.21
    - plot Argand diagram
- [Compton(HE).ipynb](/BuchEPP/Buch/blob/main/Notebooks/Compton(HE).ipynb) 
    - section 3.2 
    - Compton scattering using the high energy approximation
- [Compton.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Compton.ipynb) 
    - section 3.2 
    - Detailed calculations on photon electron scattering
- [Dalitz.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Dalitz.ipynb) 
    - section 2.1.3
    - generate a Dalitz-plot using randomly selected $(E_1, E_2)$ pairs
- [Dirac.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Dirac.ipynb)
    - section 3.1 
    - This notebook should be used for own investigations around the Dirac equation e.g. in the context of the discussion in section 3.1 of the book.
- [Drell-Yan.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Drell-Yan.ipynb)
    - section 8.1 
    - Calculate the Drell-Yan cross section analytically using a simple (non-realistic) parton distribution functions. 
    - exercise 8.2
- [Drell-Yan-numerical.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Drell-Yan-numerical.ipynb)
    - section 8.1 
    - Calculate the Drell-Yan cross-section using a more realistic parton distribution function as given in section 5.3 of the book. Now the integration can not be done easily with analytical methods. The numerical integration method `scipy.dblquad` is used. 
    - exercise 8.3
- [Higgs-Hff.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Higgs-Hff.ipynb) 
    - section 7.3 
    - Higgs decay to an on-shell fermion pair
- [Higgs-HVV.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Higgs-HVV.ipynb) 
    - section 7.3 
    - Higgs decay to an on-shell vector boson pair
- [HiggsLf.ipynb](/BuchEPP/Buch/blob/main/Notebooks/HiggsLf.ipynb) 
    - section 7.3 
    - Derive the gauge couplings ($\gamma, Z, W$) to Fermions  in the SM and compare the result with the equations for $\mathcal{L}_F$ in section 7.3.     
- [LeptonWeak.ipynb](/BuchEPP/Buch/blob/main/Notebooks/LeptonWeak.ipynb) 
    - section 6.1 
    - calculate various weak reactions with leptons
    - $\nu_\mu ~ e^-\rightarrow \nu_e ~ \mu^-$,  
    - $\bar{\nu}_{e} ~ \mu^+ \rightarrow \bar{\nu}_μ ~ e^+ $,  
    - $\mu^+\rightarrow e^+ ~\bar{\nu}_\mu ~ \nu_e$,
    - $\bar{\nu}_{e} ~ e^- \rightarrow \bar{\nu}_e ~ e^- $ 
- [Majorana.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Majorana.ipynb) 
    - section 9.3, box 9.2 
    - Calculate the Majorana mass for commutative and non-commutative spinors. Show that only in the latter case the mass term is different from zero. 
- [NeutronDecay.ipynb](/BuchEPP/Buch/blob/main/Notebooks/NeutronDecay.ipynb) 
    - section 6.2 
    - calculation of the neutron decay 
- [PiDecay.ipynb](/BuchEPP/Buch/blob/main/Notebooks/PiDecay.ipynb) 
    - section 6.2 
    - calculation of the charged pion decay 
- [Rosenbluthandmore.ipynb](/BuchEPP/Buch/blob/main/Notebooks/Rosenbluthandmore.ipynb) 
    - section 5.2 
    - derivation of the Rosenbluth formula
- [colorfactors.ipynb](/BuchEPP/Buch/blob/main/Notebooks/colorfactors.ipynb)
    - section 4.2 
    - calculate QCD color factors for qq scattering
- [eeWW.ipynb](/BuchEPP/Buch/blob/main/Notebooks/eeWW.ipynb)  
    - section 7.1 
    - calculation of the amplitudes for the reaction $ee \to WW$
- [eeee.ipynb](/BuchEPP/Buch/blob/main/Notebooks/eeee.ipynb) 
    - section 3.2 
    - Bhabha and Moller scattering
- [eemumu.ipynb](/BuchEPP/Buch/blob/main/Notebooks/eemumu.ipynb) 
    - section 3.2 
    - the reactions $e^- e^+ \to \mu^- \mu^+$ and $e^- \mu^- \to e^- \mu^-$
- [eepipi.ipynb](/BuchEPP/Buch/blob/main/Notebooks/eepipi.ipynb) 
    - section 5.1 
    - reaction $e^+ e^- \to \pi^+ \pi^-$
- [ggtogg.ipynb](/BuchEPP/Buch/blob/main/Notebooks/ggtogg.ipynb) 
    - section 5.2 
    - calculate the ampllitude of gluon-gluon scattering
- [gluon-gluon.ipynb](/BuchEPP/Buch/blob/main/Notebooks/gluon-gluon.ipynb) 
    - section 8.1 
    - Calculate the cross-section of $gg\to gg$ scattering with $p_T(g)= 0.1 \sqrt{s}$.
    - exercise 8.4 
- [heppackv0.py](/BuchEPP/Buch/blob/main/Notebooks/heppackv0.py) 
    - utility functions and definitions which are used in the notebooks 
- [higgsLf.py](/BuchEPP/Buch/blob/main/Notebooks/higgsLf.py) 
    - utility functions for the calculation of the gauge couplings for fermions.     
- [neutrino-matter.ipynb](/BuchEPP/Buch/blob/main/Notebooks/neutrino-matter.ipynb) 
    - section 9.1 
    - Calculate the neutrino oscillation in matter and derive eq. 9.30, 9.31 and 9.32 in the book. 
    - exercise 9.4
- [neutrino-vacuum.ipynb](/BuchEPP/Buch/blob/main/Notebooks/neutrino-vacuum.ipynb) 
    - section 9.1 
    - Calculate the neutrino oscillation in vacuum using the matrix method and compare with the analytic expression given by the Particle Data Group (PDG). 
    - exercise 9.3
- [random-exponential.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-exponential.ipynb) 
    - section 1.6
    - Generate random numbers distributed according to an exponential function
    - exercises 1.30 and 1.31 
- [random-function.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-function.ipynb) 
    - section 1.6
    - Three methods using numpy routines are presented, which can be used to randomly sample an arbitrary 1-dim function. The first function uses the rejection method, the second the inversion method and the third the numpy routine for sampling a histogram. All methods are timed to find out which is the fastest. 
- [random-inversion.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-inversion.ipynb) 
    - section 1.6
    - generate random numbers for an arbitrary 1-D pdf-function using the inversion method. See also notebook `random-function.ipynb`.
- [random-normal.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random_normal.ipynb) 
    - section 1.6
    - several calculations with normal (Gaussian) distributions
    - exercises 1.32 and 1.37 
- [random-numbers.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-numbers.ipynb) 
    - section 1.6
    - generate random  numbers,  plot random numbers
    - exercises 1.24, 1.25 and 1.26
- [random-poisson.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-poisson.ipynb) 
    - section 1.6
    - generate random numbers for a Poisson distribution
    - exercises 1.33
- [random-rejection.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-rejection.ipynb) 
    - section 1.6
    - generate random numbers according to the function $f(x) = \sqrt{1+\sin x}$ with the rejection method
    - exercises 1.35
- [random-sphere.ipynb](/BuchEPP/Buch/blob/main/Notebooks/random-sphere.ipynb) 
    - section 1.6
    - calculate the area of a circle and the volumes of a 3-D and 5-D sphere using the rejection method
    - exercises 1.27, 1.28, 1.29
- [tWdecay.ipynb](/BuchEPP/Buch/blob/main/Notebooks/tWdecay.ipynb) 
    - section 6.2 
    - weak decays of the top quark and the W boson
----
