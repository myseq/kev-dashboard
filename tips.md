# Tips (Using JQ)

1. List all the vulnerabilities that will due on 2022-04-15, and show in one line per object.
```console
$ cat known_exploited_vulnerabilities.json | jq -c '.vulnerabilities[] | select ( .dueDate == "2022-04-15" ) '
```

2. List all the vulnerabiities that will due on 2022-06-01, and show them in JSON format.
```console
$ cat known_exploited_vulnerabilities.json | jq '.vulnerabilities[] | select ( .dueDate == "2022-06-01" ) '

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

3. Count vulnerability that will due on 2022-04-15. [66]
```console
$ cat known_exploited_vulnerabilities.json | jq  -c '[ .vulnerabilities[] | select ( .dueDate == "2022-04-15" ) ] | length '
66
```

