xt
===

[![Build Status](https://travis-ci.org/mapbox/xt.svg?branch=master)](https://travis-ci.org/mapbox/xt) [![Coverage Status](https://coveralls.io/repos/github/mapbox/xt/badge.svg?branch=master)](https://coveralls.io/github/mapbox/xt?branch=master)

Automatically convert a stream of tile coordinates to another format

- `z/x/y | z-x-y` ==> `[x, y, z]`

- `[x, y, z]` ==> `z/x/y` | `z-x-y` | `z?x?y -d ?`


Installation
-------------
```
pip install xt
```
Or to develop:
```
git@github.com:mapbox/xt.git && cd xt && pip install -e '.[test]'
```

Examples
---------
Tile URL to [mercantile](https://github.com/mapbox/mercantile) `[x, y, z]`
```
» echo https://map.s/17/20971/5051.png | xt
[20971, 50651, 17]
```
mercantile to `z/x/y`
```
» echo '[0, 0, 0]' | xt
0/0/0
```
mercantile to `z-x-y`
```
» echo '[100, 100, 100]' | xt -d -
100-100-100
```
roundtripping
```
» pbpaste | xt | xt -d - | xt | xt | xt | xt -d | xt | xt 
17/20972/50653
```
Using mercantile to generate tile urls from a parent tile:
```
» echo '[0, 0, 0]' | mercantile children --depth 2 | xt | awk '{print "https://map.s/"$NF".png"}'
https://map.s/2/0/0.png
https://map.s/2/1/0.png
https://map.s/2/1/1.png
https://map.s/2/0/1.png
https://map.s/2/2/0.png
https://map.s/2/3/0.png
https://map.s/2/3/1.png
https://map.s/2/2/1.png
https://map.s/2/2/2.png
https://map.s/2/3/2.png
https://map.s/2/3/3.png
https://map.s/2/2/3.png
https://map.s/2/0/2.png
https://map.s/2/1/2.png
https://map.s/2/1/3.png
https://map.s/2/0/3.png
```
