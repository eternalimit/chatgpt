# REDx — 380000 Design Max

Status: REDx / preserved model state

- GROUND = `_•`
- DESIGN_MAX = `380000`
- ROOT = `379999`
- HEADROOM = `1`

Equation:

`380000 - 379999 = 1`

Audit rule:

- PASS → advance
- FAIL → reset to `0`

Scope note: `380000` is a model-defined design ceiling in this framework. It is not, by itself, a verified real-world structural load-bearing capacity without units, materials, geometry, soil conditions, code checks, and engineering validation.
