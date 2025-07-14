import json

def load_data():
    pass

def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():

    videos = load_data()

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
            case '2':
                add_video(videos)
            case '3' :
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5' :
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()