class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next_song:
                current_song = current_song.next_song
            current_song.next_song = new_song

    def remove_song(self, title):
        current_song = self.head
        previous_song = None

        while current_song:
            if current_song.title == title:
                if previous_song:
                    previous_song.next_song = current_song.next_song
                else:
                    self.head = current_song.next_song
                return True
            previous_song = current_song
            current_song = current_song.next_song
        return False

    def display_playlist(self):
        if not self.head:
            print("Playlist is empty.")
            return

        current_song = self.head
        print("Playlist:")
        while current_song:
            print(f"Title: {current_song.title}, Artist: {current_song.artist}")
            current_song = current_song.next_song

def main():
    playlist = Playlist()

    print("Hello! Welcome to Zaid's Playlist.")
    while True:
        print("\nMenu:")
        print("1. Add Song")
        print("2. Remove Song")
        print("3. Display Playlist")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            title = input("Enter the song title: ")
            artist = input("Enter the artist name: ")
            playlist.add_song(title, artist)
            print(f"Added '{title}' by {artist} to the playlist.")

        elif choice == 2:
            title = input("Enter the song title to remove: ")
            if playlist.remove_song(title):
                print(f"Removed '{title}' from the playlist.")
            else:
                print(f"'{title}' not found in the playlist.")

        elif choice == 3:
            playlist.display_playlist()

        elif choice == 4:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()