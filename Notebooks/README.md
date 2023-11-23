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
- [Argand.ipynb](Argand.ipynb)
    - section 2.4, exercise 2.21
    - plot Argand diagram
- [Compton(HE).ipynb](Compton(HE).ipynb) 
    - section 3.2 
    - Compton scattering using the high energy approximation
- [Compton.ipynb](Compton.ipynb) 
    - section 3.2 
    - Detailed calculations on photon electron scattering
- [Dalitz.ipynb](Dalitz.ipynb) 
    - section 2.1.3
    - generate a Dalitz-plot using randomly selected $(E_1, E_2)$ pairs
- [Dirac.ipynb](Dirac.ipynb)
    - section 3.1 
    - This notebook should be used for own investigations around the Dirac equation e.g. in the context of the discussion in section 3.1 of the book.
- [Drell-Yan.ipynb](Drell-Yan.ipynb)
    - section 8.1 
    - Calculate the Drell-Yan cross section analytically using a simple (non-realistic) parton distribution functions. 
    - exercise 8.2
- [Drell-Yan-numerical.ipynb](Drell-Yan-numerical.ipynb)
    - section 8.1 
    - Calculate the Drell-Yan cross-section using a more realistic parton distribution function as given in section 5.3 of the book. Now the integration can not be done easily with analytical methods. The numerical integration method `scipy.dblquad` is used. 
    - exercise 8.3
- [Higgs_decay_HVV.ipynb](Higgs_decay_HVV.ipynb) 
    - section 7.3 
    - Higgs decay to an on-shell vector boson pair
- [LeptonWeak.ipynb](LeptonWeak.ipynb) 
    - section 6.1 
    - various weak reactions with leptons
    - $\nu_\mu ~ e^-\rightarrow \nu_e ~ \mu^-$,  
    - $\bar{\nu}_{e} ~ \mu^+ \rightarrow \bar{\nu}_μ ~ e^+ $,  
    - $\mu^+\rightarrow e^+ ~\bar{\nu}_\mu ~ \nu_e$
- [NeutronDecay.ipynb](NeutronDecay.ipynb) 
    - section 6.2 
    - calculation of the neutron decay 
- [PiDecay.ipynb](PiDecay.ipynb) 
    - section 6.2 
    - calculation of the charged pion decay 
- [Rosenbluthandmore.ipynb](Rosenbluthandmore.ipynb) 
    - section 5.2 
    - derivation of the Rosenbluth formula
- [colorfactors.ipynb](colorfactors.ipynb)
    - section 4.2 
    - calculate QCD color factors for qq scattering
- [eeWW.ipynb](eeWW.ipynb)  
    - section 7.1 
    - calculation of the amplitudes for the reaction $ee \to WW$
- [eeee.ipynb](eeee.ipynb) 
    - section 3.2 
    - Bhabha and Moller scattering
- [eemumu.ipynb](eemumu.ipynb) 
    - section 3.2 
    - the reactions $e^- e^+ \to \mu^- \mu^+$ and $e^- \mu^- \to e^- \mu^-$
- [eepipi.ipynb](eepipi.ipynb) 
    - section 5.1 
    - reaction $e^+ e^- \to \pi^+ \pi^-$
- [ggtogg.ipynb](ggtogg.ipynb) 
    - section 5.2 
    - gluon-gluon scattering
- [gluon-gluon_with_cut.ipynb](gluon-gluon_with_cut.ipynb) 
    - section 8.1 
    - Calculate the cross-section of $gg\to gg$ scattering with $p_T(g)= 0.1 \sqrt{s}$.
    - exercise 8.4
- [heppackv0.py](heppackv0.py) 
    - utility functions and definitions which are used in the notebooks 
- [neutrino_oscillation_matter.ipynb](neutrino_oscillation_matter.ipynb) 
    - section 9.1 
    - Calculate the neutrino oscillation in matter and derive eq. 9.30, 9.31 and 9.32 in the book. 
    - exercise 9.4
- [random_exponential.ipynb](random_exponential.ipynb) 
    - section 1.6
    - Generate random numbers distributed according to an exponential function
    - exercises 1.30 and 1.31 
- [random_function_sampling.ipynb](random_function_sampling.ipynb) 
    - section 1.6
    - Three methods using numpy routines are presented, which can be used to randomly sample an arbitrary 1-dim function. The first function uses the rejection method, the second the inversion method and the third the numpy routine for sampling a histogram. All methods are timed to find out which is the fastest. 
- [random_general_inversion.ipynb](random_general_inversion.ipynb) 
    - section 1.6
    - generate random numbers for an arbitrary 1-D pdf-function using the inversion method
- [random_normal.ipynb](random_normal.ipynb) 
    - section 1.6
    - several calculations with normal (Gaussian) distributions
    - exercises 1.32 and 1.37 
- [random_numbers.ipynb](random_numbers.ipynb) 
    - section 1.6
    - generate random  numbers,  plot random numbers
    - exercises 1.24, 1.25 and 1.26
- [random_poisson.ipynb](random_poisson.ipynb) 
    - section 1.6
    - generate random numbers for a Poisson distribution
    - exercises 1.33
- [random_rejection_method.ipynb](random_rejection_method.ipynb) 
    - section 1.6
    - generate random numbers according to the function $f(x) = \sqrt{1+\sin x}$ with the rejection method
    - exercises 1.35
- [random_sphere.ipynb](random_sphere.ipynb) 
    - section 1.6
    - calculate the area of a circle and the volumes of a 3-D and 5-D sphere using the rejection method
    - exercises 1.27, 1.28, 1.29
- [tWdecay.ipynb](tWdecay.ipynb) 
    - section 6.2 
    - weak decays of the top quark and the W boson
----
