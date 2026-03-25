from api.repositories.game_repository import GameRepository
from zoneinfo import ZoneInfo


class GameService:

    @staticmethod
    def list_games():
        games = GameRepository.get_all_with_relations()

        result = []

        jakarta = ZoneInfo("Asia/Jakarta")

        for game in games:
            screenshots_sorted = sorted(
                game.screenshots.all(),
                key=lambda s: str(s.id)
            )

            screenshots = [s.image_src for s in screenshots_sorted]

            game_characters_sorted = sorted(
                game.game_characters.all(),
                key=lambda gc: gc.character.position
            )

            characters = [str(gc.character.id) for gc in game_characters_sorted]

            result.append({
                "id": str(game.id),
                "title": game.title,
                "imageSrc": game.image_src,
                "date": game.release_date.astimezone(jakarta).isoformat(),
                "description": game.description,
                "categories": game.categories,
                "detail": game.detail,
                "privacyPolicyLink": game.privacy_policy_link,
                "downloadLink": game.download_link,
                "longDescription": game.long_description,
                "screenshots": screenshots,
                "characters": characters,
            })

        return result
