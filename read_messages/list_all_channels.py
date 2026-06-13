
from template_folder.sync_client import client


# for dialog in client.iter_dialogs():
    # print(dialog.name)
    
    
for dialog in client.iter_dialogs():

    if dialog.is_channel:
        print(
            dialog.name,
            dialog.id
        )
# 1002715063688