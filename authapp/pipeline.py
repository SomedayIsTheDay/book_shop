from django.conf import settings
import requests


def get_user_vk_info(backend, user, response, **kwargs):
    if backend.name != "vk-oauth2":
        return

    access_token = response["access_token"]

    vk_response = requests.get(
        f"https://api.vk.com/method/users.get?&access_token="
        f"{access_token}&fields=photo_max_orig&v=5.131"
    )

    if vk_response.status_code != 200:
        return

    vk_data = vk_response.json()["response"][0]
    user.email = kwargs["details"]["email"]

    if "photo_max_orig" in vk_data:
        avatar_url = vk_data["photo_max_orig"]
        avatar_response = requests.get(avatar_url)
        avatar_path = (
            f"{settings.MEDIA_ROOT}/users_avatars/{hash(user.pk)+hash(avatar_url)}.jpg"
        )
        with open(avatar_path, "wb") as avatar_file:
            avatar_file.write(avatar_response.content)

        user.avatar = f"users_avatars/{hash(user.pk)+hash(avatar_url)}.jpg"

    user.save()
