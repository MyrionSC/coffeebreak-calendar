DEPLOY_HOST=192.168.87.177
DEPLOY_PATH=/var/www/html/coffee-break/

scp -r dist/ "$DEPLOY_HOST:$DEPLOY_PATH"
