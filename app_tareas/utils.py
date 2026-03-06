from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.core.mail import send_mail

class TokenActivacion(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) +
            six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

token_activacion = TokenActivacion()




def enviar_correo_activacion(request, user):
    current_site = get_current_site(request)
    asunto = 'Activa tu cuenta en TaskSmart'
    mensaje = render_to_string('app_tareas/correo_activacion.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_activacion.make_token(user),
    })
    send_mail(
        asunto,
        '',  # texto plano vacío
        'Luis Rubio Dev <luisdev@luisrubiodev.tech>',
        [user.email],
        html_message=mensaje,  # 👈 aquí va el HTML
        fail_silently=False,
    )