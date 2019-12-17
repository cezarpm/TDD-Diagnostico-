from django.shortcuts import render, redirect
from .models import Post

def mostrar_formulario(request):
    if request.method == 'POST':
        post = Post()
        post.titulo = request.POST.get('titulo')
        post.conteudo = request.POST.get('conteudo')
        post.nome = request.POST.get('nome')
        post.save()

        return redirect('/')

    return render(request, 'form.html')

def mostrar_home(request):
    posts = Post.objects.all()

    return render(request, 'index.html', {'posts': posts})

def apagar(request):
    post = Post.objects.filter(id=id)

    post.delete()

    return render(request, 'index.html')