from argparse import ArgumentParser, Namespace
from lyrics_extractor import SongLyrics

parser = ArgumentParser()

extract_lyrics = SongLyrics("AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg", "aa2313d6c88d1bf22")

parser.usage = "To extract lyrics from a song"

parser.add_argument("song", type=str, help="The song to extract lyrics from")

parser.add_argument("-lyrics", "--lyrics", action="store_true")

args: Namespace = parser.parse_args()

song = extract_lyrics.get_lyrics(args.song)
if args.lyrics:
    print(song['lyrics'])

else:
    print(song)
