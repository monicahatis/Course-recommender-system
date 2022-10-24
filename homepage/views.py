from multiprocessing import context
from urllib import request
from django.shortcuts import render,redirect
import pandas as pd
from scipy.sparse import csr_matrix
import numpy as np
from accounts.form import (
    SignINForm
)
from accounts.models import RaisecAnswer
# Create your views here.
from courses.models import (
    Course,
    ClusterClasses,
    AdvertUserLinks,
    CourseRattingAndComment,
    MinimumRequirement,
    UserMinimumRequirement
)
from sklearn.neighbors import NearestNeighbors
from django.contrib.auth.decorators import login_required

from raisec.models import RaisecGroup, RaisecQuestions
from .models import (
    ContactFromUser,
    ContactInfor,
    Subjects
)



def create_matrix(df):
	
	N = len(df['user'].unique())
	M = len(df['course'].unique())
	
	# Map Ids to indices
	user_mapper = dict(zip(np.unique(df["user"]), list(range(N))))
	course_mapper = dict(zip(np.unique(df["course"]), list(range(M))))
 
   
	
	# Map indices to IDs
	user_inv_mapper = dict(zip(list(range(N)), np.unique(df["user"])))
	course_inv_mapper = dict(zip(list(range(M)), np.unique(df["course"])))
	
	user_index = [user_mapper[i] for i in df['user']]
	movie_index = [course_mapper[i] for i in df['course']]

	X = csr_matrix((df["ratings"], (movie_index, user_index)), shape=(M, N))
	
	return X, user_mapper, course_mapper, user_inv_mapper, course_inv_mapper


def index(request):
    login_form = SignINForm(request.POST,None)


    all_courses = Course.objects.all()
    all_category =  ClusterClasses.objects.all()
    adverts = AdvertUserLinks.objects.all()

    context = {
        'courses' : all_courses,
        'course_category': all_category,
        'adverts' : adverts,
        'login':login_form
    }



    return render(request,'index.html',context)



def courses(request):
    all_courses = Course.objects.all()
    all_category =  ClusterClasses.objects.all()
    adverts = AdvertUserLinks.objects.all()

    context = {
        'courses' : all_courses,
        'course_category': all_category,
        'adverts' : adverts,
        'len_courses' :  len(all_courses)
    }

    return render(request,'course.html',context)


def raisec(request):
    all_raisec_group = RaisecGroup.objects.all()
    all_raisec_quiz =  RaisecQuestions.objects.all()

    context = {
        "all_raisec_group":all_raisec_group,
        "all_raisec_quiz":all_raisec_quiz


    }
    
    if request.method == "POST":
        for k in all_raisec_quiz:
           stry = f"quiz_{k.raisec_category.group_name}_{k.id}"
           t_u = request.POST.get(stry)
           if t_u is not None:
            quiz =  RaisecQuestions.objects.get(id = k.id)
            sz,created =  RaisecAnswer.objects.get_or_create(quiz = quiz ,user = request.user)
            sz.raisec_answer =  True
     
            sz.save()

        return redirect("homepage:addGrade")
    return render(request,'raisec.html',context)




def courseDetails(request,id):

    one_course =  Course.objects.get(id = id)
    all_category =  ClusterClasses.objects.all()
    course_rattings = CourseRattingAndComment.objects.filter(course = one_course)

    context = {
        'course':one_course,
         'course_category': all_category,
         'course_rattings' : course_rattings
    }

    if request.method == "POST":
        user = request.user
        
        print("request ", request.POST)
        CourseRattingAndComment.objects.create(
            user = user,
            course = one_course,
            ratings = int(request.POST.get("ratting_number")),
            comment  = request.POST.get("comment")

        )
        context['success'] = "Added Comment Successfully"
        return render(request,'course_details.html',context)
    
    return render(request,'course_details.html',context)





