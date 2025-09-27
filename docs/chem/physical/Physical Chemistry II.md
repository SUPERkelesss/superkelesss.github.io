# Physical Chemistry II

midterm exam: Nov 4th

[toc]

---

## Chapter 1 : Chemical and Electrochemical Equilibrium

### Gibbs Energy Minimum 

for rxn $A \rightleftarrows B$, def. $\xi$ as **rxn extent**(mol)

so $-\dd n_A = \dd n_B = \dd \xi$, 

$$
\dd G = \mu_A \dd n_A + \mu_B \dd n_B = (\mu_A-\mu_B)\dd\xi
$$

for 

$$
\Delta_rG = \frac{\dd G}{\dd \xi} = \mu_B - \mu_A  = \mu_B^{\circ} - \mu_A^{\circ} + RT\ln{\frac{p_B}{p_A}}
$$

def. **rxn quotient** $Q = \frac{p_B}{p_A}$

at Eq. $0 = \Delta_rG = \Delta_rG^{\circ} + RT\ln{K}$

---

### General rxns

$$
\nu_A A + \nu_B B \rightleftarrows \nu_C C + \nu_D D
$$

we get:

$$
\Delta_rG = \Delta_rG^{\circ} + RTlnQ = \Sigma_j \nu_j \Delta_fG^{\circ}(j) + RT\ln(\Pi_j a_j^{\nu_j})
$$

as $a_j$ remains **activity** or **fugacity**

### Pressure

Since $\delta _rG^{\circ}$ is defined as a single pressure, we have $(\frac{\partial K}{\partial p})_T = 0$

for rxn $A \rightleftarrows 2B$, $A$ changes from $n$ to $(1-\beta)n$

$$
x_A = \frac{(1-\beta)n}{(1-\beta)n + 2\beta n}, x_B = \frac{2\beta n}{(1-\beta)n + 2\beta n}
$$

so we have: 

$$
K = \frac{p_B^2}{p_A p^{\circ}} = \frac{x_B^2}{x_A} (\frac{p}{p^{\circ}}) = \frac{4\beta^2}{1-\beta^2}(\frac{p}{p^{\circ}})\\
\beta  = \frac{1}{(1+4 p/Kp^{\circ})^{1/2}}
$$

as $p$ increase, $\beta$ decrease

---

### Response of equilibria to changes

as $\ln{K} = -\frac{\Delta_rG^{\circ}}{RT} = -\frac{1}{R} (\frac{\partial \Delta_rG^{\circ}/T}{\partial T}) = \frac{\Delta_rH^{\circ}}{RT^2}$

that is:

$$
\frac{\partial \ln{K}}{\partial {1/T}} = -\frac{\Delta_rH^{\circ}}{R}
$$

that means: when $\Delta_rH^{\circ} < 0$, when $T$ decrease, $K$ increase. -Vice Versa-

### Equilibrium electrochemistry

for rxn $\ce{H_2O <--> H_2 + O_2}$ we got half rxns:
**Anode**: $\ce{H_2 - 2e^-<--> 2H^+}$
**Cathode**: $\ce{0.5O_2 + 2H^+ + 2e^- <--> H_2O}$

for non-electrochemistry states:
$$
Q_1 = \frac{a(\ce{H^+})^2}{(p(\ce{H_2})/p^{\circ})}, Q_2 = \frac{a(\ce{H2O})}{(p(\ce{O_2})^{1/2}/p^{\circ})a(\ce{H^+})^2}
$$

consider the **Electromotive Force(EMF)**

$$
-\nu EF = \Delta_rG = \Delta_rG^{\circ} + RT\ln{Q} = \frac{\dd W_e}{\dd \xi}\\
E = -\frac{\delta_rG_m^{\circ}}{\nu F} - \frac{RT}{\nu F} \ln{Q}
$$

this is called ***Nerst* Equation**.

At eq: $0 = E^{\circ} - \frac{RT}{\nu F}\ln{K}$, so
$$
E^{\circ} = \frac{\nu FE^{\circ}}{RT}
$$

