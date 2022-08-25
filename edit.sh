#!/usr/bin/bash

ssh-add ~/.ssh/id_rsa_lolonao
bash ./env/bin/activate
code --extensions-dir /home/nao/prj/streamlit-playground/myvscode-settings/extensions-dir/ --user-data-dir /home/nao/prj/streamlit-playground/myvscode-settings/user-data-dir ./
