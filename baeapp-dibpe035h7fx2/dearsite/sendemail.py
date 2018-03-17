from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', '565808094@qq.com',
          ['2949566227@qq.com'], fail_silently=False)