---

### Lattice gas

def. $N$ as *indistinguishable particles*, $N_0$ as *indistinguishable sites*

as ***Boltzman* Entropy** $S = k_B \ln{\Omega}$, since $\Omega = \frac{N_0!}{(N_0 - N)!(N)!}$

let x = N/N_0, using ***Stiring* Approximation**:

$$
S = -k_BN(x\ln{x} + (1-x)\ln{1-x})
$$

for general cases:

$$
S = -k_BN(\Sigma_n x_i\ln{x_i})
$$

### Electrochemical Potential

$$
G = H - TS + zeN\varphi
$$

$$
\Delta G = \Delta H - T\Delta S + \Delta(zeN)\varphi
$$

so as $\mu = (\frac{\Delta G}{\Delta N})_{T,p,\varphi} = (\frac{\partial g}{\partial x})_{T, p, \varphi}$

For a lattice as: 
$$
S' = (\frac{\partial S}{\partial x})_{T,p,\varphi} = k_B \frac{x}{1-x}
$$

so:
$$
\mu  = h' + k_BT\ln{\frac{x}{1-x}} + ze\varphi
$$

when $x \rightarrow 0$, 

$$
\mu = h' + k_BT\ln{x} + ze\varphi = k_BT\ln{x} + ze\varphi
$$

that is called **Electrochemical Potential**

---

### Standard Hydrogen Potential

define *Standard Hydrogen Potential* as 0 V as the **Standard Hydrogen Electrode**:

$$
\ce{2H^+ + 2e^- -> H_2}
$$

whereas happens Pt electrode and every species are at the standard state

eg: $\ce{2H_2 + O_2 -> 2H_2O}$, $E = 1.23\mathrm{V}$

so $\ce{0.5O_2 + 2H^+ + 2e^- <--> H_2O}$, $E = 1.23 \mathrm{V}$

eg2: $\ce{AgCl + e <--> Ag + Cl^-}$

$$
\begin{aligned}
E &= E_{AgCl/Ag}^{\circ} - \frac{RT}{F} ln{a(\ce{Cl^-})} + \frac{RT}{F} ln{\frac{1}{a(\ce{H^+})}} \\
&= E_{AgCl/Ag}^{\circ} - \frac{RT}{F} \ln{a(\ce{Cl^-})a(\ce{H^+})}\\
&= E_{AgCl/Ag}^{\circ} - \frac{RT}{F} \ln{b(\ce{Cl^-})b(\ce{H^+})} -\frac{RT}{F} \ln{\gamma(\ce{Cl^-})\gamma(\ce{H^+})}
\end{aligned}
$$

where $b$ stands **molality**, $\gamma$ stands **activity coefficient**

as ***Debye-Huckle* Formula** $\ln{\gamma} = cb^{1/2}$:

$$
E = E_{AgCl/Ag}^{\circ} - \frac{2RT}{F} \ln{b^2} +\frac{2RT}{F} cb^{1/2}
$$

---

### Reversible Hydrogen Electrode (RHE)

$$
E_{RHE}^{\circ} = E_{SHE} + \frac{RT}{F} \ln{a(\ce{H^+})}\\
V_{RHE}^{\circ} = V_{SHE} - \frac{RT}{F} \ln{a(\ce{H^+})} = V_{SHE} + 0.059\mathrm{pH}
$$

Eg: Water Electrolysis
$$
V_{SHE} = E^{\circ} - \frac{RT}{4F}\ln{\frac{1}{(p(\ce{O_2}/p^{\circ}))a(\ce{H^+})^4}}
= E^{\circ} + \frac{RT}{F} \ln{a(\ce{H^+})} + \frac{RT}{4F} \ln{p(\ce{O_2})/p^{\circ}}
$$

where $V_{RHE} = E^{\circ} + \frac{RT}{4F} \ln{p(\ce{O_2})/p^{\circ}}$

In real case, if we want to drive the rxn, need let $E > E^{\circ} = 1.23 \mathrm{V}$

