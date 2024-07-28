import json
import urllib.request
import pickle
from deepface import DeepFace
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, models
from django.http import HttpResponse,Http404
import os
from .models import UploadFile
import cv2
from zipfile import ZipFile

class LogSuccessResponse(HttpResponse):

    def close(self):
        super(LogSuccessResponse, self).close()

        try:
            os.remove('zipped/compressedtextstuff.zip')
        except:
            print("zipped/compressedtextstuff.zip not found")


        try:
            os.remove('face_matched_zipped/compressedtextstuff.zip')
        except:
            print("face_matched_zipped/compressedtextstuff.zip not found")

@csrf_exempt
def process_image(request):
    json_data = json.loads(request.body)
    data = json_data['image']

    username_from_browser = json_data['username']

    get_user = UploadFile.objects.filter(title = username_from_browser).count()

    if (get_user == 0):
        return HttpResponse("Session does not exist")




    # https://stackoverflow.com/a/57021043

    response = urllib.request.urlopen(data)

    with open('image.jpg', 'wb') as f:
        f.write(response.file.read())


    # root folder - image.jpg

    # given = Image.open('image.jpg')
    # numpy_encoded_given = np.array(given)
    # encoded_given = face_recognition.face_encodings(numpy_encoded_given)



    # TODO :- handle throws, ei function ta error throw korbe jodi image.jpg face na hoye .. 

    matching_results = []

    samy = os.listdir(os.path.abspath("uploads/{0}".format(username_from_browser)))
    for ref_files in samy:
        res = {}
        ref_file_source = cv2.imread(os.path.abspath("uploads/{0}/{1}".format(username_from_browser, ref_files)))


        face_match = 0
        result = 2
        try:
            result = DeepFace.verify(cv2.imread("image.jpg"), ref_file_source.copy())
            face_match = result["verified"]
        except:
            face_match = False

        res["path"] = "uploads/{0}/{1}".format(username_from_browser, ref_files)
        res["result"] = face_match
        matching_results.append(res)

    print(matching_results)


    not_recognized = False

    for z in matching_results:
        if z["result"]:
            not_recognized = False
            break
        else:
            not_recognized = True


    if not_recognized:
        raise Http404("no images found ?? ")



    with ZipFile('face_matched_zipped/compressedtextstuff.zip', 'w') as myzip:
        for x in matching_results:
            if x["result"]:
                myzip.write(x['path'])


    with open('face_matched_zipped/compressedtextstuff.zip', "rb") as fh:
        response = LogSuccessResponse(fh.read(),
                                      content_type="application/zip")
        response[
            'Content-Disposition'] = 'inline; filename=compressedtextstuff.zip'
        return response

