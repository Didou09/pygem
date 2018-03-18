# coding utf-8

"""
Monetary macrodynamics module of pygem
Only mono-sector so far (only one type of good) 

Definitions:
    Y0  : amount of goods produced at each time step (a.u.)
    K   : stock of capital used to produce the goods (money)
    L   : Labour (hours)
    nu  : (constant) capital-outpu ratio (money / a.u.)
            (amount of capital necessary per output unit)
    a   : Harrod-neutral labor-augmenting techo level (a.u. / hours)
    Y   : 
    Dy  :
    A   :  
   
    Pi  : Nominal profit
    p   : ...
    w   : ...
    r   : ...
    D   : ...
    Tf  : ...
    dD  : ...
     


"""



__all__ = ['eq01', 'eq02']



def eq01():
    """ Production function

    Y0 = K/nu = aL
   
    Parameters
    ---------- 
    Y0  : amount of goods produced at each time step (a.u.)
    K   : stock of capital used to produce the goods (money ?)
    L   : Labour (man-hours ?)
    nu  : (constant) capital-outpu ratio (money / a.u. ?)
            (amount of capital necessary per output unit)
    a   : Harrod-neutral labor-augmenting techo level (a.u. / hours ?)
                    
    Full capital use is assumed
    Say's law is postulated
        (i.e.: aggregate production creates an equal aggregate demand,
        or demand is not limiting production)

    Background:
    -----------
    In general a multi-sectorial production function links:
        Outputs (products of many types, Y0, Y1, Y2...)
        Inputs (labour, capital, knowledge, various ressources...)
    
            (Y0, Y1,..., Yn) = F(X0,X1,X2,...,Xm)
    
    Cross-production can be taken into account in this form.
    
    Assumptions:
        * Mono-sectorial        =>  Y0 = F(X0,X1,...,Xm)
        * Solow growth model    =>  Y0 = F(K,L,a)
            K = capital
            L = labour
            a = knowledge (or technological progress)
          Notice that this Solow model does not consider the dependency on:
            Natural ressources availability
            Energy availability

    The impact of progress is usually modelled as:
        Hicks-neutral (factor augmenting):  Y0 = a x F(K,L)
        Harrod-neutral (labor augmenting):  Y0 = F(K, a x L)
        Solow-neutral (capital augmenting): Y0 = F(a x K, L)   
    
    Assumptions:
        * Harrod-neutral progress   =>  Y0 = F(K,aL)
            Hence, a ~ labour productivity from progress
        * Constant returns  => for c>0, cY0 = F(cK,caL)
            This amounts to assuming that:
                Gains from specialization are exhausted
                i.e.: no scale benefits, no further optimizations...
                
    As a consequence, nu = K/Y0 = 1/F(1,aL/K) only depends on aL/K

    The form of the production function F is commonly:
        F = (alpha x K^(gamma) + (1-alpha) x L^(gamma))^(1/gamma)
    Several models are possible, depending on which value is chosen for gamma
    Here we choose Leontief production:  gamma -> -infty, resulting in
        F = min(K,L)
   
    Notice that a production function is usually assumed convex (F''<=0)

 
    Sources:
    --------
    [1] D. Romer, "Advanced Macroeconomics", 2005
    [2] https://en.wikipedia.org/wiki/Production_function#Natural_resources
    [3] https://en.wikipedia.org/wiki/List_of_production_functions 
    [4] http://www.econ.boun.edu.tr/hatipoglu/ec308/lecture3.pdf
    [5] https://cruel.org/econthought/essays/growth/neoclass/solowtech.html


    Questions:
    ----------
        * Units ???
            The form of the production function does not show units consistency!
            Relevance of using:
                - money for capital ? (but monetary wars ? speculation ?)
                - energy for capital ? (but inflation ?)
                - energy for labour ? (but intellectual tasks ? services ?)
                            
        * How could we include natural ressources and energy in F ?
            Can they be considred to be included in knowledge / progress (a) ?

        * What justifies the choice of a Leontieff production function ?
          Why not Cobb-Douglas, which seems to be both Hicks-neutral and
            Harrod-neutral ?

        * There are other labor-augmenting functions
            Why choose the Harrod-neutral option ?
            Which impact on the model ?  

        * Say's law : what about waste ? particularly in the food domain ?

        * Are we assuming that the labour force is the limiting factor ?
            (Y0 = aL)
    """
    
def eq02():
    """ Damaged production and abatment

    Y := (1-Dy)(1-A)Y0

    Parameters:
    -----------
    Y   : Ampiunt of output available on the market for consumption
    Dy  : Damaged - by gloab warming - proportion of the output (dimensionless)
    A   : Abatement proportion of output (dimensionless)
            (proportion diverted from markets, used to reduce CO2-e emissions)
    """


def eq03():
    """ Profit equation

    Pi := pY - wL - rD - pTf - poDK

    Parameters
    ----------
    Pi  : Nominal profit (money)
    p   : Consumption unit price (money / a.u. ?)
    w   : Unit wage (money / man-hours ?)
    r   : Short term interests rate (dimensionless)
    D   : Oustanding balance of current nominal private debt (money)
    Tf  : Carbon unit tax
    oD  : global deprecation rate of capital
    
    Background
    ----------
    Profit = earnings - everything that was paid to get it
    
    D := Lc-Mc
    Lc  : total corporate debt
    Mc  : total corporate savings (deposit of productive sector)

    pTf := ppcEind
    pc  : unit cost of CO2-e emissions (money / GTC)
    Eind: industrial CO2-e emissions (GTC)

    oD := o + Dk
    o   : standard depreciation rate of capital
    Dk  : capital degradation rate induced by gloabl warming

    This equation can be normalized by dividing by pY

    Questions
    ---------
        * Why pTf and not just Tf, since Tf = pc x Eind ?
            Also, why would the carbon tax depend on p?

        * Why pdDK and not just dDK ?

    """

def eq0405():
    """ Definition of normalized quantities
    
    omega   :=  wL/pY   wage share
    d       :=  D/pY    private debt ratio
    pi      :=  Pi/pY   nominal profit share

    """

def eq06():
    """ Investment vs profit share

    I := k(pi)Y

    I   : Investments (units ?)
    k   : risk appetance of corporate sector
            positive, increasing smooth function
            To be calibrated empirically    

    Questions
    ---------
        * Why k(pi)Y and not k(pi)pY ?
            A fraction of the money obtained from sold output is used to invest
    """

def eq07():
    """ Capital dynamics

    K_t := I - oDK

    K_t : time derivative of capital (money / time ?)

    """

def eq08():
    """ Debt dynamics
    
    D_t := pI + Pid(pi) - Pi - poDK

    D_t : time derivative of coprate debt
    Pid : dividends paid to shareholders
    
    """

def eq09():
    """ Dividends vs profits share
    
    Pid(pi) := O(pi)pY

    O   : dividends générosity of corporate sector
            positive, increasing smooth function
            To be calibrated empirically

    Background
    ----------
    The remaing retained profits Pir = Pi - Pid is used to finance other things

    """


