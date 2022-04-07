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


 _____ _____ _____    ____          _   _                 _
|  |  |   __|  |  |  |    \ ___ ___| |_| |_ ___ ___ ___ _| |
|    -|   __|  |  |  |  |  | .'|_ -|   | . | . | .'|  _| . |
|__|__|_____|\___/   |____/|__,|___|_|_|___|___|__,|_| |___|



CISA's KEV Dashboard [ 2022.04.06/616 ]


Top 5 Vendors (122)                     Top 5 Products (307)
 [*] Microsoft : 177                      [*] Windows                 :  58
 [*] Cisco     :  54                      [*] Office                  :  17
 [*] Adobe     :  33                      [*] Win32k                  :  15
 [*] Apple     :  29                      [*] Flash Player            :  14
 [*] Google    :  26                      [*] IOS and IOS XE Software :  13


Top 5 Date Added (23)                   Top 5 Due Date (41)
 [*] 2021-11-03 : 287                     [*] 2022-05-03 : 174
 [*] 2022-03-03 :  95                     [*] 2021-11-17 :  98
 [*] 2022-03-25 :  66                     [*] 2022-03-24 :  68
 [*] 2022-03-28 :  32                     [*] 2022-04-15 :  66
 [*] 2022-01-10 :  15                     [*] 2022-04-18 :  31


 [2022-04-07] Completed within [0.45 sec].

```

To show the dashboard in ASCII chart mode.
```console
$ ./kev-dashboard.py -c

 _____ _____ _____    ____          _   _                 _
|  |  |   __|  |  |  |    \ ___ ___| |_| |_ ___ ___ ___ _| |
|    -|   __|  |  |  |  |  | .'|_ -|   | . | . | .'|  _| . |
|__|__|_____|\___/   |____/|__,|___|_|_|___|___|__,|_| |___|



CISA's KEV Dashboard [ 2022.04.06/616 ]


Top 5 Vendors [ 122 ]
------------------------------
  Microsoft: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  177
  Cisco    : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  54
  Adobe    : ▇▇▇▇▇▇▇▇▇  33
  Apple    : ▇▇▇▇▇▇▇▇  29
  Google   : ▇▇▇▇▇▇▇  26


Top 5 Vulnerable Products [ 307 ]
------------------------------------------
  Windows                : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  58
  Office                 : ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇  17
  Win32k                 : ▇▇▇▇▇▇▇▇▇▇▇▇▇  15
  Flash Player           : ▇▇▇▇▇▇▇▇▇▇▇▇  14
  IOS and IOS XE Software: ▇▇▇▇▇▇▇▇▇▇▇  13


# Heatmap Calendar for Vulnerability Due Date [ 41 ]
-------------------------------------------------------------
        Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov
 Mon :           ░       ░   ░░           ░   ░
 Tue :            ░   ░░   ░   █
 Wed : ▓ ░ ░ ░                ░    ░         ░   ░
 Thu :               ░  ░▒   ░            ░░   ░
 Fri :      ░     ░░░░ ░    ▒       ░
 Sat :
 Sun :                                  ░

# Heatmap Calendar for Vulnerability Added to KEV [ 23 ]
-----------------------------------------------------------------
        Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov
 Mon :           ░       ░  ░░
 Tue :            ░   ░░  ░
 Wed : █ ░ ░ ░               ░
 Thu :               ░  ▒   ░
 Fri :      ░     ░░░░ ░   ░
 Sat :
 Sun :


 [2022-04-07] Completed within [0.21 sec].
 
```

# References
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [KEV Dashboard](https://myseq.blogspot.com/2022/04/kev-dashboard.html)
- [KEV Catalog tool](https://github.com/myseq/kev-cataglog/)
