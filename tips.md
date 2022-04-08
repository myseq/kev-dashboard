# Tips (Using JQ)
To make it easy for testing, it is recommended to download the `known_exploited_vulnerabilities.json` and rename it as `today.json`. 

### Show the information about JSON file.
```console
$ cat today.json | jq  ' .title , .catalogVersion , .dateReleased , .count  '                                                                                                                                                                         3 ⨯
"CISA Catalog of Known Exploited Vulnerabilities"
"2022.03.31.2"
"2022-03-31T16:29:24.2424Z"
609
```

### List all the vulnerabilities that will due on 2022-04-15, and show in one line per object.
```console
$ cat today.json | jq -c '.vulnerabilities[] | select ( .dueDate == "2022-04-15" ) '
```

### List all the vulnerabiities that will due on 2022-06-01, and show them in JSON format.
```console
$ cat today.json | jq '.vulnerabilities[] | select ( .dueDate == "2022-06-01" ) '

{
  "cveID": "CVE-2020-11261",
  "vendorProject": "Qualcomm",
  "product": "Snapdragon Auto, Snapdragon Compute, Snapdragon Connectivity, Snapdragon Consumer IOT, Snapdragon Industrial IOT, Snapdragon Mobile, Snapdragon Voice & Music, Snapdragon Wearables",
  "vulnerabilityName": "Qualcomm Multiple Chipsets Improper Input Validation Vulnerability",
  "dateAdded": "2021-12-01",
  "shortDescription": "Memory corruption due to improper check to return error when user application requests memory allocation of a huge size in Snapdragon Auto, Snapdragon Compute, Snapdragon Connectivity, Snapdragon Consumer IOT, Snapdragon Industrial IOT, Snapdragon Mobile, Snapdragon Voice & Music, Snapdragon Wearables",
  "requiredAction": "Apply updates per vendor instructions.",
  "dueDate": "2022-06-01"
}
{
  "cveID": "CVE-2018-14847",
  "vendorProject": "MikroTik",
  "product": "RouterOS",
  "vulnerabilityName": "MikroTik Router OS Directory Traversal Vulnerability",
  "dateAdded": "2021-12-01",
  "shortDescription": "MikroTik RouterOS through 6.42 allows unauthenticated remote attackers to read arbitrary files and remote authenticated attackers to write arbitrary files due to a directory traversal vulnerability in the WinBox interface.",
  "requiredAction": "Apply updates per vendor instructions.",
  "dueDate": "2022-06-01"
}
```

### Count vulnerability that will due on 2022-04-15. [66]
```console
$ cat today.json | jq  -c '[ .vulnerabilities[] | select ( .dueDate == "2022-04-15" ) ] | length '
66
```

### Select any vulnerability where vendor is 'Cisco'.
```console
$ cat today.json | jq  -c '[ .vulnerabilities[] | select ( .vendorProject == "Cisco" )] | length '
54
```

### Search for a particular CVE like CVE-2021-21551
```console
$ cat today.json | jq  ' .vulnerabilities[] | select ( .cveID == "CVE-2021-21551" ) '
{
  "cveID": "CVE-2021-21551",
  "vendorProject": "Dell",
  "product": "dbutil Driver",
  "vulnerabilityName": "Dell dbutil Driver Insufficient Access Control Vulnerability",
  "dateAdded": "2022-03-31",
  "shortDescription": "Dell dbutil driver contains an insufficient access control vulnerability which may lead to escalation of privileges, denial-of-service, or information disclosure.",
  "requiredAction": "Apply updates per vendor instructions.",
  "dueDate": "2022-04-21"
}
```