---

## Chapter 2 :  Fuel Cells, Batteries and Electric Double Layer

### Determining TD functions

$$
\Delta_rG^{\circ} = \Delta_rH^{\circ} - T\Delta_rS^{\circ} = -\nu FE^{\circ}\\
\frac{\dd E^{\circ}}{\dd T} = \frac{\Delta_rS^{\circ}}{\nu F} \to \Delta_rS^{\circ} = \nu F\frac{\dd E^{\circ}}{\dd T}\\
\Delta_rH^{\circ} = \Delta_rG^{\circ} + T\Delta_rS^{\circ} = -\nu F(E^{\circ} - T\frac{\dd E^{\circ}}{\dd T})
$$

---

### Energy Efficiency

$$
\text{Fuel Cell}(EE) = \frac{\text{Electrical }E}{\text{Chemical }E}\\
\text{Electrolyzer}(EE) = \frac{\text{Chemical }E}{\text{Electrical }E}
$$

![Screenshot_20250916_154624](E:\Downloads/Screenshot_20250916_154624.jpg)

![Screenshot_20250916_154643](E:\Downloads/Screenshot_20250916_154643.jpg)

---

### Charging Mode

- **Positive Electrode**: supply e^-^(Sluggish) **Anode**
- **Negative Electrode**: receive e^-^(Energetic) **Cathode**

---

### Electric Double Layer(EDL)

![Screenshot_20250916_160222](E:\Downloads/Screenshot_20250916_160222.jpg)

**Gouy-Chapman-Stern(GCS) Model**

![Screenshot_20250916_162115](E:\Downloads/Screenshot_20250916_162115.jpg)

---

### The Gibbs adsorption isotherm

Pure Phase(A)  |   ……  |  Pure Phase(B)

Ref:
$$
\dd G_R = (\frac{\partial G_R}{\partial T})\dd  T + (\frac{\partial G_R}{\partial p}) \dd p +(\frac{\partial G_R}{\partial n})\dd n
$$
Actual:
$$
\dd G_S = (\frac{\partial G_S}{\partial T})\dd  T + (\frac{\partial G_S}{\partial p}) \dd p +(\frac{\partial G_S}{\partial n})\dd n + (\frac{\partial G_S}{\partial A})\dd A
$$
we call $(\frac{\partial G_S}{\partial A})_{p,T,n} = \gamma$ as **Surface Tension**

As p&T are const., we have:
$$
\dd G^\sigma = \dd G_S - \dd G_R = \sum_i \mu_i(\dd n_i^S - \dd n_i^R) + \gamma \dd A= \sum_i \mu_i\dd n_i^\sigma + \gamma \dd A
$$
for total differential:
$$
\dd G^\sigma = \sum_i \mu_i\dd n_i^\sigma + \sum_i n_i\dd \mu_i^\sigma + \gamma \dd A + A \dd\gamma
$$


As **Gibbs-Duham Relation** :
$$
A\dd \gamma + \sum_i n_i^\sigma \dd \mu_i = 0 \\
-\dd \gamma = \sum_i \frac{n_i^\sigma}{A} \dd\mu_i = \sum_i \Gamma_i \dd\mu_i
$$
$\Gamma$ is called **Surface excess concertation**(表面过剩浓度)

---

### Electrocapillary Equation

Wire---Cu|Ag|AgCl(Ref)|   K+, Cl-,  M(ekectrolyte)   |(WE)Hg|Ni|Cu---Wire

for Working Electrode :
$$
\begin{aligned}
-\dd \gamma &= (\Gamma_{Hg}\dd\mu_{Hg} + \Gamma_{e}\dd\mu_{e})\\
&+(\Gamma_{K}\dd\mu_{K} + \Gamma_{Cl}\dd\mu_{Cl})\\
&+(\Gamma_{M}\dd\mu_{M} + \Gamma_{H_2O}\dd\mu_{H_2O})
\end{aligned}
$$
**天书**


