# kev-dashboard.py
kev-dashboard.py is a simple tool to generate a dashboard for CISA's Known Exploited Vulnerabilities (KEV).

This tool is written in python, and it can display the dashboard in two (2) modes: text mode or ASCII chart mode.


# Usage
To show the help screen.
```console
$ ./kev-dashboard.py -h
usage: kev-dashboard.py [-h] [-c] [-i <n>] [-j <file.json>] [-v]

   Zzzzz   |\      _,,,---,,_
           /,`.-'`'    -.  ;-;;,_   __author__ : [ zd ]
          |,4-  ) )-,_..;\ (  `'-'  __year__   : [ 2022.03 ]
         '---''(_/--'  `-'\_)       __file__   : [ ./kev-dashboard.py ]

         [ Analysis Dashboard for CISA's Known Exploited Vulns (KEV) Catalog ]


optional arguments:
  -h, --help      show this help message and exit
  -c              Show output as chart
  -i <n>          Specifying most common vendor/product. Default is top 5.
  -j <file.json>  Specifying local JSON file
  -v              verbose output
```

To show the dahboard in text mode.
```console
$ ./ kev-dashboard.py
```

To show the dashboard in ASCII chart mode.
```console
$ ./kev-dashboard.py -c
```

# References
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [KEV Dashboard](https://myseq.blogspot.com/2022/04/kev-dashboard.html)
- [KEV Catalog tool](https://github.com/myseq/kev-cataglog/)