def recommendation(request):
    # getting raisec group
    all_answers_for_raisec = RaisecAnswer.objects.filter(user =  request.user)
    empty_list_r = []
    empty_list_i = []
    empty_list_a = []
    empty_list_s = []
    empty_list_e = []
    empty_list_c  = []

    raisec_letter = ""

    for k in all_answers_for_raisec:
        if(k.quiz.raisec_category.group_name == "R"):
            empty_list_r.append(k.quiz.raisec_category.group_name)

        elif (k.quiz.raisec_category.group_name == "I"):
            empty_list_i.append(k.quiz.raisec_category.group_name)

        elif (k.quiz.raisec_category.group_name == "A"):
            empty_list_a.append(k.quiz.raisec_category.group_name)

        elif (k.quiz.raisec_category.group_name == "S"):
            empty_list_s.append(k.quiz.raisec_category.group_name)

        elif (k.quiz.raisec_category.group_name == "E"):
            empty_list_e.append(k.quiz.raisec_category.group_name)

        elif (k.quiz.raisec_category.group_name == "C"):
            empty_list_c.append(k.quiz.raisec_category.group_name)

    new_list = [len(empty_list_r),len(empty_list_a),len(empty_list_c),len(empty_list_e),len(empty_list_i),len(empty_list_s)]
    index = new_list.index(max(new_list))
    print(index)
    if index == 0:
        raisec_letter = "R"

    elif index == 1:
        raisec_letter = "A"

    elif index == 2:
        raisec_letter = "C"

    elif index == 3:
        raisec_letter = "E"
    
    elif index == 4:
        raisec_letter = "I"
    elif index == 5:
        raisec_letter = "S"


    # get user minimum requirement 


    user_min =  UserMinimumRequirement.objects.filter(user =  request.user)
    if len(user_min) > 0:
        us =  UserMinimumRequirement.objects.get(user = request.user )
        min_requirement =  us.minimum_requirement
        print("min requirement" , min_requirement)


        print("raisec letter ", raisec_letter)
        reisec_group =  RaisecGroup.objects.filter(group_name__icontains = raisec_letter)
        if len(reisec_group) > 0:
            print("found group name")
            get_group =  RaisecGroup.objects.get(group_name = raisec_letter)

            filter_courses_recommendation = Course.objects.filter(miniumu_requirement = min_requirement,raisec_group = get_group )
            
            context = {
                "courses" : filter_courses_recommendation
            }
            
            print("filtered ",len(filter_courses_recommendation))
            return render(request,'recommendation.html',context)

    


    
   
    # df = pd.DataFrame(list(CourseRattingAndComment.objects.all().values('user', 'course', 'ratings')))
    # print("pandas df",df)
    # X, user_mapper, course_mapper, user_inv_mapper, course_inv_mapper = create_matrix(df)
    # print(user_mapper)

    # def find_similar_movies(course_id, X, k, metric='cosine', show_distance=False):
	
    #     neighbour_ids = []
        
    #     course_ind = course_mapper[course_id]
    #     course_vec = X[course_ind]
    #     k+=1
    #     kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    #     kNN.fit(X)
    #     course_vec = course_vec.reshape(1,-1)
    #     print("course vec",course_vec)
    #     neighbour = kNN.kneighbors(course_vec, return_distance=show_distance)
    #     for i in range(0,k):
    #         n = neighbour.item(i)
    #         neighbour_ids.append(course_inv_mapper[n])
    #     neighbour_ids.pop(0)
    #     return neighbour_ids


    # movie_id = 1

    # similar_ids = find_similar_movies(movie_id, X, k=0.3)

    # print(similar_ids)


    

    # print(df)
    return render(request,'recommendation.html')



def addGrade(request):
    all_requirements = MinimumRequirement.objects.all()

    context = {
        'all_requirements':all_requirements
    }

    if request.method == "POST":
        grade =  request.POST.get("subject")
        get_min =  MinimumRequirement.objects.get(id =  int(grade))
 
        sv,created = UserMinimumRequirement.objects.get_or_create(user =  request.user)
        sv.minimum_requirement = get_min
        sv.save()

        return redirect("homepage:recommendation")

      
    return render(request,'enterGrade.html',context)





def contactPage(request):
    info =  ContactInfor.objects.first()
    subjects = Subjects.objects.all()

    if request.method == "POST":
        name =  request.POST.get("name")
        email =  request.POST.get("email")
        subject =  request.POST.get("subject")
        number =  request.POST.get("number")
        message =  request.POST.get("message")

        sub = Subjects.objects.get(id = int(subject))
      

        bh =  ContactFromUser.objects.create(
            name = name,
            email =  email,
            subject =  sub,
            phone = number,
            message = message


        )

        if bh is not None:
            context = {
                "message":"Saved successfully!",
                "info":info,
                "subjects":subjects
            }
            return render(request,'contact.html',context)





    context = {
         "message":"",
        "info":info,
        "subjects":subjects
    }
    return render(request,'contact.html',context)




