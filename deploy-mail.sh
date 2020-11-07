DEPLOY_HOST=192.168.87.177
DEPLOY_PATH=/home/marand/scripts/send_coffeebreak_mails/

scp -r src/send_mails/* src/helper_functions.py "$DEPLOY_HOST:$DEPLOY_PATH"
ssh "marand@$DEPLOY_HOST" "dos2unix $DEPLOY_PATH/*"
ssh "marand@$DEPLOY_HOST" "chmod 700 $DEPLOY_PATH/email-creds.json"
