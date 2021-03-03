class GameStatistics:
    def __init__(self, game_info: dict, game_timeline):
        self.info = game_info
        self.timeline = game_timeline

        self.score = None
        self.stat_list = None
        self.generated = False

    def generate(self) -> None:
        pass

    def get_score(self) -> float:
        return self.score

    def get_stat_list(self) -> list:
        return self.stat_list