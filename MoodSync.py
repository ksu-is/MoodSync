def get_mood():
    while True:
        mood = input("How are you feeling? ").lower().strip()
        
        if mood == "":
            print("Please enter a mood.")
        else:
            return mood


def recommend_song(mood):
    songs = {
        "happy": ["Happy - Pharrell", "Good as Hell - Lizzo"],
        "sad": ["Someone Like You - Adele", "Stay - Rihanna"],
        "stressed": ["Weightless - Ambient", "Lo-fi Beats"],
        "tired": ["Chill Vibes", "Soft Piano"],
        "energetic": ["Stronger - Kanye West", "POWER - Kanye West"]
    }

    if mood in songs:
        print("\nRecommended songs:")
        for song in songs[mood]:
            print("-", song)
    else:
        print("\nNo recommendations for that mood yet.")


def main():
    print("Welcome William Heard! List any mood to get music recommendations.\n")
    
    while True:
        mood = get_mood()
        recommend_song(mood)
        
        again = input("\nTry again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break


main()
