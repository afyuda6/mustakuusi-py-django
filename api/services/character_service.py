from api.repositories.character_repository import CharacterRepository


class CharacterService:

    @staticmethod
    def list_characters():
        characters = CharacterRepository.get_all()

        result = []

        for ch in characters:
            result.append({
                "id": str(ch.id),
                "name": ch.name,
                "imageSrc": ch.image_src,
                "description": ch.description,
            })

        return result
