# Cross section definition
# Read about KLayout XSection processor in the documentation

# input:
# Layers last updated based off of LED_test_devices.py on 6/7/18

si_wg = layer("22/0")
si_partial = layer("21/0")
si_photo_only = layer("22/1")

dp_pp = layer("1/0")
dp_np = layer("2/0")
dp_p = layer("3/0")
dp_n = layer("4/0")
dp_e = layer("5/0")

m1_nwpad = layer("11/99").or(layer("11/0"))
m2_nw = layer("12/0")
m3_res = layer("15/0")
m4_ledpad = layer("14/0").or(layer("14/99"))
m5_wiring = layer("16/0").or(layer("16/99"))
v3 = layer("31/0")
v5 = layer("32/0")


# Setup initial wafer
height(7.5) # thickness of the full stack
t_si = 220.nm # thickness of Si device layer
x_si = grow(t_si)
bOx = bulk # bOx = buried oxide; bulk = reserved keyword of the xsection script

# ######## Step 12: deposit SiN electrical isolation ########
# x_sinx = grow(0.050)


######## Step 17-18: Si etch of slab and rib ########
# Has to happen first so dopants don't remove it
si_wg = si_wg.or(m2_nw.sized(0.5)).or(si_photo_only)
rib = si_wg.not(si_partial)
etch_pedestal = rib.inverted
etch_through = si_wg.inverted
# waveguide, assume non vertical sidewall, with mid-point being the desired width; bias = sin(10)*220.
etch_angle = 0
mask(etch_pedestal).etch(150.nm, :taper => etch_angle, :bias => 0, :into => x_si)
mask(etch_through).etch(70.nm, :taper => etch_angle, :bias => -0, :into => x_si)
x_si1 = x_si.dup

# Proceed with official processing steps
# Not all of them affect the xsection

######## Step 1-2: alignment, clean, protective oxide ########

######## Steps 3-6: dopant implants ########
doping_bias = 0.01
x_dp_pp = mask(dp_pp).grow(t_si, doping_bias, :into => x_si, :bias => doping_bias, :mode => :round)
x_dp_np = mask(dp_np).grow(t_si, doping_bias, :into => x_si, :bias => doping_bias, :mode => :round)
x_dp_p = mask(dp_p).grow(t_si, doping_bias, :into => x_si, :bias => doping_bias, :mode => :round)
x_dp_n = mask(dp_n).grow(t_si, doping_bias, :into => x_si, :bias => doping_bias, :mode => :round)

######## Steps 7-8: anneal ########

######## Step 9: Si ion implant ########
x_dp_e = mask(dp_e).grow(t_si, doping_bias, :into => x_si, :bias => doping_bias, :mode => :round)

######## Step 10: anneal ########

######## Step 11: remove protective oxide ########

######## Step 12: deposit SiN electrical isolation ########
x_sinx = mask(rib).grow(50.nm)

######## Step 13: Ti/Au for contact to WSi ########
x_tiau_sc = mask(m1_nwpad).grow(90.nm)

######## Step 14: WSi for superconducting devices ########
x_wsi = mask(m2_nw).grow(90.nm, 40.nm, :mode => :round)
t_m2m3_oxide = 24.nm
x_m2m3_oxide = mask(rib).grow(t_m2m3_oxide, t_m2m3_oxide/2)

######## Step 16: PdAu layer for hTron gate and resistors ########
x_pdau = mask(m3_res).grow(60.nm, 30.nm, :mode => :round)

######## Step 15: SiO2 layer for hTrons ########
x_htron_oxide = grow(24.nm, 24.nm)

######## Step ...: TiAu-Nb vias ########
mask(v3).etch(24.nm + t_m2m3_oxide, :taper => 20, :bias => 0, :into => [x_htron_oxide, x_m2m3_oxide])

######## Step 17-18: Si etch of slab and rib ########
# see above

######## Step ...: LED contacts ########
x_tiau_led = mask(m4_ledpad).grow(90.nm)

######## Step ...: Nb wiring 1 ########
t_wire1 = 100.nm
isotropy = 0.8 # 1.0 is isotropic growth, 0.0 is perfectly anisotropic
x_nb1 = mask(m5_wiring).grow(t_wire1, t_wire1 * isotropy, :mode => :round)
######## Step ...: Nb wiring 2 ########

######## Step ...: Encapsulation ########
x_oxide = grow(0.6, 0.6, :mode => :round)

######## Step ...: Bond pad open ########
mask(v5).etch(1.0, :taper => 5, :into => x_oxide)

# x_mlopen = mask(mlopen).grow(0.4, :into => x_oxide)

#xoxide = deposit (2.950, 2.95, :mode => :round)
#x_oxide = x_oxide.or(deposit (2.950))




### outputs

layers_file(File.join(File.expand_path(File.dirname(__FILE__)), "OLMAC-xs.lyp"))
output("300/0", bOx)
output("300/0", x_oxide)
output("300/0", x_m2m3_oxide)
output("300/0", x_htron_oxide)

output("301/0", x_si1)

output("310/0", x_sinx)
output("311/0", x_tiau_sc)
output("311/0", x_tiau_led)
output("312/0", x_wsi)
output("313/0", x_pdau)

output("314/0", x_nb1)

output("320/0", x_dp_pp)
output("321/0", x_dp_np)
output("322/0", x_dp_p)
output("323/0", x_dp_n)
output("324/0", x_dp_e)



