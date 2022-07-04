#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, argparse
from argparse import RawTextHelpFormatter
from timeit import default_timer as timer
import json
import requests

from datetime import date
from datetime import datetime, timedelta
from collections import Counter
from colorama import init, Fore, Back, Style
import pyfiglet

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

description = f'Analysis Dashboard for CISA\'s Known Exploited Vulns (KEV) Catalog'
banner = f"""
   Zzzzz   |\      _,,,---,,_
           /,`.-'`'    -.  ;-;;,_   __author__ : [ zd ]
          |,4-  ) )-,_..;\ (  `'-'  __year__   : [ 2022.03 ]
         '---''(_/--'  `-'\_)       __file__   : [ {__file__} ]

         [ {description} ]
    """

url = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
verberos = False
top = 0

def cr(x): return (f'{Fore.RED}{x}{Style.RESET_ALL}')
def cb(x): return (f'{Fore.BLUE}{x}{Style.RESET_ALL}')
def cg(x): return (f'{Fore.GREEN}{x}{Style.RESET_ALL}')
def cy(x): return (f'{Fore.YELLOW}{x}{Style.RESET_ALL}')

def cal_heatmap(c_dateCal) -> None:
    """Print a calendar heatmap."""

    sc_dateCal = dict(sorted(c_dateCal.items(), key=lambda item: item[0]))

    max_key = max(sc_dateCal, key=sc_dateCal.get)
    max_val = sc_dateCal[max_key]

    mark_1 = f'\033[96m░\033[0m' # 0.01 - 0.24
    mark_2 = f'\033[94m▒\033[0m' # 0.25 - 0.49
    mark_3 = f'\033[93m▓\033[0m' # 0.50 - 0.74
    mark_4 = f'\033[91m█\033[0m' # 0.75 - 1.00

    fdate = list(c_dateCal.keys())[0]
    dt_start = datetime.strptime(fdate, '%Y-%m-%d')
    dt_start = dt_start - timedelta(dt_start.weekday())

    sys.stdout.write("        ")
    for month in range(13):
        month_dt = datetime( year=dt_start.year, month=dt_start.month, day=1) + timedelta(days=month * 31)
        sys.stdout.write(month_dt.strftime("%b") + " ")

    sys.stdout.write("\n")

    for day in range(7):
        sys.stdout.write(" " + DAYS[day] + " : ")
        for week in range(53):
            day_ = dt_start + timedelta(days=day + week * 7)
            day_str = day_.strftime("%Y-%m-%d")

            if day_str in sc_dateCal:
                if sc_dateCal[day_str] > max_val * 0.75:
                    mark = mark_4
                elif sc_dateCal[day_str] > max_val * 0.50:
                    mark = mark_3
                elif sc_dateCal[day_str] > max_val * 0.25:
                    mark = mark_2
                elif sc_dateCal[day_str] == 0.0:
                    mark = " "
                else: # show values for less than 0.25
                    mark = mark_1
            else:
                mark = " "

            sys.stdout.write(mark)


        sys.stdout.write("\n")

    #print(f'\n\n [*] Legends')
    print(f'\n [*]  [  {mark_4} >=75%    {mark_3} >=50%    {mark_2} >=25%    {mark_1} >=1%  ]')
    print(f'')

def barChart(c_dateCal, s, order) -> None:
    """Print a calendar heatmap."""

    max_width = 50

    if order:
        sc_dateCal = dict(sorted(c_dateCal.items(), key=lambda item: item[s]))
    else:
        sc_dateCal = dict(reversed(sorted(c_dateCal.items(), key=lambda item: item[s])))

    klen = 0
    for k,v in c_dateCal.items():
        if len(k) > klen:
            klen = len(k)

    max_key = max(sc_dateCal, key=sc_dateCal.get)
    max_val = sc_dateCal[max_key]

    mark0 = "▏"
    mark1 = "▇"


    for k,v in sc_dateCal.items():
        bar = v / max_val * max_width
        c = round(bar)
        if c >= 1:
            print(f'  {k:{klen}}: {cb(mark1*c)}  {v} ')
        elif bar > 0:
            print(f'  {k:{klen}}: {cb(mark0)}  {v}')
        else:
            print(f'  {k:{klen}}:  {v}')

