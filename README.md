# covid19_hoaxbust

These scripts help in translating English posters which do hoax busting to
regional languages as an effort by the community group "Indian Scientists
Response to COVID19".

`extract.sh` needs to be modified for each language to make sure it outputs the
strings that have to be placed at different locations in the image. It uses
simple markers to figure out which text has to be replaced.

```
sh extract.sh
```

This will produce 6 different files for the six different strings that have to
be inserted at different places in the poster.

`modify_poster` is a class which is able to insert the strings at the right places.

It will take an example poster and then put the strings extracted from the Main
file in the poster.

You need to have the correct fonts in the "Noto/" folder. Download these fonts
from https://www.google.com/get/noto
