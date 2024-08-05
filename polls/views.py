from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from .models import UploadFile, ReviewMessage
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
import urllib.request
import pickle
from deepface import DeepFace
from django.core.files import File
import os
from django.contrib.auth import authenticate, login, logout, models
from PIL import Image
import base64
import io
from zipfile import ZipFile
import cv2



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
# koko
def pillow_image_to_base64_string(img, ext):
    buffered = io.BytesIO()
    img.save(buffered, format=ext)
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def base64_string_to_pillow_image(base64_str):
    return Image.open(
        io.BytesIO(base64.decodebytes(bytes(base64_str, "utf-8"))))


def index(request):
    print("Hi")
    print(os.path.abspath("uploads"))
    return HttpResponse("Hello, world. You're at the polls index.")


def handle_uploaded_file(f, name, usrname):

    with open("uploads/{0}/{1}".format(usrname, name), "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def process_the_file(file, title):
    # get the count of photos uploaded by a user from existing database .... probably the last image uploaded by the user
    spam = UploadFile.objects.filter(title=title).count()
    print("count - {0}".format(spam))


    # make a directory if no images are there ??
    if (spam == 0):
        os.makedirs("uploads/{0}".format(title))

    # increase the count by 1
    spam = spam + 1
    # https://docs.djangoproject.com/en/5.0/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile.name

    eggs = file.name.split(".")
    extens = eggs[-1]

    # the filename would be the new count with the extension
    file_name = "{0}.{1}".format(spam, extens)
    print("file name - {0}".format(file_name))

    # save the file to the uploads folder
    handle_uploaded_file(file, file_name, title)

    b = UploadFile(title=title, file="uploads/{0}/{1}".format(title, file_name))
    b.save()
    # with open("uploads/{0}".format(file_name)) as f:
    #     desired = File(f)
    #     b = UploadFile(title = title, file = desired)
    #     b.save()


@csrf_exempt
def upload_file(request):
    if request.method == "POST":

        # USERNAME = request.POST.get('title')
        # Availability = models.User.objects.filter(username = USERNAME).count()

        # if Availability == 0:
        #     return JsonResponse({"message": "User does not exist"})

        # print(request.POST.get('title'))

        # save the file in disk + db (??)
        for field, file in request.FILES.items():


            # request.POST.get('title') is maybbee ?? username ????
            process_the_file(file, request.POST.get('title'))

        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():

        #     form.save()

        #     spam = UploadFile.objects.filter(title=form.cleaned_data['title'])

        #     # https://stackoverflow.com/a/68989496

        #     eggs = []

        #     for x in spam:
        #         shawl = Image.open(x.file.path)
        #         data_url = 'data:image/jpeg;base64,' + pillow_image_to_base64_string(shawl)
        #         eggs.append(data_url)

        #     return JsonResponse({ 'images': eggs })
        # else:
        #     return HttpResponse("Not")

        return JsonResponse({'images': 2})

    else:
        return HttpResponse("Not a POST request")


def bar(request):
    template = loader.get_template("polls/upload/upload.html")
    foo = {"zod": 2}
    return HttpResponse(template.render(foo, request))


def zoom(request):
    print("Hi")
    template = loader.get_template("polls/shoot.html")

    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def process(request):
    print("Hi")
    json_data = json.loads(request.body)
    data = json_data['image']

    # https://stackoverflow.com/a/57021043

    response = urllib.request.urlopen(data)

    with open('image.jpg', 'wb') as f:
        f.write(response.file.read())

    # root folder - image.jpg

    # given = Image.open('image.jpg')
    # numpy_encoded_given = np.array(given)
    # encoded_given = face_recognition.face_encodings(numpy_encoded_given)

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
        response = LogSuccessResponse(fh.read(),content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=compressedtextstuff.zip'
        return response



def home(request):
    template = loader.get_template("polls/home.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def try_login(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        user = authenticate(username=data["username"],password=data["password"])
        print(user)
        if user is not None:
            login(request, user)
            print("success")
            return HttpResponse("passed auth")
        else:
            raise Http404("Failed authentication")


def auth(request):

    # username - runner
    # pass - fall2022

    template = loader.get_template("polls/auth.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def try_sign_up(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        try:
            user = models.User.objects.create_user(username=data["username"],password=data["password"])
            user.save()
            return HttpResponse("user created")
        except:
            raise Http404("Failed to create user")


def try_logout(request):
    logout(request)
    return HttpResponse("Logged out")


def view_photos(request):
    template = loader.get_template("polls/upload/view.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def display(request):

    data = JSONParser().parse(request)
    zoo = data["username"]

    # ...

    spam = UploadFile.objects.filter(title=zoo)

    # https://stackoverflow.com/a/68989496

    eggs = []

    for x in spam:
        shawl = Image.open(x.file)
        shawn = x.file.split(".")
        shawd = shawn[-1]
        if shawd == "jpg" or shawd == "jpeg":
            data_url = 'data:image/jpeg;base64,' + pillow_image_to_base64_string(
                shawl, "JPEG")
        elif shawd == "png":
            data_url = 'data:image/png;base64,' + pillow_image_to_base64_string(
                shawl, "PNG")

        eggs.append(data_url)

    return JsonResponse({'images': eggs})


def show_photo(request):
    template = loader.get_template("polls/download_photos/givephotos.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def does_the_user_exist(request):
    data = JSONParser().parse(request)
    zoo = data["username"]
    spam = UploadFile.objects.filter(title=zoo).count()
    if spam == 0:
        return HttpResponse("none")

    return HttpResponse("yes")


# https://stackoverflow.com/questions/71277957/how-to-zip-a-file-in-python
# https://stackoverflow.com/a/58567826
# https://stackoverflow.com/a/36394206


def downloaded_page(request):
    template = loader.get_template("polls/download_photos/download.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))





@csrf_exempt
def download_files(request):
    data = JSONParser().parse(request)
    zoo = data["username"]

    spam = UploadFile.objects.filter(title=zoo)
    # https://stackoverflow.com/a/4314182

    with ZipFile('zipped/compressedtextstuff.zip', 'w') as myzip:
        for x in spam:
            myzip.write(x.file)

    with open('zipped/compressedtextstuff.zip', "rb") as fh:
        response = LogSuccessResponse(fh.read(),content_type="application/zip")
        response['Content-Disposition'] = 'inline; filename=compressedtextstuff.zip'
        print("hi")
        return response


def index_page(request):
    template = loader.get_template("polls/index.html")
    foo = {"zod": 2}

    return HttpResponse(template.render(foo, request))


@csrf_exempt
def post_review(request):
    data = JSONParser().parse(request)
    aa = ReviewMessage(fullName=data["fullName"],
                       emailAddress=data["emailAddress"],
                       phone=data["phone"],
                       emailSubject=data["emailSubject"],
                       emailMessage=data["emailMessage"])
    aa.save()
    return HttpResponse("success")


@csrf_exempt
def process_image(request):
    json_data = json.loads(request.body)
    data = json_data['image']

    username_from_browser = json_data['username']

    get_user = models.User.objects.filter(username = username_from_browser).count()

    if (get_user == 0):
        return HttpResponse("User does not exist")

    
    

    # https://stackoverflow.com/a/57021043

    response = urllib.request.urlopen(data)

    with open('image.jpg', 'wb') as f:
        f.write(response.file.read())


    # root folder - image.jpg

    # given = Image.open('image.jpg')
    # numpy_encoded_given = np.array(given)
    # encoded_given = face_recognition.face_encodings(numpy_encoded_given)



    # TODO :- handle throws, ei function ta error throw korbe jodi image.jpg face na hoye .. 
    dfs = DeepFace.find(
        img_path = "image.jpg",
        db_path = os.path.abspath("uploads/{0}".format(username_from_browser)),
    )

    objects = []
    with (open(os.path.abspath("uploads/ds_model_vggface_detector_opencv_aligned_normalization_base_expand_0.pkl"), "rb")) as openfile:
        while True:
            try:
                objects.append(pickle.load(openfile))
            except EOFError:
                break




    return HttpResponse("Found !!")
