.. _layers:

Layer Definitions
=================
These are all the available layers listed as

token : layer/datatype
    description

---

dp_p : 1/0
    p+ doping

dp_n : 2/0
    n+ doping

dp_p : 3/0
    p doping

dp_n : 4/0
    n doping

dp_e : 5/0
    emitter doping

m1_nwpad : 11/0
    nanowire wiring and pads

m1_nwgnd : 11/99
    nanowire wiring and pads

m2_nw : 12/0
    superconductor (wsi)

m4_ledpad : 14/0
    LED pads

m4_ledgnd : 14/99
    LED ground

m3_res : 15/0
    hTron AuPd resistors

m5_wiring : 16/0
    wiring

m5_gnd : 16/99
    Ground plane

wg_shallow : 21/0
    shallow Si etch

wg_deep : 22/0
    Si etch photolith

v3 : 31/0
    via opening between m3-m2

v5 : 32/0
    via opening between m5-m4

su8_thin : 52/0
    su8 short pedestals

su8 : 51/0
    su8 polymer fences

labels : 255/0
    Labels

DRC_exclude : 91/0
    DRC ignores this area

GP_KO : 92/0
    Ground plane will keep out

FLOORPLAN : 99/0
    outer bounding box