import json
from django.conf import settings


with open((settings.JSON_ROOT / "misc_data.json"), "r", encoding="utf-8") as f:
    data_json = json.load(f)


def data(request):
    return {
        "menu": data_json["menu"],
        "social_links": data_json["social_links"],
    }
