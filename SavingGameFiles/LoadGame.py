import shelve
import GameGlobalVariables


def load_game():
    shelf_file = shelve.open('saved_game_file')

    if 'score_glass' in shelf_file.keys():
        GameGlobalVariables.score_glass = shelf_file['score_glass']
    if 'score_metal' in shelf_file.keys():
        GameGlobalVariables.score_metal = shelf_file['score_metal']
    if 'score_organic' in shelf_file.keys():
        GameGlobalVariables.score_organic = shelf_file['score_organic']
    if 'score_paper' in shelf_file.keys():
        GameGlobalVariables.score_paper = shelf_file['score_paper']
    if 'score_plastic' in shelf_file.keys():
        GameGlobalVariables.score_plastic = shelf_file['score_plastic']

    if 'money' in shelf_file.keys():
        GameGlobalVariables.money = shelf_file['money']

    shelf_file.close()
