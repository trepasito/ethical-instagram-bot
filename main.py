import os
import time

def main():
    # Set the console title and color (specific to Windows)
    os.system("title Instagram Bot Interface")
    print("\033[92m")  # ANSI escape for green text
    
    print("Instagram Automation Tool")
    print("===========================")
    
    account_name = input("Enter your Instagram account username: ")
    if not account_name:
        print("Error: Please input a valid username.")
        return
    
    # Simulated check for account existence
    account_exists = check_account_exists(account_name)
    if not account_exists:
        print("Error: Instagram account not found.")
        return
    
    print("\nPlease choose a botting category:")
    print("[1] - Likes")
    print("[2] - Views")
    print("[3] - Followers")
    choice = input("> ")
    
    if choice == "1":
        handle_likes(account_name)
    elif choice == "2":
        handle_views(account_name)
    elif choice == "3":
        handle_followers()
    else:
        print("Invalid choice. Exiting.")

def check_account_exists(username):
    """
    Simulate checking if an Instagram account exists.
    In a real application, use the Instagram API to verify.
    """
    print(f"Checking account for username: {username}...")
    # Simulated logic: Assume all accounts exist
    return True

def handle_likes(account_name):
    """
    Handle automation of likes for a specific post.
    """
    post_url = input("Enter the URL of the Instagram post (must be public): ")
    if not post_url.startswith("https://www.instagram.com/"):
        print("Error: Invalid post URL.")
        return
    
    print(f"Sending likes to post: {post_url}")
    # Simulate sending likes
    for i in range(1, 101):
        time.sleep(0.1)  # Simulate delay
        print(f"Like {i} sent.")
    print("Completed sending likes!")

def handle_views(account_name):
    """
    Handle automation of views for a specific story.
    """
    story_url = input("Enter the URL of the Instagram story (must be public): ")
    if not story_url.startswith("https://www.instagram.com/stories/"):
        print("Error: Invalid story URL.")
        return
    
    print(f"Sending views to story: {story_url}")
    # Simulate sending views
    for i in range(1, 101):
        time.sleep(0.1)  # Simulate delay
        print(f"View {i} sent.")
    print("Completed sending views!")

def handle_followers():
    """
    Display a message about ethical behavior regarding follower automation.
    """
    print("Automating followers is not supported to comply with ethical standards and Instagram's Terms of Service.")
    print("Please consider using legitimate methods to grow your audience.")

if __name__ == "__main__":
    main()
