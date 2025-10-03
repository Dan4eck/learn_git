def print_menu():
    print("=== MP3 Player Menu ===")
    print("1. Play Song")
    print("2. Pause")
    print("3. Stop")
    print("4. Next Song")
    print("5. Previous Song")
    print("6. Show Playlist")
    print("7. Add Song to Playlist")
    print("8. Remove Song from Playlist")
    print("9. Quit")

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1-9): "))
        if 1 <= choice <= 9:
            return choice
        else:
            print("Invalid choice. Please select a number between 1 and 9.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def main():
    while True:
        print_menu()
        choice = get_user_choice()
        if choice is None:
            continue
        if choice == 1:
            print("Playing song...")
        elif choice == 2:
            print("Pausing song...")
        elif choice == 3:
            print("Stopping playback...")
        elif choice == 4:
            print("Next song...")
        elif choice == 5:
            print("Previous song...")
        elif choice == 6:
            print("Showing playlist...")
        elif choice == 7:
            print("Adding song to playlist...")
        elif choice == 8:
            print("Removing song from playlist...")
        elif choice == 9:
            print("Exiting MP3 player. Goodbye!")
            break

if __name__ == "__main__":
    main()