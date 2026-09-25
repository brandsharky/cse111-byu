"""
Playlist Stats

Brandon Arroyo
September 24, 2026
"""

import csv



def get_playlist_file():
    """Ask the user for the .csv playlist file and return it."""
    return input("Enter the filename of the playlist in .csv format: ")


def get_songs(filename):
    """Take in the .csv playlist file and return a dict for each song."""

    with open(filename, "r") as file:
        reader = csv.DictReader(file, fieldnames=["song", "artist", "album", "duration", "type", "plays"])

        songs_dict = [row for row in reader]

    return songs_dict


def get_playlist_length(songs):
    """Take in a dict of songs and return the length of the dict."""
    return len(songs)


def get_song(songs, index):
    """Take in a dict of song and index and return the song at the given index."""
    return songs[index]


def get_most_played_song(songs):
    """Take in a dict of songs and return the song with the most plays."""
    most_plays = songs[0]
    for song in songs:
        plays = int(song["plays"])

        if plays > int(most_plays["plays"]):
            most_plays = song

    return most_plays


def get_playlist_duration(songs):
    """Take in a list of songs, calculate the total duration of the playlist, and return the total duration in a formatted form."""
    total_seconds = 0

    for song in songs:
        minutes, seconds = song["duration"].split(':')
        total_seconds += (60 * int(minutes)) + int(seconds)

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours}:{minutes:02}:{seconds:02}"


def main():
    playlist = get_playlist_file()

    songs = get_songs(playlist)

    print(f"The playlist has {get_playlist_length(songs)} songs.")

    first_song = get_song(songs, 0)
    print(f"The first song is {first_song["song"]} by {first_song["artist"]}.")
    last_song = get_song(songs, -1)
    print(f"The last song is {last_song["song"]} by {last_song["artist"]}.")

    most_played_song = get_most_played_song(songs)
    print(f"{most_played_song["song"]} was played the most times at {most_played_song["plays"]} plays.")

    playlist_duration = get_playlist_duration(songs)
    print(f"The playlist is {playlist_duration} long.")





if __name__ == "__main__":
    main()