from django.db import models
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from .models import contends


gauth = GoogleAuth()
gauth.LoadCredentialsFile('creds.json')
drive = GoogleDrive(gauth) 

def driveuploader(ls,file,filename):
    
    pathfile= file
    print('pass')
    parernt_id=folderspcifing(ls)
    gfile = drive.CreateFile({'parents': [{'id': parernt_id}]})
    gfile.SetContentFile(pathfile)
    gfile.Upload() 
    con=contends(RoomCode=ls.RoomCode,UniqCode=ls.UniqCode,pdf=gfile.get('id'),name=filename)
    con.save()



def drivedelete(ls):
    drive.CreateFile({'id': ls.pdf}).Delete()


def folderspcifing(ls):
    foder_title="WEBCLASSROOM"
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
    folder_id=None
    folder_id_in=None
    for file in file_list:
        if(file['title']==foder_title):
            folder_id=file['id']
            break
    if folder_id==None:
        folder_id=createmainfolder()
    children = drive.ListFile({'q': "'" + folder_id + "' in parents"}).GetList()
    for file in children:    
        if(file['title']==ls.RoomCode):
            folder_id_in=file['id']
            break
    if folder_id_in==None:
        folder_id_in=classroomfolder(ls,folder_id)
    return folder_id_in
    

def createmainfolder():
    folder_name="WEBCLASSROOM"
    folder=drive.CreateFile({'title':folder_name,'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')

def classroomfolder(ls,folder_id):
    folder_name=ls.RoomCode
    folder=drive.CreateFile({'title':folder_name,'parents' :  [{"id": folder_id, "kind": "drive#childList"}],'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    return folder.get('id')
