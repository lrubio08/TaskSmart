import six
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class TokenActivacion(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) +
            six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

token_activacion = TokenActivacion()




def enviar_correo_activacion(request, user):
    domain = request.get_host() 
    
    asunto = 'Activa tu cuenta en TaskSmart'
    mensaje = render_to_string('app_tareas/correo_activacion.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_activacion.make_token(user),
    })
    send_mail(
        asunto,
        '',  
        'Luis Rubio Dev <luisdev@luisrubiodev.tech>',
        [user.email],
        html_message=mensaje,  
        fail_silently=False,
    )