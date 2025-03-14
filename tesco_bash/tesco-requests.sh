fetch_tesco_home() {
  curl 'https://www.tesco.com/' \
    -H 'accept: text/html' \
    -H 'accept-language: en-US,en;q=0.9' \
    -H 'pragma: no-cache' \
    -H 'priority: u=0, i' \
    -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"' \
    -H 'sec-ch-ua-mobile: ?0' \
    -H 'sec-ch-ua-platform: "Windows"' \
    -H 'sec-fetch-dest: document' \
    -H 'sec-fetch-mode: navigate' \
    -H 'sec-fetch-site: same-origin' \
    -H 'sec-fetch-user: ?1' \
    -H 'upgrade-insecure-requests: 1' \
    -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36' \
    -H 'cache-control: no-cache' \
    -i
}

# headers to file -D headers.txt
# cookies to file -c cookies.txt

fetch_tesco_search() {
  COOKIE=$1
  XCSRF=$2
  QUERY=$3

  curl 'https://www.tesco.com/groceries/en-GB/resources' \
    -H 'authority: www.tesco.com' \
    -H 'accept: application/json' \
    -H 'accept-language: en-GB,en;q=0.9' \
    -H 'cache-control: no-cache' \
    -H 'content-type: application/json' \
    -H 'cookie: '${COOKIE}';' \
    -H 'origin: https://www.tesco.com' \
    -H 'pragma: no-cache' \
    -H 'referer: https://www.tesco.com/groceries/en-GB/search?query=milk' \
    -H 'user-agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Mobile Safari/537.36' \
    -H x-csrf-token:${XCSRF} \
    --data '{
        "resources": [
            {
                "type": "search",
                "params": {
                    "query": {
                        "query": "'${QUERY}'",
                        "page": "1"
                    }
                }
            }
        ],
        "sharedParams": {
            "query": {}
        },
        "requiresAuthentication": false
    }'
}

fetch_tesco_search(){
  # Working verion: ger list of products Lowicz (no blocking)
  curl 'https://www.tesco.com/groceries/en-GB/search?query=Lowicz&inputType=free+text' \
  -H 'accept: text/html' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'pragma: no-cache' \
  -H 'priority: u=0, i' \
  -H 'sec-ch-ua: "Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36' \
  -H 'cache-control: no-cache'
}

# | grep "styled__Text-sc-1i711qa-1 bsLJsh ddsweb-link__text\">Lowicz"