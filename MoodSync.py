# Gets user mood input and makes sure it's valid
def get_mood():
    while True:
        mood = input("Enter your mood (happy, sad, tired, stressed, energetic, chill): ").lower().strip()

        if mood == "" or not mood.isalpha():
            print("Please enter a valid mood.")
        else:
            return mood

# Recommends songs based on the user's mood
def recommend_song(mood):
    songs = {
        "happy": ["Happy - Pharrell", "Good as Hell - Lizzo"],
        "sad": ["Someone Like You - Adele", "Stay - Rihanna"],
        "stressed": ["Weightless - Ambient", "Lo-fi Beats"],
        "tired": ["Chill Vibes", "Soft Piano"],
        "energetic": ["Stronger - Kanye West", "POWER - Kanye West"],
        "chill": ["Location - Khalid", "Pink + White - Frank Ocean"]
    }

    if mood in songs:
       print("\n🎵 --- Recommended Songs --- 🎵")
       for song in songs[mood]:
        print("-", song)
    else:
     print("\nNo recommendations for that mood yet.")
    

   # Main program loop that runs the app
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
