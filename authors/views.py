from django.shortcuts import render, redirect  # type: ignore # noqa: F401
from .forms import LoginForm, RegisterForm
from django.http import Http404  # type: ignore # noqa: F401
from django.contrib import messages  # type: ignore # noqa: F401
from django.urls import reverse  # type: ignore # noqa: F401
from django.contrib.auth import authenticate, login, logout  # type: ignore
from django.contrib.auth.decorators import login_required  # type: ignore
from news.models import News
from .forms.news_forms import AuthorNewsForm


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
        return redirect(reverse('authors:login'))
        # Após salvar, estou limpando o formulário preenchido.

    return redirect('authors:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'authors/pages/login.html', {
        'form': form,
        'form_action': reverse('authors:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Your are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid credentials.')
    else:
        messages.error(request, 'Invalid username or password.')

    return redirect(reverse('authors:dashboard'))


@login_required(login_url='authors:login', redirect_field_name='next')
def logout_view(request):
    logout(request)
    messages.success(request, 'Logout realized with success!')
    return redirect('authors:login')


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard(request):
    news = News.objects.filter(
        is_published=False,
        author=request.user
    )
    return render(request, 'authors/pages/dashboard.html',
                  context={
                      'news': news
                  })


@login_required(login_url='authors:login', redirect_field_name='next')
def dashboard_news_edit(request, id):
    news = News.objects.filter(
        is_published=False,
        author=request.user,
        pk=id,
    ).first()

    if not news:
        raise Http404()

    form = AuthorNewsForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=news
    )

    if form.is_valid():
        news = form.save(commit=False)

        news.author = request.user
        news.news_content_is_html = False
        news.is_published = False

        news.save()

        messages.success(request, 'Your news was saved successfully!')
        return redirect(reverse('authors:dashboard_news_edit', args=(id,)))

    return render(
        request,
        'authors/pages/dashboard_news.html',
        context={
            'form': form
        }
    )
