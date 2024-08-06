from django.core.mail import EmailMessage
from django import forms
from .models import Produto

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.CharField(label='Email')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(widget=forms.Textarea(), label='Mensagem')

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = (
            f"Você recebeu uma nova mensagem de contato.\n\n"
            f"Nome: {nome}\n"
            f"Email: {email}\n"
            f"Assunto: {assunto}\n\n"
            f"Mensagem:\n{mensagem}\n"
        )

        mail = EmailMessage(
            subject=f"Nova mensagem: {assunto}",
            body=conteudo,
            from_email='your_email@example.com',
            to=['destination@example.com'], 
            headers={'Reply-To': email}
        )
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']