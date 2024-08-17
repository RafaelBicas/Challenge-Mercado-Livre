# 📦 Challenge-Mercado-Livre: VirusTotal API 📦

# Scope
The test is related to the creation of a CTI report and the development of a tool to retrieve data used for our analysis.
The CTI report will be sent to the team for correction and the tool, documentation and Unit tests will be stored in GitHub.

# Documentation
This API was developed to help on CTI research when it is related to malware data. It will provide information from [VirusTotal](https://www.virustotal.com/gui/home/upload) regarding the hash searched and will return the information separated regarding it.

The data that will be returned is:
- Names
- Hashes
- IoC (hostnames, IPs, ports, url)
- Threat category
- Votes

## Endpoints
This API was developed with the following endpoints:

- /
  - This is the initial endpoint which once opened, it will show the message 'VirusTotal API: Keep searching!'
  - Use example on browser: http://127.0.0.1:5000/
- /hash_search
  - The hash_search is the endpoint that will be responsible for the research on VirusTotal. If just hash_search is typed, it will display one message to the user related to the correct syntax to use the tool: 'Use the following syntax to search on API hashsearch/valid_hash'
  - Use example on browser: http://127.0.0.1:5000/hash_search
- /hash_search/\<valid hash\>
  - This endpoint will make it able to search for the data from the VirusTotal
  - The already tested hash algorithms that are able to be used are: sha256, sha1, md5
 - Use example on browser: http://127.0.0.1:5000/hash_search/ced3557310b98b8a1ede8c1c24c4997a2eb2e05e561dd0b6ca36627f0d987d14
