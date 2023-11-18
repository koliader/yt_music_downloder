class UserDataDispatcher:
    # Get data from user
    @staticmethod
    def get_user_data():
        playlist_link = input("Enter playlist link to save: ")
        output_directory = input("Enter output directory: ")
        return {"link": playlist_link, "directory": output_directory}
