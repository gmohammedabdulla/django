from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post
from .form import PostForm
from django.shortcuts import redirect
from .business_logic import *
import json


# Create your views here.
def post_new(request):
    if request.method == "POST":
        #lat =[]
        #lag =[]
        print ("this is the post")
       # data = json.loads(request.POST)
        print(request.POST)
        lat = request.POST.getlist('lat[]')
        lag = request.POST.getlist('lag[]')
        print(lat[0])
        print(lag)
        #print(data['lat'])

        #All the logic calls
        point1 = polygon_data(0.0,0.0)
        point2 = polygon_data(0.0,0.0)

        distance_vector = []
        final = []
        simplelist = []
        #lat = 12.9086164163
        #long = 77.6456165313
        polygon = []
        house_keeping()

        if(len(lat)>2):

            for i in range(len(lat)):
                pp = polygon_data(float(lat[i]),float(lag[i]))
                print(pp.x)
                polygon.append(pp)

            lat1 = 16.4535553
            lon1 = 31.465645435
            lat2 = 12.4556756
            lon2 = 35.475676867
            lat3 = 17.23436456
            lon3 = 38.12234565


        #polygon =[]
        #x = polygon_data(lat[0],lag[0])
        #polygon.append(x)
        #y = polygon_data(lat[1],lag[1])
        #polygon.append(y)
        #z = polygon_data(lat[2],lag[2])
        #polygon.append(z)

            cen = centroid_for_polygon(polygon)
            print("i am back")
            print(cen.x)
            #centroid = centroid_for_polygon(polygon)
            dist_vect = farthest_points(polygon)
            print (dist_vect)
            final1 = business_logic_2(cen.x,cen.y,dist_vect)


        elif len(lat) == 1:
            cen = polygon_data(float(lat[0]),float(lag[0]))
            dist_vect = 4
            final1 = business_logic_2(cen.x,cen.y,dist_vect)
        elif len(lat)  == 2:
            print("in 2")
            v1=float(lat[0])
            v2 =float(lag[0])
            v3 = float(lat[1])
            v4 = float(lag[1])
            cen = polygon_data((v1+v3)/2,(v2+v4)/2)
            print("afetr centroid")
            dist_vect = distance(float(lat[0]),float(lag[0]),float(lat[1]),float(lag[1]))
            final1 = business_logic_2(cen.x,cen.y,dist_vect)

        print (final1)

       # finale = []
       # finale[0] =cen.x
       # finale[1] = cen.y
       # finale[2] = dist_vect

       # final1.append(string(cen.x))
        #for each in final1:
            #finale.append(each)

        return HttpResponse(json.dumps({'place':final1,'x':cen.x,'y':cen.y,'dist':dist_vect}),content_type = "application/json")
       # return HttpResponse(final1)
            #return HttpResponse(lat+lag)
            #return HttpResponse(
        #    json.dumps(response_data),
         #   content_type="application/json"
        #if form.is_valid():
         #   post = form.save(commit=False)
          #  post.author = request.user
           # post.save()
            #return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/index.html', {'form': form})



