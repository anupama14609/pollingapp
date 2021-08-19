from django.shortcuts import render


arr = ['HTML','CSS','Java','Javascript','Python','PHP','C','C++','R','React','Django','MLDS']
globalcnt = dict()

def home(request):
     context = {
          'arr':arr,
     }
     return render(request, 'app/home.html',context)

def Voting(request):
     q = request.GET['q']

     if q in globalcnt:
          globalcnt[q] = globalcnt[q]+1
          print(globalcnt)
     else:
          globalcnt[q] = 1

     context = {
          'globalcnt':globalcnt,
          'arr':arr,
     }
    
     return render(request, 'app/home.html',context)


def Sortdata(request):
     global globalcnt
     globalcnt = dict(sorted(globalcnt.items(), key=lambda x:x[1], reverse=True))
     context = {
          'arr':arr,
          'globalcnt':globalcnt,
     }
     return render(request, 'app/home.html',context)