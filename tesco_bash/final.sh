#set -x

source /workspaces/bk-recipes/tesco-requests.sh

PAGE=$(fetch_tesco_home)

XCSRF=$( echo $PAGE | grep -oP '"csrfToken":"\K[^"]+' | head -n 1 )

COOKIE=$( echo $PAGE | grep -oP 'set-cookie: _csrf=\K[^;]+' | head -n 1)

fetch_tesco_search $COOKIE $XCSRF "Lowicz" #failing due to http/2 stream error