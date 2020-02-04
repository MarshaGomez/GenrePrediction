from game import Game

game_downloader = Game(starting='https://api.rawg.io/api/games', dir='GamesPrev')

game_downloader.creacsv()