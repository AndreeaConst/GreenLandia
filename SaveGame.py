import shelve
import GameGlobalVariables


def save_game():
    shelf_file = shelve.open('saved_game_file')

    shelf_file['score_glass'] = GameGlobalVariables.score_glass
    shelf_file['score_metal'] = GameGlobalVariables.score_metal
    shelf_file['score_organic'] = GameGlobalVariables.score_organic
    shelf_file['score_paper'] = GameGlobalVariables.score_paper
    shelf_file['score_plastic'] = GameGlobalVariables.score_plastic

    shelf_file.close()
