import sqlite3

connection = sqlite3.connect('UtubeWithdatabase.db')

cursor =connection.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            nAME TEXT NOT NULL,
            tIME TEXT NOT NULL
    )

''')
def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos =  cursor.fetchall()
    if len(videos) == 0:
        print("=" * 50)
        print("📂 Database is empty!")
        print("➜ Please add videos first.")
        print("=" * 50)
        return

    print("\n========== All Videos ==========")
    for video in videos:
        print(f"ID   : {video[0]}")
        print(f"Name : {video[1]}")
        print(f"Time : {video[2]}")
        print("-" * 35)

    
    

def Add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(? , ?)", (name,time))
    connection.commit()

def Update_video(new_video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ? , time =?  WHERE id = ?",((new_name,new_time,new_video_id)))
    connection.commit()
    if cursor.rowcount ==0:
        print("\n No such ID exists")
    else:
        print("\n Video Updated  Successfully")
    
def Delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id =?",(video_id,))
    connection.commit()
    if cursor.rowcount ==0:
        print("\n No such ID exists")
    else:
        print("\n Video deleted Successfully")




    


def main():
    while True:
        print("\n__________________________Welcome to the Youtube Video Manager_____________________")
        print("1: list all video  ")
        print("2: Add video  ")
        print("3: Update Video  ")
        print("4: Delete Video  ")
        print("5: Exist the system  ")
        choice = int(input("Enter your choice"))
        

        if choice == 1:
            try:
                choice = int(input("Enter your choice: "))
                list_all_videos()
            except ValueError:
                print("Please enter a number.")
                continue
        elif choice == 2:
            name = input("Enter the name of the video: ")
            time = input("Enter the Time: ")
            Add_video(name,time)

        elif choice == 3:
            video_id= int(input("Enter the video ID: "))
            name = input("Enter the name of the video: ")
            time = input("Enter the Time: ")
            Update_video(video_id,name,time)

        elif choice == 4:
            video_id= int(input("Enter the video ID: "))
            Delete_video(video_id)
        elif choice == 5:
            print("System Exit")
            break
        else:
            print("Invalid choice")
    connection.close()
if __name__ == "__main__":
    main()