from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Item, Clients
from django.db.models import F
from .forms import ClientsForm
from django.contrib import messages
from pprint import pprint
from datetime import datetime    
from django.utils import timezone
import re
from django.http import JsonResponse



def clean_data(data):
    print(f"Original data: {data}")  # Verifique o valor recebido
    if not isinstance(data, str):
        return ''  # Ou algum valor padrão apropriado
    data = re.sub(r'[\'"\[\],]+$', '', data)
    data = data.strip()
    return data

class ItemListView(ListView):
    model = Item
    template_name = 'item/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/item_detail.html'

class ItemCreateView(CreateView):
    
    model = Item
    fields = ['nome', 'descricao', 'preco']
    success_url = '/'
    template_name = 'item/item_form.html'
    

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['nome', 'descricao', 'preco']
    success_url = '/'
    template_name = 'item/item_form.html'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = '/'
    template_name = 'item/item_confirm_delete.html'

class PolimorthicView(ListView):
   model = Item
   template_name = 'polimorfismo/index.html'

def CrudView(request):
    return render(request, 'crud/index.html')

def CrudCreateView(request):
    return render(request, 'crud/create.html')

def CrudReadView(request):
    return render(request, 'crud/read.html')

def CrudUpdateView(request):
    return render(request, 'crud/update.html')

def CrudDeleteView(request):
    return render(request, 'crud/delete.html')

def CrudCompleteView(request):
    return render(request, 'crud/complete.html')

def FormularioView(request):
    if request.method == 'POST':
        form = ClientsForm(request.POST or None)
        #pprint(dir(object))
        if form.is_valid():
            # Processar os dados do formulário
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # mensagem = form.cleaned_data['mensagem']
            # Adicione sua lógica aqui (e.g., salvar no banco de dados, enviar email)[]
            cd = form.cleaned_data
            pd = Clients(
                name = cd['name'],
                cpf_cnpj = cd['cpf_cnpj'],
                rg_ie = cd['rg_ie'],
                zip_code = cd['zip_code'],
                address = cd['address'],
                neighborhood = cd['neighborhood'],
                number = cd['number'],
                city = cd['city'],
                state = cd['state'],
                ddd = "", #cd['ddd']
                created_at = datetime.now(),
                #updated_at = 'null',
                #deleted_at = 'null',
            )
            pd.save()
            #messages.debug(request, "%s SQL statements were executed." % count)
            #messages.info(request, "Three credits remain in your account.")
            messages.success(request, "Dados adicionados com sucesso no Formulário!.")
            #messages.warning(request, "Your account expires in three days.")
            #messages.error(request, "Document deleted.")
            return redirect('formulario')
        else:
            print(form.errors)
    else:
        form = ClientsForm()    
    return render(request, 'forms/form_template.html', {'form': form})

def FormListView(request):
    clients =  Clients.objects.all()
    return render(request, 'forms/form_list.html', {'clients': clients})

def FormDetailView(request, pk):
   id = pk
   clients = Clients.objects.get(pk=id)
   return render(request, 'forms/form_detail.html', {'clients': clients})

def FormUpdateView(request, pk):
    id = pk
    #pega o objeto que veio do templete pala primary key
    #client_id = request.POST.get('client_id')
    #cliente = get_object_or_404(Cliente, id=client_id)
    clients = Clients.objects.get(pk=id)        
    if request.method == 'POST':
        #form = ClientsForm(request.POST or None)
        form = ClientsForm(request.POST, instance=clients) 
        #pprint(dir(object))
        if form.is_valid():
            clients = form.save(commit=False)
            #jogo no registro a data no updated_at
            clients.updated_at = timezone.now()
            clients.save()  
            # Processar os dados do formulário
            # nome = form.cleaned_data['nome']
            # email = form.cleaned_data['email']
            # mensagem = form.cleaned_data['mensagem']
            # Adicione sua lógica aqui (e.g., salvar no banco de dados, enviar email)[]
            #cd = form.cleaned_data
            #pd = clients[
            #    name == cd['name'],
            #    cpf_cnpj == cd['cpf_cnpj'],
            #    rg_ie == cd['rg_ie'],
            #    zip_code == cd['zip_code'],
            #    address == cd['address'],
            #    neighborhood == cd['neighborhood'],
            #    number == cd['number'],
            #    city == cd['city'],
            #    state == cd['state'],
            #    ddd == "", #cd['ddd']
                #created_at = datetime.now(),
                #updated_at = 'null',
                #deleted_at = 'null',
            #]
            #pd.save()
        #messages.debug(request, "%s SQL statements were executed." % count)
        #messages.info(request, "Three credits remain in your account.")
        messages.success(request, "Dados atualizados com sucesso no Formulário!.")
        #messages.warning(request, "Your account expires in three days.")
        #messages.error(request, "Document deleted.")
        return redirect('formulario')
    return render(request, 'forms/form_edit.html', {'clients': clients} )   
   
def FormDeleteView(request, pk):
    id = pk
    clients  = Clients.objects.get(pk=id)

    if request.method == 'POST':
        clients.delete()
        messages.success(request, "Cliente deletado com sucesso!.")
        return redirect('form-list')

    return render(request, 'forms/form_confirm_delete.html', {'clients': clients})
   
def FrontEndTemplate(request):
    return render(request, 'frontend/index.html')

def FrontEnd2Template(request):
    return render(request, 'frontend/index2.html')

def FrontEnd3Template(request):
    return render(request, 'frontend/index3.html')

def FeedsNews(request):
    return render(request, 'frontend/feeds.html')

def FJLocalstorage(request):
    return render(request, 'javascript/localstorage.html')

def FJSplitpop(request):
    return render(request, 'javascript/splitpop.html')

def FJNoticiafeed(request):
    return render(request, 'javascript/noticiafeed.html')

def FJTasks(request):
    return render(request, 'javascript/tasks.html')

def FJCart(request):
    return render(request, 'javascript/cart.html')

def Bootstrap(request):
    return render(request, 'bootstrap/index.html')