$$
-\dd \gamma = \sigma_M \dd E + \Gamma_{K}(H_2O)\dd\mu_{KCl} + \Gamma_M(H_2O)\dd \mu_M  =\sigma_M \dd E +  C
$$
that is : 
$$
\boxed{\sigma_M =-\frac{\dd \gamma}{\dd E}}
$$

---

### Droping Mercury Electrode















---

### Adsorption Isotherm

$$
\begin{aligned}
\mu_i^{Adsorption} &= \mu_i^{bulk}\\
\mu_i^{\circ A} + RT\ln a_i^{A} &= \mu_i^{\circ b} + RT\ln a_i^b\\
a_i^A &= a_i^be^{-\frac{\Delta G_i}{RT}}
\end{aligned}
$$

Assumptions:

- All surface sites are identical
- No lateral interactions
- A full coverage can be achieved

def $a_i = \frac{\Gamma_i}{\Gamma_s-\Gamma_i}$, $\theta = \frac{\Gamma_i}{\Gamma_s}$

that is:
$$
\frac{\theta}{1-\theta} = a_i^be^{-\frac{\Delta G_i}{RT}}\\
\theta_i = \frac{a_i^be^{-\frac{\Delta G_i}{RT}}}{1+\sum_j^N a_j^be^{-\frac{\Delta G_i}{RT}}}
$$
this is **Langmuir Isotherm**

---

## Chapter 3 : Chemical Kinetics
### Kinetic Theory of Gases KTG (Ideal Gases)
$$
p = (\frac{\partial U}{\partial V})_S \quad \text{Pressure is a measurement of energy density}
$$
Assume one molecule in a $abc$ box:

![image-20250923161117996](C:\Users\kelesss\AppData\Roaming\Typora\typora-user-images\image-20250923161117996.png)
$$
\Delta t = \frac{2a}{u_{1x}}
$$
$$
F_1 = \frac{\Delta (mu_x)}{\Delta t} = \frac{mu_{1x}^2}{a} \\
P_1 = \frac{F_1}{bc} = \frac{mu_{1x}^2}{V}\\
P = \sum_i P_i = \frac mV \sum_i u_{ix}^2
$$

With symmetry $\langle u_x^2 \rangle = \langle u_y^2 \rangle = \langle u_z^2 \rangle$

$$
u^2 = u_x^2 + u_y^2 + u_z^2 \rightarrow \langle u^2 \rangle = \langle u_x^2 \rangle + \langle u_y^2 \rangle + \langle u_z^2 \rangle = 3\langle u_x^2 \rangle \\
PV = \frac 13 Nm\langle u^2 \rangle \\
\frac 12m\langle u^2 \rangle = \frac 32 \frac{PV}{N} = \frac 32 k_BT \\
\frac 13 M\langle u^2 \rangle = RT
$$
that is :
$$
\boxed{\sqrt{\langle u_x^2 \rangle} = \sqrt{\frac{3RT}{M}}}  
$$
let $h(u_x,u_y,u_z)$ be the fraction of molecules with velocity between $u_x + du_x,u_y + du_y, u_z + du_z$, as independent:
$$
h(u_x,u_y,u_z) = f(u_x) + f(u_y) + f(u_z)
$$

$$
f(u_x) = \sqrt{\frac{m}{2\pi RT}} e^{\frac{Mu_x^2}{2RT}}\\
h(u_x,u_y,u_z) = \left( \frac{m}{2\pi RT} \right)^\frac 32 e^{-M(u_x^2 + u_y^2 + u_z^2)/2RT}
$$

as polar coordinate:
$$
F(u)du = 4\pi \left( \frac{m}{2\pi RT} \right)^\frac 32 u^2 e^{-mu^2/2RT} du\\
\boxed{
\langle u \rangle = 4\pi \left( \frac{m}{2\pi RT} \right)^\frac 32 \int u^3 e^{-mu^2/2RT} du = \sqrt{\frac{8RT}{\pi M}}
}\\
\langle u^2 \rangle = 4\pi \left( \frac{m}{2\pi RT} \right)^\frac 32 \int u^4 e^{-mu^2/2RT} du = \frac{3RT}{M}
$$

