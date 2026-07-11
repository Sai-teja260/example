## Question 3 — Extracted text

**Question 3 (8 points)**
Given are the following datasheet parameters of a photodiode:

| Parameter                                                                              |                Value |
| -------------------------------------------------------------------------------------- | -------------------: |
| Photocurrent ((E_e=0.1,\mathrm{mW/cm^2},\ \lambda=940,\mathrm{nm},\ V_R=5,\mathrm{V})) |  (3.8,\mu\mathrm{A}) |
| Radiant sensitive area                                                                 | (8.12,\mathrm{mm^2}) |
| Capacitance ((V_R=0,\mathrm{V},\ E_e=0,\mathrm{mW/cm^2}))                              |     (72,\mathrm{pF}) |

**a)** Calculate the responsivity (R_\lambda) of the photodiode for (940,\mathrm{nm}).

**b)** Calculate the resulting photocurrent (I_P) when applying (1,\mathrm{mW}) of radiant flux to the photodiode.

**c)** How high is the irradiance on the photodiode for a radiant flux of (1,\mathrm{mW})?

**d)** How will the capacitance of the photodiode change when doubling the photodiode area?

**e)** How will the capacitance of the photodiode qualitatively change if we apply a reverse-bias voltage?
The final part of this sentence is cut off in the picture, but it most likely asks about applying approximately (5,\mathrm{V}) reverse bias.

The lecture notes define photodiode responsivity as photocurrent divided by the incident optical power. They also explain that the depletion region acts as a capacitor and that increasing reverse bias widens the depletion region and reduces capacitance. 

---

# Solutions

## a) Responsivity (R_\lambda) at (940,\mathrm{nm})

Responsivity is

[
R_\lambda=\frac{I_P}{\Phi_e}
]

where:

* (R_\lambda) = responsivity in (\mathrm{A/W})
* (I_P) = photocurrent
* (\Phi_e) = radiant flux or optical power incident on the photodiode

The datasheet gives irradiance, not total optical power. Therefore, first calculate the radiant flux falling on the sensitive area.

### Step 1: Convert the area

[
A=8.12,\mathrm{mm^2}
]

Since

[
1,\mathrm{cm^2}=100,\mathrm{mm^2}
]

[
A=\frac{8.12}{100}=0.0812,\mathrm{cm^2}
]

### Step 2: Calculate incident radiant flux

[
\Phi_e=E_eA
]

[
\Phi_e=
0.1,\frac{\mathrm{mW}}{\mathrm{cm^2}}
\times 0.0812,\mathrm{cm^2}
]

[
\Phi_e=0.00812,\mathrm{mW}
]

Convert to watts:

[
0.00812,\mathrm{mW}=8.12,\mu\mathrm{W}
=8.12\times10^{-6},\mathrm{W}
]

### Step 3: Calculate responsivity

[
R_\lambda=
\frac{3.8\times10^{-6},\mathrm{A}}
{8.12\times10^{-6},\mathrm{W}}
]

[
\boxed{R_\lambda\approx0.468,\mathrm{A/W}}
]

### Final answer

[
\boxed{R_\lambda\approx0.47,\mathrm{A/W}}
]

This value is reasonable for a silicon photodiode near (940,\mathrm{nm}), where silicon has relatively high responsivity. The lecture’s spectral-response graph also shows high silicon-photodiode sensitivity in this near-infrared region. 

---

## b) Photocurrent for (1,\mathrm{mW}) radiant flux

The photocurrent is

[
I_P=R_\lambda\Phi_e
]

Given:

[
R_\lambda=0.468,\mathrm{A/W}
]

[
\Phi_e=1,\mathrm{mW}=1\times10^{-3},\mathrm{W}
]

Therefore:

[
I_P=
0.468\times1\times10^{-3}
]

[
I_P=4.68\times10^{-4},\mathrm{A}
]

[
I_P=0.468,\mathrm{mA}
]

or

[
I_P=468,\mu\mathrm{A}
]

### Final answer

[
\boxed{I_P\approx0.468,\mathrm{mA}=468,\mu\mathrm{A}}
]

