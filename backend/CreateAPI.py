import json
import uvicorn
import mimetypes
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Text, List, Optional, Dict
from backend.Helpers import get_dict_of_somenthing, get_dict_of_timestamp_counts, get_existance_of_item_in_dict_keys, get_pandas_datatime_format_from_dict

# CODE TO INITIALIZE THE SERVER: uvicorn backend.CreateAPI:app --reload
app = FastAPI()
output_file = 'E:/performanceLOGS/performance-log-updated(final).json'
users= []
UserTotalLogs = 0
UserTotalLevel = []
UserTotalTimestamp = []


# Load the file once at startup
@app.on_event("startup")
async def load_data():
    global users
    global UserTotalLogs
    global UserTotalLevel
    global UserTotalTimestamp

    with open(output_file, 'r') as f:
        users = [json.loads(line) for line in f]
   
    for user in users:
        for request in user:
            UserTotalLogs += 1
            UserTotalLevel.append(request["level"])
            UserTotalTimestamp.append(request["timestamp"])


@app.get("/")
async def fetch_users():
    
    return users[103][0]  #sample of the data


@app.get("/length")
async def fetch_lenght():

    return len(users)   #ammount of test samples


@app.get("/totallogs")
async def fetch_totalLogs():

    return UserTotalLogs


@app.get("/totallogsovertime")
async def fetch_statuscode_with_time():

    Counts=get_dict_of_timestamp_counts(UserTotalTimestamp)
    return Counts


@app.get("/level")
async def level():

    return UserTotalLevel


@app.get("/timestamp")
async def timestamp():

    return {"timestamp": UserTotalTimestamp}


@app.get("/mimetype")
async def fetch_mime_types():
    mime_types = []
    for user in users:
        for request in user:
            try:
                # try to get the mime type from the documentMimeType
                mime_type = request['message']['message']['params']['documentMimeType']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the documentMimeType
                mime_types.append(mime_type)
                continue

            try:
                # try to get the mime type from the content type
                content_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the content type
                mime_type = content_type.split(';')[0].strip()
                mime_types.append(mime_type)
                continue

            try:
                # try to get the mime type from the extension
                url = request['message']['message']['params']['request']['url']
                extension = url.split('.')[-1]
                mime_type = mimetypes.types_map.get('.' + extension, None)
            except (KeyError, IndexError):
                pass
            else:
                #if you can get the mimetype from the extension
                mime_types.append(mime_type)
                continue
            try:
                # try to get the mime type from the X-Content-Type-Options header
                content_type_options = request['message']['message']['params']['headers']['X-Content-Type-Options']
                if content_type_options == 'nosniff':
                    mime_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the X-Content-Type-Options header
                mime_type = mime_type.split(';')[0].strip()
                mime_types.append(mime_type)
                continue

    return mime_types


@app.get("/dictofmimetype")
async def fetch_dict_of_mime_types():

    Keys = {}
    for user in users:
        for request in user:
            try:
                # try to get the mime type from the documentMimeType field
                mime_type = request['message']['message']['params']['documentMimeType']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the documentMimeType
                get_dict_of_somenthing(Keys, mime_type)
                continue

            try:
                # try to get the mime type from the Content-Type header
                content_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the Content-Type header
                mime_type = content_type.split(';')[0].strip()
                get_dict_of_somenthing(Keys, mime_type)
                continue

            try:
                # try to get the mime type from the extension
                url = request['message']['message']['params']['request']['url']
                extension = url.split('.')[-1]
                mime_type = mimetypes.types_map.get('.' + extension, None)
            except (KeyError, IndexError):
                pass
            else:
                #if you can get the mimetype from the extension
                get_dict_of_somenthing(Keys, mime_type)
                continue
            try:
                # try to get the mime type from the X-Content-Type-Options header
                content_type_options = request['message']['message']['params']['headers']['X-Content-Type-Options']
                if content_type_options == 'nosniff':
                    mime_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the X-Content-Type-Options header
                get_dict_of_somenthing(Keys, mime_type)
                continue
            
    return Keys


@app.get("/mimetypeovertime")
async def fetch_mime_types():
    MimeTypeOverTime={}

    for user in users:
        for request in user:                
            timestamp = request["timestamp"]
            try:
                # try to get the mime type from the documentMimeType
                mime_type = request['message']['message']['params']['documentMimeType']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the documentMimeType
                get_existance_of_item_in_dict_keys(mime_type, MimeTypeOverTime, timestamp)
                continue

            try:
                # try to get the mime type from the content type
                content_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the content type
                mime_type = content_type.split(';')[0].strip()
                get_existance_of_item_in_dict_keys(mime_type, MimeTypeOverTime, timestamp)
                continue

            try:
                # try to get the mime type from the extension
                url = request['message']['message']['params']['request']['url']
                extension = url.split('.')[-1]
                mime_type = mimetypes.types_map.get('.' + extension, None)
            except (KeyError, IndexError):
                pass
            else:
                get_existance_of_item_in_dict_keys(mime_type, MimeTypeOverTime, timestamp)
                continue
            try:
                # try to get the mime type from the X-Content-Type-Options header
                content_type_options = request['message']['message']['params']['headers']['X-Content-Type-Options']
                if content_type_options == 'nosniff':
                    mime_type = request['message']['message']['params']['headers']['Content-Type']
            except KeyError:
                pass
            else:
                #if you can get the mimetype from the X-Content-Type-Options header
                get_existance_of_item_in_dict_keys(mime_type, MimeTypeOverTime, timestamp)
                continue
            
    
    #create a dataframe with the timestamps and convert them to dictionaries again
    StatusCodeOverTime=get_pandas_datatime_format_from_dict(MimeTypeOverTime)
    return StatusCodeOverTime


@app.get("/statuscode")
async def fetch_statuscode():
    UserTotalStatusCode = []
    for user in users:
        for request in user:
            try:
                # if you can get the status code
                if request["message"]["message"]["params"]["statusCode"]:
                    UserTotalStatusCode.append(
                        request["message"]["message"]["params"]["statusCode"])
            except KeyError:
                pass

    return UserTotalStatusCode


@app.get("/dictofstatuscode")
async def fetch_dict_of_status_code():
    Keys = {}
    for user in users:
        for request in user:
            try:
                # if you can get the status code
                if request["message"]["message"]["params"]["statusCode"]:
                    get_dict_of_somenthing(
                        Keys, request["message"]["message"]["params"]["statusCode"])
            except KeyError:
                pass

    return Keys


@app.get("/statuscodeovertime")
async def statuscodeovertime():
    Dictofstatuscode = {}
    for user in users:
        for request in user:
            try:
                # if the status code is not empty
                if request["message"]["message"]["params"]["statusCode"]:
                    statuscode = request["message"]["message"]["params"]["statusCode"]
                    timestamp = request["timestamp"]
                    get_existance_of_item_in_dict_keys(statuscode, Dictofstatuscode, timestamp)

            except KeyError:
                pass

    #for every status code, create a dataframe with the timestamps and convert them to dictionaries again
    StatusCodeOverTime=get_pandas_datatime_format_from_dict(Dictofstatuscode)
    return StatusCodeOverTime


if __name__ == "__main__":
    uvicorn.run("backend.CreateAPI:app --reload")
