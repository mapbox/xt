xt
==

Automatically convert a stream of tiles to another format

-  z/x/y \| z-x-y ==> [x, y, z]

-  [x, y, z] ==> z/x/y \| z-x-y \| z?x?y -d ?

Examples
--------

Tile URL to `mercantile <https://github.com/mapbox/mercantile>`__
``[x, y, z]``

::

    » echo https://map.s/17/20971/5051.png | xt
    [20971, 50651, 17]

mercantile to ``z/x/y``

::

    » echo '[0, 0, 0]' | xt
    0/0/0

mercantile to ``z-x-y``

::

    » echo '[100, 100, 100]' | xt -d
    100-100-100

roundtrip af

::

    » pbpaste | xt | xt -d | xt | xt | xt | xt -d | xt | xt 
    17/20972/50653
