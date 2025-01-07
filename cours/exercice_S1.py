# Donnees reelles
rho_inf = 0.3119  # kg/m3
T_inf = 273.15 - 56.5  # K
U_inf = 260  # m/s
L = 72.7  # m
mass = 500e3  # kg

# Donnees soufflerie
rho_m = 47.3  # kg/m3
nu_m = 4.5e-7  # kg/m/s
csound_m = 387  # m/s

# Constantes
gamma_isentrop = 1.4
r_air = 287.1  # J/K/kg
g_grav = 9.81  # m/s^2


def sutherland(T):
    """
    Fonction pour calculer la viscosite dynamique de l'air

    Input:
    ------
    T float
    temperature en K

    Return:
    -------
    mu float
    viscosite dynamique a la temperature specifiee en kg/(m.s)
    """
    mu_ref = 1.7894e-5  # kg/(m.s)
    S0 = 110.4  # K
    T_ref = 288.16  # K
    mu = mu_ref * (T/T_ref)**1.5 * (T_ref + S0)/(T + S0)
    return mu

# Resolution
mu_m = rho_m * nu_m
csound_inf = (gamma_isentrop * r_air * T_inf)**0.5
Ma_inf = U_inf / csound_inf
U_m = Ma_inf * csound_m

mu_inf = sutherland(T_inf)
Re_inf = rho_inf * U_inf * L / mu_inf
L_m = Re_inf * mu_m / (rho_m * U_m)

# Solution
print(f'Reynolds: {Re_inf:.2e}')
print(f'Mach: {Ma_inf:.2f}')
print(f'Vitesse soufflerie: {U_m:.1f} m/s')
print(f'Envergure maquette: {L_m:.2f} m/s')

# Calcul des efforts
Weight = mass * g_grav
Lift = Weight
CL = Lift / (0.5 * rho_inf * U_inf**2 * L**2)
Lift_m = CL * (0.5 * rho_m * U_m**2 * L_m**2)
print(f'Coefficient de portance: {CL:.3f}')
print(f'Force mesurée: {Lift_m:.1f} N')