from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver

@receiver(social_account_added)
def save_google_data(request, sociallogin, **kwargs):
    user = sociallogin.user

    user.first_name = sociallogin.account.extra_data.get('given_name', '')
    user.last_name = sociallogin.account.extra_data.get('family_name', '')

    user.is_active = True
    user.save()