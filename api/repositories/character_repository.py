from api.models import Character


class CharacterRepository:

    @staticmethod
    def get_all():
        return Character.objects.all().order_by('position')