---

### Collision of gas

assume collision in $dt$ in the oblique cylinder

![image-20250923161327057](C:\Users\kelesss\AppData\Roaming\Typora\typora-user-images\image-20250923161327057.png)





---

### Mean Free Path

![image-20250923162240436](C:\Users\kelesss\AppData\Roaming\Typora\typora-user-images\image-20250923162240436.png)

molecules in the cylinder will be collided
$$
dN_{coll}  =\rho\pi d^2 \langle u \rangle dt \\
Z_A = \frac{dN_{coll}}{dt} = \rho\pi d^2\sqrt{\frac{8RT}{\pi \mu}} = \rho\pi d^2\sqrt{\frac{16RT}{\pi m}}
$$
(in dealing with two molecules relative motion)

$Z_A$ is called **collision frequency of one molecule**
$$
l = \langle u \rangle dt = \langle u \rangle / Z_A  = \frac{1}{\sqrt{2}\rho \pi d^2} = \frac{RT}{\sqrt{2}N_AP \pi d^2}
$$
$l$ is called **mean free path**

the **total collision frequency** $Z$ is:（the average angle is 90° so $u_r = \sqrt{2}u$）
$$
Z_{AA} = \frac 12 \rho Z_A = \frac12 \pi d^2 \langle u_r \rangle \rho^2  =  \frac{1}{\sqrt2} \pi d^2 \langle u \rangle \rho^2\\
Z_{AB} = \sigma_{AB} \langle u_r \rangle \rho_A \rho_B = \pi\left( \frac{d_A + d_B}{2} \right)^2 ·\sqrt{\frac{8RT}{\pi \mu}}·\rho_A \rho_B
$$
**Collision theory**: $r \propto Z_{AB}$ and rxn only happen when $u_r > u_0$



---

### Phenomenological Kinetics

$$
\ce{\nu_AA + \nu_BB -> \nu_YY + \nu_ZZ}
$$

$$
r = \frac{d\xi}{dt} = -\frac{1}{\nu_A}\frac{dn_A}{dt} = \frac{1}{\nu_Y}\frac{dn_Y}{dt} \\
r = k[\ce{A}]^{m_A}[\ce{B}]^{m_B} \\
\ln r = \ln k +  m_A\ln{[\ce{A}]} +  m_B\ln{[\ce{B}]} \\
$$

first/second order reactions ....

**Transition State Theory**:

- Reactant are in eq. with the activated complex(AC) or transition state
- AC converts to product in a irreversible step

$$
\ce{A + B <=> [AB]^\ddagger -> P} \\
K_c^\ddagger =\frac{[AB^\ddagger]c^{\circ}}{[A][B]}
$$

at eq $\mu_A + \mu_B = \mu_{AB^\ddagger}$

from statistical mechanics:
$$
\mu = -RT(\frac{\partial \ln Q}{\partial N})_{VT} = -RT(\frac{\partial \ln {\frac{q^N}{N!}}}{\partial N})_{VT} = 
-RT\ln{q/N} \\
\mu^\ddagger = \mu_A + \mu_B \rightarrow \frac{q^\ddagger}{N^\ddagger} = \frac{q_A}{N_A} \frac{q_ B}{N_B}\\
\frac{N^\ddagger}{N_AN_B} = \frac{q^\ddagger}{q_Aq_B} \\
K_c^\ddagger = \frac{\frac{q^\ddagger}{V}·c_0}{\frac{q_A}{V}\frac{q_B}{V}} = \exp(-\frac{\Delta^\ddagger G ^\circ}{RT})
$$
let $\nu_c$ be the freq. at which AC cross over the barrier
$$
\frac{d[P]}{dt} = \nu_c[AB^\ddagger] = k[A][B] \\
k = \nu_c K_c^\ddagger /c^\circ
$$






























