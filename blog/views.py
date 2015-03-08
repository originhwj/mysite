from django.shortcuts import render

# Create your views here.
from django.template import loader,Context,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import BlogPost,Photo
from blog.forms import PhotoForm
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django import forms
import Image
import glob
import numpy

def getKey( x ):
    return float(x[0])

@csrf_exempt
def archive(request):
    posts = BlogPost.objects.get(id=6)
    t = loader.get_template("archive.html")
    c = Context({'post':posts})
    #response = HttpResponse()
    #response.write("<p>1122</p>")
    #return response
    return HttpResponse(t.render(c))


def te(request):
    posts = BlogPost.objects.get(id=1)
    t = loader.get_template("te.html")
    c = Context({'posts':posts})
    #return response
    return HttpResponse(t.render(c))

def contact(request):
    obj_list = Photo.objects.all().order_by("id")
    im = obj_list[len(obj_list)-1]
    t = loader.get_template("contact.html")
    imgurl = "/static/image/1.jpg"
    c = Context({'obj_list':obj_list,'imgurl':imgurl,'im':im,})
    #return response
    return HttpResponse(t.render(c))


def remark(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thank you')
    else:
        form = PhotoForm()

    return render_to_response('message.html', {
                'form': form,
    })
    #return render_to_response('message.html')

@csrf_exempt
def search(request):
     if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        #form = PhotoForm(request.POST)
        #message = request.POST['image']
        #print message
        if form.is_valid():

            im = request.FILES['image']

            method = request.POST['func']
            methodOfModel = method;
            if(method == 'Softmax'):
                methodOfModel = 'S'
            elif(method == 'Hex'):
                methodOfModel = 'H'
            else:
                methodOfModel = 'nothing'


            image = Image.open(im)
            image.thumbnail((128,128),Image.ANTIALIAS)

            im = str(im)
            target_im = im[2:6]
            ind = int(target_im)-1
            #print ind


            jpgfile = glob.glob("./media/photo/*.jpg")
            for i in range(0,len(jpgfile)):
                jpgfile[i] = jpgfile[i][1:]
                jpgfile[i] = jpgfile[i].replace('\\','/')
                #print i
            #print jpgfile


            #image.save("./media/photo/11.jpeg","jpeg")
            #imgurl = "/media/photo/11.jpeg"
            imgurl = jpgfile[ind]
            #imgurl2 = "/media/photo/im0001.jpg"
            #form.save()
            #t = loader.get_template("search.html")

            fi = open('./media/feature300.txt')
            line = fi.readline()
            ###### read the picture feature ##########
            groundTruth = numpy.zeros((300,4096))
            j = 0
            while line:
                line = line.strip()
                li = line.split('  ')
                groundTruth[j] = li
                for i in range(0,4096):
                    groundTruth[j,i] =float(li[i])
            #np = numpy.array(list)
                #print groundTruth[j]
                j += 1

                line = fi.readline()
            g = []
            target = groundTruth[ind]

            for i in range(0,300):
                s = []
                #mahadun
                s.append(sum(abs(target - groundTruth[i])))
                #od = abs(target - groundTruth[i])
                #s.append(numpy.dot(od,od))
                s.append(jpgfile[i])
                g.append(s)

            g.sort(key=getKey)
            g = g[0:30]
            im_list= []
            for g_item in g:
                im_list.append(g_item[1])

            fi.close()

            t = loader.get_template("mysearch.html")
            posts = Photo.objects.all()
            c = Context({'forms':posts,'im':imgurl,'md':methodOfModel,'imlist':im_list,})

            return HttpResponse(t.render(c))
        else:
            return HttpResponse('nothing')