This assumes that the photodiode remains in its linear operating region. According to the lecture, photocurrent is ideally proportional to the incoming optical power, although saturation can cause nonlinearity at high photocurrents. 

---

## c) Irradiance for a radiant flux of (1,\mathrm{mW})

Irradiance is radiant flux per unit area:

[
E_e=\frac{\Phi_e}{A}
]

Given:

[
\Phi_e=1,\mathrm{mW}
]

[
A=8.12,\mathrm{mm^2}
]

Using the area in (\mathrm{cm^2}):

[
A=0.0812,\mathrm{cm^2}
]

Therefore:

[
E_e=
\frac{1,\mathrm{mW}}
{0.0812,\mathrm{cm^2}}
]

[
E_e=12.315,\mathrm{mW/cm^2}
]

### Final answer

[
\boxed{E_e\approx12.3,\mathrm{mW/cm^2}}
]

Equivalent forms are:

[
\boxed{E_e\approx0.123,\mathrm{mW/mm^2}}
]

and

[
\boxed{E_e\approx123,\mathrm{W/m^2}}
]

---

## d) Capacitance when the photodiode area is doubled

The depletion region of a photodiode behaves approximately like a parallel-plate capacitor:

[
C=\frac{\varepsilon A}{w}
]

where:

* (C) = junction capacitance
* (\varepsilon) = semiconductor permittivity
* (A) = junction area
* (w) = depletion-region width

At constant reverse voltage and constant depletion width:

[
C\propto A
]

Therefore, doubling the area doubles the capacitance.

Original capacitance:

[
C_1=72,\mathrm{pF}
]

New area:

[
A_2=2A_1
]

Therefore:

[
C_2=2C_1
]

[
C_2=2\times72,\mathrm{pF}
]

[
\boxed{C_2=144,\mathrm{pF}}
]

### Final answer

The capacitance doubles:

[
\boxed{72,\mathrm{pF}\rightarrow144,\mathrm{pF}}
]

---

## e) Effect of applying reverse bias on capacitance

When reverse-bias voltage is applied:

1. The electric field across the p–n junction increases.
2. The depletion region becomes wider.
3. The effective separation between the capacitor plates increases.
4. Therefore, the junction capacitance decreases.

Since

[
C_j=\frac{\varepsilon A}{w}
]

an increase in depletion width (w) causes a reduction in (C_j).

### Final answer

[
\boxed{\text{The photodiode capacitance decreases when reverse bias is increased.}}
]

A larger reverse bias produces a wider depletion region and therefore a smaller junction capacitance. This is stated directly in the photodiode lecture: capacitance is inversely proportional to the depletion-zone width, and increasing reverse bias reduces capacitance. 

---

## Compact exam answer

[
A=8.12,\mathrm{mm^2}=0.0812,\mathrm{cm^2}
]

### a)

[
\Phi_e=E_eA
=0.1,\mathrm{mW/cm^2}\times0.0812,\mathrm{cm^2}
=8.12,\mu\mathrm{W}
]

[
R_\lambda=\frac{I_P}{\Phi_e}
=\frac{3.8,\mu\mathrm{A}}{8.12,\mu\mathrm{W}}
]

[
\boxed{R_\lambda=0.468,\mathrm{A/W}}
]

### b)

[
I_P=R_\lambda\Phi_e
=0.468,\mathrm{A/W}\times1,\mathrm{mW}
]

[
\boxed{I_P=468,\mu\mathrm{A}}
]

### c)

[
E_e=\frac{\Phi_e}{A}
=\frac{1,\mathrm{mW}}{0.0812,\mathrm{cm^2}}
]

[
\boxed{E_e=12.3,\mathrm{mW/cm^2}}
]

### d)

[
C\propto A
]

Doubling the area doubles the capacitance:

[
\boxed{C_2=144,\mathrm{pF}}
]

### e)

Increasing reverse bias widens the depletion region. Since

[
C_j=\frac{\varepsilon A}{w}
]

the capacitance decreases:

[
\boxed{\text{Higher reverse bias }\Rightarrow\text{ lower capacitance}}
]