def Charting(c_vendor, c_product, c_dateAdd, c_dateDue):
    g = globals()

    vlabel = []
    vdata = []
    top_vendor = {}


    for k,v in c_vendor.most_common(g['top']):
        vlabel.append(k)
        vval = []
        vval.append(v)
        vdata.append(vval)
        top_vendor[k] = v

    plabel = []
    pdata = []
    top_product = {}

    for k,v in c_product.most_common(g['top']):
        plabel.append(k)
        pval = []
        pval.append(v)
        pdata.append(pval)
        top_product[k] = v

    alabel = []
    adata = []

    for k,v in c_dateAdd.items():
        alabel.append(k)
        aval = []
        aval.append(v)
        adata.append(aval)

    dlabel = []
    ddata = []

    sc_dateDue = dict(sorted(c_dateDue.items(), key=lambda item: item[0]))

    for k,v in sc_dateDue.items():
        dlabel.append(k)
        dval = []
        dval.append(v)
        ddata.append(dval)

    print(f'')
    title = f'Top {cy(g["top"])} Vendors [ {len(c_vendor)} ]'
    print(title)
    print('-'*len(title))
    barChart(top_vendor, 1, False) # sorted by value in decending order
    print(f'')

    print('')
    title = f'Top {cy(g["top"])} Vulnerable Products [ {len(c_product)} ]'
    print(title)
    print('-'*len(title))
    barChart(top_product, 1, False) # sorted by value in decending order
    print(f'')

    print(f'')
    title = f'# Heatmap Calendar for Vulnerability Due Date [ {cy(len(c_dateDue))} ]'
    print(title)
    print('-'*len(title))
    cal_heatmap(c_dateDue)

    if g['verbose']:
        print(f'')
        title = f'## Vulnerability Due Date (chronological order) [ {cy(len(c_dateDue))} ]'
        print(title)
        print('='*len(title))
        barChart(c_dateDue, 0, True) # Sorted by KEY in ascending order


    print(f'')
    title = f'# Heatmap Calendar for Vulnerability Added to KEV [ {cy(len(c_dateAdd))} ]'
    print(title)
    print('-'*len(title))
    cal_heatmap(c_dateAdd)

    if g['verbose']:
        print(f'')
        title = f'## Dates of Vulnerability Added to KEV [ {cy(len(c_dateAdd))} ]'
        print(title)
        print('='*len(title))
        barChart(c_dateAdd, 0, True) # sorted by KEY in ascending order


def main():
    """ main() function """
    g = globals()

    parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

    parser.add_argument('-c', action='store_true', help='Show output as chart ')
    parser.add_argument('-i', dest='mostcommon', metavar='<n>', default=5, type=int,  help='Specifying most common vendor/product. Default is top 5.')
    parser.add_argument('-j', dest='jsonfile', metavar='<file.json>', help='Specifying local JSON file')
    parser.add_argument('-v', action='store_true', help='verbose output')

    args = parser.parse_args()
    g['verbose'] = True if args.v else False

    init(autoreset=True)
    print(f'')
    word = pyfiglet.figlet_format("KEV Dashboard", font="rectangles")
    print(Fore.BLUE + word)

    if args.jsonfile:
        try:
            fh = open(args.jsonfile, 'r')
            cisa = json.load(fh)
        except:
            print(f' [*] FAIL to open the {args.jsonfile}')
            return
    else:
        resp = requests.get(url)
        if resp.ok:
            cisa = resp.json()
        else:
            print(f' [*] FAIL to access the JSON file at {url}')
            return

    print(f'\nCISA\'s KEV Dashboard [ {cg(cisa["catalogVersion"])}/{cy(cisa["count"])} ]\n')

    vendors = []
    products = []
    dateAdd = []
    dateDue = []

    for vuln in cisa["vulnerabilities"]:
        vendors.append(vuln["vendorProject"].strip())
        products.append(vuln["product"].strip())
        dateAdd.append(vuln["dateAdded"].strip())
        dateDue.append(vuln["dueDate"].strip())

    g['top'] = args.mostcommon
    c_vendor = Counter(vendors)
    c_product = Counter(products)
    c_dateAdd = Counter(dateAdd)
    c_dateDue = Counter(dateDue)

    vlen = 0
    for k,v in c_vendor.most_common(g['top']):
        if len(k) > vlen:
            vlen = len(k)

    plen = 0
    for k,v in c_product.most_common(g['top']):
        if len(k) > plen:
            plen = len(k)

    if args.c:
        Charting(c_vendor, c_product, c_dateAdd, c_dateDue)
        return

    print(f'')
    t_vendor_product = f'Top {cy(top)} Vendors ({cg(len(c_vendor))})\t\t\tTop {cy(top)} Products ({cg(len(c_product))})'
    print(t_vendor_product)
    for vd, pd in zip(c_vendor.most_common(top), c_product.most_common(top)):
        vk, vv = vd
        pk, pv = pd
        print(f' [*] {vk:{vlen}} : {vv:3}\t\t\t  [*] {pk:{plen}} : {pv:3}')

    print(f'')
    print(f'')

    t_Added_Due = f'Top {cy(top)} Date Added ({cg(len(c_dateAdd))})\t\t\tTop {cy(top)} Due Date ({cg(len(c_dateDue))})'
    print(t_Added_Due)
    for da, dd in zip(c_dateAdd.most_common(top), c_dateDue.most_common(top)):
        ak, av = da
        dk, dv = dd
        print(f' [*] {ak} : {av:3}\t\t\t  [*] {dk} : {dv:3}')

        
if __name__ == "__main__":

    if sys.version_info.major == 2:
        print('This script needs Python 3.')
        exit()

    start = timer()
    main()
    end = timer()

    print(f'')
    print(f'\n [{date.today()}] Completed within [{end-start:.2f} sec].\n')


        
