

def list_all_videos(videos):
    pass

while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List all Youtube videos")
    print("2. Add a Youtube video")
    print("3. Update the Youtube video details")
    print("4. Delete a Youtube video")
    print("5. Exit the app")
    choice = input("Enter your choice")

    match choice:
        case '1':
            list_all_videos(videos)