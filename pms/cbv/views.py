
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Food,AddFile

# Create your views here.
class FoodCreateView(CreateView):
    fields  ='__all__'
    model = Food
    template_name = 'cbv/foodcreate.html'
    success_url = '/cbv/list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['info_sended'] = False # an extra variable
        return context
        

class FoodListView(ListView):
    model = Food
    context_object_name = 'foodlist'
    template_name = 'cbv/foodlist.html'

    # def get(self, request, *args, **kwargs):
    #         self.form = FoodListView(request.GET)
    #         if self.form.is_valid():
    #             self.queryset = self.form.process_search(self.queryset)
    #         return super(FoodDetailView, self).get(request, *args, **kwargs)
    
    def get_queryset(self):
        return super().get_queryset()




class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'cbv/fooddelete.html'
    success_url = '/cbv/list'

    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
      


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'cbv/foodupdate.html'
    fields = '__all__'
    success_url = '/cbv/list'
    
class FoodDetailView(DetailView):
    model = Food
    template_name = 'cbv/fooddetail.html'
    context_object_name = 'fooddetail'

class AddFileView(CreateView):
    model = AddFile
    template_name = 'cbv/addfile.html'
    success_url = '/cbv/filelist'
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
    
class FileListView(ListView):
    model = AddFile
    template_name = 'cbv/filelist.html'
    context_object_name = 'filelist'