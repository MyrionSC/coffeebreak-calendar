DEPLOY_HOST=192.168.87.177
DEPLOY_PATH=/var/www/html/n1-kaffepause-kalender/

scp -r dist/* "$DEPLOY_HOST:$DEPLOY_PATH"

