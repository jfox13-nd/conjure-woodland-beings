# conjure-woodland-beings

A simple tool to help DMs randomly determine the creatures spawned by the Dungeons and Dragons 5th Edition spell [Conjure Woodland Beings](https://www.dndbeyond.com/spells/conjure-woodland-beings).

## Usage

```bash
usage: conjure_woodland_beings.py [-h] [--max-monsters MAX_MONSTERS]
                                  [--mm-only]
                                  MAXCR [MINCR]

Randomly determine the creatured spawned by the Dungeons and Dragons 5E spell
Conjure Woodland Beings.CRs must be 2, 1, 1/2, 1/4, or 1/8.

positional arguments:
  MAXCR                 The maximum CR of conjured monsters, minimum 1/4
  MINCR                 The minimum CR of conjured monsters (default MAXCR)

optional arguments:
  -h, --help            show this help message and exit
  --max-monsters MAX_MONSTERS
                        Set a maximum number of unique monster types
  --mm-only             Only use Monster Manual creatures
```

## Example Outputs

```bash
jackfox$ ./conjure_woodland_beings.py 2
Darkling Elder x 1
    CR 2, Volo's Guide to Monsters, 134
```

```bash
jackfox$ ./conjure_woodland_beings.py 1/4
Sprite x 5
    CR 1/4, Monster Manual, 283

Blink Dog x 2
    CR 1/4, Monster Manual, 318

Pixie x 1
    CR 1/4, Monster Manual, 253
```

```bash
jackfox$ ./conjure_woodland_beings.py 1/2 1/8
Sprite x 1
    CR 1/4, Monster Manual, 283

Pixie x 2
    CR 1/4, Monster Manual, 253

Darkling x 1
    CR 1/2, Volo's Guide to Monsters, 134
```

```bash
jackfox$ ./conjure_woodland_beings.py 1/2 --max-monsters 1
Satyr x 4
    CR 1/2, Monster Manual, 267
```

```bash
jackfox$ ./conjure_woodland_beings.py 1/2 --mm-only
Satyr x 4
    CR 1/2, Monster Manual, 267
```
