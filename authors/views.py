from django.shortcuts import render, redirect  # type: ignore # noqa: F401
from .forms import LoginForm, RegisterForm
from django.http import Http404  # type: ignore # noqa: F401
from django.contrib import messages  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    # Aqui estou indicando que os dados estao sendo enviados nesta sessao.
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', {
        'form': form,
        'form_action': reverse('authors:register_create'),
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)  # Aqui só esta salvando na variavel.
        user.set_password(user.password)  # Criptográfa a senha do user.
        user.save()  # Aqui ja esta salvando na base de dados com a crip.
        messages.success(request, 'Your user is created, please log in.')
        # Aqui estou salvando o formulário na base de dados.

        del (request.session['register_form_data'])
        # Após salvar, estou limpando o formulário preenchido.

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })


def login_create(request):
    return render(request, 'authors/pages/login.html')
