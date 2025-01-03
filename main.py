import logic

if __name__ == "__main__":
    url = input("insert video url\n")  # prompt the user to input a YouTube video URL
    logic.download_and_merge(url=url)  # call the download_and_merge function with the provided URL
